---
title: 02 Colour and Theming
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, colour, theming]
related: ["[[Colour Roles]]", "[[Theme Following the System]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[Scrim]]", "[[State Layers]]", "[[Focus Ring]]", "[[01 Principles and Scope]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[Deviations from MD3]]"]
depends_on: ["[[01 Principles and Scope]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0005 Theme follows the system]]"]
---

# 02 Colour and Theming

> [!info] Summary
> Chapter-level principles for how Tesserae applications get their colour and choose a scheme. The values live in the foundation notes ([[Colour Roles]], [[Theme Following the System]], [[Elevation]], [[Scrim]], [[Motion]]); this chapter states why and links the rules, and copies no value. Material Design 3 baseline: [colour system](https://m3.material.io/styles/color/overview).

## Purpose

Colour decides whether an interface is readable, whether it respects the user's system choice and whether it is consistent across the shell, the toolkit apps and the engine. The config-app demo of 2026-11-20 showed the failure: the system theme was dark and the application was white except for its tooltips ([[Owner Feedback 2026-11-20]] F1). This chapter sets the principles that rule that out.

## Scope

- In scope: the colour roles, scheme selection and following, contrast levels, surface containers, elevation colour, scrim, and the motion and shape tokens that overlays share.
- Out of scope: state layers ([[State Layers]]), the focus ring ([[Focus Ring]]), iconography, and the layout of overlays ([[12 Overlays]]).
- Relationship to [[01 Principles and Scope]]: this chapter applies its MD3-baseline and deviation-policy rules to colour and theming.

## Principles

1. Roles, not literals. Colour is chosen by role name. A project that needs a colour the roles do not give adds a custom colour with derived roles, never a one-off value. See [[Colour Roles]].
2. One vocabulary. MD3 role names are the specification vocabulary ([[ADR-0001 MD3 role names are the specification vocabulary]]). tess-ui uses them in code; tess-shell keeps 12 flat roles and documents the mapping in [[Colour Roles]]; the engine tre takes plain colours and has no roles.
3. The system decides, the user can override. The default scheme follows the platform's light, dark and contrast preferences; the user's explicit choice persists ([[ADR-0005 Theme follows the system]], [[Theme Following the System]]).
4. The first frame is right. The scheme is known before anything is drawn; a late answer holds the window or shows an empty uniform surface ([[Theme Following the System]] rule 4).
5. Every surface follows. The window background, panels, rows and overlays all resolve from roles, so a scheme change leaves no part of the old scheme on screen. This is the direct answer to F1.
6. Contrast is measured. Text 4.5:1, large text and non-text 3:1, high contrast level 7:1 for text; a script computes it from the shipped values ([[Colour Roles]] AC-COL-3, AC-COL-4). Colour never carries state alone.
7. Elevation is tone plus shadow. A layer uses a surface container role and a shadow, with no tint overlay ([[Elevation]]); a modal layer sits above a scrim ([[Scrim]]).
8. Baseline first, Expressive by name. The 2022 role scale is the baseline; any Expressive adoption (shape steps, springs, emphasised type) is a named entry in [[Deviations from MD3]] ([[ADR-0006 MD3 baseline with named Expressive adoptions]]).
9. Motion respects the user. Durations and easings come from tokens, and reduced motion sets them to 0 ([[Motion]]).
10. Type and shape belong to the same system. Text uses the type roles ([[Typography]]); containers use the shape scale ([[Shape]]).

## Where each rule lives

| Topic | Note | Content |
|---|---|---|
| Role set, hex values, pairs, shell mapping | [[Colour Roles]] | 49 roles in light, dark, standard, medium, high; contrast rules |
| Scheme choice, override, no flash | [[Theme Following the System]] | 10 rules, 12 criteria |
| Type | [[Typography]] | 15 roles; centring and ellipsis rules |
| Shape | [[Shape]] | corner scale |
| Elevation and tone | [[Elevation]] | levels, shadows, containers, no tint |
| Motion | [[Motion]] | durations, easings, reduced motion |
| Scrim | [[Scrim]] | colour, opacity, which surfaces |

## Conformance

A project conforms to this chapter when it passes the criteria listed for each principle. Evidence of the current state per project is in the Status in code table of each foundation note; an audit in `70 Adoption` collects it.

| Principle | Where defined | Checked by |
|---|---|---|
| 1. Roles, not literals | [[Colour Roles]] Rules 1 | AC-COL-5, AC-COL-6 |
| 2. Every surface follows the scheme | [[Colour Roles]] Rules 10, [[Theme Following the System]] rule 6 | AC-COL-6, AC-COL-8, AC-TH-11 |
| 3. Follow the system, keep the user override | [[Theme Following the System]] rules 1 to 3 | AC-TH-3 to AC-TH-6 |
| 4. No wrong-scheme first frame | [[Theme Following the System]] rule 4 | AC-TH-1, AC-TH-2, AC-TH-7 |
| 5. Contrast is a measured number | [[Colour Roles]] Rules 3 and 4 | AC-COL-3, AC-COL-4, AC-COL-9 |
| 6. Colour is never the only cue | [[Colour Roles]] Rules 6 | AC-COL-10 |
| 7. One vocabulary, projects keep their own code | [[Colour Roles]] shell mapping | AC-COL-7 |
| 8. Layers have a container and a level | [[Elevation]], [[Scrim]] | AC-ELV-3, AC-SCR-2 |
| 9. Motion stops on request | [[Motion]] Rules 4 | AC-MOT-5 |

## Evidence from owner feedback

- F1, dark system theme and a white application: principles 3 to 5; criteria AC-COL-6, AC-TH-1, AC-TH-11, AC-TH-9 (an application with no seed).
- F8 and F9, tooltip text drawn with no background: principle 7 and the opaque-container rule of [[Tooltip]]; and the criteria of [[Tooltip]]; elevation criteria AC-ELV-3 and AC-ELV-4 for the shadow and container.
- Shell Launcher unreadable with no stylesheet: principle 5 and the baseline fallback ([[Colour Roles]] Rules 7), answered by shell ADR-0022.
