# Version and decision management

Use project conventions if established; otherwise `docs/prototype/versions/vMAJOR.MINOR.PATCH/`. A new design candidate gets a new directory. Keep prior files, approvals and reviewer evidence intact. Typical choice: patch for a bounded correction, minor for a new flow/surface or style iteration, major for a deliberate system redesign. This is a review convention, not a rigid compatibility promise.

The helper supports `--root` only if documented in its help; otherwise honor an established root by managing it manually with the same invariants. Never pass path traversal or modify unrelated project files to force a convention.

`init` creates a style-research draft. `record-approval` records an actual explicit decision and the current board hash. `prepare` requires that hash to remain current and creates unfinished scaffolds. `validate` checks structure, required outputs and local links; it cannot assess a visual design. `seal` records file hashes after scaffolds are replaced and checks pass; later file changes are detected by validation. A sealed snapshot is a detectable convention, not OS-level immutability. Copy to a new candidate version for changes; do not claim a copied approval applies to a different style board.

The helper is an accidental-error guard, not authentication. A user can edit JSON and files; the agent must still respect the actual conversation. Never manufacture an approval quote to satisfy the script. If the approved board changes, stop dependent full-build work and request a decision on the changed board. Keep approval to the scope actually approved; style approval does not authorize publishing, production integration or transactions.

After successful review, maintain a root prototype index linking retained versions and the current reviewed candidate; update CHANGELOG.md with changes, rationale, scope, validation and unresolved items. Don't silently replace the “latest” with an unreviewed draft. Use Git commits/tags if the project uses Git; directory snapshots remain necessary for standalone sharing. Commit only relevant prototype changes. Keep dates, provenance and superseded status explicit.
