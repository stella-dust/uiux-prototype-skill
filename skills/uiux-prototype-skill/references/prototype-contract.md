# Prototype deliverable contract

## Directory and coverage

```text
docs/prototype/
  index.html                      # additive navigation to retained versions
  CHANGELOG.md
  versions/v0.1.0/
    manifest.json                 # scope, approval evidence, state, hashes
    style-reference.html
    references.json               # actual research evidence
    index.html                    # review home; links to all surfaces and specs
    design-system.html            # rendered specification
    DESIGN.md                     # canonical design decisions
    QA.md                         # actual checks, remaining gaps
    assets/                       # local CSS, JS, fonts or permitted images
    web/index.html                # app home plus agreed screens/flows
    web/DESIGN.md
    miniapp/index.html
    miniapp/DESIGN.md
    mobile/index.html
    mobile/DESIGN.md
    desktop/index.html
    desktop/DESIGN.md
```

Only include requested surfaces. HTML may be one interactive screen with route/state views or several linked documents; don't force a file per screen. The complete deliverable means the bounded screen and state inventory agreed for this version, not an unlimited imagined product. If a scoped part is deferred, mark it as deferred before calling the agreed scope complete.

## Canonical specification

Use semantic tokens (background/surface/text/muted/border/action/focus/status); one source of values in local CSS, reflected accurately in DESIGN.md and design-system.html. Define typography for Chinese/Latin/numerals; font fallback and licensing; spacing/density/grid; icon treatment and accessible labeling; elevation/radii; tables/forms/navigation/dialogs; charts when present. Record component API behavior in plain product terms. Add motion tokens with purpose, timing/easing, interruption and reduced-motion behavior.

Show applicable default/hover/focus/pressed/disabled/loading/error/success states with actual examples, as well as empty/offline/no-results/permission states where the product needs them. Not every component needs every state. Show how a form error is recovered, how dialog focus returns, how a pending action prevents accidental duplicates, how destructive actions can be reversed when appropriate. Label persistent versus temporary state.

DESIGN.md describes users and primary task, inventory, chosen direction with approval reference, tokens, platform overrides, navigation/interaction rules, accessibility, evidence, limitations and developer handoff. Per-surface DESIGN.md links back to shared decisions and records platform-specific deviations; don't create competing token systems.

## Product behavior

Primary controls must navigate or produce an appropriate local state; inert controls require an explicit unavailable explanation. Use real labels and plausible content. Label synthetic data once in the review hub; do not flood application screens with implementation notes. Never imply a local success toast means a real payment, message, permission check or backend write succeeded. Annotate simulated integrations in QA and the relevant flow.

Reuse established components and patterns where helpful, but match the approved design rather than accepting a library's default theme. Use icons from one coherent licensed family or original simple SVGs. Do not turn all content into rounded cards; dense lists, tables and plain rows are legitimate product layouts. Avoid superfluous subtitles, repeated labels and promotional copy. Keep accessible names, error text and meaningful state feedback.

## Review evidence

QA.md records browser/runtime, local URL or file mode, viewports, tested flows and observed results, keyboard/zoom/reduced-motion checks where relevant, console/network issues, platform simulations versus actual device tests, known gaps and external-service boundaries. Capture representative screenshots after the final fix. Do not mark a scaffold, a test count or a structural validator as visual/business approval.
