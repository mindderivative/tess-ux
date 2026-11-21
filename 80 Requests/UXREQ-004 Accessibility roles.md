---
title: UXREQ-004 Accessibility roles
type: request
status: approved
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, accessibility]
related: ["[[Accessibility Tree]]", "[[List]]", "[[Radio Button]]", "[[Date Picker]]", "[[Toolbar]]", "[[Navigation Rail]]", "[[Navigation Drawer]]", "[[Side Sheet]]", "[[Status Bar]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]"]
depends_on: []
---

# UXREQ-004 Accessibility roles

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (and later tess-shell). Routed through bot:Orchestrator. Finding: TRE-011 in [[Adoption tre]].

## Principle

[[ADR-0020 The engine never blocks the design]]: the role is a node property set from Python (`role`), a closed vocabulary extended in the engine, with no per-frame Python.

## Need

The role vocabulary of tre is 24 names (`button`, `checkbox`, `radio`, `switch`, `slider`, `progressbar`, `link`, `textbox`, `tab`, `tablist`, `tabpanel`, `menu`, `menuitem`, `dialog`, `alert`, `list`, `listitem`, `tree`, `treeitem`, `heading`, `img`, `group`, `none`, `separator`; `tre:crates/engine-py/src/node_props.rs`, `ROLES`). Criteria name roles outside it. Some name a fallback (`group`, `list`); `radiogroup`, `option` and the date grid have none, so a radio group, a selectable list row and a calendar cannot be exposed correctly.

## Request

Add the roles to the vocabulary and map each to the platform role (AccessKit offers all of them): `radiogroup`, `option`, `listbox`, `toolbar`, `navigation`, `complementary`, `region`, `status`, `grid`, `row`, `gridcell`, `columnheader`. An unknown name keeps raising the existing error. No behaviour changes for the 24 existing names.

## Acceptance

[[Radio Button]] AC-RAD-7; [[List]] AC-LST-01; [[Date Picker]] AC-DTP-8; [[Toolbar]] AC-TLB-8; [[Navigation Rail]] AC-NRL-9; [[Navigation Drawer]] AC-NDR-12; [[Side Sheet]] AC-SSH-10; [[Status Bar]] AC-STB-9. A tre-level test passes when a node created with each new role appears in the accessibility tree with the matching platform role, and a `gridcell` inside a `row` inside a `grid` reports its place.

## Out of scope

Position and set size ([[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]); which roles each toolkit view sets (tess-ui and tess-shell code).

Back to [[80 Requests]].
