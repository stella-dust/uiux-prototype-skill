# Platform adaptation and quality

Read the relevant surface sections, then the common checks. HTML is a behavioral/visual prototype; native system behavior remains unverified until tested in the actual platform.

## Web application

Design around tasks, information hierarchy and appropriate density. Use sidebar/top navigation where justified; represent selected routes, filters, sort, bulk actions, pagination, form validation and details when they exist in scope. Preserve keyboard navigation, visible focus, semantic tables/form labels, URL/back behavior in a routed prototype. Narrow layouts may need priority columns, stacked rows or explicit horizontal scrolling rather than clipped content.

## Mini program

Respect the specified host (e.g. WeChat or Alipay), host navigation/capsule area, safe areas, tab navigation, keyboard and limited viewport. HTML can simulate these areas but does not validate native APIs, domain permissions, login or review compliance. Use host guidelines through available official docs for platform-sensitive details; do not install payment/onboarding tools just to draw UI. Never invent payment or host authorization behavior.

## Mobile app

Choose the target OS or record a platform-neutral concept. Navigation stacks, sheets, safe areas, touch feedback, keyboard avoidance, text expansion and system permission timing matter. Use platform-native conventions as design input; a web clone is not a native acceptance test. Prefer adequate touch targets (commonly 44pt iOS / 48dp Android) and spacing; these units are not identical to browser CSS pixels. Reference official guidance when exact behavior is material.

## Desktop app

Consider window resizing, minimum usable width, pointer/keyboard, shortcuts, selected/focused states, menus and content density. Use an app shell where the product needs one; don't draw browser chrome as if it were required desktop navigation. Native title bar/window controls/file access are illustrations unless actually integrated. Avoid intercepting platform-reserved shortcuts in the HTML review.

## Shared checks

- Accessibility: aim at WCAG 2.2 AA for web UI; test actual text/background combinations (normal text 4.5:1, large text 3:1; relevant non-text UI 3:1, with criterion exceptions). Don't use color alone. Verify semantic labels, focus order/traps/return, zoom/reflow, screen-reader names where tools permit. Touch comfort targets above are design guidance, not a false claim that WCAG universally requires 44px.
- Motion: decide whether animation serves feedback, continuity or spatial comprehension. Frequent keyboard/data operations should be immediate; don't animate every row or constantly changing value. Use transform/opacity where feasible; begin with short purposeful transitions, tune duration/easing by distance/frequency, enter generally ease-out, exit generally ease-in, springs for direct manipulation where appropriate. Don't treat these as universal formulas. Interrupted motion should continue from current state. Respect reduced motion and remove decorative movement; don't hide meaning when it is disabled.
- Performance: avoid layout-per-frame loops, oversized blur/layers, blocking assets, per-frame React state churn and unbounded lists. Use a representative dense screen to inspect scrolling/transitions. Lazy-load optional heavy media; local CSS/JS and system fonts often suffice. For an actual deployment, include relevant payload, load/interaction timing and runtime/cost measurements under the project's contract.
- Stress states: long Chinese/Latin names, unbreakable IDs, large numbers, zero items, missing avatars, permission denial, slow/retry behavior, offline, destructive action cancellation and text enlargement. Keep user intent on errors and give an actionable recovery.
- Visual QA: render the app, the style reference and the specification. Inspect task hierarchy, density, alignment, type, contrast, responsive layouts and coherent tokens. Compare against the approved original direction and existing product contract; don't score it only against generic aesthetic rules.

Official reference: [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/). Platform docs can change; consult their official current guidance when implementation depends on a specific host or OS.
