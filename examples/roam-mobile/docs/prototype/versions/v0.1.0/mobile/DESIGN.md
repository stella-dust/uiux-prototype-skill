# Roam mobile

Shared source of truth: ../DESIGN.md and ../assets/tokens.css.

Platform-neutral mobile HTML concept, designed at390px portrait and capped at430px on wide displays. Discovery gives one immersive coastal suggestion, with category/search controls and a smaller local option. Details move to a focused full route, not a compressed desktop side panel. Native-style bottom navigation holds Discover / My plans / You, with a saved-count badge.

The icon hit areas are44px, main action52px, and nav controls at least48px. Category controls are39px high with spacing. The CSS safe area and simulated status bar communicate intent; actual iOS/Android behavior is not verified. The coast image is generated and fictional, despite named destination labels in illustrative content.

Critical saved path: #discover → #trip → Save this day → #saved → date selection/reopen/remove. Persistence is on this browser/device only. A supporting #trip-city route does not offer bookings or save; this is intentional bounded scope. Browser evidence and unresolved checks: ../QA.md.
