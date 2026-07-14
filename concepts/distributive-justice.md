---
title: Distributive Justice
category: concepts
tags: [philosophy, ethics, political-philosophy, ancient-greek]
aliases: [dianemetikon, to dianemetikon dikaion, geometric proportion in justice]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-12T00:00:00Z
updated: 2026-07-14T00:00:00Z
summary: The species of particular justice governing shares of divisible common goods, structured as a geometric proportion between people and their portions.
provenance:
  extracted: 0.75
  inferred: 0.20
  ambiguous: 0.05
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-07-12
tier: supporting
relationships:
  - target: "[[concepts/justice-nicomachean]]"
    type: implements
  - target: "[[concepts/doctrine-of-the-mean]]"
    type: implements
  - target: "[[concepts/corrective-justice]]"
    type: related_to
---

# Distributive Justice

One of the two forms into which Aristotle divides **particular justice** (Bk. V, ch. 2-3) — the Greek is *to dianemetikon dikaion*, "the distributive just," from *dianemein*, "to distribute/apportion." It governs "distributions of honor or money, or as many other things as are divisible, among those who share in the political community."

## Diagram

The claim itself, stated directly with no invented numbers: justice here just *is* the equality of two ratios — merit compared to merit, share compared to share.

```mermaid
classDiagram
    class MeritRatio["Merit ratio: Person A : Person B"]
    class ShareRatio["Share ratio: Share C : Share D"]
    MeritRatio -- ShareRatio : equal ratios = just; unequal = disproportion (unjust)
```

## Key Ideas

- **Structured as a geometric proportion, not an equal share.** What is just is not that everyone gets the same amount, but that shares are proportionate to the people receiving them: "as person A is to person B, so should A's portion be to B's portion." Aristotle works this out formally as a four-term proportion (two people, two shares) — A:B :: C:D — and derives the "linking" of A with C and B with D as what a just distribution actually does, alternating and recombining the ratio so that "the whole is to the whole" as each person is to what they receive. Mathematicians call this *geometrical* proportionality, distinguishing it from the *arithmetic* proportionality of [[concepts/corrective-justice|corrective justice]]. ^[extracted]
- **Injustice here is disproportion, not mere inequality of amount.** Someone who receives too much or too little *relative to their proportionate merit* is treated unjustly, even if the raw quantities look "fair" by some other measure; conversely equal shares to unequal people is exactly where "fights and complaints" arise. ^[extracted]
- **The basis of merit is itself politically contested** — Aristotle notes that everyone agrees distributive justice must track *some* merit, but disagrees on which: "those who favor democracy mean freedom, those who favor oligarchy mean wealth, others mean being well born, and those who favor aristocracy mean virtue." The formal structure (geometric proportion) is constant; what counts as the relevant basis of proportion is a substantive political question the *Ethics* leaves open here (and defers to the *Politics*). ^[extracted]
- **Extends to bad things too, inverted**: with something bad to be apportioned, the lesser evil is treated as the "greater good" in the proportion, since "the lesser evil is more choiceworthy than the greater, and what is chosen is good" — the same proportional logic just runs in the opposite direction. ^[extracted]

## Greek Gloss

Source: Aristotle, *Ēthika Nikomacheia*, Bk. V, ch. 4 (Bekker 1131b27-29), Bywater's 1894 Oxford Classical Text, via the [Perseus Digital Library](https://scaife.perseus.org/library/urn:cts:greekLit:tlg0086.tlg010/) (public domain).

> τὸ μὲν γὰρ διανεμητικὸν δίκαιον τῶν κοινῶν ἀεὶ κατὰ τὴν ἀναλογίαν ἐστὶ τὴν εἰρημένην

**διανεμητικόν** (the operative term, morpheme by morpheme):

| δια- | νεμ | -ητικ- | -όν |
|---|---|---|---|
| *dia-* | *nem* | *-ētik-* | *-on* |
| "apart, out, distributively" | root of *nemō*, "allot, distribute, apportion by custom" | deverbal suffix marking capacity/tendency ("-ive/-able") | neut. nom./acc. sg. ending |

Sachs renders this "the distributive just" — the *-tikos* suffix is doing the same work as English "-ive" in "distribut-ive," marking a capacity or tendency rather than a completed act; the abstract noun *dianemēsis* ("a distributing") would name the act itself, while *dianemētikon* names the *kind of justice disposed toward* that act. This is the same suffix pattern as [[concepts/corrective-justice|*diorthōtikon*]], making the two species grammatically parallel in a way no English translation fully preserves.

Source: Bk. V, ch. 3 (Bekker 1131b10-14).

> καλοῦσι δὲ τὴν τοιαύτην ἀναλογίαν γεωμετρικὴν οἱ μαθηματικοί· ἐν γὰρ τῇ γεωμετρικῇ συμβαίνει καὶ τὸ ὅλον πρὸς τὸ ὅλον ὅπερ ἑκάτερον πρὸς ἑκάτερον.

| γεω- | -μετρ- | -ικ- | -ήν |
|---|---|---|---|
| *geō-* | *-metr-* | *-ik-* | *-ēn* |
| root of *gē*, "earth" | root of *metron*, "measure" | adjective-forming suffix, "-ic," "pertaining to" | fem. acc. sg. ending |
| → **γεωμετρική**, "geometric" — literally "earth-measuring" | | | |

This is the mathematicians' own technical name for the ratio-of-ratios structure described in the Diagram above, and it is precisely why the page's Key Ideas contrast this proportionality with the *arithmetic* proportion of corrective justice — the two Greek adjectives, built from "earth-measure" versus "number" (*arithmos*), name genuinely different operations, not just two flavors of one idea.

Source: Bk. V, ch. 3 (Bekker 1131a20-24).

> εἰ γὰρ μὴ ἴσοι, οὐκ ἴσα ἕξουσιν, ἀλλʼ ἐντεῦθεν αἱ μάχαι καὶ τὰ ἐγκλήματα, ὅταν ἢ μὴ ἴσα ἴσοι ἢ μὴ ἴσοι ἴσα ἔχωσι καὶ νέμωνται.

| ἀν- | ἴσος |
|---|---|
| *an-* | *isos* |
| negative prefix, "not" (before a vowel) | "equal, fair, proportionate" |
| → **ἄνισος**, "unequal," "disproportionate" | |

The sentence names exactly the failure mode the Key Ideas describe: fights (*machai*) and grievances (*enklēmata*) arise not from raw inequality of amount but from *anisos* people receiving equal shares or equal people receiving unequal ones — disproportion, not mere unequal quantity, is the injustice.

Source: Bk. V, ch. 3 (Bekker 1131a24-29).

> ἔτι ἐκ τοῦ κατʼ ἀξίαν τοῦτο δῆλον· τὸ γὰρ δίκαιον ἐν ταῖς νομαῖς ὁμολογοῦσι πάντες κατʼ ἀξίαν τινὰ δεῖν εἶναι, τὴν μέντοι ἀξίαν οὐ τὴν αὐτὴν λέγουσι πάντες, ἀλλʼ οἱ μὲν δημοκρατικοὶ ἐλευθερίαν, οἱ δʼ ὀλιγαρχικοὶ πλοῦτον, οἳ δʼ εὐγένειαν, οἱ δʼ ἀριστοκρατικοὶ ἀρετήν.

| ἀξ- | -ία |
|---|---|
| *ax-* | *-ia* |
| root related to *agō*, "to weigh (in the balance), lead" | abstract noun suffix, "-th," "-ness" (fem.) |
| → **ἀξία**, "worth," "value," "desert," "merit" | |

This is the single word every faction in the sentence is fighting over: all agree distribution must go *kat' axian* ("according to worth"), and the four regime-words that follow — freedom, wealth, good birth, virtue — are simply four rival answers to "worth of what?"

Source: Bk. V, ch. 3 (Bekker 1131b20-24).

> ἐπὶ δὲ τοῦ κακοῦ ἀνάπαλιν· ἐν ἀγαθοῦ γὰρ λόγῳ γίνεται τὸ ἔλαττον κακὸν πρὸς τὸ μεῖζον κακόν· ἔστι γὰρ τὸ ἔλαττον κακὸν μᾶλλον αἱρετὸν τοῦ μείζονος, τὸ δʼ αἱρετὸν ἀγαθόν, καὶ τὸ μᾶλλον μεῖζον.

| αἱρε- | -τ- | -όν |
|---|---|---|
| *haire-* | *-t-* | *-on* |
| root of *haireō*, "to take, seize, choose" | verbal-adjective suffix marking possibility/fitness, "-able," "-worthy" | neut. nom./acc. sg. ending |
| → **αἱρετόν**, "choiceworthy," "to-be-chosen" | | |

The inverted case runs on this one word: since whatever is *hairetos* counts as good, the lesser of two evils becomes the "greater good" of the pair simply by being the more choiceworthy of the two — the same proportional machinery, reversed in sign rather than redesigned.

## Related

- [[concepts/justice-nicomachean]] — the parent discussion (general vs. particular justice) this page is one species of
- [[concepts/corrective-justice]] — the sibling form, governing transactions by arithmetic rather than geometric proportion
- [[concepts/doctrine-of-the-mean]] — distributive justice is itself a "mean" realized as a proportion, not as a disposition toward feeling
- [[synthesis/virtue-taxonomy]] — treemap depicting this as one of justice's two leaves
- [[synthesis/justice-taxonomy]] — full treemap expanding this branch into honor / money / other divisible goods
- [[references/nicomachean-ethics]] — source text (Book V, ch. 2-3)
