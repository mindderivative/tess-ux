---
title: 07 Spacing and Density Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, spacing, density, touch]
related: ["[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[01 Principles and Scope]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[Tree]]", "[[Tree Node]]", "[[Text Field]]", "[[Iconography]]", "[[Deviations from MD3]]"]
depends_on: ["[[Spacing and Density]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
---

# 07 Spacing and Density Rules

> [!info] Summary
> The rules for using the spacing steps and density levels: how a project or container chooses a level, how hit areas relate to painted sizes, touch contexts and size classes. All values live in [[Spacing and Density]]; this chapter links to them and does not copy them.

## Principles

1. Whitespace is a scale, not a taste. Every gap, margin and padding is one of the spacing steps of [[Spacing and Density]]; a value outside the set is a defect (AC-DEN-1).
2. Density is a set, not a knob. A level (`default`, `compact`, `dense`) sets all heights, paddings, gaps, indents and icon sizes together. An element never takes the height of one level and the padding of another (AC-DEN-2, AC-DEN-6).
3. Size what the user touches, not what the user sees. The painted size may shrink with the level; the hit area never goes below 24 dp, and in a touch context never below 48 dp (AC-DEN-7).
4. Spacing is the same everywhere in a level. Two trees, two lists or two forms of one project have the same indent, padding and row height at the same level. The owner feedback of the config-app demo (tree indentation too wide, chevron too far from the container edge) is a violation of this principle and of the numbers; see [[Owner Feedback 2026-11-20]] F3 and F4.
5. Content decides the minimum, density the comfort. A row is never shorter than its line box (20 dp for `body-medium`) plus the padding that keeps text centred; the dense list row of 24 dp is the shortest row.

## Choosing a level

| Level | Use for | Why |
|---|---|---|
| `default` | content applications, touch-capable devices, dialogs of consumer-facing tools, any context without a reason for more density | equals MD3 sizes where MD3 states one (button 40 dp) |
| `compact` | config-style tools, side panels, forms with many rows, trees and lists of settings | 25 percent more rows (40 divided by 32) per screen than `default` (32 against 40 dp) with a 20 dp icon and a 32 dp hit area |
| `dense` | tool windows, property inspectors, logs, tables and trees whose rows are scanned, not read; the shell's bars and menus where a project ADR says so | 24 to 28 dp rows, the smallest sizes that meet the 24 dp target minimum |

How a level is chosen:
1. The project sets a default level in a project ADR (the config-style tools set `compact`). That ADR, not this chapter, binds the project.
2. A container may override the project level with a container property. The level applies to the container and every descendant, until a descendant container overrides it again.
3. A control reads its level from its nearest container. A control has no level of its own.
4. Mixed levels inside one window are allowed between regions (a `compact` form beside a `dense` log), never within one list, tree, form or toolbar.
5. A user setting may change the project level; it persists and applies at the next layout, without a restart.

## Hit area and painted size

- Painted size and hit area are separate. A 16 dp chevron at the `dense` level has a hit area 24 dp wide and as high as the row; a 20 dp icon sits in a 28 dp button whose hit area is the whole container.
- The hit area grows into padding and gaps, never into a neighbour's hit area.
- Gaps between targets are the spacing steps. Targets whose hit areas are smaller than 24 dp need a spacing exception from WCAG 2.2 SC 2.5.8 (a 24 dp circle on each does not overlap another target); the spec avoids exceptions by making every hit area at least 24 dp.
- The painted size never exceeds the hit area.

## Touch contexts

- A project or container declares a touch context when touch is the primary input (a tablet or touchscreen shell mode). The level stays `default`; hit areas grow to at least 48 by 48 dp; the painted sizes of [[Spacing and Density]] stay; spacing between neighbouring hit areas stays as stated (they do not overlap).
- A text field in a touch context keeps its painted height of its level and grows its hit area to 48 dp; a taller touch variant (MD3 56 dp) may be stated in [[Text Field]].
- A pointer-only desktop window never needs the 48 dp hit area, and does not use it as a reason to grow painted controls.

## Window size classes

- Window size classes (compact below 600 dp, medium 600 to 839, expanded 840 to 1199, large 1200 to 1599, extra-large 1600 and above; heights below 480, 480 to 899, 900 and above) are defined in [[Spacing and Density]] and used for layout in [[10 Layout Overflow and Scrolling]].
- A size class changes the pane layout and the margins, not the density level: a compact-width window can be `dense`.
- Page margin by width class is a layout rule, not a spacing token: compact 16 dp, medium 24 dp, expanded and larger 24 dp or more; the margin is a spacing step. These margins follow the MD3 guidance on layout margins #needs-verification.

## Defaults and conformance

- A project with no declared level uses `default`.
- A stylesheet that needs a one-off size creates a token first and a note in the component note; it does not use a literal.
- Conformance is tested with the geometry checks AC-DEN-1 to AC-DEN-10 of [[Spacing and Density]] and the layout checks of [[10 Layout Overflow and Scrolling]].
- Each departure from MD3 values is a row in [[Deviations from MD3]] with [[ADR-0002 Desktop density levels and target sizes]] as its reason.

## Acceptance criteria

- [ ] AC-DEN-12 (review): the project ADR names its default density level, and the project's stylesheets contain no per-element height literal outside the three-value sets. Pass: a reviewer lists the level and finds zero literals.
- [ ] AC-DEN-13 (geometry check): changing the level of a container from `compact` to `dense` at run time changes every height, padding, gap, indent and icon size inside it to the dense values in one layout pass, and changes nothing outside it.
- [ ] AC-DEN-14 (geometry check): in a touch context every interactive element's hit area is at least 48 by 48 dp while its painted bounds equal the values of its level.
- [ ] AC-DEN-15 (scripted input): a user setting that changes the density level applies without a restart and persists to the next start.

AC-DEN-1 to AC-DEN-11 are defined in [[Spacing and Density]].

## Sources

- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (verified 2026-11-21).
- Window size classes: https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes (verified).
- Layout margins by size class (16, 24 dp) from the MD3 layout pages #needs-verification: m3.material.io is a JavaScript app.
- Decision and values: [[ADR-0002 Desktop density levels and target sizes]], [[Spacing and Density]].
