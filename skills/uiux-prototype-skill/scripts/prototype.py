#!/usr/bin/env python3
"""Manage approval-gated, versioned HTML prototype files. Standard library only.

This utility records user decisions; it cannot obtain or verify consent itself.
An agent must never fabricate approval evidence or treat an HTML button as consent.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import sys
from datetime import datetime, timezone
from urllib.parse import unquote, urlsplit

VERSION = "1.0.0"
SURFACES = ("web", "miniapp", "mobile", "desktop")
PENDING = "UIUX_PROTOTYPE_PENDING"
MANIFEST = "manifest.json"


class PrototypeError(Exception):
    """An actionable validation or workflow error."""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def version_name(value: str) -> str:
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)?", value):
        raise PrototypeError("Version must look like v0.1.0 or v0.1.0-review.1.")
    return value


def reject_symlinks(path: Path) -> None:
    """Reject existing symlink components without following them."""
    for part in [*reversed(path.parents), path]:
        if part.is_symlink():
            raise PrototypeError(f"Refusing symlink path: {part}")


def version_dir(project: str, version: str) -> Path:
    # The caller chooses the project root; never inspect or modify another project.
    root = Path(project).expanduser().absolute()
    reject_symlinks(root)
    path = root / "docs" / "prototype" / "versions" / version_name(version)
    reject_symlinks(path)
    return path


def safe_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise PrototypeError(f"Invalid relative artifact path: {relative!r}")
    parts = PurePosixPath(relative)
    if parts.is_absolute() or ".." in parts.parts or ":" in relative:
        raise PrototypeError(f"Artifact path must stay inside this version: {relative}")
    result = root.joinpath(*parts.parts)
    reject_symlinks(result)
    return result


def read_manifest(root: Path) -> dict:
    file = safe_path(root, MANIFEST)
    try:
        data = json.loads(file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise PrototypeError(f"Cannot read {file}: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise PrototypeError("Unsupported or malformed manifest schema.")
    if data.get("version") != root.name:
        raise PrototypeError("Manifest version does not match its directory.")
    if data.get("state") not in {"direction-draft", "approved", "prepared", "sealed"}:
        raise PrototypeError("Invalid manifest state.")
    surfaces = data.get("surfaces")
    if not isinstance(surfaces, list) or not surfaces or any(s not in SURFACES for s in surfaces) or len(set(surfaces)) != len(surfaces):
        raise PrototypeError("Manifest surfaces must be a unique nonempty supported list.")
    paths = data.get("deliverable_paths")
    if not isinstance(paths, list) or not paths or any(not isinstance(p, str) for p in paths) or len(set(paths)) != len(paths):
        raise PrototypeError("Manifest deliverable_paths must be a unique nonempty list.")
    for path in paths:
        safe_path(root, path)
    if MANIFEST in paths:
        raise PrototypeError("Manifest cannot include itself as a deliverable.")
    expected = required_paths(data["surfaces"], data["state"] in {"prepared", "sealed"})
    if not set(expected).issubset(paths):
        raise PrototypeError("Manifest omits required artifact paths.")
    return data


def save_manifest(root: Path, data: dict) -> None:
    target = safe_path(root, MANIFEST)
    temporary = safe_path(root, ".manifest.tmp")
    if temporary.exists():
        raise PrototypeError("Temporary manifest already exists; inspect it before retrying.")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    temporary.replace(target)


def required_paths(surfaces: list[str], full: bool = True) -> list[str]:
    paths = ["style-reference.html"]
    if full:
        paths += ["index.html", "design-system.html", "DESIGN.md", "QA.md", "references.json"]
        for surface in surfaces:
            paths += [f"{surface}/index.html", f"{surface}/DESIGN.md"]
    return paths


def approval_valid(root: Path, data: dict) -> bool:
    approval = data.get("approval")
    if not isinstance(approval, dict):
        return False
    style = safe_path(root, "style-reference.html")
    return bool(
        style.is_file()
        and approval.get("direction")
        and approval.get("evidence")
        and approval.get("by")
        and approval.get("style_reference_sha256") == digest(style)
    )


def require_approval(root: Path, data: dict) -> None:
    if not approval_valid(root, data):
        raise PrototypeError("Explicit user direction approval is missing or stale. Present the current style-reference.html and obtain a user decision before proceeding.")


def ensure_mutable(data: dict) -> None:
    if data["state"] == "sealed":
        raise PrototypeError("This version is sealed. Create a new version instead of modifying it.")


def page(title: str, content: str) -> str:
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<style>body{{font-family:system-ui,sans-serif;max-width:1000px;margin:64px auto;padding:0 24px;color:#20242b;background:#f7f8fa;line-height:1.6}}a{{color:#1757b8}}article{{background:white;padding:24px;border:1px solid #d9dee5;border-radius:12px}}nav{{display:flex;gap:24px;flex-wrap:wrap}}h1{{line-height:1.15}}:focus-visible{{outline:3px solid #1757b8;outline-offset:4px}}</style></head>
<body><!-- {PENDING} --><main><p>待设计的脚手架 · 非完整原型</p><h1>{html.escape(title)}</h1>{content}</main></body></html>
'''


def style_template() -> str:
    return page("风格参考 · 等待研究和选择", """<p>先研究真实案例，填写来源、观察日期、可迁移规则及各端约束，再请用户拍板。</p>
<article><h2>研究记录</h2><p>优先 Dribbble；可用即时设计、Behance 和真实产品。保留原作品链接，区分已查看内容与搜索摘要。不得虚构案例或授权。</p></article>
<article><h2>方向候选</h2><p>按项目需要展示可比较的方向：用相同任务、内容和控件演示字体、色彩、密度、状态与动效。保留真实设计规范和品牌要求。</p></article>
<article><h2>用户决定</h2><p>此 HTML 中的按钮、偏好控件或助手推荐不构成批准。用户在对话中明确选择后，才记录其原话、所选方向和本文件摘要。</p></article>""")


def init(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    if root.exists():
        raise PrototypeError(f"Version already exists; nothing overwritten: {root}")
    surfaces = list(dict.fromkeys(args.surfaces))
    root.mkdir(parents=True, exist_ok=False)
    (root / "style-reference.html").write_text(style_template(), encoding="utf-8")
    data = {
        "schema_version": 1, "tool_version": VERSION, "version": args.version,
        "state": "direction-draft", "created_at": now(), "surfaces": surfaces,
        "deliverable_paths": required_paths(surfaces, False), "approval": None,
        "approval_history": [], "scope": "HTML prototype; no backend or production integration implied",
    }
    save_manifest(root, data)
    return {"version_dir": str(root), "state": data["state"], "next": "Research and finish style-reference.html, then obtain an explicit user direction decision."}


def record_approval(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    data = read_manifest(root)
    ensure_mutable(data)
    if not args.direction.strip() or not args.evidence.strip() or not args.by.strip():
        raise PrototypeError("Direction, approving user and exact decision evidence are required.")
    style = safe_path(root, "style-reference.html")
    if not style.is_file() or PENDING in style.read_text(encoding="utf-8"):
        raise PrototypeError("Finish the style-reference draft before recording user approval.")
    record = {
        "direction": args.direction.strip(), "evidence": args.evidence.strip(),
        "by": args.by.strip(), "recorded_at": now(), "style_reference_sha256": digest(style),
        "meaning": "A record of a user decision supplied by the caller, not independently verified consent.",
    }
    data["approval_history"].append(record)
    data["approval"] = record
    if data["state"] == "direction-draft":
        data["state"] = "approved"
    save_manifest(root, data)
    return {"version_dir": str(root), "state": data["state"], "approval": record}


def prepare(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    data = read_manifest(root)
    ensure_mutable(data)
    require_approval(root, data)
    if data["state"] == "prepared":
        raise PrototypeError("Scaffolds already prepared; no files overwritten.")
    paths = required_paths(data["surfaces"])
    existing_references = safe_path(root, "references.json").is_file()
    for relative in paths[1:]:
        if relative == "references.json" and existing_references:
            continue
        if safe_path(root, relative).exists():
            raise PrototypeError(f"Destination already exists; no files overwritten: {relative}")
    nav = '<nav><a href="style-reference.html">风格参考</a><a href="design-system.html">可视化设计规范</a>' + ''.join(f'<a href="{s}/index.html">{s}</a>' for s in data["surfaces"]) + '</nav>'
    contents = {
        "index.html": page("原型导航首页", nav + "<p>填入产品目标、已批准的设计方向、版本和各端完整任务入口。</p>"),
        "design-system.html": page("可视化 UI 设计规范", '<nav><a href="index.html">返回原型首页</a></nav><p>实现与 DESIGN.md 同源的 tokens：色彩、文字、布局、间距、组件、状态、动效与无障碍。此页应展示真实样式和交互。</p>'),
        "DESIGN.md": f"# Product UI design contract\n\n<!-- {PENDING} -->\n\nDirection: {data['approval']['direction']}\n\nDocument actual product users, tasks, design tokens, components, states, accessibility, motion, platform adaptations, sample-data boundary and validation evidence. Replace this scaffold with the approved design.\n",
        "QA.md": f"# Prototype verification\n\n<!-- {PENDING} -->\n\nRecord actual browsers, viewports, primary journeys, interaction and state checks, accessibility and reduced-motion checks, local asset/link checks, observed performance, evidence paths and remaining limitations. Clearly separate performed checks from plans and unverified platform/runtime behavior.\n",
    }
    if not existing_references:
        contents["references.json"] = json.dumps({"status": PENDING, "sources": [], "note": "Replace with actual research evidence, observations and access limitations; this utility does not verify source claims."}, ensure_ascii=False, indent=2) + "\n"
    for surface in data["surfaces"]:
        contents[f"{surface}/index.html"] = page(f"{surface} 应用原型", '<nav><a href="../index.html">返回原型首页</a><a href="../design-system.html">设计规范</a></nav><p>实现本端关键任务、真实控件和空白、加载、成功、错误等适用状态，按本端交互习惯设计。</p>')
        contents[f"{surface}/DESIGN.md"] = f"# {surface} adaptation\n\n<!-- {PENDING} -->\n\nInherit ../DESIGN.md. Record this platform's navigation, input, density, safe areas, viewport, component and runtime capability decisions.\n"
    for relative, content in contents.items():
        target = safe_path(root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as stream:
            stream.write(content)
    data["state"] = "prepared"
    data["deliverable_paths"] = paths
    data["prepared_at"] = now()
    save_manifest(root, data)
    return {"version_dir": str(root), "state": data["state"], "deliverable_paths": paths, "next": "Replace every pending scaffold with the approved product design; validate and browser-review before sealing."}


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.targets.append(value)


def local_link_errors(root: Path, file: Path) -> list[str]:
    parser = Links()
    parser.feed(file.read_text(encoding="utf-8"))
    errors = []
    for raw in parser.targets:
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        link = unquote(parsed.path)
        if "\\" in link or link.startswith("/"):
            errors.append(f"{file.relative_to(root)}: nonportable local link {raw}")
            continue
        target = file.parent / link
        try:
            reject_symlinks(target.absolute())
            resolved = target.resolve()
            resolved.relative_to(root.resolve())
        except (ValueError, PrototypeError):
            errors.append(f"{file.relative_to(root)}: link escapes version or uses symlink: {raw}")
            continue
        if not resolved.exists():
            errors.append(f"{file.relative_to(root)}: missing local link {raw}")
    return errors


def validate_data(root: Path, data: dict, complete: bool = False) -> dict:
    errors = []
    approved = approval_valid(root, data)
    if data["state"] != "direction-draft" and not approved:
        errors.append("User direction approval is missing or stale for the current style-reference.html.")
    if complete and data["state"] not in {"prepared", "sealed"}:
        errors.append("Full prototype has not been prepared after approval.")
    # Check every local HTML page, including added task pages beyond the initial manifest.
    for file in root.rglob("*"):
        reject_symlinks(file)
        if file.is_file() and file.suffix.lower() in {".html", ".htm"}:
            errors.extend(local_link_errors(root, file))
            if complete and PENDING in file.read_text(encoding="utf-8") and str(file.relative_to(root)) not in data["deliverable_paths"]:
                errors.append(f"Pending design scaffold: {file.relative_to(root)}")
    for relative in data["deliverable_paths"]:
        target = safe_path(root, relative)
        if not target.is_file():
            errors.append(f"Missing required artifact: {relative}")
        elif complete and target.suffix.lower() in {".html", ".htm", ".md", ".css", ".js", ".json"} and PENDING in target.read_text(encoding="utf-8"):
            errors.append(f"Pending design scaffold: {relative}")
        if relative == "references.json" and target.is_file():
            try:
                json.loads(target.read_text(encoding="utf-8"))
            except ValueError:
                errors.append("references.json is not valid JSON.")
    if data["state"] == "sealed":
        hashes = data.get("sealed_artifact_sha256")
        if not isinstance(hashes, dict) or not hashes:
            errors.append("Sealed version is missing artifact hashes.")
        else:
            current = artifact_hashes(root)
            if current != hashes:
                errors.append("Sealed version changed: file contents or file set differ from its recorded hashes.")
    return {"version_dir": str(root), "state": data["state"], "approval_valid": approved, "complete_check": complete, "ok": not errors, "errors": errors, "scope": "File/workflow checks only; browser interaction, accessibility and runtime capabilities require separate verification."}


def artifact_hashes(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob("*")):
        reject_symlinks(path)
        if path.is_file() and path != root / MANIFEST:
            result[str(path.relative_to(root))] = digest(path)
    return result


def validate(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    data = read_manifest(root)
    return validate_data(root, data, args.complete)


def inspect(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    data = read_manifest(root)
    return {"version_dir": str(root), "manifest": data, "approval_valid": approval_valid(root, data)}


def seal(args: argparse.Namespace) -> dict:
    root = version_dir(args.project, args.version)
    data = read_manifest(root)
    ensure_mutable(data)
    require_approval(root, data)
    if not args.summary.strip():
        raise PrototypeError("A summary of actual browser checks and limitations is required.")
    result = validate_data(root, data, True)
    if not result["ok"]:
        raise PrototypeError("Cannot seal: " + "; ".join(result["errors"]))
    data["state"] = "sealed"
    data["sealed_at"] = now()
    data["validation_summary"] = args.summary.strip()
    data["sealed_artifact_sha256"] = artifact_hashes(root)
    save_manifest(root, data)
    return {"version_dir": str(root), "state": "sealed", "hashed_artifacts": len(data["sealed_artifact_sha256"]), "scope": "A local immutable-by-convention snapshot with tamper detection; not production acceptance."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool-version", action="version", version=VERSION)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, handler in [("init", init), ("record-approval", record_approval), ("prepare", prepare), ("inspect", inspect), ("validate", validate), ("seal", seal)]:
        command = commands.add_parser(name)
        command.add_argument("--project", required=True, help="Project root containing docs/prototype/")
        command.add_argument("--version", required=True, help="New or existing version, e.g. v0.1.0")
        command.set_defaults(handler=handler)
        if name == "init":
            command.add_argument("--surfaces", nargs="+", choices=SURFACES, default=list(SURFACES))
        elif name == "record-approval":
            command.add_argument("--direction", required=True)
            command.add_argument("--evidence", required=True, help="Exact explicit user decision; never fabricate or infer approval")
            command.add_argument("--by", default="user", help="Approving user identifier or label")
        elif name == "validate":
            command.add_argument("--complete", action="store_true", help="Reject pending scaffolds and missing full prototype artifacts")
        elif name == "seal":
            command.add_argument("--summary", required=True, help="Actual browser checks and remaining limitations; caller-supplied evidence")
    try:
        args = parser.parse_args(argv)
        result = args.handler(args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result.get("ok", True) else 1
    except (PrototypeError, OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
