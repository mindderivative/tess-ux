---
title: 01 Principles and Scope
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, principles]
related: ["[[Owner Feedback 2026-11-20]]", "[[02 Colour and Theming]]", "[[07 Spacing and Density Rules]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Deviations from MD3]]", "[[Test Method]]", "[[Accessibility Rules]]", "[[Plan]]", "[[Inventory]]", "[[Glossary]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0010 Document structure of the specifications]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0010 Document structure of the specifications]]"]
---

# 01 Principles and Scope

> [!info] Summary
> What the Tesserae UX specifications are for, who reads them, the seven principles every rule follows, how to read a rule, and what MUST and SHOULD mean. Material Design 3 is the baseline; every departure is recorded in [[Deviations from MD3]].

## Purpose

Two specifications guide every Tesserae project that draws visual elements (applications, shells, desktop environments, dashboards):

1. The UX Design Specification (this folder, with the foundations in `20 Foundations and Tokens`): principles, tokens, interaction rules, accessibility, states and patterns.
2. The UX Component Design Specification (`30 Component Specifications`): one note per element.

The goal is that a new application written on the tess-ui toolkit, the tess-shell shell or the tre engine looks and behaves consistently without each team re-deciding spacing, tooltips, scrollbars or theme handling, and that each rule can be checked by a test rather than by taste. The first rules were derived from the owner's live demo of 2026-11-20 ([[Owner Feedback 2026-11-20]]).

## Audiences

| Audience | Reads this to | Uses |
|---|---|---|
| Application author (tess-ui) | build views that follow the rules by default and know which tokens to set | component notes, [[Spacing and Density]], [[Colour Roles]] |
| Shell and desktop-environment author (tess-shell) | map the shell's flat roles and modules onto the vocabulary and know the gaps | foundations, [[Popup]], [[Menu]], mapping in [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Engine author (tre) | learn which primitives the spec needs and where an engine gap is a request note | `Status in code` tables, `80 Requests` |
| Designer and reviewer | judge a screen against rules that are numbers and key sequences | acceptance criteria, [[Test Method]] |
| Accessibility reviewer | check roles, names, keys, contrast and announcements | [[14 Accessibility Basics]], [[Accessibility Rules]] |

## Principles

Each principle is a rule with a test; the tests live in the notes named.

1. Keyboard first. Every action reachable by pointer is reachable by keyboard, in a visible focus order, with a visible focus indicator. Test: scripted input over every control ([[14 Accessibility Basics]], AC-A11Y-1 to AC-A11Y-4).
2. Content never overflows its container. Single-line text ends in an ellipsis or scrolls, wrapping text wraps, a container with overflowing content shows a scrollbar on that axis, nothing draws outside its container. Test: geometry and pixel checks ([[10 Layout Overflow and Scrolling]]).
3. One source of truth per token. A colour, size, duration or percentage is defined once in a foundation note and referenced elsewhere by role or token name; a component stylesheet holds no literal. Test: token test ([[Test Method]]).
4. Follow the system. The colour scheme, reduced motion and high contrast come from the platform unless the user overrides them, and the first frame is already correct. Test: [[Theme Following the System]] criteria (AC-TH-*) and [[14 Accessibility Basics]].
5. Density by choice. Three levels, `default`, `compact`, `dense`, chosen per project or per container; sizes come from the level, not from literals per widget. Test: token test and geometry check ([[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]]).
6. Every control has a name. Each interactive node has a role and an accessible name, and an icon-only control also has a tooltip. Test: AT tree assertion ([[Accessibility Rules]]).
7. Rules are testable. A rule states a number, a key sequence or a measurable relation; a sentence that no test, measurement or review can pass or fail is not a rule and does not enter the spec ([[Test Method]]).

Derived rules used across chapters:

- The tooltip belongs to the control, never to its row, group or container ([[ADR-0004 Tooltip rule]]).
- Colour never is the only carrier of a state or of information ([WCAG 2.2 SC 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).
- A minimum pointer target of 24 dp, 48 dp in touch contexts ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum), [[ADR-0002 Desktop density levels and target sizes]]).

## Scope

In scope for the first slice: theme and colour roles, spacing and density, layout overflow and scrolling, overlays (tooltips, popups, menus, dialogs), accessibility basics, and the components Tooltip, Popup, Menu, Dialog, Panel and Surface, Scrollbar and Scroll Container, Tree, Tree Node, List, List Item, Accordion, Form Row, Text Field, Switch, Icon Button, Button. The remaining families follow the order in [[Plan]].

Out of scope: implementation code in the projects (this vault writes none beyond short illustrative snippets), platform-specific shell behaviour that no project owns, and visual design of a particular product.

## How to read the specification

- Each chapter states rules; each component note states anatomy, states, sizes by density, behaviour, accessibility, a numbered list of acceptance criteria, the status in code of each project, and the deviations from Material Design 3.
- Acceptance criteria ids are `AC-<prefix>-<n>`: `AC-TIP-` tooltip, `AC-SCB-` scrollbar, `AC-TRE-` tree, `AC-TXF-` text field, `AC-SWI-` switch, `AC-ICB-` icon button, `AC-BTN-` button, `AC-TH-` theme, `AC-LAY-` layout, `AC-POP-` popup, `AC-A11Y-` accessibility basics. Each criterion names how it is checked (token test, geometry check, pixel check, contrast script, scripted input, AT tree assertion, review) and the pass condition; the methods are defined in [[Test Method]].
- The `Status in code` table says per project whether the code meets, partly meets, lacks, or is not applicable to a rule. A spec may describe the target before the code reaches it; the status shows the distance. The vault never promises that a project will adopt a rule; adoption is the project's decision (audits in `70 Adoption`).
- Units: 1 dp equals 1 px at scale factor 1.0; the projects use px and multiply by the window scale factor.
- Values marked `#needs-verification` are claims the vault could not confirm against a source; they are listed in [[Open Questions]] and are not binding until confirmed. A value marked `#needs-verification-as-design-choice` is a Tesserae choice with no Material Design 3 source; it is binding once the owner accepts it.
- Links to code use `tess-ui:`, `tess-shell:`, `tre:` prefixes for repo-relative paths.

## Conformance language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are used as in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174): they carry that meaning when written in capitals. Where a rule is written in lowercase present tense ("the tooltip belongs to the control"), it is a MUST.

- MUST: a project that draws the element is non-conformant without it; an acceptance criterion exists.
- SHOULD: a project follows it unless a recorded reason makes it wrong; the project's audit lists the reason.
- MAY: optional behaviour; if present, it follows the stated form.
- A criterion marked "not testable" names why (platform cannot be driven) and what review replaces it.

## Material Design 3 baseline and deviation policy

- Material Design 3 is the baseline reference ([[ADR-0006 MD3 baseline with named Expressive adoptions]]): the 2022 role and shape scales, with named Expressive adoptions where a project already ships them.
- MD3 role names are the specification vocabulary ([[ADR-0001 MD3 role names are the specification vocabulary]]); projects keep separate code and map to it.
- Every departure (desktop density, keyboard-first use, accessibility, Tesserae-specific elements, Expressive adoptions) is recorded in the `Deviations from Material Design 3` table of the component note and in the register [[Deviations from MD3]], with its reason and, where a decision exists, its ADR.
- MD3 values are verified against a source and the source is recorded in the note's Sources section; an unverified claim carries `#needs-verification`.
- The Tesserae minimum is stricter than MD3 where a WCAG 2.2 criterion applies.

## Document structure

The structure of the vault, the order of the chapters and the slice order are fixed by [[ADR-0010 Document structure of the specifications]]: chapters in `10 UX Design Specification`, tokens in `20 Foundations and Tokens`, one note per element in `30 Component Specifications` (indexed by [[Inventory]]), patterns in `40 Patterns`, decisions in `50 Decisions`, quality in `60 Quality` ([[Test Method]], [[Accessibility Rules]]), adoption audits in `70 Adoption`, requests in `80 Requests`, research in `90 Research`.

## Acceptance criteria

- [ ] AC-PRI-1: Review. Each component note in `30 Component Specifications` contains the sections of `_templates/Component.md`, a numbered acceptance-criteria list in which every item names a check method from [[Test Method]], a Status in code table, and a Deviations table. Pass: a script that reads the headings finds all sections in every note.
- [ ] AC-PRI-2: Token test. No component stylesheet in a conformant project contains a literal colour, size or duration that [[Colour Roles]], [[Spacing and Density]] or [[Motion]] defines. Pass: a scan of the stylesheets finds zero literals outside the token files.
- [ ] AC-PRI-3: Review. Every rule in a chapter has an acceptance criterion or a reference to one; a chapter paragraph with MUST and no criterion is a defect. Pass: reviewer list empty.

## Sources

- Vault guide (hard rules 1 to 9, structure, style): `AGENTS.md`.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.1, 2.5.8.
- [Material 3](https://m3.material.io/) as the baseline reference; its pages are script-rendered and component values are cited from [Material Web](https://github.com/material-components/material-web) in each component note.
- Owner decisions and ADRs as linked.
