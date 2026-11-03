---
name: uiux-prototype-skill
description: Research visual references, get user approval on a style-reference HTML, then build versioned product application UI prototypes with a visual design system and DESIGN.md. Use for web apps, mini programs, mobile and desktop app interfaces, including inherited product redesigns. Excludes posters, slide decks and marketing-only sites.
license: MIT
metadata:
  version: 1.0.0
---

# UIUX Prototype

Design product interfaces around real tasks. Deliver reviewable HTML before application implementation. Work in the user's language; default to Chinese explanations with necessary English terms. This skill is self-contained: upstream skills and paid reference services are optional, not dependencies.

## 1. Establish the product and preserve its baseline

Read applicable AGENTS.md, HANDOFF.md, existing DESIGN.md and current prototype files first. Identify the users, scenario, entry, main task, result, business value, requested surfaces and what is outside this version. Preserve existing brand decisions and other people's edits. Resolve routine details yourself; ask only for missing information that materially changes the design.

Agree a bounded screen/flow inventory from the brief, not an arbitrary number of pages. Cover each requested surface (web, mini program, mobile, desktop); do not invent an irrelevant app. If the surface scope is unknown and the project cannot establish it, ask once before proceeding. An inherited UI gets an audit and a non-overwriting version, not an unsolicited redesign.

Read the relevant decision-rule sections (§1–7) in [source-synthesis.md](references/source-synthesis.md); use its source map (§8–10) when a tradeoff needs explanation. It integrates all seven source repositories. Product task clarity, existing design contracts and user choices take precedence over landing-page conventions, style bans and random themes.

## 2. Research references, then STOP for a style decision

Read [reference-research.md](references/reference-research.md). Start with **Dribbble**; use **即时设计** and **Behance** as fallbacks or supplements. Search for the product category, the user's task and relevant platform, not just “beautiful UI”. Use available browser/search tools; record which pages and images were actually inspected. Do not call a search snippet a visual review. Observe access restrictions; if real cases cannot be viewed, report that and ask for supplied references or an explicit waiver of research.

Create a new version under `docs/prototype/versions/vX.Y.Z/` (or the project's established prototype root). Use the CLI below to start safely. Write `style-reference.html` first: normally 2–3 differentiated, task-appropriate directions, real case links/creators, observed evidence versus your interpretation, token samples and an original small UI study of the SAME task for comparison. Include platform fit, limitations and your recommendation. Preserve known brand choices; when the user already supplied one direction, validate it instead of forcing alternatives.

**Deliver the actual style-reference HTML and ask the user to choose or revise it. Stop here.** Do not create the full app screens, design-system.html or final DESIGN.md until the user explicitly approves a named direction (or delegates that exact choice in the current task). A local selected radio/card, a preferred recommendation, elapsed time or a CLI record is not user authorization. Keep approval evidence with the approved HTML's SHA-256; a material change to that board needs a fresh decision. Do not treat this gate as permission to ask again about unrelated, already authorized work.

## 3. Build the full HTML prototype after approval

Read [prototype-contract.md](references/prototype-contract.md) and only the relevant sections of [platforms-and-quality.md](references/platforms-and-quality.md). Record the user's actual decision; the helper records evidence, it cannot verify who gave it. Then prepare and replace the generated scaffolds with designed, working artifacts:

- `index.html`: prototype home/navigation with version, surface entries, core flows, style reference and visual specification links. Each app also has its own task-oriented home. Keep implementation/status detail in this review hub, not product chrome.
- `design-system.html`: complete visual specification **for components used in this version**: semantic colors, typography, spacing, layout/density, icons, surfaces, applicable component states, interaction/motion and responsive/platform differences. Show actual rendered examples, not only tables of names.
- `DESIGN.md`: canonical decisions, token values, screen/flow inventory, interactions, platform overrides, accessibility, provenance and known prototype limitations. Per-surface DESIGN.md explains only relevant variations.
- Each requested surface's HTML screens: complete agreed critical paths, plausible labeled synthetic data, navigation and meaningful state changes. Shared semantic tokens; platform-appropriate interaction, not a shrunken desktop screenshot.

Use semantic HTML, CSS variables and small local scripts by default. Reuse the existing framework/components when it reduces complexity; no mandatory React, Tailwind, shadcn or network dependency. A static HTML prototype must open through a local HTTP server and should remain navigable with file URLs when feasible. Assets needed to review the prototype should be local and licensed. Keep the prototype separate from application source.

## 4. Verify, version and hand off

Use [platforms-and-quality.md](references/platforms-and-quality.md) to review the rendered result at narrow and wide viewports, keyboard focus, zoom and reduced motion; inspect applicable device/platform behavior. Test actual primary paths plus empty/loading/error/success and extreme-content states that matter. Do not assert device or native SDK acceptance from browser simulation. Fix the observed problems and recheck the affected paths.

Run structural validation, then record browser evidence, viewport sizes, tested flows and unresolved issues in `QA.md`. Structural validation cannot prove visual quality, business completeness, permission enforcement, external integration or production readiness. Report untested items explicitly. For deployment work, measure relevant loading/runtime/resource costs instead of reporting functional checks alone; ordinary local prototypes do not require a production benchmark suite.

Keep previous versions intact. Read [versioning.md](references/versioning.md) for approval invalidation, revisions, sealed snapshots, changelog and latest-version navigation. Do not silently edit an approved board or overwrite an older prototype. Deliver links to the actual files, how to open them, what was verified and what remains simulated.

## Helper (Python 3, standard library)

Resolve `<skill-dir>` to this installed skill's directory. Commands operate only on the specified project; they do not publish or change application source.

```sh
python3 <skill-dir>/scripts/prototype.py init --project <project> --version v0.1.0 --surfaces web miniapp mobile desktop
# Edit style-reference.html with real research; obtain the user's decision.
python3 <skill-dir>/scripts/prototype.py record-approval --project <project> --version v0.1.0 --direction "B" --evidence "Exact user decision from this conversation"
python3 <skill-dir>/scripts/prototype.py prepare --project <project> --version v0.1.0
# Replace every pending scaffold, implement the agreed flows, and render/review.
python3 <skill-dir>/scripts/prototype.py validate --project <project> --version v0.1.0 --complete
python3 <skill-dir>/scripts/prototype.py seal --project <project> --version v0.1.0 --summary "Reviewed scope and material changes"
```

`record-approval` stores a workflow record, not an identity or security boundary. Never fabricate its evidence. `prepare` produces scaffolds, not a finished prototype. `seal` records file hashes; it is not a visual sign-off or immutable storage. Use the manifest and QA evidence together.
