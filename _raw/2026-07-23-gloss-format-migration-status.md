---
title: Greek gloss format migration status (old plain-block vs ngloss)
tags: [classical-gloss, obsidian, wiki-maintenance, greek]
project: aristotle
sources:
  - "aristotle session (2026-07-23)"
created: 2026-07-23T21:39:32Z
updated: 2026-07-23T21:39:32Z
lifecycle: raw
lifecycle_changed: 2026-07-23
provenance:
  extracted: 0.6
  inferred: 0.4
base_confidence: 0.75
summary: The vault has two coexisting Greek interlinear gloss formats; many concept/synthesis pages still use the deprecated one and need migration.
---

## Finding

The `classical-gloss` skill (`.agents/skills/classical-gloss/SKILL.md`) specifies the current standard for interlinear Greek glosses: a fenced ` ```ngloss ` code block using `\ex` (original text), `\gl` (word-by-word gloss with bracketed tiers per word), and `\ft` (free translation) tags — rendered by the Obsidian `obsidian-ling-gloss` plugin. Example of the current format lives in `synthesis/primary-and-secondary-happiness.md`.

However, a substantial number of pages still use an **older, deprecated format**: a plain (unlabeled) fenced code block with three manually space-padded rows (Greek / transliteration / gloss), stacked one word-column at a time, with no `\ex`/`\gl`/`\ft` tags and no ngloss rendering. `concepts/contemplative-life.md` was found in this old format and was converted to the new `ngloss` format in this session (all 6 Greek passages, citations re-verified against `references/nicomachean-ethics-greek.xml` and found accurate — only the format was stale, not the content).

A quick grep (`grep -l '```ngloss' concepts/*.md synthesis/*.md`) found only ~12 files already migrated, while a much larger set of concept files (e.g. `akrasia.md`, `beasts-and-gods.md`, `capable-of-being-otherwise.md`, `continence.md`, `doctrine-of-the-mean.md`, and likely others) still use the old plain-block style. ^[extracted]

## Why it matters

- The old format doesn't render as an aligned interlinear gloss in Obsidian (no ngloss plugin parsing), so those pages look like a wall of manually-aligned monospace text rather than a proper glossing widget.
- Anyone running `/classical-gloss` or doing wiki maintenance on gloss-bearing pages should expect to find this split and may want to do a systematic sweep/migration rather than assuming all existing glosses are already in the current format. ^[inferred]

## How to convert (worked pattern)

1. Extract the existing Greek/transliteration/gloss triples per word directly from the old three-row block (no need to re-derive from source — they were already correct in the `contemplative-life.md` case).
2. Re-verify citations against the local Perseus TEI XML (`references/nicomachean-ethics-greek.xml`) using the bounded-context grep + milestone technique described in the skill, if verification is warranted.
3. Feed the word list as JSON through `.agents/skills/classical-gloss/scripts/align_interlinear.py` to get the properly bracketed `\gl` lines.
4. Assemble into a ` ```ngloss ` block with `\ex` (full sentence), the generated `\gl` lines, and `\ft` (free translation, usually already present as the old block's italicized translation sentence).

## Related

- [[concepts/contemplative-life]] — the page migrated in this session (worked example of the conversion)
- [[synthesis/primary-and-secondary-happiness]] — reference example already in the current `ngloss` format
