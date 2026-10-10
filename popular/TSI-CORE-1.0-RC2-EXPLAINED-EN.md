# TSI-CORE, explained without advanced mathematics
## What the proposal says, why it might help, and what it has not proved

**Original research author:** Igor Chechelnitsky · **Version:** 1.0-RC2  
**Audience:** General readers, including those without formal mathematics training.  
**Status:** An accessible explanation of a research candidate, not evidence that its applications are valid.  
**Scientific source:** [Canonical specification](../docs/TSI-CORE-1.0-RC2.md) and [English scientific edition](../science/TSI-CORE-1.0-RC2-SCIENTIFIC-EN.md).

---

## 1. Imagine a computer watching the world

A camera sees a bird. A moment later the bird turns, looks different in the image, and flies farther away. A person can still say, “That's the same bird.” What exactly would have to stay the same for a computer to reach a similar conclusion? The outline? The relationships between parts? The pattern of motion?

This is a **motivating example only**. It is not a theorem of TSI. TSI-CORE does **not** recognize birds, faces, cars, or people. It tackles a more basic question first: can we agree on a small formal language for talking about representations, changes, and relationships among them?

## 2. A small rulebook, not a theory of everything

Think of a construction kit. Before building an aircraft, you need to know which parts exist and how they may be connected. TSI-CORE is more like a rulebook for connecting basic parts than a finished aircraft.

It starts with only two types of entities:

- **Representations:** abstract things we may want to describe. Depending on a future application, they might be images, graphs, mathematical expressions, or signals.
- **Transformations:** possible operations on representations. A future application might interpret these as rescaling an image, rewriting an expression, or modifying a graph.

There are three basic relationships: two representations may be *structurally equivalent*; a transformation may *apply* to a representation and produce another; and two transformations may have a *declared composition*. There is also a special *unit transformation*, which leaves every representation unchanged.

That's the entire primitive vocabulary. Time, memory, geometry, probability, information, physical objects, and observers are **not** part of the mandatory kernel.

## 3. The six rules in ordinary language

| Identifier | What it says | Informal analogy |
|---|---|---|
| **AX-C01** | Structural equivalence is reflexive, symmetric, and transitive. | If A matches B in the specified sense and B matches C, then A matches C. |
| **AX-C02** | Given a transformation and an input, there cannot be two different outputs. | The same operation on the same input cannot yield incompatible values. |
| **AX-C04** | A declared composition behaves like executing its two steps in the specified order. | First perform operation G, then operation F. |
| **AX-C05** | The unit transformation maps each representation to itself. | “Do nothing.” |
| **AX-C06** | Composing any operation with the unit on either side is declared and gives that operation. | Adding “do nothing” before or after a step. |
| **AX-C07** | If both parenthesizations of three transformations are declared, their resulting transformations are identical. | Two permitted ways of grouping the same sequence agree. |

Why is **AX-C03** missing? It is a retired historical identifier. What used to be a separate composition-uniqueness axiom turned out to be derivable from other axioms, and is now theorem **TH-C00**. Retaining the gap keeps the audit history traceable.

### Two different kinds of “partial”

An operation may not apply to every input. For example, a square-root operation over the real numbers is not defined at negative inputs if that is the domain chosen by a future module.

Also, a pair of transformations need not have a **declared composite**. Even when we can describe the two-step behavior mathematically, the kernel does not force us to introduce a new composite transformation. This is deliberate.

## 4. What about structural invariants?

An invariant is usually a property preserved under an explicitly specified class of changes. For example, renaming a graph's vertices may leave its connection pattern unchanged. But a rigorous claim requires us to say what structures we are comparing, what counts as equivalent, and what transformations are allowed.

Here is the crucial detail: **TSI-CORE does not assume that all transformations preserve structural equivalence.** Such a requirement is called **AX-C08**, but it is *optional*. The specification presents a model satisfying all six mandatory groups while violating AX-C08.

So the claim “TSI proves that every transformation preserves structure” would be false. A more accurate claim is: “TSI provides a language in which hypotheses about structure preservation can be stated and tested.”

## 5. What has been established mathematically?

**First,** the specification gives a tiny model with one representation and one transformation in which all mandatory rules hold. This shows that the rules **can be satisfied together** in the standard mathematical interpretation.

**Second,** it presents a separate finite countermodel for each mandatory axiom group: a model where that group fails while the other five hold. These examples are intended to show that none of the six rules is redundant.

**Third,** the stated axioms yield some useful logical conclusions: a declared composite is unique; the unit operation cannot have a surprising second output; and existing associative chains agree as specified.

But the final independent re-audit, machine-checked theorem proofs, and independent reproduction of the finite countermodels remain to be completed. Reading a mathematical manuscript is not the same as verifying it in a proof assistant.

## 6. How might this connect to FCO computer vision?

The connection is **prospective**, not proven. A later module named `TSI-STRUCT-0.1` could try to make the following ideas precise:

1. A representation is a structure extracted from a camera frame.
2. An explicit criterion tells us when two observations are structurally equivalent.
3. We specify which changes of lighting, scale, orientation, or viewpoint preserve that criterion.
4. We construct counterexamples in which different real-world objects are mistakenly treated as equivalent.
5. Experiments compare this approach with established computer-vision methods.

None of these steps is already included in the RC2 kernel. The existing FCO HTML program is not proof that TSI works. Useful computer vision requires additional models, tests, and measured results.

## 7. What remains unknown?

We do not yet know whether this kernel offers meaningful advantages over established mathematics for partial maps and composition, whether its primitive structural-equivalence relation belongs in the kernel, or which future extensions will be conservative. It is **not** a predictive physical theory or a theory of consciousness. It is **not** machine-verified in Lean or Isabelle and is **not** empirically established as beneficial for camera recognition.

GitHub can expose the manuscripts, revision history, and audit evidence. Zenodo can later assign a DOI, a persistent identifier. **Neither a GitHub repository nor a DOI certifies scientific correctness.**

## 8. A simple thought experiment

Invent two abstract representations and a rule for deciding whether they are equivalent. Then invent a transformation that only works for some inputs. Ask whether you have accidentally confused “the operation is defined” with “the structure is preserved.” Check whether you silently added any extra rules.

That exercise illustrates why clearly stated assumptions matter. It is not a substitute for formal proofs, countermodels, executable validation, or comparisons with other theories.

## 9. The takeaway

**TSI-CORE is a candidate small mathematical language for representations and partial transformations.** It separates mandatory rules from additional hypotheses so they can be assessed independently. The written specification contains a finite model, proofs, and countermodels; final independent and proof-assistant verification is still pending. The next research question is whether useful applications — perhaps including an FCO-related structural module — can be built on top of it without contrived assumptions.

---

**Authoritative equations and the original normative text:** [`../docs/TSI-CORE-1.0-RC2.md`](../docs/TSI-CORE-1.0-RC2.md). If an analogy here is misleading, correct the analogy rather than silently changing the original axioms.
