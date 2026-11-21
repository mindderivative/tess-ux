---
title: MD3 Verification Status
type: research
status: research
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [research, needs-verification]
related: ["[[Open Questions]]", "[[Existing Tokens]]"]
depends_on: []
---

# MD3 Verification Status

How Material Design 3 values were checked in Phase 1 (closes OQ-12 for the slice notes, with the exceptions below).

> [!info] Method
> The official pages at m3.material.io are rendered by script and return no text to the tools used. Values were verified against the Material Web token sources (`tokens/versions/latest` and `v0_192`), the Material Components Android guides, Compose Material 3, WCAG 2.2 and the WAI-ARIA Authoring Practices; each note lists its sources. Where the only source is the m3.material.io page, the claim stays `#needs-verification`.

## Verified (examples)

- State layers: hover 8, focus 10, pressed 10, dragged 16 percent in the latest token set. The older set `v0_192` has focus and pressed at 12 percent; ADR-0009 and [[ADR-0013 Focus and pressed state layer 10 percent]] follow the latest.
- Focus ring 3 px, 2 px offset, `secondary`; ripple timings 450, 105, 225, 375 ms and hover fade 15 ms.
- Scrim opacity 0.32; dialog width 280 to 560 dp; menu item height 48 dp; switch 52 by 32 dp; button height 40 dp; elevation shadows equal tess-ui's formulas (this corrects the Phase 0 remark in [[Existing Tokens]] that called them a legacy formula).
- WCAG 2.5.8 (24 by 24 CSS px) and window size classes (600, 840, 1200, 1600 wide).

## Still unverified

| Note | Claim | Why |
|---|---|---|
| Spacing and Density | MD3 specification page gives 56 dp for a one-line list item | m3.material.io is a JavaScript app, no text returned; Material Web menu item token (48) used instead |
| Spacing and Density | MD3 states a 4 dp spacing grid | m3.material.io page unreadable by tools |
| State Layers | State precedence dragged > pressed > focused > hovered is MD3 guidance | Tesserae rule; m3.material.io unreadable |
| State Layers | Reduced motion hides the ripple as MD3 guidance | only Material Web forced-colors rule seen |
| State Layers | WCAG 1.4.3 exempts inactive components | recalled, page not opened |
| Focus Ring | text-input pointer focus indicator follows :focus-visible heuristic of Material Web | Tesserae rule; focus-ring.ts heuristic not inspected |
| Focus Ring | baseline secondary and surface hex values (contrast about 6:1 light, 10.9:1 dark) | hex from memory, only a computed example |
| Focus Ring | WCAG 2.4.11 wording | title seen, text not quoted |
| Iconography | MDI keeps 2 units padding in the 24 grid live area | Pictogrammers docs page not readable |
| Iconography | status bar inline icon 16 dp has an MD3 counterpart | no MD3 value found |
| Iconography | MDI licence: Apache 2.0 (shell vault) vs Pictogrammers Free License (LICENSE file) | sources disagree |
| 07 Spacing and Density Rules | page margins compact 16 / medium 24 dp follow MD3 layout guidance | m3 layout pages unreadable |
| 10 Layout Overflow and Scrolling | MD3 canonical layouts (list-detail, supporting pane, feed) and pane counts per class | m3 pages unreadable; widths 320 and 840 are Tesserae design choices |
| 10 Layout Overflow and Scrolling | scroll chaining delay 200 ms | Tesserae design choice, no source |
| Colour Roles | Numeric contrast-level values (0.5 medium, 1.0 high) and mapping of the OS contrast preference to medium | m3.material.io not readable by the fetch tool; medium/high hex taken from Material Web latest token files |
| Colour Roles | shell `accent` maps to the seed colour then `primary` | design choice, no MD3 role for a desktop accent |
| Theme Following the System | 200 ms re-theme budget | design choice (equals short4); no MD3 or platform source |
| Theme Following the System | pending surface colour #141218 when a frame must be shown before the scheme is known | design choice |
| Theme Following the System | mapping of OS contrast preference to the medium level | no source; only high is used by the projects |
| Elevation | surface container role for levels 4 and 5 (surface_container_highest) | no component token file read uses level 4 or 5; design choice |
| Elevation | Popup at level 2 with surface_container | MD3 has no popup; menu value reused, design choice |
| Elevation | official m3.material.io level-to-container table | page is script-rendered; levels 1 to 3 verified through Material Web component token files |
| Shape | Popup container radius extra_small | design choice; MD3 has no popup |
| Shape | navigation rail indicator radius (tess-ui 16 vs MD3 pill) | m3.material.io not readable |
| Motion | Popup and menu open/close durations (200 ms emphasized_decelerate / 100 ms emphasized_accelerate) | design choice; no MD3 source read |
| Motion | Conversion of MD3 spring damping/stiffness to tre bounce parameter | no documented mapping |
| Typography | Bold 700 face for the prominent label weight is not bundled in tre (Roboto Regular and Medium only) | tre docs read; Roboto variable font availability unchecked |
| Scrim | official m3.material.io scrim opacity page | not readable; 0.32 verified in Material Web md-comp-scrim token (contract marked 0.32 as unverified, now verified there) |
| Text Field | MD3 text field container height 56 dp and the label stack | m3.material.io is script-rendered and not fetchable; Material Web demo min-height 56 px is the only corroboration |
| Text Field | caret blink 530 ms on and off | MD3 gives no value; 530 ms is tess-ui Caret_Blink default; design choice |
| Text Field | multi-line default 3 lines and resize snapping | design choice, no MD3 value |
| Text Field | scale factor 1.25 and 2.0 geometry tests in tess-ui | not confirmed that the test window supports a scale factor |
| State Layers (cited in Text Field, Button, Icon Button, Switch) | focus 10 and pressed 10 percent | Material Web tokens v0_192 md-sys-state give focus 0.12 and pressed 0.12 (hover 0.08, dragged 0.16); contract says 10; conflict, needs the State Layers note and ADR-0009 sources |
| Switch | density scaling of the track at dense (46 by 28, handles 14, 21, 24) and 32 dp state layer at compact | design choice, MD3 gives one size |
| Icon Button | Expressive sizes xs to xl (32, 40, 56, 96, 136) and width kinds are Expressive | Expressive spec pages not fetched |
| Button | Expressive sizes, square shape, pressed squaring | Expressive spec pages not fetched |
| Button | paddings at compact and dense (16, 12 dp; icon 16 dp at dense) | design choice, MD3 gives 24 dp and 18 dp icon only |
| Button | reduced-motion behaviour of the loading spinner | design choice |
| 14 Accessibility Basics | WCAG 1.4.13 hoverable condition versus the tooltip rule | closed by [[ADR-0011 Tooltip hover grace for all tooltips]]: all tooltips get the 150 ms grace |
| 14 Accessibility Basics | high-contrast scheme thresholds 7 to 1 text and 4.5 to 1 non-text | Tesserae design choice, no MD3 value |
| 14 Accessibility Basics | scrollbar thumb rest alpha 38 percent may fail 3 to 1 contrast | needs contrast computation once Colour Roles values exist |
| Test Method | WCAG contrast ratio definition anchor and Accessibility Rules SC 1.1.1, 1.3.1, 3.3.1 | anchors not separately fetched |
| Scrollbar and Scroll Container | MD3 has no scrollbar component or guidance (checked only Material Web repo and engine comment) | m3.material.io is a JS app, not readable |
| Scrollbar and Scroll Container | thumb 8 dp, hit 12 dp, margin 2, min length 32, opacities 0.38/0.60/0.80, gutter 12 dp are Tesserae design choices | no MD3 values exist; contract marks them design choice |
| Scrollbar and Scroll Container | rest opacity 0.38 fails WCAG 1.4.11 3:1 (computed 2.57 dark, 1.94 light, baseline on_surface_variant over surface) | computed in the note, no shipped contrast script yet |
| Scrollbar and Scroll Container | 12 dp hit thickness vs WCAG 2.2 SC 2.5.8 24 dp: whether Spacing/Equivalent exception covers a scrollbar thumb | judgement, not confirmed |
| Scrollbar and Scroll Container | wheel notch 40 dp, track-click repeat 400/100 ms, gutter reserved by the framework | design choices; engine moves 20 dp per notch |
| Scrollbar and Scroll Container | whether to expose a scrollbar role with value to AT | tre/AccessKit support not verified |
| Tree Node | label type body_large at default and body_medium at compact/dense; icon 24/20/20; inset focus ring in rows | design choices derived from the density table |
| Tree | selection does not follow focus; Page keys; empty-state default text | design choices, APG leaves selection model to authors |
| List Item | two-line 60/48/40 and three-line 80/64/56 dp, avatar 40/32/24, image 56/48/40; formula sum of line heights + padding 16/12/4 | contract fixes only single-line heights |
| List Item | selected container secondary_container; vertical alignment of leading/trailing in three-line items | MD3 list tokens define no selected container; m3 page not read |
| List Item | MD3 disabled label opacity 0.30 vs Tesserae 0.38 | Material Web token read, m3 page not read |
| List | m3.material.io Lists guidance on selection, dividers, grouping | JS app not readable |
| Accordion | header 40/32/24, padding, content padding, title types; open 250 ms emphasized-decelerate, close 200 ms standard-accelerate; error dot | MD3 has no accordion, design choices |
| Form Row | label column width 160/120/96 dp, row gap 8/4/2, stacked layout below 400 dp, click on label focuses control | MD3 has no form row, design choices |
| Form Row | MD3 guidance on forms | m3.material.io not readable |
| Tooltip | Plain tooltip min height 24 dp, min width 40 dp, padding 8 by 4 dp, max width 200 dp; rich max width 320 dp, horizontal padding 16 dp, action min height 36 dp, gap to anchor 4 dp | Verified only in the Compose Material 3 source (Tooltip.kt); m3.material.io specs page is script-rendered and unreadable |
| Tooltip | Rich tooltip vertical metrics (28 dp to subhead, 24 dp subhead to text, 16 dp below text, 8 dp below actions) | Compose constants only, not the MD3 spec page |
| Tooltip | Hover delay 500 ms | MD3 sources read give no desktop hover delay (Flutter wait 0 ms, Compose long press); 500 ms is the accepted Tesserae rule (ADR-0004), so a design choice not an MD3 value |
| Tooltip | Touch long press shows the tooltip and it auto-dismisses at 1500 ms | 1500 ms is the Compose and Flutter non-persistent duration; official MD3 duration unreadable |
| Tooltip | Enter and exit animation bound of 100 ms (short2) | design choice, MD3 gives no tooltip duration in sources read |
| Popup | Fade of 100 ms and instant under reduced motion for popups | design choice, no MD3 duration read |
| Menu | Menu maximum width 280 dp | tess-ui bound; 112 dp minimum is verified in Material Web menu.scss, the 280 dp maximum is not |
| Menu | Container vertical padding 8 dp default, 4 dp compact and dense | MD3 token not read; the 4 dp values are a design choice |
| Menu | Typeahead prefix buffer 500 ms | design choice; Material Web default is 200 ms |
| Menu | Submenu hover open 250 ms and close 300 ms | shell vault values (built); Material Web uses 400 ms and 400 ms; no MD3 spec value read |
| Menu | Item horizontal padding 12 dp as an MD3 value | density table is the binding ADR-0002 set; MD3 menu item leading and trailing space not read |
| Menu | Open animation of short3 to short4 and 3 dp outline on forced colours | design choices, no MD3 value read |
| Dialog | Default width 312 dp | tess-ui default; MD3 spec page unreadable (min 280 and max 560 are verified in Material Web dialog scss) |
| Dialog | Full-screen form when the window is narrower than 328 dp | design choice derived from min width 280 plus 48 dp inset |
| Dialog | Action order dismissive then confirming, stacked order | from Material Web sample markup and Compose practice, spec page unreadable; stacked-action order not asserted |
| Dialog | Content beneath a modal dialog is hidden from the accessibility tree | not verified in tre or tess-ui |
| Dialog | A second dialog is refused while one is open | follows the Scrim note rule 7; MD3 guidance on stacked dialogs not read |
| Dialog | Dialog motion durations (500 ms open, 150 ms close, scrim 500 and 150) | Material Web implementation, not an MD3 spec value |
| Panel and Surface | Mapping of uses to container roles (window surface, pane surface_container_low, card surface_container) | MD3 defines the roles but a fixed mapping of uses was not read; follows tess-ui config app |
| Panel and Surface | Pane padding 12 dp default, 8 dp compact, 4 dp dense | design choice, not in the ADR-0002 binding numbers |
| Panel and Surface | Scheme change repaint with 300 ms animation | design choice |
| 12 Overlays | Z-order ranks (content, sheets, snackbar, popup, modal, tooltip) | Tesserae design choice, not an MD3 or tre rule (tre stacks by order of opening) |
| 12 Overlays | Window focus loss closes tooltips and non-modal popups but not dialogs | design choice, aligned with xdg_popup explicit grab semantics for popups |
| 12 Overlays | Opening a popup hides tooltips, opening a modal closes popups | design choice, derived from shell behaviour (a tooltip never opens over a focused popup) |

Back to [[90 Research]].
