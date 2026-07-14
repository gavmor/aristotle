---
title: Philia (Friendship)
category: concepts
tags: [philosophy, ethics, virtue-ethics, ancient-greek]
aliases: [friendship, philia]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-08T00:00:00Z
updated: 2026-07-14T00:00:00Z
summary: Books VIII-IX's account of friendship in three species (utility, pleasure, virtue), culminating in the claim that a friend is "another self" and that happiness requires friends.
provenance:
  extracted: 0.75
  inferred: 0.20
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-07-08
tier: core
relationships:
  - target: "[[concepts/to-kalon]]"
    type: uses
  - target: "[[concepts/justice-nicomachean]]"
    type: extends
  - target: "[[concepts/eudaimonia]]"
    type: uses
---

# Philia (Friendship)

Books VIII-IX form the Ethics' longest sustained discussion of a single topic — friendship (*philia*, a broader term than the English "friendship," covering family bonds, political alliance, and business partnership as well as intimate friendship). Aristotle calls it "a certain kind of virtue, or goes with virtue, and is also most necessary for life."

## Diagram

A direct is-a hierarchy: Aristotle names three species of friendship, each defined by a different one of the three loveable things (the useful, the pleasant, the good). No scores or rankings are invented here — the classes state only what each species actually is, per the text.

```mermaid
classDiagram
    class Philia["Philia (Friendship)"]
    class ForUtility["For Utility"] {
        Loves the other for benefit received
        Common among the old, in business
        Dissolves when benefit ends
    }
    class ForPleasure["For Pleasure"] {
        Loves the other for enjoyment
        Common among the young
        Changes as feelings change
    }
    class CompleteFriendship["Complete Friendship"] {
        Wishes the other well for their own sake
        Between the good, alike in virtue
        Also useful and pleasant, as a byproduct
        Rare and lasting: virtue endures
    }
    Philia <|-- ForUtility
    Philia <|-- ForPleasure
    Philia <|-- CompleteFriendship
```

## Key Ideas

- **Three species of friendship**, corresponding to the three things that are loveable — the good, the pleasant, and the useful:
  - **Friendship for utility**: each loves the other for benefit received, not for who the other person is; common among the old and in business. Easily dissolved when the benefit ends.
  - **Friendship for pleasure**: common among the young, who "live in accord with feeling"; changes as quickly as what is found pleasant changes.
  - **Complete friendship** (friendship "in the primary and governing sense"), between people who are good and alike in virtue: each wishes the other well *for the other's own sake*, not incidentally — and since both are good, this friendship is simultaneously useful, pleasant, and lasting, "since virtue is enduring." This kind is necessarily rare, since it requires extended time and trust ("it is not possible for people to know one another until they use up the proverbial amount of salt together"). ^[extracted]
- **Friendship requires mutual, known goodwill** — loving inanimate things (like wine) is not friendship, since there is no reciprocity; nor is unrequited or unrecognized goodwill toward a stranger. Goodwill is "friendship out-of-work" — a beginning, not yet the thing itself. ^[extracted]
- **Friendship and justice track each other**: "to whatever extent people share something in common, to that extent is there a friendship, since that too is the extent to which there is something just" — and the things owed vary by relationship (parent/child, comrades, fellow citizens), so what is unjust also scales with the closeness of the relationship (cheating a comrade is worse than cheating a stranger). Political constitutions (kingship, aristocracy, timocracy, and their corruptions into tyranny, oligarchy, democracy) each have an analogous friendship, weakest or absent in the worst regimes — "in a tyranny there is little or no friendship," since there is nothing shared between ruler and ruled. See [[concepts/justice-nicomachean]]. ^[extracted]
- **Friendships of superiority** (parent-child, older-younger, husband-wife, ruler-ruled) require *proportional*, not equal, exchange — the superior party should be loved more than they love, and honor/gratitude compensate for what cannot be materially repaid (a child, Aristotle says, can never fully repay a parent, which is why a father may disown a son but not vice versa). ^[extracted]
- **A friend is "another self" (*allos autos*)**: the qualities that make a decent person a friend to himself — wishing his own good, wanting his own existence and flourishing, taking pleasure in his own company, agreeing with himself — extend to a friend, treated as an extension of oneself. Correspondingly, a corrupt person is shown to have no real friendship even with himself, being "at civil war" internally, unable to bear his own company, and so incapable of friendship with others either. This underwrites Aristotle's resolution of the puzzle of legitimate **self-love**: most people rightly condemn self-love aimed at money, honor, and bodily pleasure, but a decent person who "loves himself" by always claiming the most beautiful actions for himself is a lover of self in the best sense, and such a person will still sacrifice money, honor, and even life for friends, "since he would choose an intense pleasure for a short time rather than a mild one for a long time... and one great and beautiful action rather than many small ones." ^[extracted]
- **Does the happy person need friends?** Against the view that a self-sufficient, blessed person needs nothing external, Aristotle argues yes: happiness is a being-at-work ([[concepts/energeia]]), and "it is easier to be [continuously at work] among and in relation to others" than alone; moreover we can contemplate a friend's virtuous actions more easily than our own, and a friend's activity is pleasant to observe in the same way one's own is. Since "being aware that one is" is itself pleasant to a good person, and a friend is another self, one ought to want to share a friend's awareness of his own being — which happens through living together and shared conversation, "not feeding in the same place like fatted cattle." ^[extracted]
- **The number of friends is naturally limited**: complete friendship cannot be extended to many people at once ("it is impossible to share a life with many people and spread oneself out among them"), any more than one can be intensely in love with many people simultaneously — a claim that also draws an analogy to a city's natural size limits. ^[extracted]
- **Friends in good and bad fortune**: friends are more *necessary* in misfortune (practical help) but more *beautiful* to have in good fortune (people to do good for); presence of friends is a "mixed blessing" in misfortune, since seeing a friend pained by one's troubles is itself painful — Aristotle recommends inviting friends readily into good fortune but being slow to burden them with bad fortune, and (conversely) going to a friend in misfortune uninvited. ^[extracted]

## Greek Gloss

Source: Bk. IX, ch. 4 (Bekker 1166a30-32).

> τῷ δὴ πρὸς αὑτὸν ἕκαστα τούτων ὑπάρχειν τῷ ἐπιεικεῖ, πρὸς δὲ τὸν φίλον ἔχειν ὥσπερ πρὸς αὑτόν (ἔστι γὰρ ὁ φίλος ἄλλος αὐτός), καὶ ἡ φιλία τούτων εἶναί τι δοκεῖ, καὶ φίλοι οἷς ταῦθʼ ὑπάρχει.

| ἀλ- | -λος |
|---|---|
| *al-* | *-los* |
| root meaning "other, different" (cf. Latin *alius*) | adjective-forming suffix |
| → **ἄλλος**, "other," "another" | |

Aristotle states outright here the formula the page's Key Ideas paraphrase as "a friend is another self" — since all these decent-making traits belong to a person in relation to himself, and he relates to a friend just as to himself, ἄλλος marks the friend as a second instance of the same self rather than a wholly separate other.

Source: Bk. IX, ch. 5 (Bekker 1167a10-14).

> διὸ μεταφέρων φαίη τις ἂν αὐτὴν ἀργὴν εἶναι φιλίαν, χρονιζομένην δὲ καὶ εἰς συνήθειαν ἀφικνουμένην γίνεσθαι φιλίαν, οὐ τὴν διὰ τὸ χρήσιμον οὐδὲ τὴν διὰ τὸ ἡδύ· οὐδὲ γὰρ εὔνοια ἐπὶ τούτοις γίνεται.

| ἀ- | ἐργ- | -ός |
|---|---|---|
| *a-* | *erg-* | *-os* |
| "not, without" (privative alpha) | root of *ergon*, "work, deed" | adjective-forming suffix |
| → **ἀργός**, "without work," "idle, inactive" | | |

This is the line behind the page's claim that goodwill is "friendship out-of-work": Aristotle literally calls goodwill an *ἀργή* (un-worked, inactive) friendship, built from the same *ergon* root as [[concepts/energeia]] but negated — goodwill is friendship that hasn't yet become a being-at-work.

Source: Bk. VIII, ch. 11 (Bekker 1161a29-34).

> ἐν δὲ ταῖς παρεκβάσεσιν, ὥσπερ καὶ τὸ δίκαιον ἐπὶ μικρόν ἐστιν, οὕτω καὶ ἡ φιλία, καὶ ἥκιστα ἐν τῇ χειρίστῃ· ἐν τυραννίδι γὰρ οὐδὲν ἢ μικρὸν φιλίας.

| δίκ- | -αιον |
|---|---|
| *dik-* | *-aion* |
| root of *dikē*, "custom, right, judgment, lawsuit" | adjective/substantive-forming suffix |
| → **δίκαιον**, "the just," "what is right" | |

This is the textual basis for the page's claim that friendship and justice track each other across the constitutions: Aristotle says explicitly that as *τὸ δίκαιον* shrinks in the deviant regimes, so does *φιλία*, vanishing almost entirely under tyranny — confirming that the two concepts scale together rather than merely resembling one another.

## Related

- [[concepts/to-kalon]] — per Sachs, the fullest working-out of the beautiful's role in virtuous action occurs in the friendship books
- [[concepts/justice-nicomachean]] — friendship and justice track the same relationships, with friendship arguably completing what justice alone cannot
- [[concepts/eudaimonia]] — happiness is argued to require friends, against the view that a self-sufficient person needs no one
- [[synthesis/threefold-good]] — treemap of the same loveable-triad that grounds these three species, alongside the general theory of goods it's drawn from
- [[synthesis/constitutions-and-households]] — how friendship tracks justice differently across the constitutional analogues Aristotle finds within the household
- [[synthesis/crown-of-virtue]] — Sachs's editorial claim that friendship is the last and highest of four successive candidates for what organizes all the virtues
- [[concepts/self-love]] — the puzzle of whether "friend as another self" is coherent, resolved by distinguishing two senses of self-love
- [[references/nicomachean-ethics]] — source text (Books VIII-IX)
