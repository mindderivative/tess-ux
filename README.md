# tess-ux

The UX source of truth for every Tesserae project that draws visual elements: applications, user interfaces, shells, desktop environments and dashboards.

- **UX Design Specification** (`10 UX Design Specification`, `20 Foundations and Tokens`, `40 Patterns`): generalised principles, foundations, tokens, interaction rules, accessibility, states and patterns. Seventeen chapters; chapter 16 is the register of deviations from Material Design 3.
- **UX Component Design Specification** (`30 Component Specifications`): one note per widget, module, block, surface, frame, tooltip, overlay and popup, each with numbered acceptance criteria and its status in each project's code. `Inventory` lists every element and where it is specified.

Foundation: Material Design 3 is the baseline reference. Every Tesserae departure from it is recorded with its reason in the note that owns it and in `Deviations from MD3`. Decisions are ADRs in `50 Decisions`.

Other folders: `60 Quality` (test method, accessibility rules, vault lint), `70 Adoption` (audit worklists per project and the adoption plan), `80 Requests` (requests to the projects), `90 Research` (evidence, MD3 verification status, gaps).

This repository is an [Obsidian](https://obsidian.md) vault. Open the folder in Obsidian, or read the Markdown notes directly. Start at `00 Home/Home.md`.

## Checks

`python3 tools/lint_vault.py` checks frontmatter, links, orphans, template sections, acceptance criteria, token names, markdown rules and private paths. `python3 tools/contrast_check.py` recomputes the WCAG contrast ratios stated in the notes. Both use only the Python standard library.

## Status

Written on 2026-11-21 and 2026-11-22; all notes are `draft` until the maintainer accepts or a project has built and confirmed them. Open decisions are in `00 Home/Open Questions.md`.

Licence: MIT.
