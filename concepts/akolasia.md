---
title: Akolasia (Dissipation)
category: concepts
tags: [philosophy, ethics, virtue-ethics, ancient-greek]
aliases: [dissipation, self-indulgence, indulgence, akolasia]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-12T00:00:00Z
updated: 2026-07-12T00:00:00Z
summary: The vice of excess opposite temperance — bodily indulgence in touch/taste pleasures; literally "unpruned" in Greek, and a settled character trait, not an episode.
provenance:
  extracted: 0.72
  inferred: 0.23
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-07-12
tier: supporting
relationships:
  - target: "[[concepts/doctrine-of-the-mean]]"
    type: implements
  - target: "[[concepts/hexis]]"
    type: implements
  - target: "[[concepts/akrasia]]"
    type: related_to
---

# Akolasia (Dissipation)

The vice of excess in the temperance row of the [[concepts/doctrine-of-the-mean|mean table]] (deficiency: insensibility / mean: temperance / **excess: akolasia**) — Greek **ἀκολασία** (*akolasia*), adjective **ἀκόλαστος** (*akolastos*). Sachs's consistent translation is "dissipation," a choice his glossary defends directly against the alternatives:

> "'Dissipation' is not an ideal translation, but it seems better than the usual alternatives, which are either obsolete (profligacy), quaint (licentiousness), or too weak (intemperance)." (Glossary)

The word trips up modern readers because English "dissipated" now mostly connotes wasted, scattered energy (a "dissipated effort"), not bodily indulgence — which is closer to what a reader might reach for with **"indulgence"** or **"self-indulgence"** instead. That instinct isn't wrong: W. D. Ross's standard translation actually uses "self-indulgence" for the same word, so it's a legitimate scholarly alternative, not a loose gloss — see *Open Questions* below for the one nuance it risks losing.

## Diagram

Both akolasia and akrasia involve giving in to bodily pleasure, but Aristotle treats them as different in *kind*, not degree — one is a fixed condition, the other a recurring cycle. The diagram models each as its own small state machine: akrasia loops (knows better → overpowered → regret → back to knowing better), while akolasia has no loop out at all.

```mermaid
stateDiagram-v2
    direction LR

    [*] --> Akrasia
    [*] --> Akolasia

    state "Akrasia (unrestraint) - episodic" as Akrasia {
        [*] --> KnowsBetter
        KnowsBetter --> Overpowered : passion overwhelms judgment
        Overpowered --> Regret : afterward
        Regret --> KnowsBetter : resolve returns
    }

    state "Akolasia (dissipation) - chronic" as Akolasia {
        [*] --> Committed
        Committed --> Committed : stands by the choice, no regret
    }
```

How to read it: akrasia's cycle always returns to "knows better" between lapses — like the "epileptic seizures" Aristotle compares it to, it's intermittent and curable. Akolasia has no return path — the person has settled, like "dropsy and consumption," into a single self-reinforcing state with no regret to pull them out.

## Key Ideas

- **Literal root: "unpruned."** Footnote 76 (on the "spoiled child" passage, Bk. III, ch. 12) gives the etymology directly: "In Greek, the same word means 'spoiled' as in the case of an overindulged child, and 'dissipated' as in a fully formed adult state of character; its root sense is 'unpruned,' extending to mean 'unpunished,' 'uncorrected,' or 'undisciplined.'" Grammatically it is alpha-privative + *kolazein* ("to prune, chastise, correct") — *a-kolastos*, "not cut back." The same word is used colloquially of an overindulged child and of a grown person of settled bad character — Aristotle's point (Bk. III, ch. 12) is that the growth was simply never checked. ^[extracted]
- **Domain: only touch and taste, not pleasure generally.** [[concepts/doctrine-of-the-mean|Temperance and dissipation]] are restricted to the bodily pleasures shared with animals — food, drink, and sex — and explicitly *not* to pleasures of sight, hearing, or smell (enjoying paintings, music, or the smell of roses doesn't make someone "dissipated"), nor to non-bodily pleasures like the love of honor or of talking. Aristotle calls this the "most widely shared" and most "slavish and animal-like" class of pleasure, which is why dissipation is, in his words, "justly the most reproached vice... because it is present not insofar as we are human beings but insofar as we are animals" (Bk. III, ch. 10). ^[extracted]
- **Aristotle's working definition** (per Sachs's glossary, citing 1146b 22-23): "the vice by which one deliberately chooses to be, or acquiesces in being, someone who indulges in the pleasures of eating, drinking, and sex whenever they are available." The operative word is *chooses* — see next point. ^[extracted]
- **A settled active condition ([[concepts/hexis|hexis]]), not an episode — this is the crucial line separating it from [[concepts/akrasia|akrasia]].** The dissipated person has decided, as a matter of principle, that one ought always to pursue pleasure, and acts on that conviction consistently; the unrestrained (*akratic*) person believes the opposite but is overpowered by passion in the moment. This is why Aristotle says the dissipated person feels **no regret** ("stands by his choice") while the unrestrained person always does, and why he reaches for a medical contrast: vice (including dissipation) is "like such diseases as dropsy and consumption" — continuous and effectively incurable — while unrestraint is "like epileptic seizures" — intermittent, and curable (Bk. VII, ch. 8). Aristotle explicitly ranks the merely unrestrained person as *better* than the dissipated one, "since the best thing in him, the source, is preserved." ^[extracted]
- **Natural desires can be indulged to excess too, without being "dissipation" in the full sense.** Aristotle distinguishes overeating out of plain appetite (the "greedyguts," who merely exceeds a natural desire in amount) from dissipation proper, which is about *how* one relates to the pleasure — pursuing it by choice, indiscriminately, and beyond what is fitting, not merely eating too much on occasion (Bk. III, ch. 11). ^[extracted]
- **Connects to habituation**: the "unpruned plant" image lines up with Book II's general claim that virtue and vice are both produced by the actions one repeatedly performs — dissipation is the specific, describable *result* of a desiring part of the soul that was never brought under the rule of reason in the way [[concepts/hexis|habituation]] is supposed to bring it, left instead to "grow" toward whatever is pleasant, the way an unpruned branch grows wherever it likes. ^[inferred]

## Open Questions

- **Does "indulgence"/"self-indulgence" lose anything "dissipation" keeps?** Ross's "self-indulgence" nicely captures that the vice is chosen and self-directed (matching the *hexis* point above), but on its own, in casual use, "indulgence" can sound momentary or mild ("I indulged a little") — closer to what Aristotle would call *akrasia* than to the settled, unregretful, principled condition he actually means. If "indulgence" is adopted as a working gloss, it's worth mentally attaching "as a settled character trait" to it, to keep the *hexis*/*akrasia* distinction from blurring back together. ^[inferred]

## Related

- [[concepts/doctrine-of-the-mean]] — akolasia is the named excess-pole opposite temperance in the mean table
- [[concepts/hexis]] — akolasia is explicitly a settled active condition, chosen and stood by, not a passing lapse
- [[concepts/akrasia]] — the concept akolasia is most often confused with; distinguished by regret, curability, and whether the person's own choice endorses the pleasure-seeking
- [[synthesis/virtue-taxonomy]] — treemap depicting akolasia as the bodily-pleasure triad's excess leaf
- [[references/nicomachean-ethics]] — source text (Book III, ch. 10-12; Book VII, ch. 4-8)
