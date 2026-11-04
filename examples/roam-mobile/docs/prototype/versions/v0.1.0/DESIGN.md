# Roam / v0.1.0

## Product contract

A platform-neutral mobile daytrip planning concept for an independent traveler. Entry: Discover. Critical path: find a nearby trip → open destination → inspect itinerary and practical details → save the coastal day → choose a date → reopen or remove the plan. Value: a small, practical plan instead of an unlimited travel search.

This is an original synthetic case, not a commissioned real itinerary. The concept uses Lisbon-area labels and illustrative timings. The generated landscape depicts a fictional, unverified coast; it is not documentary photography of Azenhas do Mar. No GPS, live weather, route verification, reservations, payment, account or backend is connected.

## Direction and authority

A / The sun-worn journal. Warm paper, dark ink, restrained rust-orange action, editorial serif destination titles and a readable plain itinerary. The style reference was written before the full prototype. User delegated the choice in this task with the exact evidence: “由你定风格，直接完成三个案例”. The manifest stores this quote and the board digest. This choice covers this case's visual direction, not external publication or transaction authority.

Inspected research: Moove by Agensip, image viewed at800px; its white sheet, day timeline and single orange action informed planning clarity. Ronas IT individual page description was read, with no image-review claim. Full research records are in references.json. No upstream shot or component kit is redistributed.

## Shared semantic tokens

Single runtime source: assets/tokens.css. Rendered examples: design-system.html.

| Role | Token | Value |
| --- | --- | --- |
| Page | --paper | #f8f3eb |
| Raised control | --surface | #fffaf4 |
| Primary text | --ink | #2b2822 |
| Secondary text | --muted | #746b5f |
| Edge | --line | #e5dbce |
| Primary action | --action | #bd441f |
| Action hover | --action-hover | #9e3518 |
| Focus | --focus | #234e78 |
| Success | --success | #38624c |
| Error | --error | #a42f23 |
| Small radius | --radius-sm |12px |
| Large radius | --radius-lg |24px |
| Feedback duration | --fast |160ms |
| Feedback easing | --ease |cubic-bezier(.2,.7,.2,1) |

CSS also uses a20px image radius,99px action/filter pills and24px screen gutters. Spacing scale:4/8/12/16/24/32/48px. Pills identify controls; itinerary content uses simple rows, not nested cards.

## Typography and material

Georgia / Times New Roman for expressive headings; Avenir Next / Avenir / Apple system / Segoe UI / sans-serif for controls and reading. All fonts are local fallbacks, with no font download. Default UI15px/1.5. Mobile discovery title43px/1.04, destination29px/1.15, detailed hero46px/.95; compact secondary content11–13px. Small labels are purposeful place/time or control annotations; key task text is larger. Text zoom and non-Latin expansion remain explicit QA items.

Generated hero: assets/roam-coast.png, original AI-generated illustration in photographic style, supplied for this case. It is not a verified real place. Supporting city illustration assets/city.svg and original icon SVGs are authored locally. A small alternate coast SVG remains as an original fallback source, not the app's current hero. See asset provenance supplied alongside the generated image.

## Screen and state inventory

- `#discover`: wordmark, changeable starting point, search, category filters, primary coastal destination and supporting city daytrip. Search preserves focus; unknown query produces an actionable recovery state.
- `#trip`: destination, distance/time/illustrative temperature, Your day itinerary, Good to know practical guidance and persistent save action.
- `#saved`: empty collection or saved coastal plan. Date field, reopen itinerary and remove. The coastal plan is the bounded saved-path demonstration; the supporting city page is a read-only detail route.
- `#you`: locally retained pace and starting point; clear prototype information.
- `#trip-city`: supporting original illustration, bounded half-day timeline and practical guidance.
- Native HTML dialog: location selection; Escape/backdrop behavior follows browser dialog support, not a native OS claim.

## Behavior and state

Hash routes support browser back. My plans and preferences use localStorage with a memory fallback when storage is unavailable. A saved state is reflected in the bookmark, bottom-nav badge and plan list. No account sync. The date is a local choice, not a booking date. Remove gives immediate empty-state recovery; the user can save again. A toast announces local action results; core saved status persists independently of the toast.

Overview/itinerary tabs update the panel and ARIA selected state. Main navigation uses aria-current. Icons have accessible names on their buttons and decorative SVGs are hidden. Main icon hit areas44px; nav minimum48px; primary action52px. Category pills are39px high with gaps; native device touch comfort is unverified.

## Motion and accessibility

No on-load parade or scroll animation.160ms image hover feedback and small button press transformation; repeated navigation is immediate. Reduced motion removes transition timing. No per-frame JS loops or external runtime dependencies. Modal semantics use dialog; visible keyboard focus uses a3px blue outline.

Measured token pairs: {"ink on paper": 13.3, "muted on paper": 4.74, "white on action": 5.24, "action on paper": 4.74}. These values cover only these color pairs, not the overall rendered interface. Photo overlay text uses a dark gradient in the detail view; image text and actual focus/zoom behavior require visual review.

## Platform handling

Portrait target390×844. Responsive width320–430px; wider screens center the mobile concept. The illustrative9:41 status bar is not native UI. CSS env(safe-area-inset-bottom) and100dvh handle browser safe area/height where supported. Bottom navigation stays fixed; detail save action is sticky above it. Native SDK, screen readers, actual touch/keyboard behavior, live location and device performance require separate acceptance.

## Handoff and verification

Open via local HTTP; file-mode is also intended to work for ordinary navigation but browser localStorage/file restrictions vary. Run the installed skill's prototype.py validate with --complete. Browser evidence is in QA.md. Keep this v0.1.0 candidate unsealed until final review of the hub and design specification as well as the app. Do not claim current browser evidence proves production or business results.
