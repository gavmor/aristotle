---
title: Philia (Friendship)
category: concepts
tags: [philosophy, ethics, virtue-ethics, ancient-greek]
aliases: [friendship, philia]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-08T00:00:00Z
updated: 2026-07-19T00:00:00Z
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

## Diagrams

### The Three Species of Friendship

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

### The Anatomy of Complete Friendship

An Ishikawa (fishbone) diagram mapping the necessary conditions and constituent parts that must come together to form true, complete friendship.

```mermaid
ishikawa-beta
    Complete Friendship (True Philia)
    Reciprocal Affection
        Active choice of loving
        Mutual awareness
        Wishing good for the other
    Defining Purpose
        Rooted in the good
        Loving the other for themselves
    Living Together
        Sharing life and activities
        Conversing and thinking together
    Equality & Proportion
        Equal relationship
        Proportional affection if unequal
    Time & Trust
        Consuming the proverbial salt
        Thorough testing
        Intimate acquaintance
    Another Self
        Sharing intimately in pain and enjoyment
        Extension of oneself
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

### Bk. VIII, ch. 3 (Bekker 1156a26-30)

```ngloss
\ex ἔτι δὲ προσδεῖται χρόνου καὶ συνηθείας· κατὰ τὴν παροιμίαν γὰρ οὐκ ἔστιν εἰδῆσαι ἀλλήλους πρὶν τοὺς λεγομένους ἅλας συναναλῶσαι· οὐδʼ ἀποδέξασθαι δὴ πρότερον οὐδʼ εἶναι φίλους, πρὶν ἂν ἑκάτερος ἑκατέρῳ φανῇ φιλητὸς καὶ πιστευθῇ.
\gl ἔτι [eti] [also]
    δὲ [de] [PTCL]
    προσδεῖται [prosdeitai] [requires]
    χρόνου [chronou] [time.GEN]
    καὶ [kai] [and]
    συνηθείας· [synētheias] [intimacy.GEN]
    κατὰ [kata] [according-to]
    τὴν [tēn] [the.ACC]
    παροιμίαν [paroimian] [proverb.ACC]
    γὰρ [gar] [for]
    οὐκ [ouk] [not]
    ἔστιν [estin] [is-possible]
    εἰδῆσαι [eidēsai] [to-know]
    ἀλλήλους [allēlous] [one-another.ACC]
    πρὶν [prin] [before]
    τοὺς [tous] [the.ACC.PL]
    λεγομένους [legomenous] [so-called.PTCP]
    ἅλας [halas] [salt.ACC]
    συναναλῶσαι· [synanalōsai] [to-use-up-together]
    οὐδʼ [oud'] [nor]
    ἀποδέξασθαι [apodexasthai] [to-accept]
    δὴ [dē] [PTCL]
    πρότερον [proteron] [beforehand]
    οὐδʼ [oud'] [nor]
    εἶναι [einai] [to-be]
    φίλους, [philous,] [friends.ACC]
    πρὶν [prin] [before]
    ἂν [an] [PTCL]
    ἑκάτερος [hekateros] [each.NOM]
    ἑκατέρῳ [hekaterō] [each.DAT]
    φανῇ [phanē] [appears]
    φιλητὸς [philētos] [lovable]
    καὶ [kai] [and]
    πιστευθῇ. [pisteuthē.] [is-trusted]
\ft Besides, it also needs time and familiarity; as the proverb says, people cannot know each other before they have used up the proverbial quantity of salt together, nor can they accept each other or be friends until each has appeared lovable to the other and been trusted.
```
![[1156a26.mp3]]

This is the textual source behind the page's claim that complete friendship "requires extended time and trust" and "is not possible... until people use up the proverbial amount of salt together": *synētheia* (σύν- "together" + *ēthos*, "custom, character" — the same root that gives *ēthikē*, "ethics" — plus the abstract-noun suffix *-eia*) names the slow-built shared disposition that alone breeds the mutual trust Aristotle says friendship of the complete kind cannot do without.

### Bk. IX, ch. 5 (Bekker 1167a10-14)

```ngloss
\ex διὸ μεταφέρων φαίη τις ἂν αὐτὴν ἀργὴν εἶναι φιλίαν, χρονιζομένην δὲ καὶ εἰς συνήθειαν ἀφικνουμένην γίνεσθαι φιλίαν, οὐ τὴν διὰ τὸ χρήσιμον οὐδὲ τὴν διὰ τὸ ἡδύ· οὐδὲ γὰρ εὔνοια ἐπὶ τούτοις γίνεται.
\gl διὸ [dio] [therefore]
    μεταφέρων [metapherōn] [using-metaphor.PTCP]
    φαίη [phaiē] [might-say]
    τις [tis] [someone]
    ἂν [an] [PTCL]
    αὐτὴν [autēn] [it.ACC]
    ἀργὴν [argēn] [idle.ACC]
    εἶναι [einai] [to-be]
    φιλίαν, [philian,] [friendship.ACC]
    χρονιζομένην [chronizomenēn] [lingering.PTCP]
    δὲ [de] [PTCL]
    καὶ [kai] [and]
    εἰς [eis] [into]
    συνήθειαν [synētheian] [intimacy.ACC]
    ἀφικνουμένην [aphiknoumenēn] [arriving.PTCP]
    γίνεσθαι [ginesthai] [becomes]
    φιλίαν, [philian,] [friendship.ACC]
    οὐ [ou] [not]
    τὴν [tēn] [the.ACC]
    διὰ [dia] [through]
    τὸ [to] [the.ACC]
    χρήσιμον [chrēsimon] [useful]
    οὐδὲ [oude] [nor]
    τὴν [tēn] [the.ACC]
    διὰ [dia] [through]
    τὸ [to] [the.ACC]
    ἡδύ· [hēdy] [pleasant]
    οὐδὲ [oude] [nor]
    γὰρ [gar] [for]
    εὔνοια [eunoia] [goodwill]
    ἐπὶ [epi] [toward]
    τούτοις [toutois] [these.DAT]
    γίνεται. [ginetai.] [arises]
\ft So someone speaking by transference might call it an idle friendship — one that, lingering on and arriving at familiarity, becomes friendship, though not the friendship based on utility or on pleasure, since goodwill does not arise from those either.
```
![[1167a10.mp3]]

This is the line behind the page's claim that goodwill is "friendship out-of-work": *argēn* (privative *a-* "not, without" + *erg-*, the root of *ergon*, "work, deed" + the adjectival suffix *-os*) is built from the very same *erg-* root as [[concepts/energeia]] but negated — goodwill is friendship that has not yet become a being-at-work.

### Bk. VIII, ch. 11 (Bekker 1161a32-33)

```ngloss
\ex ἐν τυραννίδι γὰρ οὐδὲν ἢ μικρὸν φιλίας.
\gl ἐν [en] [in]
    τυραννίδι [tyrannidi] [tyranny.DAT]
    γὰρ [gar] [for]
    οὐδὲν [ouden] [nothing]
    ἢ [ē] [or]
    μικρὸν [mikron] [little]
    φιλίας. [philias.] [friendship.GEN]
\ft For in a tyranny there is little or no friendship.
```
![[1161a32.mp3]]

This is the textual basis for the page's claim that friendship and justice track each other across the constitutions: Aristotle says explicitly that as *dikaion* (δίκ-, the root of *dikē*, "custom, right, judgment" + the substantive-forming suffix *-aion*) shrinks in the deviant regimes, so does *philia*, vanishing almost entirely under tyranny — the two concepts scale together rather than merely resembling each other.

### Bk. IX, ch. 4 (Bekker 1166a31-32)

```ngloss
\ex ἔστι γὰρ ὁ φίλος ἄλλος αὐτός.
\gl ἔστι [esti] [is]
    γὰρ [gar] [for]
    ὁ [ho] [the.NOM]
    φίλος [philos] [friend.NOM]
    ἄλλος [allos] [another.NOM]
    αὐτός. [autos.] [self.NOM]
\ft For a friend is another self.
```
![[1166a31.mp3]]

Aristotle states outright here the formula the page's Key Ideas paraphrase as "a friend is another self": *allos* (the root *al-*, "other, different" — cognate with Latin *alius* — plus the adjective-forming suffix *-los*) marks the friend as a second instance of the same self rather than a wholly separate other.

### Bk. IX, ch. 10 (Bekker 1171a3-4)

```ngloss
\ex ὅτι δʼ οὐχ οἷόν τε πολλοῖς συζῆν καὶ διανέμειν ἑαυτόν, οὐκ ἄδηλον.
\gl ὅτι [hoti] [that]
    δʼ [d'] [but]
    οὐχ [ouch] [not]
    οἷόν [hoion] [possible]
    τε [te] [PTCL]
    πολλοῖς [pollois] [many.DAT]
    συζῆν [suzēn] [to-live-with]
    καὶ [kai] [and]
    διανέμειν [dianemein] [to-distribute]
    ἑαυτόν, [heauton,] [oneself.ACC]
    οὐκ [ouk] [not]
    ἄδηλον. [adēlon.] [unclear]
\ft But that it is not possible to live together with many people and distribute oneself [among them], is not unclear.
```
![[1171a3.mp3]]

This sentence comes right at the heart of Aristotle's argument about the limits on the number of true friends a person can have. He argues that because complete friendship (*philia*) requires actually sharing a life (*suzēn* — literally "living together" from *sun-* "together" plus *zēn* "to live") and distributing one's time and self (*dianemein heauton*), it is practically impossible to do this with many people. True friendship is bottlenecked by the finite nature of a single human life.

## Related

- [[concepts/to-kalon]] — per Sachs, the fullest working-out of the beautiful's role in virtuous action occurs in the friendship books
- [[concepts/justice-nicomachean]] — friendship and justice track the same relationships, with friendship arguably completing what justice alone cannot
- [[concepts/eudaimonia]] — happiness is argued to require friends, against the view that a self-sufficient person needs no one
- [[synthesis/threefold-good]] — treemap of the same loveable-triad that grounds these three species, alongside the general theory of goods it's drawn from
- [[synthesis/constitutions-and-households]] — how friendship tracks justice differently across the constitutional analogues Aristotle finds within the household
- [[synthesis/crown-of-virtue]] — Sachs's editorial claim that friendship is the last and highest of four successive candidates for what organizes all the virtues
- [[concepts/self-love]] — the puzzle of whether "friend as another self" is coherent, resolved by distinguishing two senses of self-love
- [[references/nicomachean-ethics]] — source text (Books VIII-IX)
