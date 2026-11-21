---
title: Deviations from MD3
type: register
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [register, md3]
related: ["[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[10 UX Design Specification]]"]
depends_on: []
---

# Deviations from MD3

The register of every departure from Material Design 3 recorded in the notes, with its reason and decision (chapter 16 of the UX Design Specification). Each row is owned by the note named in its section (one source of truth); this note only collects them, so a change is made in the owning note and re-collected here. Policy: [[ADR-0006 MD3 baseline with named Expressive adoptions]]. 521 rows from 141 notes as of 2026-11-22; notes with no deviation rows: 0.

## [[03 Typography and Text Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| List, tree and menu text uses `body_medium` at compact and dense | the 20 dp line box must fit 32 and 28 dp rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Labels never wrap; single-line truncation with a tooltip on the control | desktop controls with fixed row heights; owner feedback F5 | [[ADR-0004 Tooltip rule]] |
| Vertical centring by construction at all densities | owner feedback F7 | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell type names map to the nearest role | shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[04 Shape Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| Popup takes `extra_small` | MD3 has no popup; menu value used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No shape change on state or press | baseline scale only; Expressive shape morphing is not adopted | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| List rows are square (`none`) | desktop rows run edge to edge for density | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell shape names are shifted by one step | shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[05 Elevation Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| Containers for level 4 and 5 are `surface_container_highest` | no component token file gives them; keeps the ladder monotonic | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Regions of a window separate by tone at level 0, not by shadow | desktop windows have many neighbouring regions | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell keeps one scalable shadow | shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[06 Motion Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| Desktop duration limits (control change at most 200 ms) | pointer-driven UI; MD3 durations are phone-scale | [[ADR-0002 Desktop density levels and target sizes]] |
| No focus ring animation, no caret blink, no marquee | testable in one frame; accessibility | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Springs excluded from the baseline | Expressive | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[08 Iconography Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| Material Design Icons, no weight, fill, grade or optical size | static path set used by all projects | [[ADR-0007 Icon set and Material Symbols deviation]] |
| 20 and 16 dp icons at compact and dense | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Every icon-only control has a tooltip | desktop keyboard-first and pointer use, no label to read | [[ADR-0004 Tooltip rule]] |

## [[09 State Feedback Rules]]

| Deviation | Reason | ADR |
|---|---|---|
| Focus and pressed layers 10 percent | latest published tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| One layer at a time with fixed precedence | avoids stacked opacity | [[ADR-0009 State layer percentages]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0009 State layer percentages]] |
| Ring for pointer focus in text inputs; no ring animation | caret may be hidden; testable in one frame | [[ADR-0009 State layer percentages]] |
| Reason tooltip on disabled controls | desktop users need to know why | [[ADR-0004 Tooltip rule]] |

## [[10 Layout Overflow and Scrolling]]

| Deviation | Reason | ADR |
|---|---|---|
| Scrollbars always visible on desktop when content overflows, both axes | MD3 treats scrollbars as a platform concern; the owner reported unreachable content | [[ADR-0003 Scrollbar rule]] |
| Middle ellipsis allowed for paths | the end of a path is the part that identifies it | [[ADR-0004 Tooltip rule]] |
| Tooltip with full value on truncated text | desktop pointer affordance | [[ADR-0004 Tooltip rule]] |
| Single-line field height 40, 32, 28 dp with vertical centring (MD3 56 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[11 Interaction]]

| Deviation | Reason | ADR |
|---|---|---|
| Keyboard-first model: roving groups, typeahead, F6, Escape order | Material Design describes touch first; desktop use needs a complete key map (principle 1) | [[ADR-0002 Desktop density levels and target sizes]] covers target sizes only; the key map itself has no ADR #needs-verification-as-design-choice |
| Hover layer 8 and focus layer 10 percent with focus winning | Material Web latest tokens; older tokens use 12 | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Hover grace of 150 ms for all tooltips and tooltip on keyboard focus | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Cursor shapes, double click timing, drag threshold, context menu keys | MD3 specifies none for pointer input | none; design choices |
| Scrollbar hit area 12 dp below 24 dp target | equivalent keyboard scrolling | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] |

## [[15 Writing]]

| Deviation | Reason | ADR |
|---|---|---|
| Sentence case for titles and dialog headlines where the ux-writing skill sets title case | every shipped string uses sentence case; one rule is easier to lint | none; recorded here and in [[Deviations from MD3]] #needs-verification-as-design-choice |
| Hard character limits on labels, tooltips and messages | testable rule; Material Design gives guidance, not limits | none; design choice |
| Keyboard shortcut hint in the tooltip and label | desktop keyboard-first use ([[11 Interaction]]) | none |
| Material Design writing guidance for components is script-rendered and not read by tools | the rules above come from the ux-writing skill, WCAG and project strings | #needs-verification |

## [[17 Conformance]]

| Deviation | Reason | ADR |
|---|---|---|
| Material Design 3 has no conformance model; this chapter is Tesserae's own | the vault turns rules into testable criteria; [[01 Principles and Scope]], principle 7 | [[ADR-0010 Document structure of the specifications]] |
| Result values `not testable` and `not applicable` added to [[Test Method]]'s three | a criterion about an absent element or an undrivable platform is neither a failure nor "not run" | none; Test Method is to be aligned |
| Version tags and levels are Tesserae design choices | no external standard prescribes them for this vault | none #needs-verification-as-design-choice |

## [[Colour Roles]]

| Deviation | Reason | ADR |
|---|---|---|
| Role names from MD3, values from a project's own flat roles in tess-shell (12 roles, mapping above) | The shell is independent of tess-ui and ships its own theme format | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Light `on_*_container` roles at tone 10 (2022 scale), not tone 30 (latest token set) | The 2022 role scale is the baseline | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| High contrast level requires 7:1 for every text pair | Tesserae choice, matches WCAG 1.4.6; the measured baseline already meets it | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| `outline_variant` limited to decoration | Its measured contrast is under 3:1 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Custom colours (warning, success) with four derived roles | MD3 defines the extension method but no warning or success role | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Elevation]]

| Deviation | Reason | ADR |
|---|---|---|
| Container role for levels 4 and 5 is `surface_container_highest` | No component token file read gives a level 4 or 5 container; choice keeps the ladder monotonic | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Popup container at level 2 | MD3 has no popup; the menu level is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell expresses elevation as a percentage of one shadow | The shell has its own flat token set; an adoption of levels is not decided | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Focus Ring]]

| Deviation | Reason | ADR |
|---|---|---|
| No ring animation (MD3 grows the ring to 8 dp and shrinks it) | animation adds nothing for desktop use; keeps the ring testable in one frame | [[ADR-0009 State layer percentages]] |
| Ring also shown for pointer focus in text inputs | the caret may be hidden when the window is not active; pointer users need to see which field has focus | [[ADR-0009 State layer percentages]] |
| Inward ring where the control touches a clip edge | prevents clipping in scroll containers | [[ADR-0009 State layer percentages]] |
| Optional gradient ring | Tesserae identity option | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Iconography]]

| Deviation | Reason | ADR |
|---|---|---|
| Material Design Icons instead of Material Symbols; no weight, fill, grade, optical size axes | existing icon set in all projects, engine draws static paths | [[ADR-0007 Icon set and Material Symbols deviation]] |
| 20 dp icon at compact and dense (also in the 24 dp dense list and tree row, which leaves 2 dp above and below), 16 dp only where nothing else fits | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Fallback icon is a broken-image glyph | MD3 states no fallback; a visible glyph exposes the missing name | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[Motion]]

| Deviation | Reason | ADR |
|---|---|---|
| `emphasized` is a single cubic (0.2, 0, 0, 1) | The two-segment path cannot be expressed in the engines' easing forms; Material Web does the same | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Desktop limits on duration (control change at most 200 ms) | Pointer-driven desktop UI; MD3 durations are phone-scale | [[ADR-0002 Desktop density levels and target sizes]] |
| Springs are not in the baseline | Expressive; adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell keeps 3 duration tokens | Shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Scrim]]

| Deviation | Reason | ADR |
|---|---|---|
| One scrim opacity (0.32) for every modal surface | Material Web uses 0.32 for the dialog; Android uses other values per component; one value is testable | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Scrim fade-in of 500 ms is a Material Web value | Verified in Material Web; a desktop shortening is not decided | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Shape]]

| Deviation | Reason | ADR |
|---|---|---|
| Expressive steps 20, 32 and 48 dp excluded from the baseline | Baseline is the 2022 shape scale; Expressive adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell scale has 5 steps with names shifted by one | The shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Popup container radius `extra_small` | MD3 has no popup; the menu value is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Spacing and Density]]

| Deviation | Reason | ADR |
|---|---|---|
| Three density levels (default, compact, dense) | MD3 specifies touch-first sizes; desktop forms and trees need more rows per screen | [[ADR-0002 Desktop density levels and target sizes]] |
| Desktop minimum target 24 dp (touch 48 dp) | WCAG 2.2 SC 2.5.8 gives 24 CSS px as the AA minimum; MD3 states 48 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Text field 40 dp high at default (MD3 56 dp) | row economy on desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Menu item 40 dp at default (Material Web 48 px) | same | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 (MD3 16) and icon gap 8, 8, 4 (MD3 16) | narrow side panels | [[ADR-0002 Desktop density levels and target sizes]] |
| Spacing token set with a 2 dp half step | the shell already ships a 2 dp step; focus ring offset is 2 dp | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[State Layers]]

| Deviation | Reason | ADR |
|---|---|---|
| Focus and pressed use 10 percent (the latest MD3 tokens), not the 12 percent of older tokens | follows the current published tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| One layer at a time, with precedence | avoids stacked opacity that changes contrast unpredictably | [[ADR-0009 State layer percentages]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0009 State layer percentages]] |

## [[Theme Following the System]]

| Deviation | Reason | ADR |
|---|---|---|
| Selection of scheme, override and flash rules are Tesserae-specific | MD3 specifies the schemes, not how an application chooses one | [[ADR-0005 Theme follows the system]] |
| Pending surface and re-theme budget values | Design choices to make the no-flash rule testable | [[ADR-0005 Theme follows the system]] |

## [[Typography]]

| Deviation | Reason | ADR |
|---|---|---|
| tess-ui applies tracking 0 for all roles | Engine and theme defaults predate the tracking table; flagged as a gap to close, not a design choice | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Dimensions in dp equal px at scale 1.0 | Projects scale by the window scale factor | [[ADR-0002 Desktop density levels and target sizes]] |
| The 5 shell type roles map to the nearest MD3 role | Shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Single-line text vertical centring and ellipsis rules | Desktop controls; owner feedback F5 and F7 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Accessibility Tree]]

| Deviation | Reason | ADR |
|---|---|---|
| Engine-level contract for the tree | MD3 states principles and no tree API | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| `disabled` does not stop input in the engine; controls must | engine design | [[ADR-0004 Tooltip rule]] |

## [[Accordion]]

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | settings grouping | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Header heights 40, 32, 24 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Open and close use different durations and easings | decelerate in, accelerate out is the MD3 pattern for enter and exit; applied by analogy | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Active Descendant]]

| Deviation | Reason | ADR |
|---|---|---|
| Tesserae-specific behaviour (MD3 has none) | search-and-list patterns keep focus in the field | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Anchored Placement]]

| Deviation | Reason | ADR |
|---|---|---|
| Overlays clipped to the window, not to the control | desktop windows | [[ADR-0004 Tooltip rule]] |
| Tooltips and menus placed by the engine's flip and shift rule | MD3 gives no algorithm | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Application Window]]

| Deviation | Reason | ADR |
|---|---|---|
| Desktop window with minimum size, drag regions and resize border | MD3 specifies content for window size classes, not the window | [[ADR-0002 Desktop density levels and target sizes]] |
| Minimum pane width 320 dp and the minimum window rule | desktop panes; chapter 10 | [[ADR-0010 Document structure of the specifications]] |

## [[Applications Module]]

| Deviation | Reason | ADR |
|---|---|---|
| Search is a type-to-filter list inside a panel, not an MD3 search bar and view | launcher pattern; the MD3 search bar is 56 dp high with a full shape, the field here follows [[Text Field]] densities | [[ADR-0002 Desktop density levels and target sizes]] |
| Row density 40, 32, 24 and two-line 60, 48, 40 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Audio Module]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status control | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltips per control, none on the root group | owner feedback F8 | [[ADR-0004 Tooltip rule]] |
| Icon button sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Audio Outputs]]

| Deviation | Reason | ADR |
|---|---|---|
| Single-choice marker is a bullet in the end slot, not a leading check | the shell Menu Item has no check slot; shape plus the word in the name | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row heights by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Auto Hide]]

| Deviation | Reason | ADR |
|---|---|---|
| Hide on pointer absence and show on pointer presence at the edge (MD3 Top app bar: scroll direction) | a desktop shell has a pointer and no scrolling content under the Bar | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| On by default with opt-out | owner decision 2026-10-27 | none (owner decision) |
| Hide and show take the same duration (MD3 and the Tesserae motion rule: exit shorter than enter) | one `Animation` block for both directions | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| The reserved zone changes once at the end of the hide and the start of the show | a zone change is a configure round trip; animating it would reflow windows on every frame | none (compositor limit) |

## [[Badge]]

| Deviation | Reason | ADR |
|---|---|---|
| Badge size does not scale with density | a badge is decoration on a host; shrinking it below 6 or 16 dp would lose legibility | [[ADR-0002 Desktop density levels and target sizes]] |
| Default `max` 99 (MD3 gives no limit; Android truncates only when set) | two of three projects and the shell design use 99; the pill stays at most 4 characters wide | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Badge carries no tooltip and no live announcement | the host owns the name, tooltip and announcement | [[ADR-0004 Tooltip rule]] |
| Disabled host dims the badge to 38 percent | state rule of [[State Layers]]; MD3 gives no badge disabled state | [[ADR-0009 State layer percentages]] |

## [[Banner]]

| Deviation | Reason | ADR |
|---|---|---|
| A banner component is specified although the current MD3 specification lists none | desktop apps need a persistent in-flow message (disk change, offline); Material Web keeps tokens for it | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Severity variants `tertiary_container` and `error_container` | MD3 has one container; severity needs a non-text cue and a role per level | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Heights 52, 44, 36 for single line | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Assertive live region allowed for a decision banner only | one-time interrupt for what must be acted on; MD3 gives no accessibility rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Vibrant and standard container pairs of the newer tokens not adopted | Expressive-era; adopt by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Divider colour `outline_variant` instead of `surface_variant` | `surface_variant` is a legacy role in the vault ([[Colour Roles]]) | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Bar]]

| Deviation | Reason | ADR |
|---|---|---|
| A Bar has no MD3 component; it reserves screen space through layer-shell | desktop shell element | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Fill `surface` at level 0 instead of the Navigation bar's `surface_container` at level 2 | the shell ground colour is the Bar ground; separation by tone, shadow only when floating | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Thickness 48, 40, 36 dp (MD3 Navigation bar 80 dp) | desktop density, one-line modules | [[ADR-0002 Desktop density levels and target sizes]] |
| Text is not rotated on a vertical Bar | readability; rotation is opt-in and not built | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Keyboard default is none; access by Shortcut Mode | a layer surface that grabs the keyboard unasked steals it from windows | none (shell design of 2026-10-27) |

## [[Battery Module]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status module; baseline MD3 only for roles and shape names | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Roles `warning` and `error` for state text | the shell theme has no MD3 tertiary or extended roles; state keeps a second cue | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Bitmap]]

| Deviation | Reason | ADR |
|---|---|---|
| Image block with four fit modes | shell block set; MD3 has no image primitive | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Box]]

| Deviation | Reason | ADR |
|---|---|---|
| Container primitive with no MD3 counterpart; padding steps are the Tesserae scale (2 dp half step) | MD3 defines no container block or spacing tokens | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Children share one cell instead of stacking | Tesserae block set decision R1 (shell vault); stacking is [[FlexBox]] | [[ADR-0010 Document structure of the specifications]] |

## [[Button Group]]

| Deviation | Reason | ADR |
|---|---|---|
| Button group (standard and connected) adopted though Expressive | needed for the choice and action sets | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Gap 8 dp standard (4 dp dense); Android default is 12 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Per-mode Tab stops (single: one, others: each) | desktop keyboard-first and APG | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 28 dp; paddings reduced at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon 16 dp at dense | 28 dp container | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs, m, l, xl (32 to 136 px) and the square shape, pressed squaring (Expressive) | tess-ui implements Expressive sizes; the baseline is the 2022 scale | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Pointer hit area is the container (24 dp floor), 48 dp only in touch contexts | desktop density, WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus ring 3 dp, 2 dp offset, `secondary` | [[Focus Ring]] | [[ADR-0009 State layer percentages]] |

## [[Canvas]]

| Deviation | Reason | ADR |
|---|---|---|
| Imperative drawing block | MD3 has none; charts are app specific | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Card]]

| Deviation | Reason | ADR |
|---|---|---|
| Padding, gaps and media height scale with the three density levels | desktop information density; MD3 gives one touch size | [[ADR-0002 Desktop density levels and target sizes]] |
| Selected container `secondary_container` (outlined: border `outline`) | MD3 defines a checkable card in Android (checked icon) but the Material Web card tokens have no selected state; Tesserae uses the tonal selected pattern of other components #needs-verification | [[Deviations from MD3]] |
| Draggable card must also be movable by keyboard | WCAG 2.2 SC 2.5.7 Dragging Movements; MD3 shows only the pointer drag | [[Accessibility Rules]] |
| Hover on a plain card has no feedback | a card that cannot be pressed must not look pressable; MD3 tokens define hover for an interactive card | [[Deviations from MD3]] |
| Dragged elevation taken from Material Web tokens, not from the Android guide | the sources differ; one value is testable | [[Deviations from MD3]] |

## [[Carousel]]

| Deviation | Reason | ADR |
|---|---|---|
| Caption band `scrim` at 0.60 with caption text `on_scrim` | the image does not follow the theme, so no role pair under the image guarantees 4.5:1; the band at 0.60 gives 5.7:1 over a white image; no colour literal remains | [[ADR-0016 Carousel caption colour]] |
| Scrollbar thumb shown whenever items overflow | owner rule for every scroll container | [[ADR-0003 Scrollbar rule]] |
| Gap, caption band and small item width scale with density | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Items do not resize continuously while scrolling (not built) | engine has no per-item size animation tied to scroll; MD3 describes the effect | [[Deviations from MD3]] |
| Full-screen layout not specified | no desktop use case; touch layout | [[Deviations from MD3]] |
| No auto-advance by default; opt-in with pause | WCAG 2.2 SC 2.2.2 and reduced-motion rule | [[Motion]] |
| Arrow keys, Home and End move between items | desktop keyboard-first use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |

## [[Checkbox]]

| Deviation | Reason | ADR |
|---|---|---|
| Row height 40, 32, 28 dp; state layer 32 dp at compact and 28 dp at dense; box 16 dp at dense | desktop rows; the layer must not exceed the row | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum; 48 dp only in touch contexts | WCAG 2.2 SC 2.5.8; desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp, role `secondary` | foundation rule for all controls | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Space toggles; Enter optional | follows the WAI-ARIA Authoring Practices | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Error also exposes `invalid` and supporting text | MD3 shows error by colour; WCAG 1.4.1 and 3.3.1 need more | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule only) |

## [[Chip]]

| Deviation | Reason | ADR |
|---|---|---|
| Container 28 dp at compact and 24 dp at dense (MD3 32 dp) | desktop rows; 24 dp keeps the minimum target | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed layer 10 percent; focus ring 3 dp, offset 2 dp, role `secondary` instead of the outline colour change | foundation rule for all controls | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Delete or Backspace removes a focused input chip; the close button is not a keyboard stop | desktop keyboard-first use; fewer Tab stops | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Single-choice filter chips are `radio` with a `radiogroup`, arrows choose | APG radio group model | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Maximum width 256 dp with ellipsis and tooltip | overflow rule of chapter 10 | [[ADR-0004 Tooltip rule]] |

## [[Choice Picker]]

| Deviation | Reason | ADR |
|---|---|---|
| Built as a modal Dialog, not an anchored menu | the config app picks options with long hints in a narrow window; recorded as built, anchored form is the target | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hint as supporting text, not as a tooltip | tooltips are for controls only | [[ADR-0004 Tooltip rule]] |
| Rows 40, 32, 24 dp (Material Web menu item 48 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Type-ahead buffer 1 s (Material Web 200 ms) | consistent with [[List]] | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Circle]]

| Deviation | Reason | ADR |
|---|---|---|
| Disc as a block | no MD3 block; shape scale has `full` only as a corner value | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Clock Module]]

| Deviation | Reason | ADR |
|---|---|---|
| Tooltip and Clock have no MD3 counterpart | Tesserae-specific status module; nearest pattern is the MD3 plain tooltip | [[ADR-0004 Tooltip rule]] |
| Hover grace for the plain tooltip | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Hover box minimum 24 dp | desktop target floor | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Colour Picker]]

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | MD3 chooses colours for a theme, not content; desktop editors need a square, strips, fields | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Trigger and field heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Contrast row with truncated ratio | WCAG 1.4.3 and 1.4.11 apply to a colour the user picks | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Focus and pressed state layer 10 percent | latest Material Web tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Tooltips on swatches and handles, not on the surface | owner feedback | [[ADR-0004 Tooltip rule]] |

## [[Date Picker]]

| Deviation | Reason | ADR |
|---|---|---|
| Day pitch 40, 32, 28 dp and dialog width 328, 280, 280 dp (MD3 modal 360 dp, 48 dp cells in docked) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Fixed six-row grid | the dialog keeps its height; the number of rows MD3 shows is not verified #needs-verification | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (layout only) |
| Keyboard model, grid roles and day names follow the APG date picker dialog | MD3 gives no keyboard rules | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Docked picker commits on selection; modal commits on OK | MD3 modal has OK and Cancel; docked has none | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Invalid typed date shows the field error and disables OK | WCAG 3.3.1 error identification; MD3 shows a field error only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Range picker not specified | not built; no project use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Dialog]]

| Deviation | Reason | ADR |
|---|---|---|
| Several actions allowed in the full-screen header | tess-ui allows `Actions` list there; MD3 has one confirming action | [[Deviations from MD3]] |
| Dialog metrics do not scale with density | Rare, spacious surface; actions still follow density | [[ADR-0002 Desktop density levels and target sizes]] |
| Alert dialog is a `dialog` role where `alertdialog` is missing | Engine limit | [[Deviations from MD3]] |

## [[Divider]]

| Deviation | Reason | ADR |
|---|---|---|
| Emphasised variant in `outline` | `outline_variant` is below 3 to 1; a divider that is the only separating cue must pass WCAG 1.4.11 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Space inside lists and menus is 8, 4, 4 dp by density | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| No heavy 8 dp divider | Android-only option; not in the Material Web tokens | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Insets stay 16 dp at all levels | alignment across levels; MD3 value kept | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Dock Panel]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has no dock panel; tabs are the nearest) | desktop tool windows | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tab height 40 at compact and 32 at dense (MD3 secondary tab container 48) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tabs are draggable between zones and halves, with a menu alternative | MD3 tabs are fixed; docking needs movement | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed layers 10 percent, dragged 16 | Material Web latest state tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Inward focus ring | the tab touches the strip edge | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Close button on a tab, 24 dp hit area | desktop panels are dismissable; MD3 tabs have no close | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Dock]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has no dock; nearest are the navigation rail and canonical layouts) | desktop tool windows hold many rearrangeable panels | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tab strip follows the MD3 secondary tab (48 dp) but adds drag, a menu and a roving Tab stop | MD3 tabs are not draggable; desktop users move panels | [[ADR-0002 Desktop density levels and target sizes]] |
| Handle hit area 24 dp, grip 4 by 48 dp | desktop pointer minimum | [[ADR-0002 Desktop density levels and target sizes]] |
| Drop highlight `primary` at 16 percent | dragged state layer value | [[ADR-0009 State layer percentages]] |

## [[Drag and Drop]]

| Deviation | Reason | ADR |
|---|---|---|
| Required non-drag alternative for every drag | WCAG 2.2 SC 2.5.7 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Dragged layer 16 percent, as MD3 | none | [[ADR-0009 State layer percentages]] |

## [[Expander]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific reveal primitive; [[Accordion]] covers the disclosure with a header | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Duration 200 ms standard easing | a desktop control change is at most 200 ms | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Extended Floating Action Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense heights 40 and 32 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor | desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| State layer 10 percent for focus and pressed | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Other deviations as [[Floating Action Button]] | shared | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[File Dialog]]

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | desktop applications need a file chooser; built from MD3 dialog, list, text field, menu | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row 40, 32, 24 dp and padding 12, 8, 4 dp | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltips on toolbar buttons and truncated names only, never on rows | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |
| Entry list scrollbar always visible when it overflows | desktop pointer use | [[ADR-0003 Scrollbar rule]] |
| Panel width 480 to 1080 dp (MD3 and [[Dialog]] 280 to 560 dp) | a file list with size and time columns needs width | [[ADR-0002 Desktop density levels and target sizes]] |
| Middle ellipsis for paths | the end of a path identifies it | [[ADR-0004 Tooltip rule]] |

## [[FlexBox]]

| Deviation | Reason | ADR |
|---|---|---|
| Gap defaults 8, 8, 4 dp by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| No MD3 counterpart for a layout block | MD3 specifies layout by grid and canonical layouts, not by primitives | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Floating Action Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense FAB sizes (small 32 and 28, medium 48 and 40) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor; 48 dp only in touch contexts | WCAG 2.2 SC 2.5.8, desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed state layer 10 percent (Material Web v0_192 has 12) | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Disabled FAB defined (MD3 has none) | a view may need to show an unavailable action | [[ADR-0009 State layer percentages]] |
| Lowered, branded and FAB menu variants not adopted | no desktop use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Font List]]

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | desktop apps pick installed fonts | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Trigger and rows 40, 32 and 28 or 24 dp (MD3 menu item 48 dp in Material Web) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrollbar visible when the list overflows | desktop pointer use | [[ADR-0003 Scrollbar rule]] |
| Tooltip on the trigger and truncated name only | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |

## [[Form Row]]

| Deviation | Reason | ADR |
|---|---|---|
| A settings row pattern that MD3 lacks | configuration tools are lists of named values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Label beside the control, not a floating or in-field label | scan by label column, fixed grid | [[ADR-0002 Desktop density levels and target sizes]] |
| Persistent reset button | defaults matter in config files | none; design choice |

## [[Frame]]

| Deviation | Reason | ADR |
|---|---|---|
| A ring that reserves screen space has no MD3 counterpart | desktop shell element | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Concave inner corners of 14 dp (off the shape scale) allowed as a literal | the owner chose the look; the scale has no named concave radius | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Square outer corners by default (shape `none`) | the outer corner meets the monitor's own corner | none (owner decision of 2026-10-27) |
| Thickness 48, 40, 36 dp for a strip (MD3 rail width 80 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Reserved space steps, it never animates | one configure round trip per change | none (compositor limit) |

## [[Grid]]

| Deviation | Reason | ADR |
|---|---|---|
| Row and column gaps 12 and 8 dp at default (MD3 gutters 16 or 24 dp, touch layouts) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Grid is a container block, not a page layout grid | MD3 grid is a page-level concept (columns by window size class); page panes are specified in chapter 10 | [[ADR-0010 Document structure of the specifications]] |

## [[Icon Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Container 32 dp and 28 dp, icon 20 dp at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| 48 dp hit area only in touch contexts; pointer contexts use the container with a 24 dp floor | desktop density and WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs to xl, width kinds, square shape and pressed squaring (Expressive) only as named adoptions | MD3 baseline is the 2022 scales | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Icons from Material Design Icons, not Material Symbols | existing icon set | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[Icon Picker]]

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | desktop apps pick icons for launchers and blocks | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Icon set is Material Design Icons with Material Symbols names where they exist | existing assets | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Cell 48, 40, 32 dp; trigger 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on every cell | cells show no text; the tooltip is the name | [[ADR-0004 Tooltip rule]] |

## [[Image]]

| Deviation | Reason | ADR |
|---|---|---|
| An Image element is specified at all | MD3 has no image component; the spec uses the shape scale and card media rules | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Default fit `contain` (tess-ui view default is `cover`) | cropping loses content silently; cropping is an explicit choice | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Themed glyph error image instead of the shell's raster `error.png` | the glyph follows light, dark and high contrast | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Clip shapes limited to the corner scale | path masks are an Expressive shape set | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Tooltip only on an interactive image | tooltips belong to controls | [[ADR-0004 Tooltip rule]] |

## [[Key Chord Field]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no key chord field | settings app needs recorded shortcuts | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Field and button heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Recording state is shown by text and `pressed`, plus a container colour | colour must not be the only cue | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Label]]

| Deviation | Reason | ADR |
|---|---|---|
| Single-line read-only text; no MD3 component named Label | MD3 has type roles, not a Label component | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Ellipsis by default | silent clipping is a defect (F5) | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Launcher]]

| Deviation | Reason | ADR |
|---|---|---|
| A desktop launcher surface with exclusive keyboard, no scrim (MD3 Search view is a modal full-screen view on phone) | global search-and-start on a desktop; the owner chose no dimming | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| A click outside closes it and the click is swallowed | Wayland shows no outside press to a client; the click-away layer takes it | none (compositor limit) |
| Container `surface_container` at level 2 with a 12 dp radius and 20 percent shadow | shell flat roles and one scalable shadow | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Rows 40 dp single and two-line (MD3 list one line 56 dp #needs-verification) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Layer Window]]

| Deviation | Reason | ADR |
|---|---|---|
| Layer surfaces have no MD3 counterpart | desktop shell element | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Keyboard-exclusive panels are a dialog, not a popup | no grab without a user-action serial | [[ADR-0004 Tooltip rule]] |

## [[Link]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no link component | text that navigates is needed in help, about and settings | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Space does not activate a link, only Enter | link keyboard convention (WAI-ARIA link pattern) | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Underline on hover and focus for a standalone link; always for inline | colour must not be the only cue | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area extended to 24 dp at compact and dense | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[List Editor]]

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | MD3 has no editor for a list of values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on the icon buttons only | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |
| Alt+arrow keys to reorder, Delete to remove | keyboard-first desktop use | [[ADR-0002 Desktop density levels and target sizes]] |

## [[List Item]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 24 (one line) instead of 56 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Padding 12, 8, 4 dp and gap 8, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Disabled text 0.38 instead of MD3 label opacity 0.30 | one disabled content value across Tesserae ([[State Layers]]) | [[ADR-0009 State layer percentages]] |
| State layer focus and pressed 10 percent instead of the 12 percent listed in the Material Web tokens | decided state layer scale | [[ADR-0009 State layer percentages]] |
| Selected container `secondary_container` | MD3 list tokens give no selected container | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[List]]

| Deviation | Reason | ADR |
|---|---|---|
| Keyboard model from the WAI-ARIA listbox pattern; MD3 defines no list keyboard behaviour | desktop, keyboard first | [[ADR-0010 Document structure of the specifications]] |
| Densities per [[List Item]] | desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrollbar visible, no auto-hide | desktop | [[ADR-0003 Scrollbar rule]] |

## [[Marquee Text]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Hover and focus pause of the scroll | WCAG 2.2 SC 2.2.2 | [[ADR-0004 Tooltip rule]] |

## [[Media Module]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status control | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltip per control, none on the group | owner feedback F8 | [[ADR-0004 Tooltip rule]] |
| Control sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Menu Item]]

| Deviation | Reason | ADR |
|---|---|---|
| Row heights, icon size and padding by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Key hint is display only | keys are bound elsewhere | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Menu]]

| Deviation | Reason | ADR |
|---|---|---|
| Item height 40 / 32 / 28 dp (MD3: 48 dp) | Desktop density with a 24 dp minimum target; 48 dp kept for touch | [[ADR-0002 Desktop density levels and target sizes]] |
| State layers 8, 10, 10 percent on items | Same as MD3; the shell has none yet (gap, not a promise) | [[ADR-0009 State layer percentages]] |
| Tab closes the menu | WAI-ARIA Authoring Practices menu pattern; Material Web closes on focusout | [[Deviations from MD3]] |
| Typeahead buffer 500 ms, submenu hover delays 250 and 300 ms | Material Web defaults are 200 ms and 400 ms; shell values are built and decided in the shell vault | [[Deviations from MD3]] |

## [[Navigation Drawer]]

| Deviation | Reason | ADR |
|---|---|---|
| Destination height, paddings and width per density level (56, 40, 32 dp) | desktop information density; MD3 gives the 56 dp touch size | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrim 0.32 for the modal drawer; the Material Web drawer token is 0.4 with colour `neutral-variant20` | one scrim value and role for every modal surface | [[Scrim]] |
| Selection does not follow focus; Enter or Space chooses | a screen change per arrow press is disruptive; WAI-ARIA APG tabs allow selection to follow focus only when the panel loads instantly | [[14 Accessibility Basics]] |
| Standard and modal choice follows window size class and the 320 dp pane minimum | desktop layout chapter; MD3 and Android advise standard on tablet and desktop, modal on mobile | [[10 Layout Overflow and Scrolling]] |
| Home, End, Arrow keys and Escape specified | desktop keyboard-first use; MD3 documents no keyboard model (Android advises an Escape handler) | [[14 Accessibility Basics]] |
| Modal drawer swipe and edge gestures also reachable by keyboard | WCAG 2.2 SC 2.5.7 | [[Accessibility Rules]] |
| Frosted variant (72 percent container, 20 dp blur) | tess-ui effect; not an MD3 surface; kept as a named project effect | [[Deviations from MD3]] |
| Slide timings (400 ms in, 200 ms out) | not published as tokens; Tesserae choice | [[Deviations from MD3]] |

## [[Navigation Rail]]

| Deviation | Reason | ADR |
|---|---|---|
| Width, pill, spacing and expanded sizes per density level | desktop information density; MD3 gives touch sizes | [[ADR-0002 Desktop density levels and target sizes]] |
| Baseline 2022 rail (80 dp, active label `on_surface`); Expressive 96 dp width, 64 dp item and `secondary` label not adopted | ADR-0006 names each Expressive adoption; only the expanded rail is adopted | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Expanded rail adopted (Expressive); it replaces the standard drawer for few destinations | already built in tess-ui; fits desktop width | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Selection does not follow focus; Enter or Space chooses | a screen change per arrow press is disruptive; APG tabs allow selection to follow focus only when the panel loads instantly | [[14 Accessibility Basics]] |
| Arrow keys, Home and End specified | desktop keyboard-first use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |
| Rail removed at compact width; modal drawer takes over | MD3 puts a navigation bar at the bottom on compact windows, a touch pattern that Tesserae desktop does not specify | [[10 Layout Overflow and Scrolling]] |
| Vertical scroll of the destination column with a scrollbar | owner rule for every scroll container; MD3 does not specify overflow | [[ADR-0003 Scrollbar rule]] |
| Pill grows from the icon (Expressive) not adopted; the pill fades in | engine has no per-node size animation of this kind in the view; keeps motion simple | [[Deviations from MD3]] |

## [[Network Module]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status module | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Roles `warning` and `on_surface_muted` for state | second cue is the glyph | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Node Graph]]

| Deviation | Reason | ADR |
|---|---|---|
| Element with no MD3 counterpart, built from MD3 surface roles | tools need it | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Panning and zooming replace scrollbars on the canvas; no scrollbar is shown | the canvas has no content extent, so there is no extent to show (deviation from ADR-0003, keyboard pan and zoom required) | [[ADR-0017 Node Graph pans instead of scrolling]] |
| Dragged state layer 16 percent | MD3 dragged state | [[ADR-0009 State layer percentages]] |

## [[Pagination]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no pagination component | desktop result sets need a page control | none (Tesserae element) |
| Heights 40, 32, 28 dp and dot hit area 24 dp | desktop density and target size | [[ADR-0002 Desktop density levels and target sizes]] |
| One Tab stop with arrow keys, Home and End | desktop keyboard-first; same group rule as [[Toolbar]] | none |
| Non-current dots in `outline` (3 to 1) rather than a lower-contrast role | WCAG 2.2 SC 1.4.11 | none |

## [[Panel and Surface]]

| Deviation | Reason | ADR |
|---|---|---|
| Surface tint layer is not applied | tone steps and shadows carry depth in all three projects | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Shell uses 12 flat roles mapped to MD3 roles | shell independent of tess-ui (shell ADR-0006); mapping documented | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Shell elevation is one shadow scaled by a percentage | engine takes shadow lists; levels are a gap, not a promise | [[Deviations from MD3]] |
| Shell shape scale 0, 4, 8, 16, 999 | existing shell tokens; mapped to the MD3 names | [[Deviations from MD3]] |
| Shell surface types (Bar, Frame, Panel, Popup) and melding | desktop shell elements with no MD3 counterpart | [[Deviations from MD3]] |

## [[Path Block]]

| Deviation | Reason | ADR |
|---|---|---|
| Icon sizes 24, 20, 20 dp by density (MD3 24 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon set and its deviation | see the ADR | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[Peek]]

| Deviation | Reason | ADR |
|---|---|---|
| Three handle icons (dots, bar, chevron) tell the trigger; MD3 bottom sheet has one drag handle | the owner's design from the Fabric version, 2026-11-07 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Handle 24 by 8 dp, not a 48 dp touch target | the owner's design; the tab is the target and is at least 24 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Handle rest opacity 0.6, adjustable | owner decision 2026-11-08 | none (owner decision) |
| A hover trigger opens a peek | desktop pointer; MD3 sheets open by touch | none (desktop shell) |
| The reserved space never changes | a peek must not move windows | none (compositor limit) |

## [[Popup Window]]

| Deviation | Reason | ADR |
|---|---|---|
| Menu surface placed by the compositor, shadow in a transparent margin | Wayland protocol | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltip hover grace for all tooltips | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |

## [[Popup]]

| Deviation | Reason | ADR |
|---|---|---|
| A popup that takes text input is allowed; MD3 menus hold commands only | Launcher and search flyouts; the text input rule is needed because the outside-click mechanism broke typing on KWin | [[ADR-0001 MD3 role names are the specification vocabulary]] (vocabulary); behaviour recorded here |
| The popup-window route (`xdg_popup`) and its grab have no MD3 counterpart | MD3 is platform-agnostic; Wayland layer-shell hosts clip layers to the surface | [[Deviations from MD3]] |
| Outside click is consumed | MD3 menus dismiss on outside tap; whether the tap is consumed is not specified in the sources read | [[Deviations from MD3]] |

## [[Progress Indicator]]

| Deviation | Reason | ADR |
|---|---|---|
| Ring sizes 24 dp (compact) and 16 dp (dense) | a ring inside a 32 or 28 dp control must fit without changing its height | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell `ProgressBar` default 8 dp thick (MD3 4 dp) | legibility on a shell bar; kept as a shell choice #needs-verification | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Indeterminate indicators are still under reduced motion | the busy state is also exposed to assistive technology; the baseline takes the stricter rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Delay-to-show 300 ms and minimum visible time 500 ms | avoids flashing indicators on short operations on a desktop | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Expressive wavy, thick and morphing variants excluded | baseline is the 2022 system; adoption by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-ui ring box 48 dp (Material Web latest and Android: 40 dp) | the older MD3 spec size; the vault takes the latest token value | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Radio Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Row height 40, 32, 28 dp; ring 18 dp at dense; layer 32 and 28 dp | desktop rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Error state in `error` colours | the Material Web radio tokens define none; forms need group validation ([[Validation]]); only the group is exposed as invalid | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Focus and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Group keyboard model of the APG (arrows choose, wrap) | MD3 gives no keyboard rules; APG is the reference | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |

## [[Rectangle Block]]

| Deviation | Reason | ADR |
|---|---|---|
| Shape primitive with no MD3 counterpart | Tesserae shell blocks draw dividers and tracks | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Ring Block]]

| Deviation | Reason | ADR |
|---|---|---|
| A static ring block; MD3 only has the animated circular progress | block set of the shell | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Routed View]]

| Deviation | Reason | ADR |
|---|---|---|
| Routes, history, guards and back rules exist (MD3 states destinations only) | an application with many screens needs addressing and back behaviour | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Alt+Left and Alt+Right and mouse side buttons go back and forward | desktop convention; MD3 has the Android system back gesture | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Focus placement and screen announcement on a screen change | keyboard-first and screen-reader use; MD3 does not state them | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Fade through 300 ms (90 out, 210 in) from [[Motion]] | an MD3 transition pattern with Tesserae timings | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[SVG]]

| Deviation | Reason | ADR |
|---|---|---|
| An SVG element is specified; MD3 specifies icons and no SVG component | the stack draws icons and illustrations as SVG documents | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Icons come from Material Design Icons (Pictogrammers), not Material Symbols; no variable axes (weight, fill, grade, optical size) | the stack ships that set | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Reduced motion draws an animated SVG's first frame | MD3 does not specify; the vault baseline is no non-essential motion | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No scripts, no external references, size limits | a desktop shell reads untrusted files | [[ADR-0001 MD3 role names are the specification vocabulary]] (roles only; safety rule is Tesserae's) |

## [[ScrollBox]]

| Deviation | Reason | ADR |
|---|---|---|
| Visible scrollbar on both axes when content overflows | owner feedback F6 | [[ADR-0003 Scrollbar rule]] |
| Thumb opacity states and 12 dp hit area | accepted exception | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] |

## [[Scrollbar and Scroll Container]]

| Deviation | Reason | ADR |
|---|---|---|
| MD3 has no scrollbar component; Tesserae specifies one | desktop content overflows on two axes and needs a visible indicator | [[ADR-0003 Scrollbar rule]] |
| No auto-hide by default | desktop users need a permanent cue that content continues | [[ADR-0003 Scrollbar rule]] |
| Track-less thumb with opacity states instead of state layers | a thumb is an indicator, not a surface | [[ADR-0003 Scrollbar rule]] |

## [[Search]]

| Deviation | Reason | ADR |
|---|---|---|
| Bar height 40 and 32 dp at compact and dense (MD3 56 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Search field variant (a text field with role `searchbox`) beside the bar | filtering inside a dense panel needs no pill or elevation | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Down and Up move an active row while focus stays in the input; Escape steps through close, clear, deactivate | keyboard-first | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Global focus shortcut for the main search bar | keyboard-first | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Result updates debounced and not run on IME pre-edit text | desktop IME use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Segmented Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 28 dp; smaller paddings at dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Baseline (2022) segmented button kept although Expressive replaces it by the connected [[Button Group]] | both are specified; the segmented button is the compact form | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area is the segment with a 24 dp floor; 48 dp high only in touch contexts | WCAG 2.2 SC 2.5.8, desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed state layer 10 percent | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Multiple choice exposes `button` with `pressed` | the toggle button pattern fits a pressable segment | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Side Sheet]]

| Deviation | Reason | ADR |
|---|---|---|
| Width, header and paddings per density level | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Standard form only where the main content keeps 320 dp; else modal | pane minimum of the layout chapter; MD3 does not give a desktop rule | [[10 Layout Overflow and Scrolling]] |
| Standard sheet moves focus on user-initiated open; Escape closes it | keyboard-first desktop use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |
| Drag-to-dismiss of a modal sheet must also be reachable by keyboard | WCAG 2.2 SC 2.5.7 | [[Accessibility Rules]] |
| Detached sheet not specified | no desktop use case in the projects | [[Deviations from MD3]] |
| Scrim 0.32 for the modal sheet | one scrim value for all modals; Material Web drawer token uses 0.4 | [[Scrim]] |
| Slide timings (400 ms in, 200 ms out) | not published as tokens; Tesserae choice from [[Motion]] | [[Deviations from MD3]] |

## [[Slider]]

| Deviation | Reason | ADR |
|---|---|---|
| Hit band 40, 32, 28 dp; handle 16 dp and label 24 dp at dense | desktop rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Expressive sizes xs to xl adopted (track in pieces with 6 dp gap, 4 dp handle), default density only | tess-ui ships them; named adoption | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| 4 dp stop indicator at the inactive end in `on_surface_variant` | the inactive track `surface_container_highest` is below 3 to 1 against the surface; WCAG 1.4.11 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule; Material Components Android adds a 4 dp stop indicator for the same reason) |
| Value label is the handle's tooltip, shown on hover after 500 ms as well as on press and focus | tooltip belongs to the control; keyboard users see it on focus | [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Wheel does not change the value | a wheel over a slider in a scrolling panel changes a value by accident | [[ADR-0002 Desktop density levels and target sizes]] (desktop use) |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |

## [[Snackbar]]

| Deviation | Reason | ADR |
|---|---|---|
| Duration 4000 ms, 10000 ms with an action (Android presets 1500 and 2750 ms) | desktop reading time and WCAG 2.2.1; figures from Compose Material 3 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Messages queue (Android replaces the visible snackbar) | a result must not be lost | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 48, 40, 32 and two lines 64, 56, 48 (MD3 48 and 68) | density levels; padding on the 4 dp grid | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard path: last Tab stops and `Alt+Shift+N` (proposed default) | desktop keyboard-first; MD3 describes touch | [[ADR-0019 Banner and snackbar focus chords]] |
| Role `status` with polite live region, never assertive | assertive is reserved for what must be acted on | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Focus ring role `inverse_primary` on the snackbar (vault ring role is `secondary`) | `secondary` has too little contrast on `inverse_surface` #needs-verification | [[ADR-0009 State layer percentages]] |

## [[Spacer]]

| Deviation | Reason | ADR |
|---|---|---|
| Spacer exists as a block; MD3 has none | bars need end-aligned groups | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Spin Box]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no spin box | desktop settings need stepped numbers | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 40, 32, 28 dp (MD3 text field 56 dp, icon button 40 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| The step buttons are outside the Tab order, the field is one tab stop | keyboard-first forms: Up and Down already step | [[ADR-0002 Desktop density levels and target sizes]] (target sizes only; the tab-stop rule is a Tesserae convention) |
| Role `spinbutton` instead of a plain textbox | MD3 has no spin box; WAI-ARIA defines it | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Split Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Split button adopted although it is an Expressive component (not in the 2022 baseline) | useful for save and send with variants | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 40, 32, 28 dp and smaller trailing widths | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Two Tab stops and Up/Down menu keys on both parts | desktop keyboard-first | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Splitter]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has drag handles in canonical layouts, no splitter) | desktop panes are resized by the user | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Handle hit area 24 dp (touch 48 dp) | desktop pointer minimum per WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard operation per the APG window splitter (arrows, Enter, Home, End), required not optional | MD3 describes pointer and touch dragging only; the keyboard path is the dragging alternative | [[ADR-0014 Window resize border and splitter alternative]] |
| Focus and pressed layers 10 percent, dragged 16 percent on the handle | Material Web latest state tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |

## [[Status Bar]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no status bar | desktop convention; the config app and any editor need a stable place for results | none (Tesserae element) |
| Height 24 dp at every level | 24 dp is the desktop minimum target; the line is 16 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| `label_small` 11 dp text on `surface_container` | MD3 label and surface styles; 11 dp is the minimum text size | none |
| Hover state layer on pressable items at 8 percent with corner 4 dp | MD3 hover value, small shape | [[ADR-0002 Desktop density levels and target sizes]] |
| Narrow-window rule drops items by priority | no clipping rule (chapter 10) | none |

## [[Switch]]

| Deviation | Reason | ADR |
|---|---|---|
| Track 46 by 28 dp with scaled handles at dense | dense row height 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| 40 dp state layer is 32 dp at compact and 28 dp at dense | the layer must not exceed the row | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard focus ring 3 dp, 2 dp offset, role `secondary` | [[Focus Ring]] rule for all controls | [[ADR-0009 State layer percentages]] |
| Enter optional for toggling | follows the WAI-ARIA Authoring Practices | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |

## [[Tabs]]

| Deviation | Reason | ADR |
|---|---|---|
| Bar heights 48, 40, 32 dp; icon above label only at default | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon 20 dp at compact and dense | smaller container | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the tab, 24 dp floor, 48 dp in touch contexts | desktop target size | [[ADR-0002 Desktop density levels and target sizes]] |
| Tab bar overflow scrolls with a visible scrollbar thumb | scrollbar rule: content never silently clipped | [[ADR-0003 Scrollbar rule]] |
| Focus ring inward, 3 dp, `secondary` | the ring must not be clipped by the bar or a scroller | [[ADR-0009 State layer percentages]] |
| Manual activation mode and roving focus keys (Home, End, wrap) | desktop keyboard-first use, WAI-ARIA tabs pattern | none (no ADR needed; Tesserae-only behaviour) |
| Focus and pressed state layers 10 percent (Material Web v0_192 has 12) | latest token set | [[ADR-0013 Focus and pressed state layer 10 percent]] |

## [[Task Item]]

| Deviation | Reason | ADR |
|---|---|---|
| Active window marked by fill and 2 px border, not a `secondary_container` pill | legible at 28 dp height without a colour role | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights, paddings by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tasks Module]]

| Deviation | Reason | ADR |
|---|---|---|
| Row of buttons, not an MD3 navigation bar | a Bar window list differs from a bottom navigation of 3 to 5 destinations | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Terminal]]

| Deviation | Reason | ADR |
|---|---|---|
| Terminal element with no MD3 counterpart | shell feature | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Text Box]]

| Deviation | Reason | ADR |
|---|---|---|
| Read-only multi-line text; no MD3 component | MD3 has type roles, not a text box | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Text Editor]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights by density, 40 dp single-line base | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Escape then Tab as the documented way out until the engine lets Tab through | WCAG 2.2 SC 2.1.2 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Text Field]]

| Deviation | Reason | ADR |
|---|---|---|
| Container height 40, 32, 28 dp instead of 56 dp (MD3 height from Material Web `textfield/demo` min-height 56 px and the label plus padding stack #needs-verification) | desktop density, config panels hold many fields | [[ADR-0002 Desktop density levels and target sizes]] |
| Body text `body_medium` at compact and dense | 20 dp line box fits 32 and 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Label may be external (above the field), and is the only placement at compact and dense | a floating label does not fit a 32 or 28 dp container; forms with aligned label column ([[Form Row]]) | [[ADR-0023 Text Field label placement by density]] |
| Keyboard focus indicator is the 2 dp indicator or outline, no extra ring | MD3 text fields draw no separate ring | [[ADR-0009 State layer percentages]] |
| Escape clears only in search fields | keyboard-first rule | [[ADR-0010 Document structure of the specifications]] (convention only) |

## [[Text Selection]]

| Deviation | Reason | ADR |
|---|---|---|
| Static text selection with copy as a behaviour | desktop users copy paths and values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Highlight from a role pair rather than the text colour at 30 percent | guaranteed contrast | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Highlight alpha 30 percent (Compose Material 3 uses 40 percent of `primary`) | body text in `on_surface` on a 40 percent `primary` highlight is 3.74 to 1 on the dark `surface_bright` container, below the 4.5 to 1 of AC-SEL-8; at 30 percent the minimum is 4.61 to 1 | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Text]]

| Deviation | Reason | ADR |
|---|---|---|
| Body text 14 dp (`body_medium`) in controls at compact and dense where MD3 uses `body_large` 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Ellipsis rule for every single-line text, middle truncation for paths | desktop content such as paths and file names | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Selection and copy of read-only text is a property of the text | desktop users copy values; MD3 is silent | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No deviation in the 15 type roles and their sizes, line heights, weights | roles are MD3's | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## [[Time Input]]

| Deviation | Reason | ADR |
|---|---|---|
| Inline variant with fields 40, 32, 28 dp high instead of the 72 dp picker field | desktop forms hold many rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Up, Down stepping, A and P keys, auto-advance and colon hand-over in the fields | keyboard-first entry | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Fields exposed as `spinbutton` | each field has a numeric range | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| The input is a stand-alone element, not only the keyboard mode of a dialog | desktop forms need a typed time without a dialog | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Time Picker]]

| Deviation | Reason | ADR |
|---|---|---|
| Dial 224 and 192 dp, selectors and period sizes scaled at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Dial keyboard model (arrows, Page, Home, End, Enter) from the slider pattern | MD3 and the APG give no time dial keys | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Period selector is a radio group with arrow keys | APG radio group model | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| 24-hour time opens in typed mode; no 24-hour dial yet | the MD3 24-hour dial layout is not verified | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Invalid typed time shows the field error and disables OK | WCAG 3.3.1 error identification | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |

## [[Title Bar]]

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has the top app bar inside the window, no title bar) | a framework-drawn window frame needs a drag region and window buttons | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Height 40, 32, 28 dp by density (MD3 small top app bar container 64 dp in the deprecated tokens of Material Web `_md-comp-top-app-bar-small.scss`) | desktop title bars are about 30 to 40 dp; the bar follows the control height tokens | [[ADR-0002 Desktop density levels and target sizes]] |
| Window buttons 46 dp wide, 16 dp glyph | the desktop standard on Windows; MD3 icon button is 40 by 40 | [[ADR-0002 Desktop density levels and target sizes]] |
| Close hover and pressed layer in `error` | desktops colour close red; `error_container` is too pale at an 8 percent layer | [[ADR-0009 State layer percentages]] |
| Inactive fade to 0.6 | desktop convention for an inactive title bar; MD3 has no window focus state | [[ADR-0002 Desktop density levels and target sizes]] |
| Inward focus ring on the window buttons | the buttons touch the window edge; an outward ring would be clipped | [[ADR-0013 Focus and pressed state layer 10 percent]] |

## [[Toggle]]

| Deviation | Reason | ADR |
|---|---|---|
| Track and handle scaled by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on the Toggle only | owner feedback F8 | [[ADR-0004 Tooltip rule]] |

## [[Token Button]]

| Deviation | Reason | ADR |
|---|---|---|
| Field height 40, 32, 28 dp (outlined button and field are 40 and 56 in MD3) | desktop forms need rows per screen | [[ADR-0002 Desktop density levels and target sizes]] |
| Rows 56, 48, 40 dp two-line (MD3 list row 56 for two lines, 48 in menus) | density | [[ADR-0002 Desktop density levels and target sizes]] |
| Layer corners 12 dp and a search field in a menu-like surface (MD3 menu: 4 dp, no search) | tess-ui build; the layer is a searchable list | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area is the field with a 24 dp floor | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Toolbar]]

| Deviation | Reason | ADR |
|---|---|---|
| Thickness 64, 48, 36 dp; items 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Labelled variant with text buttons and a Switch in the trailing slot | desktop commands need visible names; the config app already needs it | none (Tesserae-only variant) |
| Overflow always by menu, never scroll or wrap | no hidden or clipped command (chapter 10 rule 3) | none (chapter 10) |
| Roving focus with Home, End and wrap; one Tab stop | WAI-ARIA toolbar, desktop keyboard-first | none |
| Fade, not slide, to hide | engine has no scroll-linked slide | none (code limit) |

## [[Tooltip]]

| Deviation | Reason | ADR |
|---|---|---|
| Hover delay 500 ms | MD3 sources read (Flutter M3 default wait 0 ms, Compose long-press only) give no desktop hover delay; desktop toolkits use about 500 ms and the code already uses it | [[ADR-0004 Tooltip rule]] |
| Tooltip on keyboard focus is shown within one frame | Keyboard users have no hover; matches WAI-ARIA tooltip pattern | [[ADR-0004 Tooltip rule]] |
| Dismiss on scroll, press and activation | WCAG 1.4.13 dismissible; prevents the F2 and F9 symptoms | [[ADR-0004 Tooltip rule]] |
| Grace period 150 ms for plain and rich tooltips | Hoverable condition of WCAG 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Rich tooltip actions reachable by Tab | Keyboard access; MD3 describes touch and pointer | [[ADR-0004 Tooltip rule]] |
| Trigger is the control, never a row or group | Owner feedback F8; MD3 has no row-level tooltip, so this is a restriction rather than a deviation | [[ADR-0004 Tooltip rule]] |

## [[Top App Bar]]

| Deviation | Reason | ADR |
|---|---|---|
| Heights 48 and 40 dp at compact and dense; medium and large only at default | desktop density; no use for tall headers in windows | [[ADR-0002 Desktop density levels and target sizes]] |
| Title roles `title_medium` and `title_small` at compact and dense | smaller bar | [[ADR-0002 Desktop density levels and target sizes]] |
| On scroll only the container colour changes, no shadow | the shadow tokens are deprecated in Material Web; tonal separation is enough | none |
| Frosted variant (translucent with blur) | tess-ui effect; not in MD3 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| More than three actions overflow into a menu | no hidden command (chapter 10) | none |
| Hit area is the icon button, 24 dp floor, 48 dp in touch contexts | desktop target size | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tray Item]]

| Deviation | Reason | ADR |
|---|---|---|
| Hit area by density, 24 dp floor | desktop density, WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Rich tooltip without actions | title and text, no interactive parts | [[ADR-0004 Tooltip rule]] |

## [[Tray Menu]]

| Deviation | Reason | ADR |
|---|---|---|
| Popup corner 8 dp and `surface_raised`, not `extra_small` and `surface_container` | shell theme tokens; recorded in [[Menu]] | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tray Module]]

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status area | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Hit areas by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tree Node]]

| Deviation | Reason | ADR |
|---|---|---|
| A tree row exists although MD3 has no tree | hierarchical data in the config app and shell | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row heights 40, 32, 24 dp instead of the 56 dp one-line list item | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Label type `body_medium` at `compact` and `dense` | fits 32 and 24 dp rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Tree]]

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | hierarchical navigation | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Selection does not follow focus | APG: authors choose; avoids accidental action in file trees | none; design choice |

## [[Video Player]]

| Deviation | Reason | ADR |
|---|---|---|
| A video player is specified; MD3 has none | Tesserae-only element; built from MD3 icon buttons, slider and the scrim | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Controls row follows density levels | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard map (`Space`, `K`, `M`, `Home`, `End`, `Page` keys) | desktop keyboard-first | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltips on icon buttons and on the slider track only | tooltips belong to controls | [[ADR-0004 Tooltip rule]] |
| State layers 8, 10, 10 percent on the controls | accepted state layer values | [[ADR-0009 State layer percentages]] |

## [[Volume OSD]]

| Deviation | Reason | ADR |
|---|---|---|
| Container `surface_container`, level 2, shape 12 dp (MD3 Snackbar `inverse_surface`, level 3, shape 4 dp) | the shell's one raised surface colour serves every card; the OSD is a card, not an inverted message | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| No action and no dismiss control (MD3 Snackbar has an optional action and close) | the OSD only reflects a state change | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Auto-hide 1500 ms, restarted by each change | a volume key can repeat; MD3 Snackbar durations are presets #needs-verification | none (shell design) |
| Click-through and no keyboard | it must not take input from the windows below | none (shell design) |
| Icons from the Material Design Icons set | project icon set | [[ADR-0007 Icon set and Material Symbols deviation]] |

## [[Window]]

| Deviation | Reason | ADR |
|---|---|---|
| A window element exists at all (MD3 has none; it covers window size classes only) | desktop applications own an OS window and need rules for it | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Window minimum size 320 by 240 dp at every density | no MD3 value; 320 dp is the pane minimum of [[10 Layout Overflow and Scrolling]] | [[ADR-0002 Desktop density levels and target sizes]] |
| Resize border 6 dp, below the 24 dp target minimum | the platform resize path (window manager keyboard resize, title bar maximise and restore) is the equivalent control for WCAG 2.5.8 | [[ADR-0014 Window resize border and splitter alternative]] |
| Initial focus on the first content control | desktop keyboard-first use; MD3 gives no window focus rule | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Workspaces Module]]

| Deviation | Reason | ADR |
|---|---|---|
| Current desktop shown by fill and a 2 px border, not an MD3 `secondary_container` pill | works for a Bar button of 28 to 40 dp height; shape cue without a role | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights and padding by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Drag and Drop Pattern]]

| Deviation | Reason | ADR |
|---|---|---|
| A required non-drag alternative for every drag | WCAG 2.2 SC 2.5.7 and SC 2.1.1 | none; accessibility rule, [[14 Accessibility Basics]] |
| 4 dp start threshold, Escape cancel, 700 ms hover open, autoscroll values | MD3 gives no desktop drag rules | none; design choice |
| Drag image, drop indicator shapes and hover-to-open | MD3 gives the dragged state layer only | none; design choice |

## [[Empty States]]

| Deviation | Reason | ADR |
|---|---|---|
| A pattern note for a state MD3 specifies only as illustration | desktop containers (lists, trees, result panes) need one rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| `body_medium` text and 24 dp or 20 dp icon, density-scaled gaps | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## [[Error States]]

| Deviation | Reason | ADR |
|---|---|---|
| A scope table choosing among inline, banner, snackbar and dialog | MD3 treats them as separate components without a selection rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Snackbar with an action stays at least 10 s | WCAG 2.2 SC 2.2.1 and keyboard reachability on desktop | none; design choice |
| No focus move for background errors | avoids stealing focus from the user | none; design choice |

## [[Forms and Settings]]

| Deviation | Reason | ADR |
|---|---|---|
| Label beside the control instead of a floating or in-field label | scan by a fixed label column | [[ADR-0002 Desktop density levels and target sizes]] |
| Persistent per-row reset and a staged or live mode | defaults matter in configuration files | none; design choice |
| Banner as a page-level surface | external changes need a persistent message | none; see [[Notifications]] |
| Commit on Enter or focus leave | desktop forms with many rows | none; see [[Validation]] |

## [[Keyboard Navigation]]

| Deviation | Reason | ADR |
|---|---|---|
| F6 pane cycling and a Tab-stop-per-composite model | MD3 is touch-first and gives no desktop keyboard model | none; desktop keyboard-first ([[01 Principles and Scope]]) |
| Shell `Tab_Index` positive ordering kept until the shell adopts layout order | the shell orders surfaces across windows, which layout order cannot express | none; recorded for the audit |
| Shortcut text in tooltips and menu items | desktop discoverability | [[ADR-0004 Tooltip rule]] |

## [[Loading States]]

| Deviation | Reason | ADR |
|---|---|---|
| 200 ms show delay, 400 ms minimum display, skeleton and timeout rules | MD3 gives no timing rule; desktop waits are mostly short and flashing is a defect | none; design choice |
| Inline indicator 18 dp and 16 dp at dense | matches the button icon size | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Still indicator plus text under reduced motion | WCAG 2.2 SC 2.3.3 is adopted as a MUST | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Notifications]]

| Deviation | Reason | ADR |
|---|---|---|
| Queue with priority instead of replacing the previous snackbar | several results arrive in a desktop session; none may be lost | none; design choice |
| 10 s with an action; hold on focus | WCAG 2.2 SC 2.2.1; keyboard reaches the action | none; design choice |
| A banner as a first-class surface | MD3 removed the banner component from the current set #needs-verification; the config app needs it | none |
| Snackbar not density scaled | message reads at the same size at every density | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## [[Selection]]

| Deviation | Reason | ADR |
|---|---|---|
| Shift and Ctrl range and toggle rules, anchor, select all | MD3 gives no multi-select model for lists; desktop file managers and APG define one | none; design choice, [[ADR-0006 MD3 baseline with named Expressive adoptions]] for the MD3 baseline |
| Shift+Arrow extends a range from the anchor (APG recommended model toggles the next item) | desktop convention; Shift+Space and Ctrl+Space give the toggle forms | none; design choice |
| Start indicator bar in addition to the `secondary_container` fill | selection must not rest on colour alone | none; [[14 Accessibility Basics]] |
| Unfocused container selection colour | desktop windows keep a selection while another pane has focus | none |

## [[Validation]]

| Deviation | Reason | ADR |
|---|---|---|
| Validation on commit, not on every keystroke, except impossible characters | typing must not flash errors on desktop forms with many fields | none; design choice |
| Summary plus inline for several errors | MD3 shows per-field text only | none; design choice |
| Message states the allowed range | WCAG 2.2 SC 3.3.3 Error Suggestion | none |
| Error line below the control column of a [[Form Row]] | label beside the control layout | [[ADR-0002 Desktop density levels and target sizes]] |

Back to [[10 UX Design Specification]].
