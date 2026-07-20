---
title: "Courage (Andreia)"
category: concepts
tags: [philosophy, ethics, virtue-ethics, ancient-greek]
aliases: [andreia, bravery, the mean concerning fear and confidence]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-14T00:00:00Z
updated: 2026-07-19T00:00:00Z
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

### Bk. III, ch. 7 (Bekker 1115b23-24)

> καλοῦ δὴ ἕνεκα ὁ ἀνδρεῖος ὑπομένει καὶ πράττει τὰ κατὰ τὴν ἀνδρείαν.

```
καλοῦ          δὴ    ἕνεκα        ὁ    ἀνδρεῖος        ὑπομένει   καὶ  πράττει  τὰ          κατὰ          τὴν      ἀνδρείαν.
kalou          dē    heneka       ho   andreios        hypomenei  kai  prattei  ta          kata          tēn      andreian
beautiful.GEN  PTCL  for-sake-of  the  courageous-one  endures    and  does     the.ACC.PL  according-to  the.ACC  courage.ACC
```

*So for the sake of the beautiful the courageous person endures and does what accords with courage.* This is the sentence the page's first bullet paraphrases as "acts for the sake of the beautiful": it directly follows the immediately preceding line that every being-at-work's end (τέλος) matches the settled disposition (ἕξις) it flows from, so the conclusion here is a logical consequence rather than an added motive — and note that *andreios* and *andreian* both carry the ἀνδρ- root of *anēr*, "man, adult male," courage cast grammatically as the virtue proper to manhood.

### Bk. III, ch. 8 (Bekker 1116a15-17)

> ἔστι μὲν οὖν ἡ ἀνδρεία τοιοῦτόν τι, λέγονται δὲ καὶ ἕτεραι κατὰ πέντε τρόπους· πρῶτον μὲν ἡ πολιτική· μάλιστα γὰρ ἔοικεν.

```
ἔστι  μὲν   οὖν   ἡ    ἀνδρεία  τοιοῦτόν  τι,      λέγονται    δὲ   καὶ   ἕτεραι   κατὰ          πέντε  τρόπους·  πρῶτον  μὲν   ἡ    πολιτική·     μάλιστα      γὰρ  ἔοικεν.
esti  men   oun   hē   andreia  toiouton  ti       legontai    de   kai   heterai  kata          pente  tropous   prōton  men   hē   politikē      malista      gar  eoiken
is    PTCL  then  the  courage  such      a-thing  are-called  and  also  other    according-to  five   ways.ACC  first   PTCL  the  citizen-kind  most-of-all  for  it-seems
```

*Courage, then, is a thing of this sort, but there are also others called courage in five ways; first the citizen-kind, for it seems closest.* This opens the exact five-fold list the page's third bullet reproduces almost item for item, starting with citizen-courage; each is literally a *tropos* — from *trepein*, "to turn" — a "turning" away from true courage that still keeps its outward shape.

### Bk. III, ch. 8 (Bekker 1116a25-29)

> ὡμοίωται δʼ αὕτη μάλιστα τῇ πρότερον εἰρημένῃ, ὅτι διʼ ἀρετὴν γίνεται· διʼ αἰδῶ γὰρ καὶ διὰ καλοῦ ὄρεξιν (τιμῆς γάρ) καὶ φυγὴν ὀνείδους, αἰσχροῦ ὄντος.

```
ὡμοίωται       δʼ    αὕτη      μάλιστα      τῇ       πρότερον    εἰρημένῃ,           ὅτι      διʼ      ἀρετὴν      γίνεται·        διʼ      αἰδῶ       γὰρ  καὶ  διὰ      καλοῦ          ὄρεξιν      (τιμῆς      γάρ)  καὶ  φυγὴν       ὀνείδους,     αἰσχροῦ       ὄντος.
hōmoiōtai      d'    hautē     malista      tēi      proteron    eirēmenēi           hoti     di'      aretēn      ginetai         di'      aidō       gar  kai  dia      kalou          orexin      (timēs      gar)  kai  phygēn      oneidous      aischrou      ontos
it-is-likened  PTCL  this-one  most-of-all  the.DAT  previously  mentioned.PTCP.DAT  because  through  virtue.ACC  it-comes-to-be  through  shame.ACC  for  and  through  beautiful.GEN  desire.ACC  (honor.GEN  for)  and  flight.ACC  reproach.GEN  shameful.GEN  being.PTCP.GEN
```

*This kind is likened most of all to the one spoken of before, because it comes about through virtue — through shame, and desire of the beautiful (for honor), and flight from reproach, since that is shameful.* This names exactly what the page calls citizen-courage's "virtue-adjacent" motive: not virtue itself but *aidōs* — built on the root of *aidesthai*, "to feel shame or reverence before another" — paired with desire for honor and flight from reproach.

### Bk. III, ch. 8 (Bekker 1117a3-6)

> φυσικωτάτη δʼ ἔοικεν ἡ διὰ τὸν θυμὸν εἶναι, καὶ προσλαβοῦσα προαίρεσιν καὶ τὸ οὗ ἕνεκα ἀνδρεία εἶναι.

```
φυσικωτάτη    δʼ    ἔοικεν    ἡ        διὰ      τὸν      θυμὸν       εἶναι,  καὶ  προσλαβοῦσα        προαίρεσιν  καὶ  τὸ       οὗ         ἕνεκα        ἀνδρεία  εἶναι.
physikōtatē   d'    eoiken    hē       dia      ton      thymon      einai   kai  proslabousa        proairesin  kai  to       hou        heneka       andreia  einai
most-natural  PTCL  it-seems  the-one  through  the.ACC  spirit.ACC  to-be   and  having-added.PTCP  choice.ACC  and  the.ACC  which.GEN  for-sake-of  courage  to-be
```

*The most natural kind seems to be the one through spirit, and once it has taken on choice and the end for whose sake, it is courage.* Aristotle calls *thymos*-courage the most natural of the look-alikes and says outright it becomes courage only once choice and the beautiful end are added onto it — precisely the page's account of spirited courage as "courage's nearest neighbor"; *thymos* itself names the spirited passion or seat of felt urgency, the surge Homer calls into a warrior's chest.

### Bk. III, ch. 9 (Bekker 1117b1-4)

> οὐ μὴν ἀλλὰ δόξειεν ἂν εἶναι τὸ κατὰ τὴν ἀνδρείαν τέλος ἡδύ, ὑπὸ τῶν κύκλῳ δʼ ἀφανίζεσθαι, οἷον κἀν τοῖς γυμνικοῖς ἀγῶσι γίνεται.

```
οὐ   μὴν   ἀλλὰ  δόξειεν        ἂν    εἶναι  τὸ   κατὰ        τὴν      ἀνδρείαν     τέλος  ἡδύ,      ὑπὸ   τῶν         κύκλῳ           δʼ    ἀφανίζεσθαι,   οἷον     κἀν      τοῖς        γυμνικοῖς      ἀγῶσι         γίνεται.
ou   mēn   alla  doxeien        an    einai  to   kata        tēn      andreian     telos  hēdy      hypo  tōn         kyklōi          d'    aphanizesthai  hoion    kan      tois        gymnikois      agōsi         ginetai
not  PTCL  but   it-would-seem  PTCL  to-be  the  concerning  the.ACC  courage.ACC  end    pleasant  by    the.GEN.PL  encircling.DAT  PTCL  to-be-hidden   just-as  even-in  the.DAT.PL  gymnastic.DAT  contests.DAT  it-happens
```

*Nevertheless the end that belongs to courage would seem to be pleasant, but hidden by the things that surround it, as also happens in athletic contests.* The image behind the page's second bullet — that courage's pleasant end is "blocked from sight by the things that encircle it" — is literally this dative, κύκλῳ, "in a circle" or "encircling": the painful blows ringed around the end hide it the way a boxer's punishment hides the wreath waiting past it.

## Related

- [[concepts/doctrine-of-the-mean]] — courage as the mean's first fully worked example, concerning fear and confidence
- [[concepts/to-kalon]] — the beautiful, the end that distinguishes true courage from all five look-alikes
- [[concepts/voluntary-involuntary]] — courage is exercised precisely in facing what is fearsome by choice, not merely willingly
- [[concepts/akolasia]] — temperance and dissipation, the mean and vice Bk. III, ch. 10-12 treats immediately after courage
- [[references/nicomachean-ethics]] — source text (Book III, ch. 6-9)
