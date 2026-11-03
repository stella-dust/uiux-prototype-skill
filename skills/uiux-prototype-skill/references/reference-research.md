# Reference research and style decision

## Where to look

1. Dribbble: https://dribbble.com/ — prefer product screens, multi-screen cases and interaction studies for the actual task. Search category + task + platform, e.g. resident services + request status + mobile; compare hierarchy, density and states rather than likes.
2. 即时设计: https://js.design/community?category=explore — useful for Chinese typography, mini program conventions and localized workflows.
3. Behance: https://www.behance.net/galleries/ui-ux/ui-ux — useful for end-to-end case studies and systems. Reference libraries connected by the user may supplement these sources; UXKIN paid search is optional.

Use an available connector first when it can inspect the source. Otherwise use the built-in browser or Chrome; do not use Vivaldi without the user's permission. Readable HTML does not mean a shot image was viewed. If a source requires JavaScript, try the browser. If login/403 prevents access, record it and try the next source; do not bypass restrictions, invent cases or repeatedly retry an unchanged block.

## Evidence to retain

Store a small `references.json` next to the style board. For each used case record `url`, `title`, `creator` (unknown if unavailable), `accessed_at`, `source`, `inspection` (image-viewed / page-text-only / blocked), `observed`, `adaptation`, and `asset_rights`. Links alone do not justify claims about visual details. Distinguish an observation from a proposed design choice. Open promising individual works; a generic search page is a search trail, not a chosen case.

Select enough evidence to support a decision, commonly 3–6 relevant cases across 2–3 directions. These are defaults, not quotas. For an inherited or strongly branded product, compare within its constraints. Do not clone a composition without considering actual navigation, content density, states and platform limits. A Dribbble shot is often a concept, not evidence of usability or a shipped product.

## style-reference.html

Make a locally readable page with an understandable comparison. Each direction has:

- A concise name and task/platform fit.
- Linked source cases with creators and inspection status; cite directly beside the observation.
- Proposed palette, type hierarchy, density, surface treatment and motion character.
- Your own original rendering of a small representative interface using the SAME content/goal across directions. Label it a direction study, not the full prototype.
- Tradeoffs, what is retained from the existing design, what is changing and why.

Use screenshot excerpts only with appropriate permission/licensing. A public URL does not grant redistribution rights. Prefer attributed links and original CSS studies when rights are unclear. Do not bundle third-party shots or hotlink them as permanent prototype dependencies. The public README must use original demonstration media, not an unlicensed inspiration collage.

Recommend a direction and explain it in product terms. Hand over the HTML and ask for a named choice, blend or revision. A selector can preview alternatives and copy a decision phrase, but it cannot grant approval or trigger development. Save explicit conversational approval and the approved board digest before full production. If the user asks to skip research/choose autonomously, retain their exact waiver/delegation and its scope; do not infer it from a request to “make it polished”.
