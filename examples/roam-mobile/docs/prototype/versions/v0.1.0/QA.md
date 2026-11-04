# Roam v0.1.0 / QA evidence

Date:2026-11-04. Candidate received root browser review and is being sealed for this local demonstration. This record distinguishes root-agent browser observations from local structural checks.

## Actual browser review reported by the root agent

- Runtime: browser automation against http://127.0.0.1:61531/roam-mobile/docs/prototype/versions/v0.1.0/mobile/ . Browser product/version was not supplied in the handoff, so it is not inferred here.
- Viewport:390×844, device scale factor2.
- Discover → Open itinerary → Save this day → #saved: passed with actual visible state changes.
- Reload after saving retains the saved plan: passed.
- Remove gives the actionable empty state: passed.
- Search `no-such-place` gives the recovery action `See all daytrips`; activating it clears the query: passed.
- Document width390px, no horizontal overflow observed.
- All images loaded; no console warning or error reported.
- Root export files: share/assets/roam-discover.png, share/assets/roam-trip.png and share/assets/roam-saved.png in the parent case delivery. These are actual app captures, not separately mocked interface pictures.

## Local checks

- Actual installed uiux-prototype-skill used. Style-reference HTML and references.json were created first, then named direction A was recorded with exact delegated evidence, then prepare created version scaffolds.
- app.js passed Node syntax checking.
- Shared token contrast ratios: {"ink on paper": 13.3, "muted on paper": 4.74, "white on action": 5.24, "action on paper": 4.74}. This is pair measurement, not an overall WCAG conformance claim.
- Structural complete validation is run after final files are written; see command/result in parent completion evidence.
- Current generated hero bytes: 3610967. CSS and JS are local; fonts are system fallbacks. Large hero is a known first-open cost of this local prototype and should be compressed into an appropriate delivery format for a deployed app. No production timing or concurrency benchmark was performed.

## Remaining verification

The root's browser report covers the primary app path. Hub and design-system visual review,320/430px widths,200% zoom, keyboard-only traversal/dialog focus restoration, reduced motion, non-Latin/long content and real mobile devices remain unverified unless added in a later dated review. The date input, preferences and supporting city detail are implemented but were not included in the root's reported interaction test.

The location sheet is curated selection, not GPS. The coast asset is an original generated fictional landscape, not verified photography of the named UI destination. Forecast, routes, distances and opening/access conditions are illustrative. No live bookings, payment, messaging, external writes, route safety or native SDK behavior has been validated. Local saved state is not account synchronization.


Root final review: the visual specification was rendered at1440px and checked for visible tokens, type, states and component examples. Version sealed as a local demonstration snapshot; native platform and complete accessibility acceptance remain outside this verification.

Final saved-screen correction retested at390×844: action row bottom749.16px, navigation top763.5px; action buttons are fully visible. Bottom navigation is opaque. The discovery→details→save path was rerun and final screenshots regenerated after this CSS correction.
