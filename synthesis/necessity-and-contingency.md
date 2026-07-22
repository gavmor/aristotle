---
title: "Necessity and Contingency"
category: synthesis
tags: [philosophy, ethics, metaphysics, ancient-greek, visualization]
aliases: [incapable of being otherwise, capable of being otherwise, necessity, contingency]
sources:
  - "Nicomachean Ethics - Aristotle.txt"
summary: Aristotle's fundamental ontological division between things that are incapable of being otherwise (necessity) and things that are capable of being otherwise (contingency).
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.80
lifecycle: draft
lifecycle_changed: 2026-07-22
tier: supporting
relationships:
  - target: "[[concepts/incapable-of-being-otherwise]]"
    type: related_to
  - target: "[[concepts/capable-of-being-otherwise]]"
    type: related_to
  - target: "[[concepts/soul/knowing-part]]"
    type: related_to
  - target: "[[concepts/soul/calculating-part]]"
    type: related_to
created: 2026-07-22T08:10:00Z
updated: 2026-07-22T08:24:00Z
---

# Necessity and Contingency

Aristotle's framework relies on a fundamental ontological division between two realms of being: that which is strictly necessary and that which is contingent. This distinction governs both the structure of the world and the parts of the rational soul designed to apprehend it.

## The Two Realms

- **[[concepts/incapable-of-being-otherwise|Necessity (Incapable of Being Otherwise)]]**: The realm of eternal, fixed truths (including the past). These are the objects of true knowledge (*episteme*) and are contemplated by the knowing part of the soul. No one deliberates about them.
- **[[concepts/capable-of-being-otherwise|Contingency (Capable of Being Otherwise)]]**: The realm of variable things that can be otherwise. This is the domain of human deliberation, contemplated by the calculating part of the soul. It further divides into:
  - **Things made** (the realm of art / *[[art|techne]]*)
  - **Things done** (the realm of human action / *[[praxis]]*)

## Diagram

```mermaid
classDiagram
    class Reality["All Things"]
    class Necessity["Incapable of Being Otherwise (Necessity)"] {
        Everlasting, ungenerated, indestructible
        Objects of true knowledge / demonstration
        No deliberation possible
        Includes the Past
    }
    class Contingency["Capable of Being Otherwise (Contingency)"] {
        Variable, lacks absolute necessity
        Domain of calculation and deliberation
    }
    class Making["Things Made (Art / Techne)"] {
        Source is in the maker
    }
    class Doing["Things Done (Action / Praxis)"] {
        Governed by practical judgment
    }
    
    Reality <|-- Necessity
    Reality <|-- Contingency
    Contingency <|-- Making
    Contingency <|-- Doing
```

## Related

- [[synthesis/five-ways-of-truth]] — how this ontological division maps onto the five truth-disclosing capacities of the soul
- [[concepts/incapable-of-being-otherwise]] — the concept page for necessity and its Greek citations
- [[concepts/capable-of-being-otherwise]] — the concept page for contingency and its Greek citations
- [[concepts/soul/knowing-part]] — the part of the rational soul that contemplates necessity
- [[concepts/soul/calculating-part]] — the part of the rational soul that contemplates contingency
- [[concepts/art]] — the truth-disclosing capacity for things made
- [[concepts/phronesis]] — practical judgment, the truth-disclosing capacity for things done
