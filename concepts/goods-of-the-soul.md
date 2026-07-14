---
title: "Goods: External, of the Soul, of the Body"
category: concepts
tags: [philosophy, ethics, metaphysics, ancient-greek]
aliases: [threefold division of goods, external goods, goods of the soul, goods of the body]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-13T00:00:00Z
updated: 2026-07-13T00:00:00Z
summary: Aristotle's three-way classification of goods by where they reside (external, of the soul, of the body), used to argue happiness must be an activity of the soul.
provenance:
  extracted: 0.75
  inferred: 0.20
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-07-13
tier: supporting
relationships:
  - target: "[[concepts/eudaimonia]]"
    type: uses
  - target: "[[concepts/energeia]]"
    type: related_to
---

# Goods: External, of the Soul, of the Body

A three-way division Aristotle invokes in Bk. I, ch. 8 to test the ergon argument's conclusion against received opinion: "good things have been parceled out into three kinds, some being called external while the others are associated with the soul or the body." This is a completely different axis from the [[synthesis/threefold-good|beautiful/pleasant/advantageous triad]] — that one classifies goods by what they're *for* (chosen as an end vs. merely instrumental); this one classifies them by *where they reside* (outside a person, in the soul, or in the body).

## Key Ideas

- **Goods of the soul are called "the most governing and especially good"** — Aristotle explicitly identifies "the actions and ways of being at work that belong to the soul" as the ones set down under this heading, which is exactly the category [[concepts/eudaimonia|happiness]] needed to fall into, given the [[concepts/eudaimonia|ergon argument]]'s conclusion that happiness is a [[concepts/energeia|being-at-work]] of the soul rather than a possession. ^[extracted]
- **This is a consistency check, not a new argument** — Aristotle notes it's "consonant with our statement" that the end (happiness) belongs among goods of the soul, since he had already independently reached that conclusion via the ergon argument; the threefold division is invoked to show the conclusion fits an "ancient" opinion "agreed to by the philosophers," not to derive it. ^[extracted]
- **External goods still matter, just not as the substance of happiness.** Elsewhere Aristotle is explicit that a happy person needs external goods (friends, wealth, political standing, good birth, good looks) as instruments and conditions for beautiful action — someone friendless or destitute is "not very apt to be happy" — but these remain instrumental *supports*, categorically distinct from the being-at-work of the soul that happiness actually consists in. ^[extracted]
- **Bodily goods (health, strength, beauty of body) form the third category**, needed for action but likewise not where happiness itself resides — this is the same three-way split that later grounds Book X's point that the contemplative life "has need of external props," even though it needs the least of any life, since contemplation is the being-at-work most purely located in the soul alone. ^[inferred]

## Diagram

A direct containment claim, not a metaphor: Aristotle names these as three genuinely distinct kinds of good, and places happiness in exactly one of them.

```mermaid
classDiagram
    class Good["Good (Bk. I, ch. 8)"]
    class External["External Goods"] {
        Friends, wealth, political standing, good birth
        Instruments and conditions, not happiness itself
    }
    class OfTheSoul["Goods of the Soul"] {
        Actions and being-at-work
        Most governing, especially good
        Where happiness is located
    }
    class OfTheBody["Goods of the Body"] {
        Health, strength, beauty
        Needed for action, not happiness itself
    }
    Good <|-- External
    Good <|-- OfTheSoul
    Good <|-- OfTheBody
```

## Related

- [[concepts/eudaimonia]] — the ergon argument this division is used to vindicate
- [[concepts/energeia]] — being-at-work, the category that makes happiness a good "of the soul"
- [[synthesis/threefold-good]] — the other, independent threefold division of goods (by end vs. means, not by location)
- [[references/nicomachean-ethics]] — source text (Book I, ch. 8)
