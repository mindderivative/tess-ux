---
title: Frame
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, shell, frame, layer-shell, owner-feedback]
related: ["[[Panel and Surface]]", "[[Bar]]", "[[Popup]]", "[[Peek]]", "[[Auto Hide]]", "[[Dock]]", "[[Frame#Anatomy|Frame Ring]]", "[[Frame#Anatomy|Frame Strip]]", "[[Frame|Frame Surface]]", "[[Frame#Frame join: rendering decisions|Frame Join]]", "[[Frame#Frame join: rendering decisions|Meld Join]]", "[[Frame#Anatomy|Frame Meld]]", "[[Frame#Tokens used|Frame Border]]", "[[Frame#Anatomy|Reserved Space]]", "[[Frame#Anatomy|Input Region]]", "[[Auto Hide|Content Fade]]", "[[Layer Window]]", "[[Keyboard Navigation|Shortcut Mode]]", "[[12 Overlays]]", "[[Owner Feedback 2026-11-20]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[Spacing and Density]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Frame

> [!info] Summary
> A Frame is a ring of reserved space around one monitor, with square outer corners and rounded inner corners, that can hold strips (thick edges that act as bars) and melded Panels that grow out of it. Tesserae-only element with no Material Design 3 counterpart; the nearest patterns are the [Navigation rail](https://m3.material.io/components/navigation-rail/overview) and [Top app bar](https://m3.material.io/components/top-app-bar/overview) for a strip, and the [Shape](https://m3.material.io/styles/shape/overview) scale for the corner radii. Source of truth in code: see Status in code.

A Frame is not an MD3 element. This note specifies the whole surface: reserved space, layers, input, monitors, keys, accessibility, and the decisions about how a join is drawn. The ring, a strip, a melded Panel, a join and a border each have a note of their own ([[Frame#Anatomy|Frame Ring]], [[Frame#Anatomy|Frame Strip]], [[Frame#Anatomy|Frame Meld]], [[Frame#Frame join: rendering decisions|Frame Join]], [[Frame#Frame join: rendering decisions|Meld Join]], [[Frame#Tokens used|Frame Border]]); this note holds the rules that cross them.

## Purpose

Frame the desktop: reserve a band on every side of the monitor so windows stay inside it, give the shell edge strips that look like part of the ring, and let clicks in the opening go to the desktop.

## When to use and not

- Use when: the shell wants one continuous bezel with rounded inner corners, thick edges that hold modules, and docks or drawers that grow out of the ring.
- Do not use when: a single strip along one edge is enough ([[Bar]]); the surface floats or moves ([[Panel and Surface]], a Panel); the content is a menu ([[Popup]]).
- A strip does what a Bar does inside the Frame's surface. A Bar and a strip can share an edge (the strip holds icons, a Bar opens from the strip's inner edge); the icon-to-Bar link is open.

## Anatomy

1. Painter: one full-screen window per monitor on layer `TOP`, anchored to all four edges, `exclusive_zone` -1, input region following what is drawn. It draws the ring, corners, borders, strips and melded bodies as one tree.
2. Reservers: up to four thin windows per monitor, one per side whose total is above 0, on layer `TOP`, anchored to that side and both sides across it, 1 px on the short axis, `exclusive_zone` equal to the side total, empty input region. They draw nothing; they push maximised windows inside the ring.
3. Ring: an outer contour (the screen rectangle, outer corners square by default) and an inner contour (the opening, inner corners rounded), filled with the Frame colour.
4. Margin: transparent space between the ring and the display edge; it is added to the side total.
5. Borders: an inner border (facing the desktop) and an outer border (at the screen edge); each takes layout space.
6. Strips: per-edge thicker bands (`Edges`) that hold modules and blocks.
7. Melded Panels: Panels drawn inside the painter with a join to the ring.
8. Peek tabs and handles: see [[Peek]].

## Variants

| Variant | Keys | Use |
|---|---|---|
| Plain ring | `Thickness` only | Bezel with no content |
| Ring with strips | `Edges { Top { Thickness, Children } }` | Edge bars hosted in the ring ([[Frame#Anatomy|Frame Strip]]) |
| Ring with melded Panels | Panels with `Meld: true`, `Attach_To: <Frame>`, no `Margin` | Dock or drawer that grows out of the ring ([[Frame#Anatomy|Frame Meld]], [[Dock]]) |
| Ring with margin | `Margin` above 0 | Frame inset from the display edge |
| Per-side thickness | `Thickness { Top: 8, Left: 24 }` or `[left, top, right, bottom]` | Unequal bands; a side of 0 reserves nothing |

## States

| State | Visual change | Token values |
|---|---|---|
| Shown | Ring, strips and melded Panels drawn; reservers hold their zones | fill `surface` |
| Hidden (`Visible: false`, or `Hide` with `Target`) | Nothing drawn; reservers closed, zones released | not applicable |
| Strip contracted / expanded / peek | Strip at base thickness / full thickness / pushed out over windows | see [[Peek]], [[Frame#Anatomy|Frame Strip]] |
| Fullscreen window on the monitor | The Frame and its reservers hide until the window leaves fullscreen | not applicable |
| Monitor removed | All of the Frame's windows close; created again when the monitor returns | not applicable |

The ring has no pointer state of its own; modules in strips carry the state layers ([[State Layers]]).

## Tokens used

| Part | Role or token |
|---|---|
| Ring fill | `surface` by default (shell `$color.surface`); a colour or gradient through `Style { Background }`; a joining surface repeats this colour |
| Inner and outer border | `outline_variant` by default when written; width in dp; a role, a token or a gradient |
| Content in strips | `on_surface`, `on_surface_variant` |
| Outer corner radius | `none` 0 dp by default; a square outer corner touches the monitor's own corner |
| Inner corner radius | any value of the [[Shape]] scale (4, 8, 12, 16, 28); the shell example uses 14, which is off the scale and is allowed as a literal radius today |
| Elevation | level 0 (the ring casts no shadow); `Elevation`, `Shadows`, `Shadow_Bleed` are not built |
| Motion | thickness is not animated; slide and join animation 200 ms ([[Motion]] `short4`) with `emphasized` easing from the shell tokens |

Roles and shell mapping: [[Colour Roles]]. Radii are in [[Shape]]. Shadows from the painter need no transparent bleed margin because the painter covers the output ([[Elevation]]).

## Sizing and density

Side total = `Thickness` + each border width + `Margin` on that side. Examples: thickness 10 gives 10; with a 2 px border 12; with a 2 px inner and a 2 px outer border 14; with `Margin: [5, 5, 5, 5]` and one 2 px border 17.

- A ring with no strips has no density level: thickness is a design value in dp.
- A side used as a strip holds controls, so its thickness is at least the tallest control plus 8 dp, as for a [[Bar]]: 48 dp at default, 40 at compact, 36 at dense #needs-verification (design choice). The base thickness of a strip that peeks can be smaller.
- A peek tab or handle needs at least 8 dp of thickness; see [[Peek]].
- Changing a thickness changes a reserver's zone in one step and windows reflow once. It is not animated.
- Radii larger than the band allows are reduced and a warning names the key.

## Layout and overflow

- The top and bottom strips own the corner squares and run the full width of the output; the left and right strips run between them and lay their children out vertically. Text is not rotated.
- A corner is laid out with the horizontal strip that reaches it.
- Strip content ends in an ellipsis at its maximum width and never paints outside the band ([[10 Layout Overflow and Scrolling]]).
- Where a melded Panel meets the ring, one path contour draws the ring and the join with a fillet that uses the Frame's inner corner radius; the join, not the Panel, owns that corner.
- A Panel with a `Margin` on a Frame-facing side does not meld: the Frame edge continues straight and the Panel's corners round as a floating Panel's do. A Bar with a `Gap` above 0 on the Frame-facing side does not meld either.

## Behaviour

- Pointer: a press on the ring or a strip is taken by the shell; a press in the opening, or in the notch of a concave corner, passes to the desktop. The ring's hit shape is `painted`; the compositor input region follows the same shape (`auto`). A shadow takes no clicks.
- Keyboard: `Keyboard: NONE` is the default; the painter takes `ON_DEMAND` when any strip holds a text input (a warning if `NONE` was written). Keyboard-only access is through [[Keyboard Navigation|Shortcut Mode]]: `Enter_Shortcut_Mode` puts a Frame with `Shortcut_Mode: true` in focus and every peek of the Frame shows at once; `Next_Focus` and `Previous_Focus` cycle panels, peeks, bars and strips by `Tab_Index`. Mode keys arrive only if the compositor gives the surface the keyboard (`Debug { Mode_Keyboard }`, default `EXCLUSIVE`; not yet checked on KWin).
- Show and hide: `Show`, `Hide` and `Toggle` with `Target: <name>` act on a Frame, a melded Panel and a strip with a `Name` and a `Peek`. A hidden Frame releases every reserved zone; a shown one restores them, each in one reflow.
- Layer: `TOP` only. A different layer is a load error.
- Fullscreen: a fullscreen window covers the Frame and releases its zones on that monitor.
- Multi-monitor: one Frame per monitor, each a complete ring with its own thickness and corners. A monitor with no Frame gets none. Whatever lies between stacked monitors is left alone.
- Plasma coexistence: both reserve space; on one edge the compositor orders the zones. #needs-verification.
- Touch: strips follow [[Bar]] hit-area rules.

## Tooltip and overlay behaviour

The Frame itself carries no tooltip. A control in a strip puts its tooltip on the control ([[Tooltip]], [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]); a popup from a strip module is a Popup surface ([[Popup]]). A melded Panel that must draw over the ring is hosted in the painter, so no layer order applies; a melded Panel in its own window uses `overlay` and shows up to one frame of seam while moving.

## Motion

- Strip expand and contract, peek slide, melded Panel show and hide: the visual extent is animated inside the painter, which is full-screen; reserved space changes in steps (set the zone first then animate out; animate in then set the zone).
- Content fades with the slide by default (`Content_Fade`, accepted 2026-11-08), see [[Auto Hide|Content Fade]]; a plain show and hide fades too.
- Reduced motion: every transition is instant (strips switch state, the chevron changes direction at once, no fade).
- An idle Frame draws no frames.

## Accessibility

- The ring is decoration: the painter's nodes are hidden from the accessibility tree and are not focusable; the reserving windows are empty.
- Content in strips is reachable by keyboard like any module and carries roles, labels and states ([[Accessibility Rules]] AR-1 to AR-9).
- The handle of a peek should be a focusable button named "Expand dock"; it is not today (see [[Peek]]).
- Contrast: text on the ring fill at least 4.5 to 1; a border or handle that identifies a control at least 3 to 1 ([[Accessibility Rules]] AR-16, AR-17). High contrast takes the border colour and background from the high-contrast tokens.
- Announcements go through one window of the shell (the Frame, else the Bar) by owner decision of 2026-11-19 ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]).

## Dark and light

The ring fill, borders and strip content resolve from the scheme ([[ADR-0005 Theme follows the system]]). The Frame colour is the colour the melded surfaces repeat. A shell with no `Appearance.Stylesheets` key uses the `Default` stylesheet (shell ADR-0022), so strip text is readable in both schemes (owner feedback S1, [[Owner Feedback 2026-11-20]]).

## Defaults

| Setting | Default |
|---|---|
| `Layer` | `TOP` (only value) |
| `Corner_Radius` (outer) | 0 |
| `Inner_Radius` | 0 |
| `Margin`, `Padding` | 0 |
| `Visible` | `true` |
| `Keyboard` | `NONE` |
| Ring fill | `surface` (proposed role default; the shell asks for `Background` and ships none) |
| `Debug { Frame_Join }` | `PARAM` |
| `Debug { Frame_Blend }` | `LINEAR` |

## Frame join: rendering decisions

Decided by the owner on 2026-11-07 (record: `shell-vault:40 Specifications/Surfaces/Frame.md`, "KWin Retests and the Join Choice"):

- The default join of a melded Panel is PARAM, a parametric path driven by `animate_param`. SMIL (an `svg` contour morph) is second. STRUCTURE, SHADER and CONCAVE stay selectable through `Debug { Frame_Join }`. The owner's order at 100 percent scale was PARAM, SMIL, SHADER, STRUCTURE, CONCAVE; at 150 percent PARAM, SMIL, STRUCTURE, SHADER, CONCAVE.
- The join is one path contour: the ring and every hosted meld are drawn together, with a fillet at each join that uses the Frame's inner corner radius (decided 2026-11-06). The fillet grows with the slide; a join that shows a 90 degree angle and then a chamfer fails the owner's look test of 2026-11-06.
- Cost of the five options (KWin, 1920 by 1080): mean `total_ms` 1.3 to 1.7 per frame while animating, 0 idle frames; SMIL keeps more video memory after a slide (10.6 to 19.0 MiB against 0 to 1.1 MiB); SHADER is the only one that redraws part of the frame.
- Remaining look fault (owner, 2026-11-07): the border looks slightly thinner at the rounding than on straights. The code session measured a summed linear-light brightness of 1.70 on a curve against 2.00 on a straight at 1x (sRGB edge blending). The shell answers with `Frame_Blend: LINEAR` (default): the ring is drawn by one shader that blends in linear light; it falls back to paths, with one warning, for a translucent colour, an `Opacity` below 1, a `FADE` body, or more than eight melded bodies. The engine-side fix is the request `shell-vault:80 Requests/TRE-REQ-015 Linear-Light Edge Blending.md`. Not re-measured here.
- Detail of the join shapes: [[Frame#Frame join: rendering decisions|Meld Join]], [[Frame#Frame join: rendering decisions|Frame Join]].

## Acceptance criteria

Check types follow [[Test Method]]. Geometry checks run at scale 1.0, 1.25 and 2.0 unless stated.

- [ ] AC-FRM2-1 (geometry check, side total): `Thickness: 10` reserves 10 on that side; with a 2 px inner border 12; with a 2 px inner and a 2 px outer border 14; with `Margin: [5, 5, 5, 5]` and one 2 px border 17. Pass: 4 of 4 equal to the dp, measured as the reserver's `exclusive_zone`.
- [ ] AC-FRM2-2 (geometry check, reservers): with `Thickness { Top: 8, Left: 24 }` exactly two reservers exist, with zones 8 and 24, anchored to their side and both sides across it; a maximised window on KWin starts 8 px below the top and 24 px from the left. Pass: reserver count 2, zones and window origin equal.
- [ ] AC-FRM2-3 (scripted input, click-through): a press on the ring is taken by the shell (handler count 1); a press at a point at least 3 dp inside the opening, and at a point at least 3 dp inside the unfilled notch of a concave corner, reaches the window underneath. Pass: counts 1, 0, 0. The engine may take a press up to about 2 px inside a curve, so points nearer than 3 dp are not tested.
- [ ] AC-FRM2-4 (pixel check, corners): with `Inner_Radius: 14` and a 10 dp band, the pixel at (10 + 3, 10 + 3) from the output corner equals the ring fill and the pixel at (10 + 7, 10 + 7) has alpha 0; with default `Corner_Radius` the pixel at (0, 0) equals the ring fill. Pass: equal to the sampled values (tolerance 1 px in position).
- [ ] AC-FRM2-5 (scripted input, radius clamp): `Inner_Radius: 100` on a 10 dp band loads with one warning naming the property and draws the largest radius the band allows; no pixel lies outside the band. Pass: warning count 1; the pixel check of AC-FRM2-4 holds at the clamped radius.
- [ ] AC-FRM2-6 (scripted input, hide and show): `Hide` on the Frame releases all reserver zones (a maximised window fills the output) and `Show` restores them; each reserver receives one configure per change. Pass: zones 0 then equal to the side totals; configure count 1 per reserver per change.
- [ ] AC-FRM2-7 (scripted input, thickness step): changing `Thickness` on a running Frame changes each affected zone in one step with no intermediate zone values. Pass: sampled zones over 500 ms are the old value then the new value only.
- [ ] AC-FRM2-8 (scripted input, fullscreen, hand check on KWin): a fullscreen window on a monitor hides the Frame and releases its zones on that monitor; leaving fullscreen restores them. Pass: zone 0 then restored; the other monitor's Frame unchanged.
- [ ] AC-FRM2-9 (scripted input, multi-monitor): with two monitors each has its own Frame windows (painter plus reservers); removing one monitor closes only its windows and re-adding it creates them again within 2 s. Pass: window counts and geometry equal.
- [ ] AC-FRM2-10 (pixel check, idle): over 5 s with no animation and no module update the Frame commits 0 frames. Pass: frame count 0.
- [ ] AC-FRM2-11 (scripted input, not-built keys): writing each of `Children`, `Border_Tile`, `Meld`, `Exclusive_Zone`, `Input_Region`, `Class`, `Elevation`, `Shadows`, `Shadow_Bleed` on a Frame yields a loader message naming the key as not built (`Children`, `Meld`, `Exclusive_Zone`, `Input_Region`, `Border_Tile` are errors, `Class` a warning). Pass: 9 of 9. When a key is built its row is replaced by its own criterion; a built shadow takes no clicks (a press in it reaches the window below).
- [ ] AC-FRM2-12 (scripted input, keyboard mode): a Frame with no text-input strip has painter keyboard `none`; with a strip that holds a `TextInput` it is `on_demand`, and writing `Keyboard: NONE` there logs one warning. Pass: mode values and warning count as stated.
- [ ] AC-FRM2-13 (AT tree assertion): the ring nodes are hidden from the accessibility tree and not focusable; each interactive module in a strip has a role and a non-empty name. Pass: 0 ring nodes in the tree; 0 unnamed interactive nodes.
- [ ] AC-FRM2-14 (token test and contrast script): the ring `Background` and border colours are roles or tokens, not hex literals, except in a documented swatch; text in a strip reaches 4.5 to 1 on the ring fill in light, dark and high contrast. Pass: 0 literals; 6 of 6 pairs.
- [ ] AC-FRM2-15 (scripted input, layer): `Layer: OVERLAY` or `BOTTOM` on a Frame is a load error naming the key. Pass: error count 1.
- [ ] AC-FRM2-16 (token test, join default): with no `Debug { Frame_Join }` the join mode is `PARAM`; the five values `PARAM`, `SMIL`, `STRUCTURE`, `SHADER`, `CONCAVE` load, any other is an error; `Frame_Blend` defaults to `LINEAR`. Pass: 5 of 5 accepted, default values as stated.
- [ ] AC-FRM2-17 (pixel check, join at idle): at idle, the row of pixels across the seam between a melded Panel body and the ring has a colour difference of 0 from the Frame fill at every pixel (no gap, no hairline) at scale 1.0 and 1.5. Pass: 0 differing pixels (see AC-PNL-9).
- [ ] AC-FRM2-18 (pixel check, join during the slide): at slide progress 0.5 the join corner is rounded: the pixel 0.2 radii along the diagonal from the inner corner is Frame fill and the pixel 0.5 radii along the diagonal is not, for the default `PARAM` join. Pass: both samples as stated; no frame shows a right-angle corner.
- [ ] AC-FRM2-19 (geometry check, join cost): while a join animates at 1920 by 1080 the mean `total_ms` per frame is at most 2.0, and idle frames are 0. Pass: mean at most 2.0 ms (measured 1.3 to 1.7 for all five joins).
- [ ] AC-FRM2-20 (pixel check, border at the rounding): the summed linear-light brightness across a 2 px border at the middle of a fillet is at least 95 percent of that across a straight stretch, at scale 1.0 and 1.5. Pass: ratio at least 0.95 (threshold is a proposal #needs-verification; the sRGB blend measured 0.85).
- [ ] AC-FRM2-21 (geometry check, input region size): for a 3840 by 2160 output with a 48 dp band, inner radius 24 and ten join fillets, the input region has at most 256 rectangles and a press more than one band away from a curve is classified correctly. Pass: rectangles at most 256; 0 misclassified presses beyond one band.
- [ ] AC-FRM2-22 (geometry check, fractional scale): at scale 1.5 the ring's inner edge in device pixels equals the reserved zone times 1.5 rounded to a whole pixel (within 1 device pixel), and a maximised window touches the ring edge with no gap. Pass: difference at most 1 device pixel. Not measured to date.
- [ ] AC-FRM2-23 (scripted input, keyboard-only): `Enter_Shortcut_Mode` then `Next_Focus` visits every strip, peek and melded Panel of the Frame once in `Tab_Index` order; `Exit_Shortcut_Mode` restores the previous focus. Pass: visit list equals the element list. Hand check on KWin until the mode's keyboard is confirmed.
- [ ] AC-FRM2-24 (scripted input, version check): with an engine older than the shell's floor the shell stops at start with a message naming the required version. Pass: message contains the version number.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/surfaces/frame.py`, `ring.py`, `outline.py`, `join.py`, `join_param.py`, `join_shader.py`, `frame_shader.py`, `handle.py`, `tess-shell:docs/guide/surfaces.md#frame`, `tess-shell:docs/guide/settings.md#debug` | Partly meets. Built: ring, margin, per-side thickness, inner and outer borders, radii, strips, melded Panels, peek, hide and show, `Frame_Join` (default `PARAM`), `Frame_Blend` (default `LINEAR`). Not built: `Children`, `Border_Tile`, `Meld` on the Frame, `Exclusive_Zone`, `Input_Region`, `Class`, `Elevation`, `Shadows`, `Shadow_Bleed` (AC-FRM2-11). The owner's join choice is in force (AC-FRM2-16). Measurements recorded in the shell vault (1.3 to 1.7 ms per frame, 66 region rectangles) support AC-FRM2-19 and AC-FRM2-21 but were not re-run here. AC-FRM2-20 should now hold through the LINEAR shader; not measured. AC-FRM2-22 and AC-FRM2-23 unmeasured (fractional scale; Shortcut Mode keyboard on KWin). A melded Panel ignores its own `Background`, `Fill`, `Opacity`, `Elevation`, `Shadows` and `Shadow_Bleed`: it is drawn in the Frame's colour. |
| shell vault | `shell-vault:40 Specifications/Surfaces/Frame.md`, `shell-vault:90 Research/Hit Testing for Concave Corners.md` | Source design and the owner's KWin records of 2026-11-06, 2026-11-07, 2026-11-08. |
| tess-ui | not applicable | tess-ui draws window chrome ([[Window]], [[Title Bar]]), not a screen frame. |
| tre | `tre:docs/reference/layer-window.md`, `tre:docs/reference/paint.md` | Mechanism only: `LayerWindow`, `path` with `hit_shape="painted"`, `input_region="auto"`, linear, radial and sweep gradients, `animate_param`. Not applicable as a component. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A ring that reserves screen space has no MD3 counterpart | desktop shell element | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Concave inner corners of 14 dp (off the shape scale) allowed as a literal | the owner chose the look; the scale has no named concave radius | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Square outer corners by default (shape `none`) | the outer corner meets the monitor's own corner | none (owner decision of 2026-10-27) |
| Thickness 48, 40, 36 dp for a strip (MD3 rail width 80 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Reserved space steps, it never animates | one configure round trip per change | none (compositor limit) |

## Sources

- Shape scale values 0, 4, 8, 12, 16, 28 and full: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss (verified 2026-11-21).
- Navigation rail 80 dp default width: https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md.
- Layer-shell protocol: https://wayland.app/protocols/wlr-layer-shell-unstable-v1.
- WCAG 2.2 SC 1.4.3 and 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html , https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html ; SC 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html.
- Shell: `shell-vault:40 Specifications/Surfaces/Frame.md`, `shell-vault:40 Specifications/Surfaces/Surface Types.md`, `shell-vault:90 Research/Hit Testing for Concave Corners.md`; `tess-shell:src/tess_shell/surfaces/frame.py`, `tess-shell:src/tess_shell/schema/docs.py`, `tess-shell:docs/guide/surfaces.md#frame`, `tess-shell:docs/guide/settings.md#debug` (origin/main, 2026-11-21).
