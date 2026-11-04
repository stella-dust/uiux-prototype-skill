# Product UI case studies

[简体中文](README.zh-CN.md) · [Back to the skill](../README.md)

These three original examples exercise the installed skill's research, delegated style choice, full prototype and review workflow. Each v0.1.0 is a sealed local demonstration snapshot. User delegation is retained in its manifest; it does not grant permission for unrelated future actions.

| Case | Main flow | Files |
|---|---|---|
| **Roam** — Mobile daytrip planner | Discover nearby escapes, inspect an itinerary, save a plan and recover from an empty search. | [App](roam-mobile/docs/prototype/versions/v0.1.0/mobile/index.html) · [Style research](roam-mobile/docs/prototype/versions/v0.1.0/style-reference.html) · [System](roam-mobile/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](roam-mobile/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](roam-mobile/docs/prototype/versions/v0.1.0/QA.md) |
| **Pulse** — Web studio workspace | Review projects and capacity, filter work, create a project with validation, and inspect milestones. | [App](pulse-web/docs/prototype/versions/v0.1.0/web/index.html) · [Style research](pulse-web/docs/prototype/versions/v0.1.0/style-reference.html) · [System](pulse-web/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](pulse-web/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](pulse-web/docs/prototype/versions/v0.1.0/QA.md) |
| **Arc Library** — Desktop asset organizer | Browse original assets, search and filter, switch views, inspect metadata and preview with the keyboard. | [App](arc-desktop/docs/prototype/versions/v0.1.0/desktop/index.html) · [Style research](arc-desktop/docs/prototype/versions/v0.1.0/style-reference.html) · [System](arc-desktop/docs/prototype/versions/v0.1.0/design-system.html) · [DESIGN.md](arc-desktop/docs/prototype/versions/v0.1.0/DESIGN.md) · [QA](arc-desktop/docs/prototype/versions/v0.1.0/QA.md) |

## Run locally

From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open [the gallery](http://localhost:8765/examples/). Each app uses local browser state; it has no production backend. The gallery's HTML source is [index.html](index.html).

## Provenance and scope

Dribbble references and actual inspection limits are retained in each `references.json`. Reference artworks are not bundled. Interface code and SVG artwork are original; Roam's generated coast has its own provenance record. Named destinations, project data, asset sizes and other fixture metadata are illustrative. Browser evidence does not establish native SDK, device, backend or full accessibility acceptance. Consult each QA file for the tested scope.

The sealed case folders were copied without editing their contents; their manifest hashes remain valid. Gallery navigation and README images sit outside these snapshots. The original files follow the repository [MIT license](../LICENSE).
