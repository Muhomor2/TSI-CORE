# TSI-CORE-1.0-RC2

## Minimal Formal Kernel for Representations and Partial Transformations

**Version:** 1.0-RC2  
**Document class:** Canonical minimal-kernel specification  
**Status:** Publication candidate; mathematically audited, not yet machine-verified  
**Logical basis:** Classical many-sorted first-order logic with equality  
**Author:** Igor Chechelnitsky  
**Date:** 2026-07-30  
**Language:** English  
**Intended repositories:** GitHub and Zenodo  

---

## Abstract

TSI-CORE is a deliberately minimal many-sorted first-order theory for reasoning about representations, partial transformations, declared partial composition, structural equivalence, and a distinguished unit transformation. The kernel contains exactly two sorts, three primitive relations, one distinguished constant, and six mandatory axiom groups. It does not introduce time, dynamics, memory, probability, information, geometry, topology, computation, observation, physical objects, or empirical semantics.

The purpose of the kernel is not to assert a theory of reality. Its purpose is to provide a small common formal substrate against which independently developed extension modules can be stated, audited, compared, rejected, or replaced. The kernel is finitely satisfiable. Explicit finite countermodels are supplied for the independence of each mandatory axiom from the other five. A proposed structural-preservation principle is shown not to follow from the mandatory kernel and is therefore retained only as an optional module axiom.

This release candidate adds an explicit epistemic-status statement, a failure and revision policy, a conservative-extension contract, a publication checklist, and a distinction between logical consistency and scientific usefulness. No mandatory formula of the previously audited kernel is changed.

---

## 0. Reader Contract

This document is normative for TSI-CORE-1.0-RC2.

1. Only the signature and mandatory axioms in Sections 2 and 3 define the kernel.
2. Explanatory prose, examples, roadmaps, and intended applications do not add axioms.
3. Derived definitions are abbreviations and introduce no new primitive entities.
4. Derived theorems may be used only with the assumptions explicitly stated in their proofs.
5. No empirical interpretation is part of the kernel.
6. Logical consistency does not establish scientific usefulness.
7. A successful extension does not prove that the kernel is uniquely necessary.
8. A failed extension does not by itself prove inconsistency, but it may demonstrate inadequacy.
9. Any formula-changing revision requires a new version identifier.
10. Future modules must not silently redefine kernel symbols.
11. Machine verification is not claimed until proof-assistant sources compile and reproduce all stated results.
12. This release is a candidate for public review, not a declaration that the wider TSI research program is correct.

---

# 1. Purpose, Scope, and Scientific Status

## 1.1 Purpose

TSI-CORE fixes the minimum common vocabulary required to discuss:

1. representations;
2. transformations;
3. partial application of transformations to representations;
4. declared partial composition of transformations;
5. structural equivalence between representations;
6. a distinguished unit transformation.

The kernel is intended to support modular research. A future theory of time, dynamics, memory, probability, information, observation, or cognition may refer to the kernel, but none of those notions is presupposed here.

## 1.2 Why the kernel is intentionally small

A broad foundational theory can easily become unfalsifiable because every new problem is answered by adding another primitive entity or another unrestricted axiom. TSI-CORE adopts the opposite design rule:

> A notion belongs to the kernel only when removing it prevents the intended minimal discourse about representations and partial transformations.

Everything else must be introduced by a separately justified module.

This restriction has four purposes:

- **auditability:** a small theory is easier to inspect for hidden assumptions;
- **reusability:** applications with different semantics can share the same formal substrate;
- **revisability:** an extension can fail without forcing immediate reconstruction of every other module;
- **epistemic discipline:** formal consistency is kept distinct from empirical adequacy.

## 1.3 What TSI-CORE is

TSI-CORE is:

- a typed first-order formal specification;
- a theory of partial action and declared partial composition;
- a minimal common interface for future modules;
- a candidate reusable formal kernel;
- an object of mathematical and machine-verification study.

## 1.4 What TSI-CORE is not

TSI-CORE is not:

- a physical theory;
- a theory of consciousness;
- a theory of information by itself;
- a computational architecture;
- a theory of time or causality;
- a probability theory;
- a category-theoretic foundation;
- an ontology of objects;
- a proof that the TSI or FCO research directions are useful;
- a claim of novelty relative to every existing algebraic formalism;
- a claim that all transformations preserve structural equivalence.

## 1.5 Epistemic status

The present status is:

\[
\boxed{\text{formally specified} \;+\; \text{finitely satisfiable} \;+\; \text{finite independence witnesses}}
\]

but not yet:

\[
\boxed{\text{machine-verified} \;+\; \text{empirically validated} \;+\; \text{shown necessary for applications}}
\]

The kernel must therefore be treated as a **research candidate**. Its long-term retention depends on whether later modules can use it without artificial encodings, hidden strengthening, or repeated reformulation of its primitives.

---

# 2. Formal Language

## 2.1 Logical framework

The underlying logic is classical many-sorted first-order logic with equality.

Logical symbols are:

\[
\neg,\quad \land,\quad \lor,\quad \rightarrow,\quad
\leftrightarrow,\quad \forall,\quad \exists,\quad =
\]

Equality is logical equality within each sort. Every sort is non-empty.

No set sort, function-space sort, real-number sort, temporal sort, or modal operator belongs to the kernel language.

## 2.2 Sorts

The language contains exactly two primitive sorts:

\[
\mathsf{Rep}
\qquad
\mathsf{Trans}
\]

Their intended readings are:

- \(\mathsf{Rep}\): representations;
- \(\mathsf{Trans}\): transformations.

The words “representation” and “transformation” are formal labels. The kernel does not prescribe what their elements are in any application.

Typical variables are:

\[
X,Y,Z,X',Y',Z' : \mathsf{Rep},
\]

\[
f,g,h,u,v,w,z,h_1,h_2 : \mathsf{Trans}.
\]

## 2.3 Primitive signature

The non-logical signature contains exactly four symbols.

### SIG-C01 — Structural equivalence

\[
\equiv_{\mathsf S}
\;\subseteq\;
\mathsf{Rep}\times\mathsf{Rep}.
\]

The expression

\[
X\equiv_{\mathsf S}Y
\]

means that \(X\) and \(Y\) are structurally equivalent according to the interpretation supplied by a model or extension.

The kernel does not define structural equivalence as isomorphism, metric proximity, observational equivalence, behavioral equivalence, or equality. Any such interpretation belongs to a module.

### SIG-C02 — Partial application

\[
\operatorname{Apply}
\;\subseteq\;
\mathsf{Trans}\times\mathsf{Rep}\times\mathsf{Rep}.
\]

The formula

\[
\operatorname{Apply}(f,X,Y)
\]

reads:

> transformation \(f\) is defined at representation \(X\) and yields representation \(Y\).

Application is represented relationally so that partiality is expressible without adding undefined values or option objects to the kernel.

### SIG-C03 — Declared composition

\[
\operatorname{Comp}
\;\subseteq\;
\mathsf{Trans}\times\mathsf{Trans}\times\mathsf{Trans}.
\]

The formula

\[
\operatorname{Comp}(f,g,h)
\]

reads:

\[
h=f\circ g,
\]

with \(g\) applied first and \(f\) second.

`Comp` is a declaration relation. The kernel does not require every pair of transformations to possess a declared composite.

### SIG-C04 — Distinguished unit

\[
e:\mathsf{Trans}.
\]

The constant \(e\) is the distinguished unit transformation.

## 2.4 Signature closure

No additional primitive symbol belongs to TSI-CORE-1.0-RC2.

In particular, the following are not primitive:

- domains and ranges;
- trajectories;
- histories;
- events;
- states;
- time points;
- probabilities;
- entropy;
- information;
- objects;
- observers;
- memories;
- metrics;
- coordinates;
- derivatives;
- causal arrows;
- computational procedures.

---

# 3. Derived Definitions

All definitions in this section are abbreviations in the kernel language. They add no axioms.

## DEF-C01 — Definedness

\[
\operatorname{DefinedAt}(f,X)
\;\;:\!\!\iff\;\;
\exists Y\,\operatorname{Apply}(f,X,Y).
\]

## DEF-C02 — Reachability

\[
\operatorname{Reaches}(f,Y)
\;\;:\!\!\iff\;\;
\exists X\,\operatorname{Apply}(f,X,Y).
\]

## DEF-C03 — Total transformation

\[
\operatorname{Total}(f)
\;\;:\!\!\iff\;\;
\forall X\,\operatorname{DefinedAt}(f,X).
\]

## DEF-C04 — Empty action

\[
\operatorname{EmptyAction}(f)
\;\;:\!\!\iff\;\;
\forall X\,\forall Y\,
\neg\operatorname{Apply}(f,X,Y).
\]

This definition does not assert that an empty transformation exists.

## DEF-C05 — Extensional equivalence of transformations

\[
f\approx_{\mathrm{ext}}g
\;\;:\!\!\iff\;\;
\forall X\,\forall Y
\left(
\operatorname{Apply}(f,X,Y)
\leftrightarrow
\operatorname{Apply}(g,X,Y)
\right).
\]

This compares application graphs. The kernel does not identify extensionally equivalent transformations.

## DEF-C06 — Structural transformation

\[
\operatorname{Structural}(f)
\;\;:\!\!\iff\;\;
\forall X\,X'\,Y\,Y'
\Big[
X\equiv_{\mathsf S}X'
\land
\operatorname{Apply}(f,X,Y)
\land
\operatorname{Apply}(f,X',Y')
\rightarrow
Y\equiv_{\mathsf S}Y'
\Big].
\]

This definition requires structural preservation only where both applications exist. It does not imply domain closure under structural equivalence.

## DEF-C07 — Kernel sentence

A **kernel sentence** is a closed formula formed solely from:

- the two kernel sorts;
- the four primitive kernel symbols;
- logical symbols and equality.

This notion is used in the conservative-extension policy.

---

# 4. Mandatory Axiom System

There are exactly six mandatory axiom groups.

The historical identifier `AX-C03` is retired. Earlier drafts used that position for functionality of declared composition. That formula is now derivable as TH-C00 and is therefore not an axiom.

## AX-C01 — Structural equivalence

Structural equivalence is an equivalence relation:

\[
\forall X\;X\equiv_{\mathsf S}X,
\]

\[
\forall X\,Y\,
\big(
X\equiv_{\mathsf S}Y
\rightarrow
Y\equiv_{\mathsf S}X
\big),
\]

\[
\forall X\,Y\,Z\,
\big(
X\equiv_{\mathsf S}Y
\land
Y\equiv_{\mathsf S}Z
\rightarrow
X\equiv_{\mathsf S}Z
\big).
\]

## AX-C02 — Functionality of application

\[
\forall f\,X\,Y\,Z\;
\Big[
\operatorname{Apply}(f,X,Y)
\land
\operatorname{Apply}(f,X,Z)
\rightarrow
Y=Z
\Big].
\]

Thus each transformation behaves as a partial function on representations.

AX-C02 does not imply that application is total.

## AX-C04 — Correctness of declared composition

\[
\forall f\,g\,h\;
\Big[
\operatorname{Comp}(f,g,h)
\rightarrow
\forall X\,Z
\Big(
\operatorname{Apply}(h,X,Z)
\leftrightarrow
\exists Y
[
\operatorname{Apply}(g,X,Y)
\land
\operatorname{Apply}(f,Y,Z)
]
\Big)
\Big].
\]

Only the displayed direction is assumed.

The axiom states:

> whenever a composite \(h=f\circ g\) is declared, the application graph of \(h\) is exactly the relational composite of the application graphs of \(g\) and \(f\).

It does not state:

> whenever a transformation has the correct composite graph, it must be declared as the composite.

This asymmetry is intentional. The converse, combined with additional kernel principles, risks forcing an extensional collapse of transformations.

## AX-C05 — Action of the unit

\[
\forall X\;\operatorname{Apply}(e,X,X).
\]

The unit is defined on every representation and returns that representation.

Together with AX-C02, this yields uniqueness of its value.

## AX-C06 — Unit compositions

AX-C06 has two named conjuncts:

\[
\text{AX-C06}_{L}:
\qquad
\forall f\;\operatorname{Comp}(e,f,f),
\]

\[
\text{AX-C06}_{R}:
\qquad
\forall f\;\operatorname{Comp}(f,e,f).
\]

The mandatory axiom is:

\[
\text{AX-C06}
:=
\text{AX-C06}_{L}
\land
\text{AX-C06}_{R}.
\]

## AX-C07 — Conditional intensional associativity

\[
\forall f\,g\,h\,u\,v\,w\,z
\Big[
\operatorname{Comp}(f,g,u)
\land
\operatorname{Comp}(u,h,v)
\land
\operatorname{Comp}(g,h,w)
\land
\operatorname{Comp}(f,w,z)
\rightarrow
v=z
\Big].
\]

AX-C07 is conditional because it compares only branches whose required composites are declared.

It is intensional because the conclusion is equality of transformations, not merely equality of their application graphs.

It does not require the existence of either associative branch.

---

# 5. Optional and Explicitly Excluded Principles

## 5.1 AX-C08 — Optional structural preservation

\[
\text{AX-C08}:
\qquad
\forall f\;\operatorname{Structural}(f).
\]

AX-C08 is not part of the mandatory kernel.

A module may adopt AX-C08 when all of its transformations are intended to preserve the selected structural equivalence. Other modules may reject it.

## 5.2 Total application

Not assumed:

\[
\forall f\,X\,\exists Y\,
\operatorname{Apply}(f,X,Y).
\]

## 5.3 Total composition

Not assumed:

\[
\forall f\,g\,\exists h\,
\operatorname{Comp}(f,g,h).
\]

## 5.4 Transformation extensionality

Not assumed:

\[
f\approx_{\mathrm{ext}}g
\rightarrow
f=g.
\]

Distinct transformations may possess the same application graph.

This permits future modules to distinguish transformations by provenance, internal construction, cost, history, label, implementation, or other intensional data, provided those distinctions are introduced outside the kernel.

## 5.5 Domain closure under structural equivalence

Not assumed:

\[
X\equiv_{\mathsf S}X'
\land
\operatorname{DefinedAt}(f,X)
\rightarrow
\operatorname{DefinedAt}(f,X').
\]

## 5.6 Mandatory empty transformation

Not assumed:

\[
\exists f\;\operatorname{EmptyAction}(f).
\]

## 5.7 Algebraic principles not assumed

The kernel assumes no:

- inverse;
- cancellation;
- commutativity;
- idempotence;
- absorbing element;
- zero transformation;
- order relation on transformations;
- lattice structure;
- closure under arbitrary composition;
- unique decomposition;
- factorization system.

---

# 6. Derived Theorems

## TH-C00 — Functionality of declared composition

\[
\forall f\,g\,h_1\,h_2
\Big[
\operatorname{Comp}(f,g,h_1)
\land
\operatorname{Comp}(f,g,h_2)
\rightarrow
h_1=h_2
\Big].
\]

### Dependency

\[
\boxed{
\text{AX-C06}_{R}
+
\text{AX-C07}
\vdash
\text{TH-C00}
}
\]

### Proof

Assume:

\[
\operatorname{Comp}(f,g,h_1)
\]

and

\[
\operatorname{Comp}(f,g,h_2).
\]

By \(\text{AX-C06}_{R}\):

\[
\operatorname{Comp}(h_1,e,h_1)
\]

and

\[
\operatorname{Comp}(g,e,g).
\]

Instantiate AX-C07 with:

\[
h:=e,\qquad
u:=h_1,\qquad
v:=h_1,\qquad
w:=g,\qquad
z:=h_2.
\]

Its antecedent becomes:

\[
\operatorname{Comp}(f,g,h_1)
\land
\operatorname{Comp}(h_1,e,h_1)
\land
\operatorname{Comp}(g,e,g)
\land
\operatorname{Comp}(f,g,h_2).
\]

All four conjuncts hold. Therefore:

\[
h_1=h_2.
\]

\[
\blacksquare
\]

### Consequence

Although `Comp` is represented as a relation, the mandatory axioms force it to be functional in its third argument.

### Important asymmetry

The proof uses only \(\text{AX-C06}_{R}\). It does not use \(\text{AX-C06}_{L}\).

This does not remove the left-unit law from the kernel. It records only the minimal dependency of TH-C00.

## TH-C01 — Uniqueness of the unit value

\[
\forall X\,Y
\Big(
\operatorname{Apply}(e,X,Y)
\rightarrow
Y=X
\Big).
\]

### Dependency

\[
\boxed{
\text{AX-C02}
+
\text{AX-C05}
\vdash
\text{TH-C01}
}
\]

### Proof

By AX-C05:

\[
\operatorname{Apply}(e,X,X).
\]

Assume additionally:

\[
\operatorname{Apply}(e,X,Y).
\]

By AX-C02:

\[
Y=X.
\]

\[
\blacksquare
\]

## TH-C02 — Extensional associativity of existing branches

Assume:

\[
\operatorname{Comp}(f,g,u),
\]

\[
\operatorname{Comp}(u,h,v),
\]

\[
\operatorname{Comp}(g,h,w),
\]

\[
\operatorname{Comp}(f,w,z).
\]

Then:

\[
v\approx_{\mathrm{ext}}z.
\]

### Dependency

\[
\boxed{
\text{AX-C04}
\vdash
\text{TH-C02}_{\mathrm{ext}}
}
\]

AX-C07 strengthens the conclusion to:

\[
v=z.
\]

### Proof sketch

By AX-C04, applying \(v\) is equivalent to:

1. applying \(h\);
2. applying \(g\);
3. applying \(f\).

By AX-C04 again, applying \(z\) is equivalent to exactly the same three-stage relation. Hence \(v\) and \(z\) possess the same application graph:

\[
v\approx_{\mathrm{ext}}z.
\]

AX-C07 identifies the two declared transformations intensionally.

\[
\blacksquare
\]

## TH-C03 — Totality of the unit

\[
\operatorname{Total}(e).
\]

### Proof

From AX-C05, for every \(X\):

\[
\operatorname{Apply}(e,X,X).
\]

Therefore:

\[
\exists Y\,\operatorname{Apply}(e,X,Y).
\]

Hence:

\[
\forall X\,\operatorname{DefinedAt}(e,X).
\]

\[
\blacksquare
\]

TH-C03 is included as an elementary corollary, not as part of the frozen historical theorem numbering TH-C00–TH-C02.

## TH-C04 — Reflexivity of extensional equivalence

\[
\forall f\;f\approx_{\mathrm{ext}}f.
\]

This follows directly from DEF-C05 and propositional logic.

## TH-C05 — Extensional equivalence is an equivalence relation

The relation \(\approx_{\mathrm{ext}}\) is reflexive, symmetric, and transitive on \(\mathsf{Trans}\).

This is a definitional theorem of classical logic and does not require the mandatory axioms.

---

# 7. Model-Theoretic Semantics

## 7.1 Kernel structure

A TSI-CORE structure is a tuple

\[
\mathfrak M
=
\left(
R,
T,
E_{\mathsf S},
A,
C,
e^{\mathfrak M}
\right),
\]

where:

- \(R\neq\varnothing\) interprets \(\mathsf{Rep}\);
- \(T\neq\varnothing\) interprets \(\mathsf{Trans}\);
- \(E_{\mathsf S}\subseteq R\times R\) interprets \(\equiv_{\mathsf S}\);
- \(A\subseteq T\times R\times R\) interprets \(\operatorname{Apply}\);
- \(C\subseteq T\times T\times T\) interprets \(\operatorname{Comp}\);
- \(e^{\mathfrak M}\in T\) interprets \(e\).

A model of TSI-CORE is a structure satisfying AX-C01, AX-C02, AX-C04, AX-C05, AX-C06, and AX-C07.

## 7.2 No hidden semantic commitment

The set \(R\) may consist of:

- strings;
- graphs;
- states;
- equivalence classes;
- probability distributions;
- formal terms;
- sensor frames;
- physical configurations;
- arbitrary abstract objects.

The set \(T\) may consist of:

- partial functions;
- programs;
- rewrite rules;
- labeled operations;
- morphism-like entities;
- abstract transformation tokens.

These examples are not restrictions.

## 7.3 Partiality

A transformation \(f\) may be undefined at \(X\):

\[
\neg\operatorname{DefinedAt}(f,X).
\]

A pair \((f,g)\) may have no declared composite:

\[
\neg\exists h\,\operatorname{Comp}(f,g,h).
\]

The kernel distinguishes these two forms of partiality:

1. partiality of action;
2. partiality of declared composition.

Neither is encoded through a distinguished undefined value.

---

# 8. Finite Satisfiability

## 8.1 Minimal model \(\mathfrak M_0\)

Let:

\[
\mathsf{Rep}^{\mathfrak M_0}=\{r\},
\]

\[
\mathsf{Trans}^{\mathfrak M_0}=\{e\},
\]

\[
\equiv_{\mathsf S}^{\mathfrak M_0}=\{(r,r)\},
\]

\[
\operatorname{Apply}^{\mathfrak M_0}=\{(e,r,r)\},
\]

\[
\operatorname{Comp}^{\mathfrak M_0}=\{(e,e,e)\}.
\]

Then:

\[
\mathfrak M_0
\models
\text{AX-C01},
\text{AX-C02},
\text{AX-C04},
\text{AX-C05},
\text{AX-C06},
\text{AX-C07}.
\]

Therefore the mandatory theory is satisfiable relative to classical many-sorted first-order semantics.

## 8.2 What this result proves

The existence of \(\mathfrak M_0\) proves that the six mandatory axioms are jointly satisfiable.

## 8.3 What this result does not prove

It does not prove:

- empirical correctness;
- nontrivial applicability;
- categoricity;
- completeness;
- decidability;
- uniqueness of the axiomatization;
- conservativity of future modules;
- usefulness for FCO or any implementation.

---

# 9. Independence of the Mandatory Axioms

For each mandatory axiom group, a finite structure is supplied that falsifies that axiom while satisfying the other five.

These models establish mutual independence at the level of the stated axiom groups.

## 9.1 Countermodel for AX-C01

Let:

\[
R=\{0,1\},
\qquad
T=\{e\},
\]

\[
\equiv_{\mathsf S}=\varnothing,
\]

\[
\operatorname{Apply}
=
\{(e,0,0),(e,1,1)\},
\]

\[
\operatorname{Comp}
=
\{(e,e,e)\}.
\]

AX-C01 fails because structural equivalence is not reflexive. The other mandatory axioms hold.

## 9.2 Countermodel for AX-C02

Let:

\[
R=\{0,1\},
\qquad
T=\{e\},
\]

\[
\equiv_{\mathsf S}
=
\{(0,0),(1,1)\},
\]

\[
\operatorname{Apply}
=
\{(e,0,0),(e,0,1),(e,1,1)\},
\]

\[
\operatorname{Comp}
=
\{(e,e,e)\}.
\]

AX-C02 fails because \(e\) maps \(0\) to both \(0\) and \(1\). The other mandatory axiom groups hold.

## 9.3 Countermodel for AX-C04

Let:

\[
R=\{0,1\},
\qquad
T=\{e,f\},
\]

with structural equivalence interpreted as equality.

Let:

\[
\operatorname{Apply}
=
\{
(e,0,0),
(e,1,1),
(f,0,1),
(f,1,1)
\},
\]

and:

\[
\operatorname{Comp}
=
\{
(e,e,e),
(e,f,f),
(f,e,f),
(f,f,e)
\}.
\]

The declaration

\[
\operatorname{Comp}(f,f,e)
\]

does not match the relational composite of \(f\) with itself. Thus AX-C04 fails, while the other mandatory axiom groups hold.

## 9.4 Countermodel for AX-C05

Let:

\[
R=\{0\},
\qquad
T=\{e\},
\]

with structural equivalence interpreted as equality,

\[
\operatorname{Apply}=\varnothing,
\]

\[
\operatorname{Comp}=\{(e,e,e)\}.
\]

AX-C05 fails. The remaining mandatory axiom groups hold.

## 9.5 Countermodel for AX-C06

Let:

\[
R=\{0\},
\qquad
T=\{e\},
\]

\[
\equiv_{\mathsf S}=\{(0,0)\},
\]

\[
\operatorname{Apply}=\{(e,0,0)\},
\]

\[
\operatorname{Comp}=\varnothing.
\]

AX-C06 fails because neither unit composition is declared. The remaining mandatory axiom groups hold.

## 9.6 Countermodel for AX-C07

Let:

\[
R=\{0,1\},
\]

\[
T=\{e,a,b,c,p,q,r,s\},
\]

where all eight transformations are pairwise distinct.

Interpret every transformation with the identity application graph:

\[
\operatorname{Apply}(t,0,0),
\qquad
\operatorname{Apply}(t,1,1)
\]

for every \(t\in T\).

Include all required left and right unit compositions. Also include:

\[
\operatorname{Comp}(a,b,p),
\]

\[
\operatorname{Comp}(p,c,r),
\]

\[
\operatorname{Comp}(b,c,q),
\]

\[
\operatorname{Comp}(a,q,s).
\]

Since all transformations have the identity graph, AX-C04 holds for these declarations. However, the antecedent of AX-C07 holds with:

\[
f=a,\quad g=b,\quad h=c,\quad
u=p,\quad v=r,\quad w=q,\quad z=s,
\]

while:

\[
r\neq s.
\]

Therefore AX-C07 fails and the other mandatory axiom groups hold.

## 9.7 Independence conclusion

For each mandatory axiom group \(A_i\), there exists a finite model of the other five axiom groups in which \(A_i\) is false.

Hence:

\[
\boxed{
\text{AX-C01, AX-C02, AX-C04, AX-C05, AX-C06, AX-C07 are mutually independent}
}
\]

relative to the presented countermodels and classical many-sorted first-order semantics.

---

# 10. Non-Derivability of AX-C08

Consider:

\[
R=\{0,1,2\},
\qquad
T=\{e,a\}.
\]

Let:

\[
\equiv_{\mathsf S}
=
\{
(0,0),(0,1),(1,0),(1,1),(2,2)
\}.
\]

Let:

\[
\operatorname{Apply}
=
\{
(e,0,0),
(e,1,1),
(e,2,2),
(a,0,0),
(a,1,2)
\}.
\]

Let:

\[
\operatorname{Comp}
=
\{
(e,e,e),
(e,a,a),
(a,e,a)
\}.
\]

The six mandatory axiom groups hold.

However:

\[
0\equiv_{\mathsf S}1,
\]

\[
\operatorname{Apply}(a,0,0),
\]

\[
\operatorname{Apply}(a,1,2),
\]

but:

\[
0\not\equiv_{\mathsf S}2.
\]

Therefore:

\[
\neg\operatorname{Structural}(a).
\]

Hence:

\[
\boxed{
\text{TSI-CORE-1.0-RC2}
\nvdash
\text{AX-C08}
}
\]

AX-C08 must remain optional.

---

# 11. Metatheoretic Status Ledger

## 11.1 Established in the present specification

1. The language is many-sorted and type-correct.
2. The two primitive sorts are non-empty.
3. Application is partial-functional under AX-C02.
4. Declared composition has the correct application graph under AX-C04.
5. The unit acts identically under AX-C05.
6. Unit compositions are declared under AX-C06.
7. Existing associative branches agree intensionally under AX-C07.
8. Declared composition is functional by TH-C00.
9. The unit value is unique by TH-C01.
10. Existing associative branches are extensionally equivalent from AX-C04 alone.
11. The mandatory kernel has a finite model.
12. Each mandatory axiom group has a finite independence countermodel.
13. AX-C08 is not derivable from the mandatory kernel.
14. Full extensionality is not assumed.
15. Total application and total composition are not assumed.

## 11.2 Not established

The following are not claimed:

- categoricity;
- syntactic completeness;
- semantic completeness of any extension;
- decidability;
- finite-model property in general;
- model completeness;
- quantifier elimination;
- elimination of imaginaries;
- uniqueness up to definitional equivalence;
- conservativity of any future module;
- interpretability in a particular established theory;
- empirical usefulness;
- computational efficiency;
- physical realizability;
- necessity for FCO;
- novelty of every mathematical ingredient;
- proof-assistant verification.

## 11.3 Open formal questions

1. Are \(\text{AX-C06}_{L}\) and \(\text{AX-C06}_{R}\) independent of one another relative to the remaining axioms?
2. Is there a smaller definitionally equivalent presentation preserving the intended intensional distinction?
3. Can the theory be faithfully interpreted in a standard theory of partial maps or restriction categories?
4. Which useful extension classes are conservative?
5. Which extension classes force extensionality?
6. Which extensions require domain closure under structural equivalence?
7. Is the primitive relation \(\equiv_{\mathsf S}\) genuinely useful across multiple modules, or should it eventually move to TSI-STRUCT?
8. Does the separation between partial application and partial declared composition produce practical formal advantages?
9. Can all finite countermodels be independently reproduced in Lean and Isabelle?
10. Do nontrivial applied models exist without ad hoc encodings?

---

# 12. Conservative Extension Contract

Let \(K\) denote TSI-CORE and \(E\) a proposed extension.

## 12.1 Symbol preservation

An extension may use:

\[
\mathsf{Rep},
\quad
\mathsf{Trans},
\quad
\equiv_{\mathsf S},
\quad
\operatorname{Apply},
\quad
\operatorname{Comp},
\quad
e.
\]

It must not redefine their kernel meanings.

## 12.2 Model-reduct requirement

Every model of \(E\), reduced to the kernel signature, must satisfy all six mandatory kernel axiom groups.

Formally:

\[
\mathfrak M\models E
\quad\Rightarrow\quad
\mathfrak M\!\upharpoonright_{L_K}\models K.
\]

## 12.3 Explicit strengthening requirement

An extension must state explicitly if it assumes any of the following:

- AX-C08;
- total application;
- total composition;
- extensionality;
- domain closure;
- existence of an empty transformation;
- inverses;
- cancellation;
- commutativity;
- idempotence;
- temporal structure;
- probability;
- measure;
- topology;
- metric structure;
- geometry;
- information;
- observation;
- computation;
- physical semantics.

## 12.4 Proof obligation for conservativity

An extension \(E\) is conservative over \(K\) only if:

\[
\forall\varphi\in\operatorname{Sent}(L_K),
\qquad
E\vdash\varphi
\Rightarrow
K\vdash\varphi.
\]

Conservativity is not inherited automatically from modular organization. It must be proved for each extension.

## 12.5 Non-conservative modules

A useful module may be non-conservative. Such a module is not forbidden, but it must be labeled accurately.

Recommended labels:

- `DEFINITIONAL_EXTENSION`;
- `CONSERVATIVE_EXTENSION`;
- `NONCONSERVATIVE_EXTENSION`;
- `INTERPRETATION_MODULE`;
- `EMPIRICAL_MODULE`;
- `EXPERIMENTAL_MODULE`.

## 12.6 No retroactive kernel modification

A module must not silently insert its assumptions into TSI-CORE.

If repeated modules independently require the same missing principle, this is evidence for reviewing the kernel, not permission to rewrite the kernel under the same version number.

---

# 13. Kernel Failure and Revision Policy

The kernel is a research instrument, not an object to be defended regardless of evidence.

## 13.1 Formal failure conditions

A new kernel version is required if:

1. a contradiction is derived from the mandatory axioms;
2. a stated theorem is shown not to follow from its declared assumptions;
3. an independence countermodel is invalid;
4. a mandatory formula is ill-typed;
5. a primitive symbol has incompatible uses;
6. a hidden assumption is found in a proof;
7. the intended composition order is ambiguous;
8. machine verification exposes a mismatch between prose and formulas.

## 13.2 Architectural inadequacy conditions

Kernel review is required if several serious extensions show that:

1. a necessary concept cannot be expressed without artificial reification;
2. `Apply` has the wrong argument structure;
3. `Comp` is too weak or too strong for actual modules;
4. the distinguished unit cannot be shared meaningfully;
5. intensional distinction between transformations has no use;
6. structural equivalence is consistently module-specific rather than kernel-level;
7. every useful module must add the same strengthening;
8. conservative extension repeatedly fails for the same structural reason;
9. direct module formalization is simpler than formalization through TSI-CORE;
10. the kernel adds notation without adding explanatory, deductive, or verification value.

## 13.3 Empirical inadequacy conditions

The kernel itself has no empirical content. Nevertheless, its research role may be judged unsuccessful if:

1. it does not support any nontrivial executable or mathematical module;
2. it does not improve error detection;
3. it does not improve modularity;
4. it does not reduce hidden assumptions;
5. it does not support reusable proofs;
6. it repeatedly obstructs applied formalization.

## 13.4 Permitted outcomes

The research program must permit all of the following outcomes:

- retain TSI-CORE-1.0 unchanged;
- publish TSI-CORE-1.1 with clarified metatheory;
- publish TSI-CORE-2.0 with formula changes;
- move structural equivalence out of the kernel;
- replace the kernel with an established formalism;
- retain only selected modules;
- abandon the kernel entirely.

Abandonment is a valid scientific outcome when the formalism adds no value.

---

# 14. First Extension Test

The recommended first test is:

\[
\boxed{\mathrm{TSI\text{-}STRUCT\text{-}0.1}}
\]

Its purpose is not to enlarge the kernel automatically. Its purpose is to test whether the primitive structural-equivalence relation is useful.

The module should answer:

1. What structures do representations carry?
2. Is \(\equiv_{\mathsf S}\) equality, isomorphism, bisimulation, observational equivalence, or a parameter?
3. Which transformations preserve it?
4. Is AX-C08 appropriate globally or only for a subclass of transformations?
5. Is domain closure required?
6. Can nontrivial models be constructed?
7. Does the module remain conservative?
8. Does the primitive relation simplify proofs compared with defining equivalence inside the module?
9. Are counterexamples easy to formulate?
10. Does the module reveal that \(\equiv_{\mathsf S}\) should not be primitive in the core?

Only after this test should time, dynamics, memory, information, or FCO-specific mathematics be added.

---

# 15. Versioning Policy

## 15.1 Version 1.0-RC2

This release preserves:

- two sorts;
- three primitive relations;
- one constant;
- six mandatory axiom groups;
- the historical gap at AX-C03;
- TH-C00, TH-C01, and TH-C02;
- the finite satisfiability model;
- the six independence countermodels;
- non-derivability of AX-C08.

## 15.2 Formula-preserving corrections

The following may be corrected without changing the mathematical version:

- typographical errors;
- formatting;
- broken references;
- wording that does not alter a formula;
- repository metadata;
- bibliographic metadata.

Such changes should be recorded as document revisions.

## 15.3 Formula-changing revisions

Any change to:

- a primitive symbol;
- a sort;
- an axiom;
- a theorem statement;
- a model specification;
- a proof dependency;

requires a new mathematical version.

## 15.4 Machine-verified release

A machine-verified release should be labeled separately, for example:

\[
\mathrm{TSI\text{-}CORE\text{-}1.0\text{-}MV}.
\]

It must not be declared until all required source files compile and all formal claims are reproduced.

---

# 16. Machine Verification Roadmap

## 16.1 Primary proof assistant

Recommended:

- Lean 4.

## 16.2 Independent cross-check

Recommended:

- Isabelle/HOL.

## 16.3 Repository structure

```text
TSI-CORE/
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── docs/
│   ├── TSI-CORE-1.0-RC2.md
│   └── TSI-CORE-1.0-RC2.pdf
├── lean/
│   └── TSI/
│       └── Core/
│           ├── Signature.lean
│           ├── Axioms.lean
│           ├── Definitions.lean
│           ├── Theorems.lean
│           ├── Independence.lean
│           └── Models/
│               ├── Satisfiable.lean
│               ├── NotC01.lean
│               ├── NotC02.lean
│               ├── NotC04.lean
│               ├── NotC05.lean
│               ├── NotC06.lean
│               ├── NotC07.lean
│               └── NotC08.lean
├── isabelle/
│   └── TSI_Core.thy
└── tests/
    └── finite_model_checks/
```

## 16.4 Verification milestones

### MV-0 — Text freeze

- freeze formulas;
- assign identifiers;
- check notation;
- check all cross-references.

### MV-1 — Signature and axioms

- encode both sorts;
- encode primitive symbols;
- encode the six axiom groups.

### MV-2 — Theorems

- prove TH-C00;
- prove TH-C01;
- prove TH-C02;
- record minimal dependencies.

### MV-3 — Satisfiability

- encode \(\mathfrak M_0\);
- prove every mandatory axiom.

### MV-4 — Independence

- encode all six independence countermodels;
- prove the intended axiom fails;
- prove the other five hold.

### MV-5 — Optional axiom status

- encode the AX-C08 countermodel;
- prove the mandatory kernel;
- prove failure of structural preservation.

### MV-6 — Independent replication

- reproduce the formal claims in Isabelle/HOL;
- compare theorem statements;
- record toolchain versions and hashes.

---

# 17. Publication Package

## 17.1 Minimum GitHub package

A public repository should contain:

1. canonical Markdown specification;
2. README;
3. license;
4. citation metadata;
5. changelog;
6. audit history;
7. finite-model data or scripts;
8. proof-assistant directory, even if initially marked incomplete.

## 17.2 Minimum Zenodo package

The first Zenodo release should contain:

1. `TSI-CORE-1.0-RC2.md`;
2. rendered PDF;
3. `README.md`;
4. `LICENSE`;
5. `CITATION.cff`;
6. audit report;
7. machine-readable model appendix;
8. repository release archive.

## 17.3 Recommended publication status wording

Use:

> TSI-CORE-1.0-RC2 is a publication candidate for a minimal many-sorted first-order kernel. The specification is finitely satisfiable and accompanied by explicit finite independence countermodels. Proof-assistant verification and empirical validation of extension modules remain future work.

Do not use:

> proven universal theory;

> theory of reality;

> complete foundation of cognition;

> experimentally confirmed;

> machine-verified;

unless those claims later become true and are documented.

## 17.4 Suggested keywords

- many-sorted first-order logic;
- partial transformations;
- partial composition;
- structural equivalence;
- formal specification;
- finite model;
- axiom independence;
- conservative extension;
- modular formal theory;
- mathematical foundations.

---

# 18. Release Checklist

## Formal specification

- [x] Sorts declared.
- [x] Primitive symbols typed.
- [x] Composition order fixed.
- [x] Derived definitions separated from axioms.
- [x] Six mandatory axiom groups stated.
- [x] Optional AX-C08 separated.
- [x] Non-assumptions listed.
- [x] Principal derived theorems stated.
- [x] Finite satisfiability model stated.
- [x] Six independence countermodels stated.
- [x] AX-C08 countermodel stated.
- [x] Conservative-extension contract stated.
- [x] Failure and revision policy stated.

## Independent audit

- [ ] Recheck every countermodel.
- [ ] Recheck TH-C00 substitution.
- [ ] Recheck TH-C02 proof in full first-order detail.
- [ ] Review terminology against established partial-map theories.
- [ ] Check whether “structural equivalence” should remain primitive.
- [ ] Check novelty claims.
- [ ] Check bibliography and related work.

## Machine verification

- [ ] Lean project compiles.
- [ ] All six axiom groups encoded.
- [ ] TH-C00 proved.
- [ ] TH-C01 proved.
- [ ] TH-C02 proved.
- [ ] \(\mathfrak M_0\) verified.
- [ ] Six independence models verified.
- [ ] AX-C08 non-derivability witness verified.
- [ ] Isabelle cross-check completed.
- [ ] Toolchain versions recorded.
- [ ] Source hashes recorded.

## Publication

- [ ] License selected.
- [ ] ORCID added if applicable.
- [ ] GitHub repository created.
- [ ] CITATION.cff validated.
- [ ] PDF rendered and checked.
- [ ] Zenodo metadata prepared.
- [ ] GitHub release archived by Zenodo.
- [ ] DOI inserted into README after minting.

---

# 19. Canonical Summary

TSI-CORE-1.0-RC2 consists of:

\[
\boxed{
\begin{aligned}
&\text{Sorts: } \mathsf{Rep},\mathsf{Trans};\\
&\text{Relations: } \equiv_{\mathsf S},\operatorname{Apply},\operatorname{Comp};\\
&\text{Constant: } e;\\
&\text{Mandatory axioms: AX-C01, AX-C02, AX-C04, AX-C05, AX-C06, AX-C07.}
\end{aligned}
}
\]

The kernel supports partial application, partial declared composition, a unit transformation, and conditional intensional associativity. It does not assume totality, extensionality, structural preservation, time, dynamics, memory, probability, information, geometry, observation, computation, or physics.

Its current justified claims are limited to its formal specification, finite satisfiability, the supplied finite independence witnesses, and the stated derived results. Its scientific value remains conditional on successful, non-artificial extension modules.

---

# 20. Final Status Statement

\[
\boxed{
\text{TSI-CORE-1.0-RC2 is ready for final independent audit before public release.}
}
\]

It is not yet labeled `FINAL`, `MACHINE_VERIFIED`, or `EMPIRICALLY_VALIDATED`.

The next action is not to expand this document into a monograph. The next action is:

\[
\boxed{
\text{independent audit}
\rightarrow
\text{GitHub release candidate}
\rightarrow
\text{Zenodo archival release}
\rightarrow
\text{TSI-STRUCT-0.1 test module}
}
\]

---

**End of TSI-CORE-1.0-RC2.**
