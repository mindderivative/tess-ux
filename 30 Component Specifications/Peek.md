---
title: Peek
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, shell, peek, frame, owner-feedback]
related: ["[[Frame]]", "[[Frame Strip]]", "[[Frame Meld]]", "[[Meld Join]]", "[[Peek Handle]]", "[[Peek Trigger]]", "[[Content Fade]]", "[[Auto Hide]]", "[[Bar]]", "[[Dock]]", "[[Attached Panel]]", "[[Panel and Surface]]", "[[Popup]]", "[[Shortcut Mode]]", "[[Global Shortcuts]]", "[[Drag Interaction]]", "[[Surface Animation]]", "[[12 Overlays]]", "[[Colour Roles]]", "[[Motion]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Peek

> [!info] Summary
> A peek makes a melded Panel or a Frame strip rest as a thin tab or sliver that comes out on hover, click or drag. Tesserae-only behaviour; the nearest Material Design 3 pattern is the [Bottom sheet](https://m3.material.io/components/bottom-sheets/overview) with a peek height, a collapsed state and a drag handle. Source of truth in code: see Status in code.

A peek is not an MD3 element. The bottom sheet gives the vocabulary (a collapsed state that shows only a peek height, a handle that takes a tap or a drag, a handle that assistive technology can expand and collapse); the values here come from the shell design and the owner's decisions of 2026-11-07 and 2026-11-08.

## Purpose

Let a dock, drawer or strip stay out of the way and come out when the user asks, without moving windows (the reserved space does not change) and without hiding the way back.

## When to use and not

- Use when: a melded Panel or a Frame strip should rest as a sliver ([[Frame Meld]], [[Frame Strip]], [[Dock]]).
- Do not use when: a whole Bar should hide (use [[Auto Hide]]; a Bar peek is not built); the surface is an unmelded Panel (it has Show, Hide and an `Animation`, see [[Panel and Surface]]); the content is a menu ([[Popup]]).
- A hover-only peek hides content from keyboard and touch users: pair `HOVER` with `CLICK` or a shortcut ([[Accessibility Rules]]).

## Anatomy

1. Tab or sliver: `Size` dp of the body standing out of the ring edge, with no content shown. It is the pointer target.
2. Body: the Panel or strip; slides out along its slide axis.
3. Handle: a small icon on the tab (dots, bar or chevron); part of the Frame painter, never a click target of its own.
4. Contour: the ring and body drawn as one path with fillets ([[Meld Join]]).
5. Content: faded with the slide ([[Content Fade]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Melded Panel peek | Dock or drawer | `Peek { }` inside a Panel with `Meld: true`; may use `Slide_From` in a corner |
| Strip peek | A Frame edge that rests as a sliver | `Peek { }` inside an `Edges` entry; needs `Children` and a `Name` to be shown and hidden by name |
| `Trigger: HOVER` | Default | Opens after `Enter_Delay`, closes after `Exit_Delay` |
| `Trigger: CLICK` | Pointer click | Opens on a click on the tab, closes on a click on the handle again |
| `Trigger: DRAG` | Pull to open | The body follows the pointer; released at 50 percent or more it opens |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest (tab) | `Size` dp of the body visible, content hidden, handle at rest opacity | handle opacity 0.6 (`Handle_Opacity`) |
| Pointer on the tab | handle opacity rises to 1 | `Handle_Opacity` to 1.0 |
| Opening / closing | body slides along the contour, content fades with the progress | 200 ms, shell `standard` easing |
| Out | full depth; chevron points toward the Frame | handle at rest opacity |
| Dragging | body follows the pointer | no timing |
| Keyboard focus on the Frame in Shortcut Mode | every peek of the Frame shows at once | see Behaviour |

## Tokens used

| Part | Role or token |
|---|---|
| Handle colour | the Frame's inner border colour, else its outer border colour, else a light or dark grey chosen from the fill luminance (shell literals 235 or 30 grey) |
| Handle opacity at rest | `Handle_Opacity`, default 0.6 |
| Body | the Frame's fill (`surface`); a melded body ignores its own style keys |
| Motion | slide duration and easing from the Panel `Animation` or shell tokens ([[Motion]]); chevron direction follows the slide progress |

The handle colour is a literal in code, not a role; see Deviations and AC-PEK-14.

## Sizing and density

| Item | Value |
|---|---|
| Tab or sliver depth (`Size`) | default 24 dp, at least 1 dp and below the Panel `Depth` or strip thickness |
| Hover delays | `Enter_Delay` 150 ms, `Exit_Delay` 300 ms |
| Click-or-drag threshold | a press that moves under 4 dp is a click and toggles |
| Drag decision | released at 50 percent of the full depth or more opens; below returns |
| Handle box: dots | 24 by 8 dp, three circles of diameter 6 dp with centres at 4, 12 and 20 dp along the box |
| Handle box: bar | 22 by 4 dp, corner radii 1.5 by 1 dp |
| Handle box: chevron | 24 by 8 dp, a filled wedge 22 dp wide and about 6.7 dp high |
| Handle minimum | drawn only when the tab depth and the side thickness are each at least 8 dp |
| Hit area of the tab | at least 24 by 24 dp (WCAG 2.2 SC 2.5.8) |

The reserved space is the base thickness in every state; a peek never pushes windows. Density does not change these values; a strip that holds controls follows the [[Bar]] thickness rule.

## Layout and overflow

- The handle sits at the middle of the visible tab, centred along the edge, and moves with the far edge of the contour while it slides.
- A handle that does not fit is not drawn; this is not a load error and logs nothing above debug level.
- Content stays hidden in the tab; it does not paint outside the body ([[10 Layout Overflow and Scrolling]]).
- A Panel in a Frame corner touches two edges; `Slide_From` names the edge it slides out of and the handle sits on that edge. An edge the Panel does not touch is a load error. The default is the edge the Panel is attached to.

## Behaviour

- Pointer, `HOVER`: the pointer on the tab for `Enter_Delay` brings the body out; the pointer off the tab and off the body for `Exit_Delay` sends it back. The body stays open while the pointer is on it (the revealed content stays hoverable).
- Pointer, `CLICK`: a click on the tab or sliver opens it fully; a click on the handle closes it. No hover action.
- Pointer, `DRAG`: a press on the tab then a move pulls the body along its slide axis; release at 50 percent or more opens it, below returns it; under 4 dp of movement toggles it.
- `Trigger` takes one value or a list (`[HOVER, DRAG]`); a list is not built (the loader says a Peek takes one value). `Handle: AUTO` takes the icon of the first trigger.
- Keyboard: no focusable handle exists yet. The ways in are the `Show`, `Hide`, `Toggle` actions and `Toggle_<Name>` shortcuts ([[Global Shortcuts]]), and [[Shortcut Mode]]: `Enter_Shortcut_Mode` shows every peek of the Frame at the same time; `Next_Focus` and `Previous_Focus` cycle through its panels, peeks, bars and strips by `Tab_Index`. This is the owner's decision of 2026-11-10; the mode's keys arrive only if the compositor gives the Frame the keyboard (not yet checked on KWin).
- Touch: a tap acts as a click; a drag as a drag; the tab is at least 24 by 24 dp, 48 by 48 in a touch context.
- Faint content can be clicked during a slide because the engine delivers pointer events to a node at opacity 0; accepted until a mis-mapped click is seen.

## Tooltip and overlay behaviour

The handle has no tooltip: it is not a click target ([[Tooltip]]). The revealed body is part of the Frame's surface, not an overlay; it is not modal and takes no scrim. Dismissal is by the trigger rule above, not by Escape; Escape belongs to the focused module ([[12 Overlays]]).

## Motion

- Slide: the contour animates the body along its slide axis with the Panel's `Animation` duration (default 200 ms) and easing ([[Surface Animation]]); the join and the chevron run on the same clock and easing, with no Python per frame.
- Chevron: one path with the same command sequence in both states; parameter 0 (collapsed) points away from the Frame, 1 (out) points toward it; it changes direction with the slide progress.
- Content fade: content opacity equals the slide progress (0 collapsed, 1 out) with the slide's duration and easing, on by default, for a peek slide and drag, a plain show and hide of a melded Panel, and strip children with their strip; `Content_Fade: false` turns it off (accepted 2026-11-08).
- `Handle_Opacity` does not change while the handle travels; hover raises it to 1.
- Reduced motion: no slide animation, no fade, the chevron switches at once, the body is in its end state on the next frame.

## Accessibility

- The design asks for a focusable handle named "Expand dock" (the Edge Shell's rule). It needs a focus model that does not exist yet; until then Shortcut Mode and the show actions are the non-pointer way, and the handle nodes are drawn with `hit_testable=False` and are not exposed.
- A hover-only peek is content on hover: it stays open while the pointer is on the body, can be closed by moving away, and does not hide the control that opened it (WCAG 2.2 SC 1.4.13).
- Contrast: the handle at rest is a non-text mark that identifies the control; it needs 3 to 1 against the fill (SC 1.4.11). With the shell's fallback greys on the Default theme fills the default 0.6 gives 6.09 (dark) and 4.31 (light); the least opacity that keeps 3 to 1 is about 0.37 (dark) and 0.48 (light). A project that lowers `Handle_Opacity` below 0.5 re-runs the contrast check.
- Target size: the tab is at least 24 by 24 dp. A `Size` below 24 dp relies on the equivalent keyboard controls (SC 2.5.8 exception for an equivalent control); record it in the project.
- Reduced motion: see Motion.

## Dark and light

The handle colour and the body follow the scheme through the Frame fill and borders. The fallback grey chosen from the fill luminance keeps the handle readable in both schemes; with a border colour set, the handle takes that colour.

## Defaults

| Setting | Default |
|---|---|
| `Size` | 24 dp |
| `Enter_Delay`, `Exit_Delay` | 150 ms, 300 ms |
| `Trigger` | `HOVER` |
| `Handle` | `AUTO` (`DOTS` for `HOVER`, `BAR` for `DRAG`, `CHEVRON` for `CLICK`) |
| `Handle_Opacity` | 0.6 |
| `Slide_From` | the edge the Panel is attached to |
| `Content_Fade` | `true` |

## Acceptance criteria

Check types follow [[Test Method]]. Timings are measured on the engine clock in a headless test (the drag and hover cases also run as a hand check on KWin).

- [ ] AC-PEK-1 (geometry check, rest): a melded Panel with `Peek { Size: 24 }` at rest shows exactly 24 dp of its body outside the ring edge and no content pixels; the reserved zone equals the base thickness. Pass: visible depth 24 dp; zone unchanged in every state (rest, opening, out, closing).
- [ ] AC-PEK-2 (scripted input, hover timing): pointer enter on the tab, then 149 ms: the body has not moved; at 150 ms plus one frame it starts to move; pointer leave then 299 ms: still out; at 300 ms plus one frame it starts to return. Pass: moves as stated (tolerance one frame).
- [ ] AC-PEK-3 (scripted input, hover grace): with the body out, the pointer moves from the tab onto the body within 100 ms and stays; after 2 s the body is still out. Pass: state out at 2 s.
- [ ] AC-PEK-4 (scripted input, click): with `Trigger: CLICK`, hovering for 2 s opens nothing; a click on the tab opens the body fully; a click on the handle closes it. Pass: states closed, closed, out, closed.
- [ ] AC-PEK-5 (scripted input, drag): with `Trigger: DRAG`, a press then a move of 3 dp then release toggles it; a drag released at 49 percent of the full depth returns it; released at 50 percent opens it; during the drag the body edge is within 1 dp of the pointer along the slide axis. Pass: states as stated.
- [ ] AC-PEK-6 (token test, handle choice): `Handle: AUTO` draws dots for `HOVER`, a bar for `DRAG` and a chevron for `CLICK`; `NONE` draws nothing; `DOTS`, `BAR`, `CHEVRON` force the shape. Pass: 6 of 6 cases.
- [ ] AC-PEK-7 (geometry check, handle size and fit): the dots box is 24 by 8 dp with circle centres at 4, 12 and 20 dp (diameter 6); the bar box is 22 by 4 dp; the chevron box is 24 by 8 dp; with a tab depth or side thickness of 7 dp no handle is drawn and no error or warning is logged. Pass: sizes equal within 0.5 dp; draw count 0 and log count 0 at 7 dp, 1 at 8 dp.
- [ ] AC-PEK-8 (pixel check, handle opacity): at rest the handle's pixels equal the handle colour blended at 0.6 over the fill (±2 per channel); with the pointer on the tab they equal the colour at 1.0; `Handle_Opacity: 0.3` shows 0.3; the value does not change while the handle travels. Pass: sampled colours as stated.
- [ ] AC-PEK-9 (scripted input, opacity range): `Handle_Opacity: 0`, `0.6` and `1` load; `1.1` and `-0.1` are load errors naming the key. Pass: 3 accepted, 2 errors.
- [ ] AC-PEK-10 (pixel check, chevron): at progress 0 the chevron apex points away from the Frame; at progress 1 toward it; at progress 0.5 the apex lies on the middle line of the box (±1 dp), and the direction changes monotonically over the slide. Pass: apex positions as stated at 0, 0.5 and 1.
- [ ] AC-PEK-11 (scripted input, Slide_From): a Panel in the top-right corner with `Slide_From: TOP` slides out of the top edge with its handle on the top edge; with `RIGHT` out of the right edge; with `LEFT` (an edge it does not touch) loading fails with an error naming the key. Pass: slide axes as stated; error count 1.
- [ ] AC-PEK-12 (pixel check, content fade): at slide progress 0.5 the content's opacity is 0.5 (±0.05) and follows the slide's easing; with `Content_Fade: false` it is 1 at every progress; content stays hidden in the tab. Pass: opacities as stated.
- [ ] AC-PEK-13 (scripted input, reduced motion): with reduced motion on, a trigger puts the body in its end state on the next frame, content opacity is 0 or 1 only, and the chevron has its end direction. Pass: end state on frame 1; no intermediate sample.
- [ ] AC-PEK-14 (contrast script, handle at rest): the handle colour at the default 0.6 against the Frame fill reaches 3 to 1 in the dark, light and high contrast modes. Pass: 3 of 3 (computed: 6.09 dark, 4.31 light for the fallback greys; high contrast not computed). A handle colour that is a hex literal fails the token rule of [[Panel and Surface]] AC-PNL-2 and is listed as a finding.
- [ ] AC-PEK-15 (scripted input, keyboard way in): `Toggle_<Name>` (or `Show` with `Target`) opens and closes a named peek with no pointer event; `Enter_Shortcut_Mode` shows every peek of the Frame at once. Pass: states as stated. Hand check on KWin for the mode.
- [ ] AC-PEK-16 (AT tree assertion): the tab or its handle exposes a role `button` and the name "Expand <name>" while collapsed and "Collapse <name>" while out. Pass: both names present. Status today: fails (handle nodes are not exposed).
- [ ] AC-PEK-17 (geometry check, target size): the pointer-sensitive tab is at least 24 by 24 dp (48 by 48 in a touch context); a `Size` below 24 dp is allowed only when AC-PEK-15 passes. Pass: hit area read from the engine hit test.
- [ ] AC-PEK-18 (scripted input, single value): `Trigger: [HOVER, DRAG]` today produces a load error that says a Peek takes one value; when a list is built this criterion becomes: both triggers work and `AUTO` takes the first. Pass: error text as stated.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/surfaces/frame.py` (peek state, `_handle_colour`), `tess-shell:src/tess_shell/surfaces/handle.py`, `tess-shell:src/tess_shell/surfaces/mode.py`, `tess-shell:docs/guide/surfaces.md#peek`, `tess-shell:src/tess_shell/schema/docs.py` | Partly meets. `Size` 24, `Enter_Delay` 150, `Exit_Delay` 300, `Trigger` HOVER/CLICK/DRAG, `Handle`, `Handle_Opacity` 0.6, `Slide_From`, `Content_Fade` and reduced-motion handling are built, and the owner's KWin check of 2026-11-08 passed ("Everything implemented looks good"; the middle of the chevron turn is not visible). Fails AC-PEK-14 in part (handle colour is a literal grey or the border colour, not a role), AC-PEK-16 (handle nodes `hit_testable=False`, not exposed), AC-PEK-18 (single trigger only). Untested for lack of a demo knob: `Size` and a button inside a panel body. AC-PEK-3 (body stays open under the pointer) and AC-PEK-17 were not checked in code. AC-PEK-15 holds through the show actions; Shortcut Mode keyboard on KWin unchecked. |
| shell vault | `shell-vault:40 Specifications/Surfaces/Frame.md` (Peek Triggers and Handles, M3 Final Pass), `shell-vault:_attachments/Handle Icons/` | Source design; three SVG handles by the owner. |
| tess-ui | not applicable | tess-ui has dock panels and a docking host ([[Dock]]); no peek. |
| tre | `tre:docs/guide/animation.md` (`animate_param`) | Mechanism only. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Three handle icons (dots, bar, chevron) tell the trigger; MD3 bottom sheet has one drag handle | the owner's design from the Fabric version, 2026-11-07 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Handle 24 by 8 dp, not a 48 dp touch target | the owner's design; the tab is the target and is at least 24 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Handle rest opacity 0.6, adjustable | owner decision 2026-11-08 | none (owner decision) |
| A hover trigger opens a peek | desktop pointer; MD3 sheets open by touch | none (desktop shell) |
| The reserved space never changes | a peek must not move windows | none (compositor limit) |

## Sources

- Bottom sheet peek height, collapsed state, drag handle that handles accessibility commands, 48 dp minimum handle target (Material Components Android): https://github.com/material-components/material-components-android/blob/master/docs/components/BottomSheet.md (verified 2026-11-21).
- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html ; SC 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html ; SC 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; SC 2.3.3: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html.
- Shell: `shell-vault:40 Specifications/Surfaces/Frame.md`, `shell-vault:40 Specifications/Surfaces/Panel.md`, `shell-vault:_attachments/Handle Icons/`; `tess-shell:src/tess_shell/surfaces/handle.py`, `tess-shell:src/tess_shell/surfaces/frame.py`, `tess-shell:docs/guide/surfaces.md#peek` (origin/main, 2026-11-21).
- Contrast values computed for this note from the WCAG formula with the shell fallback greys (235 and 30) over `#12171D` and `#F4F7FA`.
