---
title: >-
  Aristotelian Justice Taxonomy Updates
category: journal
tags: [justice, taxonomy, aristotle, ancient-greek]
sources:
  - conversation:2026-07-21
created: 2026-07-21T16:03:30Z
updated: 2026-07-21T16:03:30Z
summary: >-
  Captured updates to the Aristotle Justice taxonomy, adding Equity as a corrective to conventional law and mapping Reciprocity alongside Distributive and Corrective justice.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: draft
lifecycle_changed: 2026-07-21
---

# Aristotelian Justice Taxonomy Updates

*Session captured: 2026-07-21*

## Topics Covered
- Integration of new `ngloss` interlinear formatting for Book V justice passages.
- Revision of the justice taxonomy mermaid diagram to accurately reflect the complexities of *Nicomachean Ethics*.
- The mechanical limits of the `speak-greek` TTS skill and enforcing slower playback.

## Key Takeaways
- **Equity (Decency) as a Corrective:** Aristotle frames Equity not as a rival to justice, but as the essential corrective to the inevitable rigidity of universal conventional laws. It acts as a modification/corrective to Conventional Justice.
- **Household vs. Political Justice:** Strict political justice only applies between free and equal citizens. Household relationships (master/slave, father/child) are structurally different because subordinates are treated as "parts of oneself," making strict injustice impossible.
- **Natural vs. Conventional Justice:** Even within the fluctuating sphere of human affairs (unlike the unchangeable physical world where "fire burns both here and among the Persians"), there is still a natural baseline of justice distinct from conventional legal agreements.
- **Reciprocity and Exchange:** Reciprocity does not fit perfectly into either Distributive or Corrective justice. It acts as a distinct proportional exchange mechanism held together by mutual need and currency, which sustains the city.

## Decisions Made
- Replaced the simplistic "General vs. Particular" tree in the `justice.md` diagram with a comprehensive multi-axis graph encompassing Universal, Particular, Distributive, Corrective (willing/unwilling), Reciprocal, Political, Household, Natural, Conventional, and Equity.
- Hardcoded the `speak-greek` audio playback speed to `--rate=-60%` to ensure the ancient Greek synthesized by `edge-tts` is actually intelligible.
- Migrated manual interlinear glosses in `prohairesis.md` and related justice files to the standardized bracket-based `ngloss` block format for consistency.

## Open Questions
- We still need to locate and gloss the anchor passage for Universal Justice to complete the Book V concepts.

## Related
- [[concepts/justice/justice.md|Justice in the Nicomachean Ethics]]
- [[concepts/justice/particular-justice.md|Particular Justice]]
- [[concepts/justice/distributive-justice.md|Distributive Justice]]
- [[concepts/justice/corrective-justice.md|Corrective Justice]]
- [[concepts/justice/epieikeia.md|Equity / Decency]]
- [[concepts/prohairesis.md|Prohairesis]]
- [[synthesis/justice-taxonomy.md|Justice Taxonomy]]
