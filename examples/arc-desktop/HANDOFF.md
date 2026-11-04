# Arc Library handoff

Prototype root: docs/prototype/. Main candidate: versions/v0.1.0/. Installed skill used: uiux-prototype-skill. Style-reference created before full prototype, chosen under exact current user delegation “由你定风格，直接完成三个案例”. Do not seal until root browser QA is complete.

No dependencies, no external runtime assets. All12 artworks are original SVG in version assets/art. Synthetic file type/size/dimension metadata is design content; there are no actual PNG/PDF files or native filesystem operations. App JS stores only local demo favorites/tags/new collections. Browser clipboard failure has a manual text-copy dialog.

Research: Chrome rendered3 specific Dribbble shots (Cargo/Juless Design, Foyer/Geoffrey Crofte, DAM Details/Thuan Nguyen); source works are linked, not bundled. iab unavailable in this worker session; Chrome was the available browser. Source inspection used actual screenshots after navigation rather than claims based on text snippets.

Browser finding: explicit HTML image height attributes can keep a preview600px tall despite CSS width/aspect-ratio. Inspector original SVG preview now sets height:auto with4:3 and object-fit:contain. Main asset grid owns its own bounded image height. Root observed the issue at1440×900; retest before sealing.
