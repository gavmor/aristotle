---
title: Distributive Justice
category: concepts
tags: [philosophy, ethics, political-philosophy, ancient-greek]
aliases: [dianemetikon, to dianemetikon dikaion, geometric proportion in justice]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
created: 2026-07-12T00:00:00Z
updated: 2026-07-19T00:00:00Z
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

Source: Aristotle, *Ēthika Nikomacheia*, Bk. V, Bywater's 1894 Oxford Classical Text (Bekker 1831 pagination), via the [Perseus Digital Library](https://scaife.perseus.org/library/urn:cts:greekLit:tlg0086.tlg010/) (public domain). Every word of each cited sentence is glossed below, in order.

### Bk. V, ch. 3 (Bekker 1131a20-24)

> εἰ γὰρ μὴ ἴσοι, οὐκ ἴσα ἕξουσιν, ἀλλʼ ἐντεῦθεν αἱ μάχαι καὶ τὰ ἐγκλήματα, ὅταν ἢ μὴ ἴσα ἴσοι ἢ μὴ ἴσοι ἴσα ἔχωσι καὶ νέμωνται.

```
εἰ  γὰρ  μὴ   ἴσοι          οὐκ  ἴσα           ἕξουσιν            ἀλλʼ  ἐντεῦθεν   αἱ            μάχαι          καὶ  τὰ            ἐγκλήματα          ὅταν      ἢ       μὴ   ἴσα           ἴσοι          ἢ   μὴ   ἴσοι          ἴσα           ἔχωσι          καὶ  νέμωνται
ei  gar  mē   isoi          ouk  isa           hexousin           all'  enteuthen  hai           machai         kai  ta            enklēmata          hotan     ē       mē   isa           isoi          ē   mē   isoi          isa           echōsi         kai  nemōntai
if  for  not  equal.NOM.PL  not  equal.ACC.PL  will-have.FUT.3PL  but   hence      the.NOM.PL.F  fights.NOM.PL  and  the.NOM.PL.N  grievances.NOM.PL  whenever  either  not  equal.ACC.PL  equal.NOM.PL  or  not  equal.NOM.PL  equal.ACC.PL  have.SUBJ.3PL  and  are-allotted.SUBJ.3PL
```

*"For if people are not equal, they will not have equal shares — rather, this is where fights and grievances come from, whenever either unequal people have and are allotted equal shares, or equal people unequal ones."* This is the sentence the Key Ideas' second bullet names directly: the failure mode is *disproportion* — *isoi* (equal people) against *isa* (equal shares) mismatched in either direction — not raw inequality of amount; the *an-* privative that would produce *anisos*, "unequal," is the same negating prefix stacked onto *isos* seen four times over in this one sentence, underlining how the whole passage pivots on matching or mismatching that single root.

### Bk. V, ch. 3 (Bekker 1131a24-29)

> ἔτι ἐκ τοῦ κατʼ ἀξίαν τοῦτο δῆλον· τὸ γὰρ δίκαιον ἐν ταῖς νομαῖς ὁμολογοῦσι πάντες κατʼ ἀξίαν τινὰ δεῖν εἶναι, τὴν μέντοι ἀξίαν οὐ τὴν αὐτὴν λέγουσι πάντες, ἀλλʼ οἱ μὲν δημοκρατικοὶ ἐλευθερίαν, οἱ δʼ ὀλιγαρχικοὶ πλοῦτον, οἳ δʼ εὐγένειαν, οἱ δʼ ἀριστοκρατικοὶ ἀρετήν.

```
ἔτι          ἐκ    τοῦ           κατʼ          ἀξίαν         τοῦτο          δῆλον         τὸ            γὰρ  δίκαιον      ἐν  ταῖς          νομαῖς                ὁμολογοῦσι   πάντες      κατʼ          ἀξίαν         τινὰ         δεῖν      εἶναι   τὴν           μέντοι   ἀξίαν         οὐ   τὴν           αὐτὴν        λέγουσι  πάντες      ἀλλʼ  οἱ            μὲν   δημοκρατικοὶ      ἐλευθερίαν      οἱ            δʼ   ὀλιγαρχικοὶ       πλοῦτον        οἳ                 δʼ   εὐγένειαν          οἱ            δʼ   ἀριστοκρατικοὶ      ἀρετήν
eti          ek    tou           kat'          axian         touto          dēlon         to            gar  dikaion      en  tais          nomais                homologousi  pantes      kat'          axian         tina         dein      einai   tēn           mentoi   axian         ou   tēn           autēn        legousi  pantes      all'  hoi           men   dēmokratikoi      eleutherian     hoi           d'   oligarchikoi      plouton        hoi                d'   eugeneian          hoi           d'   aristokratikoi      aretēn
furthermore  from  the.GEN.SG.N  according-to  worth.ACC.SG  this.NOM.SG.N  clear.NOM.SG  the.NOM.SG.N  for  just.NOM.SG  in  the.DAT.PL.F  distributions.DAT.PL  agree.3PL    all.NOM.PL  according-to  worth.ACC.SG  some.ACC.SG  must.INF  be.INF  the.ACC.SG.F  however  worth.ACC.SG  not  the.ACC.SG.F  same.ACC.SG  say.3PL  all.NOM.PL  but   the.NOM.PL.M  PTCL  democrats.NOM.PL  freedom.ACC.SG  the.NOM.PL.M  and  oligarchs.NOM.PL  wealth.ACC.SG  the-others.NOM.PL  and  good-birth.ACC.SG  the.NOM.PL.M  and  aristocrats.NOM.PL  virtue.ACC.SG
```

*"Further, this is clear from the case of worth: everyone agrees that what is just in distributions must go by some worth, but they do not all name the same worth — democrats say freedom, oligarchs wealth, some good birth, and aristocrats virtue."* *Axian* (from *axios*, "weighing as much as," itself tied to the verb *agō*, "to weigh in the balance") is the single word every faction is fighting over — the Key Ideas' third bullet's whole point is that the formal structure (proportion *kat' axian*) is agreed while the content of *axia* is a live political dispute, and this sentence lists the four rival fillers verbatim.

### Bk. V, ch. 3 (Bekker 1131b10-14)

> καλοῦσι δὲ τὴν τοιαύτην ἀναλογίαν γεωμετρικὴν οἱ μαθηματικοί· ἐν γὰρ τῇ γεωμετρικῇ συμβαίνει καὶ τὸ ὅλον πρὸς τὸ ὅλον ὅπερ ἑκάτερον πρὸς ἑκάτερον.

```
καλοῦσι   δὲ   τὴν           τοιαύτην     ἀναλογίαν          γεωμετρικὴν       οἱ            μαθηματικοί            ἐν  γὰρ  τῇ            γεωμετρικῇ        συμβαίνει    καὶ   τὸ            ὅλον          πρὸς    τὸ            ὅλον          ὅπερ   ἑκάτερον   πρὸς    ἑκάτερον
kalousi   de   tēn           toiautēn     analogian          geōmetrikēn       hoi           mathēmatikoi           en  gar  tēi           geōmetrikēi       symbainei    kai   to            holon         pros    to            holon         hoper  hekateron  pros    hekateron
call.3PL  and  the.ACC.SG.F  such.ACC.SG  proportion.ACC.SG  geometric.ACC.SG  the.NOM.PL.M  mathematicians.NOM.PL  in  for  the.DAT.SG.F  geometric.DAT.SG  happens.3SG  also  the.NOM.SG.N  whole.NOM.SG  toward  the.ACC.SG.N  whole.ACC.SG  which  each       toward  each.ACC.SG
```

*"Mathematicians call this sort of proportion geometric, since in the geometric proportion it works out that the whole stands to the whole exactly as each part stands to each part."* *Geōmetrikēn* is built from *gē* ("earth") plus the *-metr-* root of *metron* ("measure") — literally "earth-measuring" — and this is the mathematicians' own technical label for the ratio-of-ratios the page's Diagram depicts, the reason the Key Ideas' first bullet contrasts it by name with the *arithmētikē* ("number"-based) proportion of [[concepts/corrective-justice|corrective justice]].

### Bk. V, ch. 3 (Bekker 1131b20-24)

> ἐπὶ δὲ τοῦ κακοῦ ἀνάπαλιν· ἐν ἀγαθοῦ γὰρ λόγῳ γίνεται τὸ ἔλαττον κακὸν πρὸς τὸ μεῖζον κακόν· ἔστι γὰρ τὸ ἔλαττον κακὸν μᾶλλον αἱρετὸν τοῦ μείζονος, τὸ δʼ αἱρετὸν ἀγαθόν, καὶ τὸ μᾶλλον μεῖζον.

```
ἐπὶ             δὲ   τοῦ           κακοῦ       ἀνάπαλιν    ἐν  ἀγαθοῦ       γὰρ  λόγῳ            γίνεται      τὸ            ἔλαττον        κακὸν        πρὸς         τὸ            μεῖζον          κακόν        ἔστι    γὰρ  τὸ            ἔλαττον        κακὸν        μᾶλλον  αἱρετὸν              τοῦ              μείζονος        τὸ            δʼ   αἱρετὸν              ἀγαθόν       καὶ  τὸ            μᾶλλον  μεῖζον
epi             de   tou           kakou       anapalin    en  agathou      gar  logōi           ginetai      to            elatton        kakon        pros         to            meizon          kakon        esti    gar  to            elatton        kakon        mallon  haireton             tou              meizonos        to            d'   haireton             agathon      kai  to            mallon  meizon
in-the-case-of  but  the.GEN.SG.N  bad.GEN.SG  conversely  in  good.GEN.SG  for  account.DAT.SG  becomes.3SG  the.NOM.SG.N  lesser.NOM.SG  evil.NOM.SG  relative-to  the.ACC.SG.N  greater.ACC.SG  evil.ACC.SG  is.3SG  for  the.NOM.SG.N  lesser.NOM.SG  evil.NOM.SG  more    choiceworthy.NOM.SG  than-the.GEN.SG  greater.GEN.SG  the.NOM.SG.N  and  choiceworthy.NOM.SG  good.NOM.SG  and  the.NOM.SG.N  more    greater.NOM.SG
```

*"With something bad, though, it runs the other way: the lesser evil counts, in the reckoning of a good, as the greater relative to the greater evil — for the lesser evil is more choiceworthy than the greater, and what is choiceworthy is good, and the more choiceworthy the greater good."* This is the Key Ideas' fourth bullet's inverted case, and it turns on *haireton* (from *haireō*, "to take, seize, choose," plus the *-t-* verbal-adjective suffix marking fitness, "-able/-worthy"): since whatever is *hairetos* counts as good, the lesser of two evils becomes the "greater good" of the pair simply by being the more choiceworthy of the two — the same proportional machinery, reversed in sign rather than redesigned.

### Bk. V, ch. 4 (Bekker 1131b27-29)

> τὸ μὲν γὰρ διανεμητικὸν δίκαιον τῶν κοινῶν ἀεὶ κατὰ τὴν ἀναλογίαν ἐστὶ τὴν εἰρημένην

```
τὸ            μὲν   γὰρ  διανεμητικὸν         δίκαιον      τῶν         κοινῶν                ἀεὶ     κατὰ          τὴν           ἀναλογίαν          ἐστὶ    τὴν           εἰρημένην
to            men   gar  dianemētikon         dikaion      tōn         koinōn                aei     kata          tēn           analogian          esti    tēn           eirēmenēn
the.NOM.SG.N  PTCL  for  distributive.NOM.SG  just.NOM.SG  the.GEN.PL  common-things.GEN.PL  always  according-to  the.ACC.SG.F  proportion.ACC.SG  is.3SG  the.ACC.SG.F  aforementioned.PTCP.ACC.SG
```

*"For the distributive form of the just, applied to common goods, always follows the proportion already described."* *Dianemētikon* is built from *dia-* ("apart, out, distributively") plus the root of *nemō* ("to allot, distribute, apportion by custom") plus the *-ētik-* suffix marking a capacity or tendency (the same work English "-ive" does in "distribut-ive"), rather than a completed act — this is the term the whole page names itself after, and the same suffix pattern makes it grammatically parallel to [[concepts/corrective-justice|*diorthōtikon*]], a parallel no single English word preserves.

## Related

- [[concepts/justice-nicomachean]] — the parent discussion (general vs. particular justice) this page is one species of
- [[concepts/corrective-justice]] — the sibling form, governing transactions by arithmetic rather than geometric proportion
- [[concepts/doctrine-of-the-mean]] — distributive justice is itself a "mean" realized as a proportion, not as a disposition toward feeling
- [[synthesis/virtue-taxonomy]] — treemap depicting this as one of justice's two leaves
- [[synthesis/justice-taxonomy]] — full treemap expanding this branch into honor / money / other divisible goods
- [[references/nicomachean-ethics]] — source text (Book V, ch. 2-3)
