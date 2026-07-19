---
title: "Courage (Andreia)"
category: concepts
tags: [philosophy, ethics, virtue-ethics, ancient-greek]
aliases: [andreia, bravery, the mean concerning fear and confidence]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-14T00:00:00Z
updated: 2026-07-14T00:00:00Z
summary: The mean between rashness and cowardice regarding fear of death in battle, plus Aristotle's five named look-alikes that resemble but aren't true courage.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-07-14
tier: supporting
relationships:
  - target: "[[concepts/doctrine-of-the-mean]]"
    type: implements
  - target: "[[concepts/to-kalon]]"
    type: uses
  - target: "[[concepts/voluntary-involuntary]]"
    type: related_to
---

# Courage (Andreia)

Bk. III, ch. 6-9 gives courage the first full worked-out treatment of the mean-doctrine's structure — the model case [[concepts/doctrine-of-the-mean|the mean table]] later summarizes in outline. Courage is the mean concerning fear and confidence, but not with respect to every frightening thing: it is narrowed specifically to fear of death "of the most beautiful sort," in battle. Fearing poverty, disease, or the loss of reputation may be reasonable or even praiseworthy, but has nothing to do with courage proper — a person unafraid of those things is called courageous only "by a likeness."

## Key Ideas

- **True courage acts "for the sake of the beautiful."** The courageous person "is as undaunted as a human being can be," yet still feels fear at things genuinely terrible — courage isn't fearlessness, but enduring and fearing "what one ought, for the reason one ought, as one ought, when one ought." Since "the end of any way of being at work is what corresponds to the active condition it comes from," and courage's end is [[concepts/to-kalon|the beautiful]], the courageous person endures fear specifically because doing so is beautiful, not from lack of feeling. ^[extracted]
- **Courage is concerned more with enduring fear than with confidence** — Aristotle notes it's harder to endure painful things than to abstain from pleasant ones, which is why courage is itself painful even though its end (like an athlete's) is genuinely pleasant, just "blocked from sight by the things that encircle it." ^[extracted]
- **Five named look-alikes resemble true courage without being it** — each substitutes some other motive for "acting on account of the beautiful": ^[extracted]
  - *Citizen-courage*: enduring danger from fear of legal penalty and reproach, or desire for honor — closest to the real thing, since shame and love of honor are at least *virtue-adjacent* motives.
  - *Experience-based courage*: professional soldiers, confident from knowing "many empty threats" — but they flee "the very moment" the danger exceeds their calculated advantage, unlike citizen-soldiers who die holding their ground.
  - *Spirited courage*: courage that is really just anger or spiritedness "carried away" like a wounded animal — natural and courage's nearest neighbor, but not courage unless choice and a beautiful end are added to it.
  - *Hopeful courage*: confidence from a habit of winning (or from drunkenness) — collapses the moment events depart from expectation.
  - *Ignorant courage*: mistaking the danger for something smaller than it is — the weakest imitation, since "they have nothing they consider worth facing" once they realize their error.
- **The upshot is a warning against confusing the appearance of fearlessness with virtue** — several of the look-alikes (professional soldiers, angry men, the falsely confident, the ignorant) can be just as *effective* in battle as the truly courageous person, sometimes more so, but effectiveness is not what makes an act courageous; only acting for the beautiful, by choice, does. ^[inferred]

## Diagram

A direct classification, not a metaphor: Aristotle names true courage and five distinct look-alikes, each defined by what it substitutes for acting-for-the-beautiful.

```mermaid
classDiagram
    class ApparentCourage["Enduring Danger Without Fleeing"]
    class TrueCourage["True Courage"] {
        Acts for the sake of the beautiful
        By choice
        Fears what one ought, as one ought, when one ought
    }
    class CitizenCourage["Citizen-Courage"] {
        Motive: legal penalty, reproach, honor
    }
    class ExperienceCourage["Experience-Based Courage"] {
        Motive: calculated confidence from training
        Flees once the danger exceeds the calculation
    }
    class SpiritedCourage["Spirited Courage"] {
        Motive: anger, spiritedness alone
    }
    class HopefulCourage["Hopeful Courage"] {
        Motive: a habit of winning, or drunkenness
    }
    class IgnorantCourage["Ignorant Courage"] {
        Motive: mistaking the danger's true size
    }
    ApparentCourage <|-- TrueCourage
    ApparentCourage <|-- CitizenCourage
    ApparentCourage <|-- ExperienceCourage
    ApparentCourage <|-- SpiritedCourage
    ApparentCourage <|-- HopefulCourage
    ApparentCourage <|-- IgnorantCourage
```

## Greek Gloss

Source: Bk. III, ch. 6-7 (Bekker 1115b20-24).

> τέλος δὲ πάσης ἐνεργείας ἐστὶ τὸ κατὰ τὴν ἕξιν... τοιοῦτον δὴ καὶ τὸ τέλος· ὁρίζεται γὰρ ἕκαστον τῷ τέλει. καλοῦ δὴ ἕνεκα ὁ ἀνδρεῖος ὑπομένει καὶ πράττει τὰ κατὰ τὴν ἀνδρείαν.

| ἐν- | -ἐργ- | -εια |
|---|---|---|
| *en-* | *erg-* | *-eia* |
| "in" | root of *ergon*, "work, deed" | abstract noun suffix |
| → **ἐνέργεια**, "a being-in-work," "at-work-ness" | | |

This is the line the page's first bullet paraphrases directly: the end (τέλος) proper to any being-at-work matches the settled disposition (ἕξις) it flows from, which is why the sentence's own conclusion — *for the sake of the beautiful the courageous person endures* — follows as a logical consequence rather than an added motive.

Source: Bk. III, ch. 8 (Bekker 1116a15-17).

> ἔστι μὲν οὖν ἡ ἀνδρεία τοιοῦτόν τι, λέγονται δὲ καὶ ἕτεραι κατὰ πέντε τρόπους· πρῶτον μὲν ἡ πολιτική· μάλιστα γὰρ ἔοικεν.

| τροπ- | -ος |
|---|---|
| *trop-* | *-os* |
| root of *trepein*, "to turn" | nominalizing suffix |
| → **τρόπος**, "a turning," "a way," "a manner" |

Each look-alike is literally a *tropos* — a "turn" away from true courage that still resembles it in outward shape; the page's five-fold classification follows this sentence's own list almost item for item, starting here with citizen-courage.

Source: Bk. III, ch. 8 (Bekker 1116a25-29).

> ὡμοίωται δʼ αὕτη μάλιστα τῇ πρότερον εἰρημένῃ, ὅτι διʼ ἀρετὴν γίνεται· διʼ αἰδῶ γὰρ καὶ διὰ καλοῦ ὄρεξιν (τιμῆς γάρ) καὶ φυγὴν ὀνείδους, αἰσχροῦ ὄντος.

| αἰδ- | -ώς |
|---|---|
| *aid-* | *-ōs* |
| root shared with *aidesthai*, "to feel shame/reverence before another" | abstract-noun ending |
| → **αἰδώς**, "shame," "a sense of what others would think" |

This names exactly what the page calls citizen-courage's "virtue-adjacent" motive: not virtue itself but *aidōs* — shame before onlookers — paired with desire for honor and flight from reproach.

Source: Bk. III, ch. 8 (Bekker 1117a3-6).

> φυσικωτάτη δʼ ἔοικεν ἡ διὰ τὸν θυμὸν εἶναι, καὶ προσλαβοῦσα προαίρεσιν καὶ τὸ οὗ ἕνεκα ἀνδρεία εἶναι.

| θυμ- | -ός |
|---|---|
| *thym-* | *-os* |
| root denoting spirited passion, anger, the seat of felt urgency | nominative masculine ending |
| → **θυμός**, "spirit," "passion," "anger" |

Aristotle here calls *thymos*-courage the most natural of the look-alikes and says outright that it becomes courage only once choice and the beautiful end are added — precisely the page's account of spirited courage as "courage's nearest neighbor."

Source: Bk. III, ch. 9 (Bekker 1117a35-1117b3).

> διὸ καὶ ἐπίλυπον ἡ ἀνδρεία, καὶ δικαίως ἐπαινεῖται· χαλεπώτερον γὰρ τὰ λυπηρὰ ὑπομένειν ἢ τῶν ἡδέων ἀπέχεσθαι. οὐ μὴν ἀλλὰ δόξειεν ἂν εἶναι τὸ κατὰ τὴν ἀνδρείαν τέλος ἡδύ, ὑπὸ τῶν κύκλῳ δʼ ἀφανίζεσθαι, οἷον κἀν τοῖς γυμνικοῖς ἀγῶσι γίνεται.

| κύκλ- | -ῳ |
|---|---|
| *kykl-* | *-ōi* |
| "circle, ring" | dative singular ending: "in," "by," "round about" |
| → **κύκλῳ**, "in a circle," "encircling" |

The image behind the page's claim that courage's pleasant end is "blocked from sight by the things that encircle it" is literally this dative, κύκλῳ — the painful things ringed around the end hide it the way a boxer's blows hide the wreath waiting past them.

## Related

- [[concepts/doctrine-of-the-mean]] — courage as the mean's first fully worked example, concerning fear and confidence
- [[concepts/to-kalon]] — the beautiful, the end that distinguishes true courage from all five look-alikes
- [[concepts/voluntary-involuntary]] — courage is exercised precisely in facing what is fearsome by choice, not merely willingly
- [[concepts/akolasia]] — temperance and dissipation, the mean and vice Bk. III, ch. 10-12 treats immediately after courage
- [[references/nicomachean-ethics]] — source text (Book III, ch. 6-9)
