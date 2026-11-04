# Pulse / Ink & Cadence

Version: v0.1.0. Surface: Web product. Project: Morrow Studio, an invented creative studio.

## User and business task

A studio lead needs a daily view of active client work, delivery risk and capacity. The bounded journey is overview -> project detail -> milestone/status update, or Projects -> team/status/search -> new project -> persisted project. The benefit is clearer prioritization and less cross-project coordination overhead; no business outcome has been measured.

## Direction and provenance

`style-reference.html` was generated before the full prototype. It compares **A / Ink & Cadence** and **B / Cobalt Blocks** with the same project content. A was selected using the current task's explicit delegation, retained verbatim in `manifest.json` and `references.json`. The approved board is bound by SHA-256. Final UI slightly tunes warm neutral values for dense text; the direction remains warm paper, near-black ink and selective cobalt.

Two Dribbble individual works were opened and their first images visually inspected in Chrome: Dodik Danang/Korsa's Studio (27574945) and Jason D's Project Workspace Dashboard UI (26904547). Their original artwork is not bundled. All cover artwork, SVG paths and interface composition here are original. System fonts require no downloaded font asset. Detailed source links, observations versus adaptation and rights limitations are in `references.json`.

## Single-source design tokens

Canonical source: `assets/app.css` :root. Visual examples: `design-system.html`.

| Role | Value | Use |
|---|---|---|
| paper | #f7f6f2 | App canvas |
| surface | #ffffff | Project cards, form fields |
| sidebar | #eeeee7 | Quiet persistent navigation |
| ink | #24251f | Primary text, selected nav, capacity anchor |
| muted | #6c6e63 | Secondary text |
| line | #dedfd5 | Nonessential surface separation |
| soft | #f0f0e9 | Hover and grouped controls |
| action | #354cdb | Primary action, selection and progress |
| action-hover | #263fc6 | Hovered primary action |
| lilac | #c6b9ed | Selected availability bar / allocation meaning |
| warning | #a35b2c | Semantic review state |
| warning-bg | #f7ecdf | Review badge surface |
| error | #ad443c | Inline form recovery |
| error-bg | #faeeeb | Error surface |
| radius | 14px | Principal card material |
| ease | cubic-bezier(.16,1,.3,1) | Short entrance/feedback transitions |

`line` is a low-contrast decorative divider, not the sole indication of an actionable control. Focus uses a 3px cobalt outline with 4px offset. Status text and labels accompany color. The white card-on-paper separation is supplemented by borders and composition.

Typography: -apple-system / BlinkMacSystemFont / Segoe UI / sans-serif, with Georgia for original client-cover lettering. Body 14px, app H1 34px (29px at intermediate, 26px narrow), section 16px, card title 16px, supporting content 10-12px. Tabular numerals on summary metrics; no unnecessary monospaced labels. Metric value 38px. Compact desktop data is intentionally small; zoom/reflow is required QA, and body text remains resizeable.

Space: 4/8/12/16/20/24/32/36px family, with optical adjustments (e.g. 25px column gap). Sidebar 216px; wide content padding 36px; summary uses plain columns rather than a card wall. Main overview has two featured projects and a 292px capacity context column. Project card art 145px at the primary target, then restrained detail rows. Icons are original 24-unit SVG, consistent 1.6px rounded strokes. Principal cards radius14, cover8, controls7, badges4; borders1px. No baseline floating shadows; card hover adds only subtle depth.

## Screens and complete scoped flow

- `web/index.html#overview`: studio summary, two active project cards, delivery rhythm and capacity.
- `#projects`: all seeded/client-created projects, status/team/search/sort and card/list modes.
- `#capacity`: weekly allocations for eight synthetic people; project blocks open details.
- `#project=forma` (and each project id): native HTML dialog showing owners, delivery, milestones, status advancement and progress.
- New project: name/client/delivery validation, optional context, native controls, local success then Projects view.
- Activity dialog: three synthetic updates; Onda update opens that project.

Header search runs on Enter and filters immediately while Projects is active. Slash focuses it unless a field or dialog is active. Navigation is hash based, preserving browser back/forward. Detail closes back to its previous route. State changes are immediate except a short toast entrance. Status transitions are Planned -> In progress -> In review -> Completed. Completed work moves into its own filter; no destructive operation is implemented.

## States and persistence

Seed dataset has six projects, including In progress, In review and Planned; Completed starts empty. Empty/no-results states have clear-filter recovery. Required form fields expose adjacent errors using aria-describedby and aria-invalid, preserve typed values and focus the first error. Project creation disables its submit during the synchronous save to prevent accidental duplicate execution. Native modal focus confinement, Escape dismissal and focus return are used. Milestone updates preserve checkbox focus after rerender.

`localStorage` key `pulse.morrow.projects.v1` persists projects, milestones and statuses in this browser origin. Filter/sort/layout state is session-local only. When storage is unavailable, the app retains session changes and communicates that limitation in a toast. Local data must not be treated as an access-controlled backend; reload storage validation is deliberately modest for a synthetic prototype. No external network/API call exists in the runtime.

## Narrow adaptation and accessibility

At <=1000px, capacity moves below primary project content. At <=740px, sidebar becomes an explicitly opened off-canvas navigation with a dismissal scrim; header condenses, projects remain two compact cards, and typography/spacing reprioritize content. The weekly delivery strip and capacity table retain their minimum readable width inside explicit scrollable regions instead of forcing document overflow. Project list hides secondary Team/Delivery columns at narrow sizes while retaining identity/status/progress. Dialogs fit viewport height and scroll; detail metadata moves below tasks.

Semantic landmarks, link navigation, button actions, accessible names for icon controls, select/input labels, visible focus, status text and live-region feedback are built in. Reduced motion disables nonessential transition and backdrop blur while preserving all meaning. Desktop workflow is pointer/keyboard first. Small metadata is not itself a touch target; actionable rows/buttons provide sufficient area where feasible. Actual screen-reader, zoom and small viewport findings belong in QA.md, not inferred from markup.

## Validation and implementation boundary

`QA.md` records checks actually performed and outstanding acceptance. The structural helper checks artifact/link validity and approval freshness; it cannot establish visual quality or working native/platform SDK behavior. Root review may add screenshots and browser findings before sealing. Do not seal until that review is complete. Prototype file mode is supported by local relative assets, but persistence depends on browser policy for file origins; a local HTTP server is the preferred review route.
