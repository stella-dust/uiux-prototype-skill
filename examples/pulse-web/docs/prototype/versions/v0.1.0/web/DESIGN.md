# Pulse Web adaptation

Inherits [canonical decisions](../DESIGN.md) and `../assets/app.css`; no competing token set.

- Desktop is a studio working surface, not a marketing landing page. 216px navigation, 74px toolbar and a content grid optimize daily scanning.
- Browser hash routes: #overview, #projects, #capacity, #project=<id>. Back/forward and dialog close are part of the flow.
- Inputs use real labels and native date/select controls. Browser-native modal dialog handles focus containment and Escape; forms are custom-validated with inline recovery.
- Project cards switch to a compact list. Filter and sort state is temporary; project/milestone/status state is browser-local persisted data.
- At <=740px navigation moves off-canvas; explicit horizontal scroll is confined to the timeline and weekly capacity grid. No desktop screenshot is scaled to a phone.
- The summary, capacity values and delivery timeline are synthetic editorial fixtures. Created project counters and filters derive from current local project state. Capacity does not auto-replan when a project is created; that scheduling feature is outside this bounded example.
- Current date labels are intentionally fixed to the example week, November 2-6, 2026. Form validation uses that scenario's November 4 date, not a live clock.
- No native host APIs, authentication, messages, files, calendar synchronization or real task service is connected.
