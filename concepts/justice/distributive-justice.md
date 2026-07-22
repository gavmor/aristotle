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

```ngloss
\ex εἰ γὰρ μὴ ἴσοι, οὐκ ἴσα ἕξουσιν, ἀλλʼ ἐντεῦθεν αἱ μάχαι καὶ τὰ ἐγκλήματα, ὅταν ἢ μὴ ἴσα ἴσοι ἢ μὴ ἴσοι ἴσα ἔχωσι καὶ νέμωνται.
\gl εἰ [ei] [if]
    γὰρ [gar] [for]
    μὴ [mē] [not]
    ἴσοι [isoi] [equal.NOM.PL]
    οὐκ [ouk] [not]
    ἴσα [isa] [equal.ACC.PL]
    ἕξουσιν [hexousin] [will-have.FUT.3PL]
    ἀλλʼ [all'] [but]
    ἐντεῦθεν [enteuthen] [hence]
    αἱ [hai] [the.NOM.PL.F]
    μάχαι [machai] [fights.NOM.PL]
    καὶ [kai] [and]
    τὰ [ta] [the.NOM.PL.N]
    ἐγκλήματα [enklēmata] [grievances.NOM.PL]
    ὅταν [hotan] [whenever]
    ἢ [ē] [either]
    μὴ [mē] [not]
    ἴσα [isa] [equal.ACC.PL]
    ἴσοι [isoi] [equal.NOM.PL]
    ἢ [ē] [or]
    μὴ [mē] [not]
    ἴσοι [isoi] [equal.NOM.PL]
    ἴσα [isa] [equal.ACC.PL]
    ἔχωσι [echōsi] [have.SUBJ.3PL]
    καὶ [kai] [and]
    νέμωνται [nemōntai] [are-allotted.SUBJ.3PL]
\ft For if people are not equal, they will not have equal shares — rather, this is where fights and grievances come from, whenever either unequal people have and are allotted equal shares, or equal people unequal ones.
```
 This is the sentence the Key Ideas' second bullet names directly: the failure mode is *disproportion* — *isoi* (equal people) against *isa* (equal shares) mismatched in either direction — not raw inequality of amount; the *an-* privative that would produce *anisos*, "unequal," is the same negating prefix stacked onto *isos* seen four times over in this one sentence, underlining how the whole passage pivots on matching or mismatching that single root.

### Bk. V, ch. 3 (Bekker 1131a24-29)

```ngloss
\ex ἔτι ἐκ τοῦ κατʼ ἀξίαν τοῦτο δῆλον· τὸ γὰρ δίκαιον ἐν ταῖς νομαῖς ὁμολογοῦσι πάντες κατʼ ἀξίαν τινὰ δεῖν εἶναι, τὴν μέντοι ἀξίαν οὐ τὴν αὐτὴν λέγουσι πάντες, ἀλλʼ οἱ μὲν δημοκρατικοὶ ἐλευθερίαν, οἱ δʼ ὀλιγαρχικοὶ πλοῦτον, οἳ δʼ εὐγένειαν, οἱ δʼ ἀριστοκρατικοὶ ἀρετήν.
\gl ἔτι [eti] [furthermore]
    ἐκ [ek] [from]
    τοῦ [tou] [the.GEN.SG.N]
    κατʼ [kat'] [according-to]
    ἀξίαν [axian] [worth.ACC.SG]
    τοῦτο [touto] [this.NOM.SG.N]
    δῆλον [dēlon] [clear.NOM.SG]
    τὸ [to] [the.NOM.SG.N]
    γὰρ [gar] [for]
    δίκαιον [dikaion] [just.NOM.SG]
    ἐν [en] [in]
    ταῖς [tais] [the.DAT.PL.F]
    νομαῖς [nomais] [distributions.DAT.PL]
    ὁμολογοῦσι [homologousi] [agree.3PL]
    πάντες [pantes] [all.NOM.PL]
    κατʼ [kat'] [according-to]
    ἀξίαν [axian] [worth.ACC.SG]
    τινὰ [tina] [some.ACC.SG]
    δεῖν [dein] [must.INF]
    εἶναι [einai] [be.INF]
    τὴν [tēn] [the.ACC.SG.F]
    μέντοι [mentoi] [however]
    ἀξίαν [axian] [worth.ACC.SG]
    οὐ [ou] [not]
    τὴν [tēn] [the.ACC.SG.F]
    αὐτὴν [autēn] [same.ACC.SG]
    λέγουσι [legousi] [say.3PL]
    πάντες [pantes] [all.NOM.PL]
    ἀλλʼ [all'] [but]
    οἱ [hoi] [the.NOM.PL.M]
    μὲν [men] [PTCL]
    δημοκρατικοὶ [dēmokratikoi] [democrats.NOM.PL]
    ἐλευθερίαν [eleutherian] [freedom.ACC.SG]
    οἱ [hoi] [the.NOM.PL.M]
    δʼ [d'] [and]
    ὀλιγαρχικοὶ [oligarchikoi] [oligarchs.NOM.PL]
    πλοῦτον [plouton] [wealth.ACC.SG]
    οἳ [hoi] [the-others.NOM.PL]
    δʼ [d'] [and]
    εὐγένειαν [eugeneian] [good-birth.ACC.SG]
    οἱ [hoi] [the.NOM.PL.M]
    δʼ [d'] [and]
    ἀριστοκρατικοὶ [aristokratikoi] [aristocrats.NOM.PL]
    ἀρετήν [aretēn] [virtue.ACC.SG]
\ft Further, this is clear from the case of worth: everyone agrees that what is just in distributions must go by some worth, but they do not all name the same worth — democrats say freedom, oligarchs wealth, some good birth, and aristocrats virtue.
```
 *Axian* (from *axios*, "weighing as much as," itself tied to the verb *agō*, "to weigh in the balance") is the single word every faction is fighting over — the Key Ideas' third bullet's whole point is that the formal structure (proportion *kat' axian*) is agreed while the content of *axia* is a live political dispute, and this sentence lists the four rival fillers verbatim.

### Bk. V, ch. 3 (Bekker 1131b10-14)

```ngloss
\ex καλοῦσι δὲ τὴν τοιαύτην ἀναλογίαν γεωμετρικὴν οἱ μαθηματικοί· ἐν γὰρ τῇ γεωμετρικῇ συμβαίνει καὶ τὸ ὅλον πρὸς τὸ ὅλον ὅπερ ἑκάτερον πρὸς ἑκάτερον.
\gl καλοῦσι [kalousi] [call.3PL]
    δὲ [de] [and]
    τὴν [tēn] [the.ACC.SG.F]
    τοιαύτην [toiautēn] [such.ACC.SG]
    ἀναλογίαν [analogian] [proportion.ACC.SG]
    γεωμετρικὴν [geōmetrikēn] [geometric.ACC.SG]
    οἱ [hoi] [the.NOM.PL.M]
    μαθηματικοί [mathēmatikoi] [mathematicians.NOM.PL]
    ἐν [en] [in]
    γὰρ [gar] [for]
    τῇ [tēi] [the.DAT.SG.F]
    γεωμετρικῇ [geōmetrikēi] [geometric.DAT.SG]
    συμβαίνει [symbainei] [happens.3SG]
    καὶ [kai] [also]
    τὸ [to] [the.NOM.SG.N]
    ὅλον [holon] [whole.NOM.SG]
    πρὸς [pros] [toward]
    τὸ [to] [the.ACC.SG.N]
    ὅλον [holon] [whole.ACC.SG]
    ὅπερ [hoper] [which]
    ἑκάτερον [hekateron] [each]
    πρὸς [pros] [toward]
    ἑκάτερον [hekateron] [each.ACC.SG]
\ft Mathematicians call this sort of proportion geometric, since in the geometric proportion it works out that the whole stands to the whole exactly as each part stands to each part.
```
 *Geōmetrikēn* is built from *gē* ("earth") plus the *-metr-* root of *metron* ("measure") — literally "earth-measuring" — and this is the mathematicians' own technical label for the ratio-of-ratios the page's Diagram depicts, the reason the Key Ideas' first bullet contrasts it by name with the *arithmētikē* ("number"-based) proportion of [[concepts/corrective-justice|corrective justice]].

### Bk. V, ch. 3 (Bekker 1131b20-24)

```ngloss
\ex ἐπὶ δὲ τοῦ κακοῦ ἀνάπαλιν· ἐν ἀγαθοῦ γὰρ λόγῳ γίνεται τὸ ἔλαττον κακὸν πρὸς τὸ μεῖζον κακόν· ἔστι γὰρ τὸ ἔλαττον κακὸν μᾶλλον αἱρετὸν τοῦ μείζονος, τὸ δʼ αἱρετὸν ἀγαθόν, καὶ τὸ μᾶλλον μεῖζον.
\gl ἐπὶ [epi] [in-the-case-of]
    δὲ [de] [but]
    τοῦ [tou] [the.GEN.SG.N]
    κακοῦ [kakou] [bad.GEN.SG]
    ἀνάπαλιν [anapalin] [conversely]
    ἐν [en] [in]
    ἀγαθοῦ [agathou] [good.GEN.SG]
    γὰρ [gar] [for]
    λόγῳ [logōi] [account.DAT.SG]
    γίνεται [ginetai] [becomes.3SG]
    τὸ [to] [the.NOM.SG.N]
    ἔλαττον [elatton] [lesser.NOM.SG]
    κακὸν [kakon] [evil.NOM.SG]
    πρὸς [pros] [relative-to]
    τὸ [to] [the.ACC.SG.N]
    μεῖζον [meizon] [greater.ACC.SG]
    κακόν [kakon] [evil.ACC.SG]
    ἔστι [esti] [is.3SG]
    γὰρ [gar] [for]
    τὸ [to] [the.NOM.SG.N]
    ἔλαττον [elatton] [lesser.NOM.SG]
    κακὸν [kakon] [evil.NOM.SG]
    μᾶλλον [mallon] [more]
    αἱρετὸν [haireton] [choiceworthy.NOM.SG]
    τοῦ [tou] [than-the.GEN.SG]
    μείζονος [meizonos] [greater.GEN.SG]
    τὸ [to] [the.NOM.SG.N]
    δʼ [d'] [and]
    αἱρετὸν [haireton] [choiceworthy.NOM.SG]
    ἀγαθόν [agathon] [good.NOM.SG]
    καὶ [kai] [and]
    τὸ [to] [the.NOM.SG.N]
    μᾶλλον [mallon] [more]
    μεῖζον [meizon] [greater.NOM.SG]
\ft With something bad, though, it runs the other way: the lesser evil counts, in the reckoning of a good, as the greater relative to the greater evil — for the lesser evil is more choiceworthy than the greater, and what is choiceworthy is good, and the more choiceworthy the greater good.
```
 This is the Key Ideas' fourth bullet's inverted case, and it turns on *haireton* (from *haireō*, "to take, seize, choose," plus the *-t-* verbal-adjective suffix marking fitness, "-able/-worthy"): since whatever is *hairetos* counts as good, the lesser of two evils becomes the "greater good" of the pair simply by being the more choiceworthy of the two — the same proportional machinery, reversed in sign rather than redesigned.

### Bk. V, ch. 4 (Bekker 1131b27-29)

```ngloss
\ex τὸ μὲν γὰρ διανεμητικὸν δίκαιον τῶν κοινῶν ἀεὶ κατὰ τὴν ἀναλογίαν ἐστὶ τὴν εἰρημένην
\gl τὸ [to] [the.NOM.SG.N]
    μὲν [men] [PTCL]
    γὰρ [gar] [for]
    διανεμητικὸν [dianemētikon] [distributive.NOM.SG]
    δίκαιον [dikaion] [just.NOM.SG]
    τῶν [tōn] [the.GEN.PL]
    κοινῶν [koinōn] [common-things.GEN.PL]
    ἀεὶ [aei] [always]
    κατὰ [kata] [according-to]
    τὴν [tēn] [the.ACC.SG.F]
    ἀναλογίαν [analogian] [proportion.ACC.SG]
    ἐστὶ [esti] [is.3SG]
    τὴν [tēn] [the.ACC.SG.F]
    εἰρημένην [eirēmenēn] [aforementioned.PTCP.ACC.SG]
\ft For the distributive form of the just, applied to common goods, always follows the proportion already described.
```
 *Dianemētikon* is built from *dia-* ("apart, out, distributively") plus the root of *nemō* ("to allot, distribute, apportion by custom") plus the *-ētik-* suffix marking a capacity or tendency (the same work English "-ive" does in "distribut-ive"), rather than a completed act — this is the term the whole page names itself after, and the same suffix pattern makes it grammatically parallel to [[concepts/corrective-justice|*diorthōtikon*]], a parallel no single English word preserves.

## Related

- [[concepts/justice-nicomachean]] — the parent discussion (general vs. particular justice) this page is one species of
- [[concepts/corrective-justice]] — the sibling form, governing transactions by arithmetic rather than geometric proportion
- [[concepts/doctrine-of-the-mean]] — distributive justice is itself a "mean" realized as a proportion, not as a disposition toward feeling
- [[synthesis/virtue-taxonomy]] — treemap depicting this as one of justice's two leaves
- [[synthesis/justice-taxonomy]] — full treemap expanding this branch into honor / money / other divisible goods
- [[references/nicomachean-ethics]] — source text (Book V, ch. 2-3)
