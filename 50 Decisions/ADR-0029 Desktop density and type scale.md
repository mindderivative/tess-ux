---
title: ADR-0029 Desktop density and type scale
type: adr
status: accepted
owner: phil
created: 2026-11-28
updated: 2026-11-28
tags: [adr, density, typography]
related: ["[[Typography]]", "[[Spacing and Density]]", "[[07 Spacing and Density Rules]]", "[[Switch]]", "[[Tabs]]", "[[Checkbox]]", "[[Radio Button]]", "[[Chip]]", "[[Choice Picker]]", "[[Icon Button]]", "[[Button]]", "[[Text Field]]", "[[Tree Node]]", "[[List Item]]", "[[Menu Item]]", "[[Config App Layout]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0023 Text Field label placement by density]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]"]
---

# ADR-0029 Desktop density and type scale

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-28 (the owner decided scale A, the desktop Switch track and density on every element). The owner can overturn it. Amends [[ADR-0002 Desktop density levels and target sizes]]. Raised by the owner's feedback on the config app: buttons, switches and dropdowns are too big and do not match the text or the input box; the text in Files and Structure is too large; the specifications read as if for mobile, not desktop.

## Context

[[ADR-0002 Desktop density levels and target sizes]] fixed three density levels and the control heights 40, 32 and 28 dp for button, text field, icon button container, switch row and menu item, but left two things at the touch size:

1. **The type scale does not follow the density.** Every component note names its text role from the MD3 table: `body_large` (16/24) for field text and `body_medium` (14/20) for most rows. At `compact` (32 dp controls) and `dense` (28 dp controls) 16 and 14 dp text beside a 32 dp or 28 dp control looks large, and the Files and Structure trees set 14 dp text in 24 dp rows. A 32 dp field with 16 dp text and a 32 dp button with 14 dp text do not read as one set.
2. **The Switch, Tabs, Checkbox, Radio and Chip keep their MD3 sizes at every level.** The Switch track is 52 by 32 dp at `compact` and `dense`, so its painted track is as high as the whole compact row (32 dp) and 4 dp higher than the dense row (28 dp); this is the "switches are too big" report. The tab bar is 48 dp in a 32 dp-row application.

Evidence about desktop UI scales, as passed on by the Researcher through the Orchestrator (the research note itself is in the Researcher's chat, not in this vault):

- Desktop toolkits set body text at about 13 to 14 px with controls 24 to 32 px high: Windows (Fluent) body 14 px and caption 12 px, control height 32; GNOME and KDE Breeze 10 to 11 pt UI fonts, about 13 to 15 px at 96 dpi, with buttons and fields in the 24 to 32 px range; macOS regular controls about 22 px high with 13 pt system text.
- The nearest published desktop switch is Fluent's 40 by 20 px track; MD3 is 52 by 32 dp.
- MD3 itself offers density (-1 to -3, in steps of 4 dp from the default component height, mainly in the Android and Compose component APIs) and large-screen layout guidance, but no desktop type scale; the Material Web token source gives one size per component.

What was not verified: the macOS values and the MD3 per-component density behaviour (m3.material.io is not readable by tools, so the density page and the per-component density values are `#needs-verification`); the desktop toolkit values above are the Researcher's, not re-measured here. **The Switch sizes below are a design proposal of this decision, not a published value**; Fluent's 40 by 20 is the nearest published form.

## Options

1. Desktop scale A, a type scale and control set that follows the density: body 16/24 at `default`, 14/20 at `compact`, 13/18 at `dense`; a desktop Switch track at `compact` and `dense`; Tabs, Chip, Checkbox and Radio follow the control height (recommended; the owner's choice)
2. Keep the MD3 type scale and only shrink the Switch
3. One desktop size (13/18 text, 28 dp controls) for every level, dropping the touch-sized `default`

## Decision

Option 1. The three levels of [[ADR-0002 Desktop density levels and target sizes]] stay. `default` is the touch-first MD3 size and changes nothing. `compact` and `dense` are desktop sizes: they carry a desktop type scale and the control sizes below. Container heights and paddings of ADR-0002 are unchanged; this record adds the type scale, the Switch, Tabs, Checkbox, Radio, Chip and Select sizes and the icon size at `dense`.

**Type by density** (size / line height in dp; weight in the Typography note):

| Use | default | compact | dense |
|---|---|---|---|
| Body, field text, row label | `body_large` 16/24 | `body_medium` 14/20 | `body_dense` 13/18 (new) |
| Small text, helper, caption | `body_small` 12/16 | `body_small` 12/16 | `body_small` 12/16 |
| Section title | `title_medium` 16/24/500 | `title_small` 14/20/500 | `title_dense` 13/18/500 (new) |
| Page title | `title_large` 22/28 | `page_title_compact` 20/28/400 (new) | `page_title_dense` 18/24/400 (new) |

A control reads the text role of its level from `density.font_body` (below). No `body_large` inside a compact or dense container ([[Typography]] AC-TYP-10).

**Control sizes by density** (dp at scale 1.0):

| Element | default | compact | dense |
|---|---|---|---|
| Button, text field, select trigger container height | 40 | 32 | 28 |
| Tab bar height | 48 (MD3) | 32 | 28 |
| Icon button container, icon | 40, 24 | 32, 20 | 28, 18 |
| Switch track (width by height) | 52 by 32 | 40 by 24 | 36 by 20 |
| Switch handle, off / on / pressed | 16 / 24 / 28 | 12 / 18 / 20 | 10 / 15 / 17 |
| Switch row (hit row, unchanged) | 40 | 32 | 28 |
| Checkbox box, radio ring | 18, 20 | 16, 18 | 14, 16 |
| List, tree row | 40 | 32 | 24 |
| Menu item | 40 | 32 | 28 |
| Chip container height | 32 | 28 | 24 |

The hit row of a Switch, Checkbox and Radio stays 40, 32 and 28 dp: the painted control is smaller than its hit area, and the hit area is never below 24 dp ([[Spacing and Density]] Target sizes). No 48 dp hit area outside a touch context.

**Config app** ([[Config App Layout]]): the application level is `compact`; the Files and Structure panels are `dense` (a region of its own, [[07 Spacing and Density Rules]] rule 4). The config app's project ADR records it.

**Density on every element** (owner direction, 2026-11-28): every element has an optional `Density` property (`default`, `compact`, `dense`; empty means the nearest ancestor's, else the application density; `default` is the roomy touch level, not "inherit"). The order of resolution is: an explicit number on the element (size, padding, row height, font size, track size) first, then the element's own `Density`, then the nearest ancestor's `Density` (it cascades), then the application density. An overlay (popup, menu, tooltip, dialog) takes the density of its opener unless it sets its own. The rule and AC-DEN-12 are in [[Spacing and Density]]; it is toolkit-agnostic (tess-ui implements; a TDL file names the value). tess-shell implements the overlay rule (tess-shell #207).

## Consequences

- [[Typography]] gains four desktop roles (`body_dense`, `title_dense`, `page_title_compact`, `page_title_dense`), the density-to-role table and AC-TYP-10. The shell's `$type.label` (13/500/18) is `title_dense` exactly and `$type.body` (14/20) is `body_medium`.
- A follow-up PR changes the component notes and the token table of [[Spacing and Density]] (`density.switch_track_w`, `density.switch_track_h`, `density.font_body`, `density.tab_height`) and regenerates the [[Defaults Matrix]]: [[Switch]] (desktop track), [[Tabs]], [[Checkbox]], [[Radio Button]], [[Chip]], [[Choice Picker]], [[Icon Button]] (dense icon 18), and the status lines of [[Tree Node]], [[List Item]] and [[Menu Item]].
- Projects: tess-ui needs a density-dependent text role in its stylesheets and the Switch module at three sizes; tess-shell's Toggle (40 by 22) is already near the compact track. Both are worklist rows after the component PR ([[Adoption tess-ui]], [[Adoption tess-shell]]).
- Risk: a 13 dp body role is below the 14 dp most desktop guidance sets as a minimum for long reading; it is for dense lists and trees only, and body text of a document stays at `body_medium` or larger. The minimum text size of [[Typography]] (11 dp) does not change.
- Contrast and focus ring rules do not change; the focus ring offset is 2 dp at every level.

## Affected notes

- [[Typography]]
- [[Spacing and Density]]
- [[Switch]]
- [[Tabs]]
- [[Checkbox]]
- [[Radio Button]]
- [[Chip]]
- [[Choice Picker]]
- [[Icon Button]]
- [[Tree Node]]
- [[List Item]]
- [[Menu Item]]
- [[ADR-0002 Desktop density levels and target sizes]]
