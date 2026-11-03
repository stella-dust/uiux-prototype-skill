"""Observable workflow and file-safety tests; standard library only."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/uiux-prototype-skill/scripts/prototype.py"
spec = importlib.util.spec_from_file_location("prototype", SCRIPT)
prototype = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prototype)


class PrototypeWorkflow(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name).resolve()
        self.version = "v0.1.0"

    @property
    def root(self):
        return self.project / "docs/prototype/versions" / self.version

    def cli(self, command, *extra, version=None):
        args = [command, "--project", str(self.project), "--version", version or self.version, *extra]
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = prototype.main(args)
        output = stdout.getvalue() or stderr.getvalue()
        return code, json.loads(output)

    def initialized(self, *extra):
        code, _ = self.cli("init", *extra)
        self.assertEqual(0, code)

    def direction_ready(self):
        self.initialized("--surfaces", "web", "mobile")
        (self.root / "style-reference.html").write_text("<!doctype html><html><body><h1>Direction A</h1><p>Research and comparison ready.</p></body></html>")

    def approved(self):
        self.direction_ready()
        code, result = self.cli("record-approval", "--direction", "A", "--evidence", "TEST FIXTURE: user selected A")
        self.assertEqual(0, code, result)

    def prepared(self):
        self.approved()
        code, result = self.cli("prepare")
        self.assertEqual(0, code, result)

    def complete(self):
        self.prepared()
        for f in self.root.rglob("*"):
            if f.is_file() and f.suffix in {".html", ".md", ".json"}:
                f.write_text(f.read_text().replace(prototype.PENDING, "COMPLETED_TEST_FIXTURE"))

    def test_init_creates_only_direction_artifact_and_manifest(self):
        self.initialized()
        self.assertEqual({"manifest.json", "style-reference.html"}, {f.name for f in self.root.iterdir()})
        self.assertFalse((self.root / "index.html").exists())
        self.assertEqual("direction-draft", json.loads((self.root / "manifest.json").read_text())["state"])

    def test_prepare_requires_explicit_approval(self):
        self.initialized()
        code, result = self.cli("prepare")
        self.assertEqual(2, code)
        self.assertIn("approval", result["error"])
        self.assertFalse((self.root / "index.html").exists())

    def test_unfinished_style_template_cannot_be_approved(self):
        self.initialized()
        code, result = self.cli("record-approval", "--direction", "A", "--evidence", "TEST")
        self.assertEqual(2, code)
        self.assertIn("Finish", result["error"])

    def test_editing_style_invalidates_approval(self):
        self.approved()
        with (self.root / "style-reference.html").open("a") as f:
            f.write("<p>Different palette</p>")
        code, data = self.cli("prepare")
        self.assertEqual(2, code)
        self.assertIn("stale", data["error"])
        self.assertFalse((self.root / "index.html").exists())

    def test_approval_evidence_is_bound_to_exact_style_bytes(self):
        self.approved()
        _, result = self.cli("inspect")
        record = result["manifest"]["approval"]
        self.assertTrue(result["approval_valid"])
        self.assertEqual("A", record["direction"])
        self.assertEqual("TEST FIXTURE: user selected A", record["evidence"])
        self.assertEqual(prototype.digest(self.root / "style-reference.html"), record["style_reference_sha256"])

    def test_prepare_covers_only_selected_surfaces_and_is_incomplete(self):
        self.prepared()
        self.assertTrue((self.root / "web/index.html").is_file())
        self.assertTrue((self.root / "mobile/DESIGN.md").is_file())
        self.assertFalse((self.root / "desktop").exists())
        code, result = self.cli("validate", "--complete")
        self.assertEqual(1, code)
        self.assertTrue(any("Pending" in e for e in result["errors"]))

    def test_existing_version_is_never_overwritten(self):
        self.initialized()
        target = self.root / "style-reference.html"
        original = target.read_bytes()
        code, _ = self.cli("init")
        self.assertEqual(2, code)
        self.assertEqual(original, target.read_bytes())

    def test_prepare_preflights_existing_files(self):
        self.approved()
        (self.root / "design-system.html").write_text("Unrelated draft")
        code, _ = self.cli("prepare")
        self.assertEqual(2, code)
        self.assertEqual("Unrelated draft", (self.root / "design-system.html").read_text())
        self.assertFalse((self.root / "index.html").exists())

    def test_version_traversal_rejected(self):
        for version in ["../../outside", "/tmp/danger", "v1.0.0/../../escape", "v1.0.0\\escape"]:
            code, _ = self.cli("init", version=version)
            self.assertEqual(2, code, version)
        self.assertFalse((self.project / "docs").exists())

    def test_second_version_preserves_first(self):
        self.initialized()
        before = {str(f.relative_to(self.root)): f.read_bytes() for f in self.root.rglob("*") if f.is_file()}
        code, _ = self.cli("init", version="v0.2.0")
        self.assertEqual(0, code)
        self.assertEqual(before, {str(f.relative_to(self.root)): f.read_bytes() for f in self.root.rglob("*") if f.is_file()})

    def test_manifest_path_traversal_rejected(self):
        self.prepared()
        file = self.root / "manifest.json"
        data = json.loads(file.read_text())
        data["deliverable_paths"].append("../../outside.txt")
        file.write_text(json.dumps(data))
        code, result = self.cli("validate")
        self.assertEqual(2, code)
        self.assertIn("inside", result["error"])

    def test_symlink_artifact_is_rejected_without_touching_target(self):
        self.prepared()
        outside = self.project / "outside.txt"
        outside.write_text("Preserve")
        (self.root / "web/linked.txt").symlink_to(outside)
        code, result = self.cli("validate")
        self.assertEqual(2, code)
        self.assertIn("symlink", result["error"])
        self.assertEqual("Preserve", outside.read_text())

    def test_symlink_directory_prevents_init(self):
        actual = self.project / "actual"
        actual.mkdir()
        (self.project / "docs").symlink_to(actual, target_is_directory=True)
        code, _ = self.cli("init")
        self.assertEqual(2, code)
        self.assertEqual([], list(actual.iterdir()))

    def test_links_strip_queries_fragments_and_allow_external_urls(self):
        self.prepared()
        file = self.root / "web/index.html"
        file.write_text('<a href="../index.html?view=web#main">Home</a><a href="https://example.com/missing">Source</a><img src="data:image/png;base64,AAAA">')
        code, result = self.cli("validate")
        self.assertEqual(0, code, result)
        file.write_text('<a href="missing.html?x=1#target">Broken</a>')
        code, result = self.cli("validate")
        self.assertEqual(1, code)
        self.assertTrue(any("missing.html" in e for e in result["errors"]))

    def test_link_may_not_escape_its_version(self):
        self.prepared()
        (self.project / "secret.txt").write_text("test")
        (self.root / "web/index.html").write_text('<a href="../../../../../../secret.txt">Outside</a>')
        code, result = self.cli("validate")
        self.assertEqual(1, code)
        self.assertTrue(any("escapes" in e for e in result["errors"]))

    def test_missing_required_deliverable_is_detected(self):
        self.prepared()
        (self.root / "web/DESIGN.md").unlink()
        code, result = self.cli("validate")
        self.assertEqual(1, code)
        self.assertIn("Missing required artifact: web/DESIGN.md", result["errors"])

    def test_qa_and_research_files_are_required(self):
        self.prepared()
        for relative in ["QA.md", "references.json"]:
            (self.root / relative).unlink()
        code, result = self.cli("validate", "--complete")
        self.assertEqual(1, code)
        for relative in ["QA.md", "references.json"]:
            self.assertIn(f"Missing required artifact: {relative}", result["errors"])

    def test_prepare_preserves_existing_research(self):
        self.approved()
        evidence = b'{"sources": [{"url": "https://example.com", "status": "test fixture"}]}\n'
        (self.root / "references.json").write_bytes(evidence)
        code, result = self.cli("prepare")
        self.assertEqual(0, code, result)
        self.assertEqual(evidence, (self.root / "references.json").read_bytes())
        self.assertIn("references.json", result["deliverable_paths"])

    def test_complete_check_rejects_pending_research_json(self):
        self.prepared()
        for f in self.root.rglob("*"):
            if f.is_file() and f.suffix in {".html", ".md"}:
                f.write_text(f.read_text().replace(prototype.PENDING, "COMPLETED_TEST_FIXTURE"))
        code, result = self.cli("validate", "--complete")
        self.assertEqual(1, code)
        self.assertIn("Pending design scaffold: references.json", result["errors"])

    def test_malformed_research_json_is_detected(self):
        self.prepared()
        (self.root / "references.json").write_text("{broken")
        code, result = self.cli("validate")
        self.assertEqual(1, code)
        self.assertIn("references.json is not valid JSON.", result["errors"])

    def test_manifest_cannot_hide_a_required_artifact(self):
        self.prepared()
        f = self.root / "manifest.json"
        data = json.loads(f.read_text())
        data["deliverable_paths"].remove("web/DESIGN.md")
        f.write_text(json.dumps(data))
        code, result = self.cli("validate")
        self.assertEqual(2, code)
        self.assertIn("omits", result["error"])

    def test_seal_rejects_pending_artifacts(self):
        self.prepared()
        code, result = self.cli("seal", "--summary", "test only")
        self.assertEqual(2, code)
        self.assertIn("Pending", result["error"])

    def test_seal_detects_edits_and_added_files(self):
        self.complete()
        code, result = self.cli("seal", "--summary", "TEST fixture, no real browser acceptance claimed")
        self.assertEqual(0, code, result)
        code, result = self.cli("validate", "--complete")
        self.assertEqual(0, code, result)
        (self.root / "extra.txt").write_text("post-seal change")
        code, result = self.cli("validate", "--complete")
        self.assertEqual(1, code)
        self.assertTrue(any("Sealed version changed" in e for e in result["errors"]))

    def test_nested_manifest_json_is_included_in_sealed_hashes(self):
        self.complete()
        nested = self.root / "web/manifest.json"
        nested.write_text('{"name":"PWA"}')
        code, result = self.cli("seal", "--summary", "TEST fixture")
        self.assertEqual(0, code, result)
        nested.write_text('{"name":"Changed"}')
        code, result = self.cli("validate", "--complete")
        self.assertEqual(1, code)


if __name__ == "__main__":
    unittest.main()
