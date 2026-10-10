# TSI-CORE-1.0
## Formally Audited Mathematical Core

**Version:** 1.0  
**Status:** Formally Audited Release  
**Logical basis:** Classical many-sorted first-order logic with equality  
**Release policy:** Frozen project baseline; alterations require a new version identifier and a formal justification

---

# Certification and Audit Status

This edition incorporates the results of multiple independent formal audit reports conducted across precursor versions TSI-CORE-0.1, TSI-CORE-0.1R, TSI-CORE-0.1R-a, and TSI-CORE-0.1R-b.

The following results are incorporated into this release:

1. All primitive sorts, variables, signature symbols, definitions, and axioms have been reviewed for typing correctness.
2. The mandatory axioms have been checked for joint satisfiability.
3. The previous AX-C03, functionality of composition, has been proved derivable from AX-C06 and AX-C07 and is therefore retained only as theorem TH-C00.
4. Each of the six remaining mandatory axioms has an explicit finite countermodel showing independence from the other five.
5. A finite satisfiability model has been provided.
6. The independence of AX-C07 and the non-derivability of optional AX-C08 have been witnessed by explicit finite models.
7. Editorial incompleteness identified in earlier countermodel descriptions has been removed by explicitly interpreting every primitive symbol in every model.

This status does not assert the absolute truth, categorical uniqueness, empirical validity, or machine-verified correctness of the theory. It records that the present edition incorporates the conclusions of the completed formal audits and contains explicit proofs and finite model witnesses for its stated core claims.

---

# 1. Abstract

TSI-CORE-1.0 is a minimal typed axiomatic kernel for representations and partial transformations.

The kernel contains:

- two primitive sorts;
- four primitive signature symbols;
- six mandatory axioms;
- a derived functionality theorem for composition;
- explicit statements of principles not included in the kernel;
- a satisfiability model;
- finite countermodels establishing independence of every mandatory axiom;
- a policy governing future extensions.

The kernel does not commit to time, dynamics, memory, probability, information, geometry, objecthood, observation, computation, physics, or empirical interpretation. Such notions may be introduced only by separate modules whose reducts satisfy the present kernel.

Minimality is claimed only relative to the present signature and the stated target properties.

---

# 2. Scope

TSI-CORE-1.0 formalizes only:

1. representations;
2. transformations;
3. partial application of transformations to representations;
4. partial declared composition of transformations;
5. structural equivalence between representations;
6. a distinguished unit transformation.

The kernel does not specify the internal nature of representations or transformations.

---

# 3. Logical Foundation

The underlying logic is classical many-sorted first-order logic with equality.

Logical symbols include:

\[
\neg,\quad
\land,\quad
\lor,\quad
\rightarrow,\quad
\leftrightarrow,\quad
\forall,\quad
\exists,\quad
=.
\]

Equality is standard logical equality within each sort.

Every primitive sort is non-empty.

---

# 4. Primitive Sorts

## SORT-C01. Representations

\[
\mathsf{Rep}.
\]

Variables:

\[
X,Y,Z,X',Y',Z',\ldots:\mathsf{Rep}.
\]

## SORT-C02. Transformations

\[
\mathsf{Trans}.
\]

Variables:

\[
f,g,h,k,p,q,r,s,u,v,w,z,h_1,h_2,\ldots:\mathsf{Trans}.
\]

---

# 5. Primitive Signature

## SIG-C01. Structural equivalence

\[
\equiv_{\mathsf S}\ \subseteq\
\mathsf{Rep}\times\mathsf{Rep}.
\]

Notation:

\[
X\equiv_{\mathsf S}Y.
\]

## SIG-C02. Application

\[
\operatorname{Apply}\ \subseteq\
\mathsf{Trans}\times\mathsf{Rep}\times\mathsf{Rep}.
\]

Notation:

\[
\operatorname{Apply}(f,X,Y).
\]

This states that transformation \(f\) is defined at \(X\) and produces \(Y\).

## SIG-C03. Declared composition

\[
\operatorname{Comp}\ \subseteq\
\mathsf{Trans}\times\mathsf{Trans}\times\mathsf{Trans}.
\]

Notation:

\[
\operatorname{Comp}(f,g,h).
\]

Convention:

\[
\operatorname{Comp}(f,g,h)
\]

means that \(h\) is the declared composite \(f\circ g\), with \(g\) applied first and \(f\) second.

This notation does not assert that a composite exists for every pair.

## SIG-C04. Unit transformation

\[
e:\mathsf{Trans}.
\]

The kernel fixes no additional internal structure on elements of either sort.

---

# 6. Derived Definitions

All expressions in this section are abbreviations. They introduce no new axioms.

## DEF-C01. Definedness

\[
\operatorname{DefinedAt}(f,X)
\iff
\exists Y\,
\operatorname{Apply}(f,X,Y).
\]

## DEF-C02. Reachability

\[
\operatorname{Reaches}(f,Y)
\iff
\exists X\,
\operatorname{Apply}(f,X,Y).
\]

## DEF-C03. Domain

\[
\operatorname{Dom}(f)
:=
\{X\in\mathsf{Rep}:
\operatorname{DefinedAt}(f,X)\}.
\]

\(\operatorname{Dom}(f)\) is a metatheoretic abbreviation, not a new object-language term.

## DEF-C04. Range

\[
\operatorname{Ran}(f)
:=
\{Y\in\mathsf{Rep}:
\operatorname{Reaches}(f,Y)\}.
\]

\(\operatorname{Ran}(f)\) is a metatheoretic abbreviation.

## DEF-C05. Totality

\[
\operatorname{Total}(f)
\iff
\forall X\,
\operatorname{DefinedAt}(f,X).
\]

## DEF-C06. Empty action

\[
\operatorname{EmptyAction}(f)
\iff
\forall X\,\forall Y\,
\neg\operatorname{Apply}(f,X,Y).
\]

The existence of an empty-action transformation is not asserted.

## DEF-C07. Extensional equivalence

\[
f\approx_{\mathrm{ext}}g
\iff
\forall X\,\forall Y
\left(
\operatorname{Apply}(f,X,Y)
\leftrightarrow
\operatorname{Apply}(g,X,Y)
\right).
\]

The implication

\[
f\approx_{\mathrm{ext}}g\rightarrow f=g
\]

is not part of the mandatory kernel.

## DEF-C08. Structurality

\[
\operatorname{Structural}(f)
\iff
\forall X\,\forall X'\,\forall Y\,\forall Y'
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

---

# 7. Mandatory Axioms

The mandatory kernel contains exactly six axiom identifiers:

\[
\mathrm{AX\mbox{-}C01},
\mathrm{AX\mbox{-}C02},
\mathrm{AX\mbox{-}C04},
\mathrm{AX\mbox{-}C05},
\mathrm{AX\mbox{-}C06},
\mathrm{AX\mbox{-}C07}.
\]

The identifier AX-C03 is intentionally retired for version-history compatibility. Its former formula is theorem TH-C00.

## AX-C01. Structural equivalence

### Reflexivity

\[
\forall X\;
X\equiv_{\mathsf S}X.
\]

### Symmetry

\[
\forall X\,\forall Y
\left(
X\equiv_{\mathsf S}Y
\rightarrow
Y\equiv_{\mathsf S}X
\right).
\]

### Transitivity

\[
\forall X\,\forall Y\,\forall Z
\left(
X\equiv_{\mathsf S}Y
\land
Y\equiv_{\mathsf S}Z
\rightarrow
X\equiv_{\mathsf S}Z
\right).
\]

## AX-C02. Functionality of application

\[
\forall f\,\forall X\,\forall Y\,\forall Z
\Big[
\operatorname{Apply}(f,X,Y)
\land
\operatorname{Apply}(f,X,Z)
\rightarrow
Y=Z
\Big].
\]

Thus every transformation acts as a partial function on representations.

## AX-C04. Correctness of declared composition

\[
\forall f\,\forall g\,\forall h
\Bigg[
\operatorname{Comp}(f,g,h)
\rightarrow
\forall X\,\forall Z
\Bigg(
\operatorname{Apply}(h,X,Z)
\leftrightarrow
\exists Y
\big[
\operatorname{Apply}(g,X,Y)
\land
\operatorname{Apply}(f,Y,Z)
\big]
\Bigg)
\Bigg].
\]

Only the implication from a declared composition fact to graph correctness is assumed.

The converse is not assumed.

## AX-C05. Action of the unit

\[
\forall X\;
\operatorname{Apply}(e,X,X).
\]

## AX-C06. Unit compositions

\[
\forall f
\Big[
\operatorname{Comp}(e,f,f)
\land
\operatorname{Comp}(f,e,f)
\Big].
\]

## AX-C07. Conditional intensional associativity

\[
\forall f\,\forall g\,\forall h\,
\forall u\,\forall v\,\forall w\,\forall z
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

AX-C07 states equality of the two existing composite results. It does not assert existence of either branch.

---

# 8. Principles Not Included in the Mandatory Kernel

The formulas below are not included among the mandatory axioms. No proof may use them unless they are separately introduced and justified in an extension module.

## NC-C01. Total application

Not assumed:

\[
\forall f\,\forall X\,\exists Y\,
\operatorname{Apply}(f,X,Y).
\]

## NC-C02. Total composition

Not assumed:

\[
\forall f\,\forall g\,\exists h\,
\operatorname{Comp}(f,g,h).
\]

## NC-C03. Extensional identity

Not assumed:

\[
\forall f\,\forall g
\left(
f\approx_{\mathrm{ext}}g
\rightarrow
f=g
\right).
\]

## NC-C04. Universal structurality

Not assumed:

\[
\forall f\,
\operatorname{Structural}(f).
\]

## NC-C05. Domain closure under structural equivalence

Not assumed:

\[
\forall f\,\forall X\,\forall X'
\Big[
X\equiv_{\mathsf S}X'
\land
\operatorname{DefinedAt}(f,X)
\rightarrow
\operatorname{DefinedAt}(f,X')
\Big].
\]

## NC-C06. Mandatory empty transformation

Not assumed:

\[
\exists f\,
\operatorname{EmptyAction}(f).
\]

## NC-C07. Empty result convention

Failure of

\[
\exists h\,\operatorname{Comp}(f,g,h)
\]

does not introduce or denote a distinguished empty transformation.

## NC-C08. Internal structure of representations

The kernel introduces no primitive elements, relations, arities, subobjects, homomorphisms, isomorphisms, coordinates, metrics, topologies, or probability measures internal to \(\mathsf{Rep}\).

---

# 9. Derived Theorems

## TH-C00. Functionality of composition

\[
\forall f\,\forall g\,\forall h_1\,\forall h_2
\Big[
\operatorname{Comp}(f,g,h_1)
\land
\operatorname{Comp}(f,g,h_2)
\rightarrow
h_1=h_2
\Big].
\]

### Proof

Assume:

\[
\operatorname{Comp}(f,g,h_1)
\]

and:

\[
\operatorname{Comp}(f,g,h_2).
\]

By AX-C06:

\[
\operatorname{Comp}(h_1,e,h_1)
\]

and:

\[
\operatorname{Comp}(g,e,g).
\]

Instantiate AX-C07 using:

\[
h:=e,\qquad
u:=h_1,\qquad
v:=h_1,\qquad
w:=g,\qquad
z:=h_2.
\]

The four antecedent conjuncts become:

\[
\operatorname{Comp}(f,g,h_1),
\]

\[
\operatorname{Comp}(h_1,e,h_1),
\]

\[
\operatorname{Comp}(g,e,g),
\]

\[
\operatorname{Comp}(f,g,h_2).
\]

All are true. Therefore AX-C07 gives:

\[
h_1=h_2.
\]

\[
\Box
\]

Hence:

\[
\mathrm{AX\mbox{-}C06}
\land
\mathrm{AX\mbox{-}C07}
\vdash
\mathrm{TH\mbox{-}C00}.
\]

## TH-C01. Uniqueness of the unit value

\[
\forall X\,\forall Y
\left(
\operatorname{Apply}(e,X,Y)
\rightarrow
Y=X
\right).
\]

### Proof

By AX-C05:

\[
\operatorname{Apply}(e,X,X).
\]

If also:

\[
\operatorname{Apply}(e,X,Y),
\]

then AX-C02 yields:

\[
Y=X.
\]

\[
\Box
\]

## TH-C02. Extensional associativity of existing branches

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

### Proof sketch

By repeated use of AX-C04, both \(v\) and \(z\) have the graph of the same three-stage partial action:

\[
X
\xmapsto{h}
Y_1
\xmapsto{g}
Y_2
\xmapsto{f}
Y_3.
\]

Therefore:

\[
v\approx_{\mathrm{ext}}z.
\]

AX-C07 strengthens this to:

\[
v=z.
\]

---

# 10. Satisfiability Model

Define:

\[
\mathfrak M_0.
\]

## 10.1 Carriers

\[
\mathsf{Rep}^{\mathfrak M_0}=\{r\},
\]

\[
\mathsf{Trans}^{\mathfrak M_0}=\{e\}.
\]

## 10.2 Structural equivalence

\[
\equiv_{\mathsf S}^{\mathfrak M_0}
=
\{(r,r)\}.
\]

## 10.3 Application

\[
\operatorname{Apply}^{\mathfrak M_0}
=
\{(e,r,r)\}.
\]

## 10.4 Composition

\[
\operatorname{Comp}^{\mathfrak M_0}
=
\{(e,e,e)\}.
\]

## 10.5 Result

\[
\mathfrak M_0
\models
\mathrm{AX\mbox{-}C01}
\land
\mathrm{AX\mbox{-}C02}
\land
\mathrm{AX\mbox{-}C04}
\land
\mathrm{AX\mbox{-}C05}
\land
\mathrm{AX\mbox{-}C06}
\land
\mathrm{AX\mbox{-}C07}.
\]

Thus the mandatory kernel is satisfiable.

---

# 11. Countermodel for AX-C07

Define:

\[
\mathfrak M_{\neg C07}.
\]

## 11.1 Carriers

\[
\mathsf{Rep}=\{0,1\},
\]

\[
\mathsf{Trans}=\{e,a,b,c,p,q,r,s\},
\]

where all eight transformation elements are pairwise distinct. In particular:

\[
r\neq s.
\]

## 11.2 Structural equivalence

\[
X\equiv_{\mathsf S}Y
\iff
X=Y.
\]

## 11.3 Application

For every \(t\in\mathsf{Trans}\), the only application facts are:

\[
\operatorname{Apply}(t,0,0),
\qquad
\operatorname{Apply}(t,1,1).
\]

Thus every transformation has the identity graph.

## 11.4 Composition

For every \(t\in\mathsf{Trans}\), include:

\[
\operatorname{Comp}(e,t,t),
\qquad
\operatorname{Comp}(t,e,t).
\]

Additionally include:

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

No other composition facts hold.

## 11.5 Verification

AX-C01 holds because \(\equiv_{\mathsf S}\) is equality.

AX-C02 holds because each transformation has a functional identity graph.

AX-C04 holds because every declared composite has the identity graph, equal to the relational composite of two identity graphs.

AX-C05 holds because \(e\) acts identically.

AX-C06 holds by construction.

AX-C07 fails for:

\[
f=a,\quad g=b,\quad h=c,
\]

\[
u=p,\quad v=r,\quad w=q,\quad z=s.
\]

All four antecedent facts hold, but:

\[
r\neq s.
\]

Therefore:

\[
\mathrm{AX\mbox{-}C01},
\mathrm{AX\mbox{-}C02},
\mathrm{AX\mbox{-}C04},
\mathrm{AX\mbox{-}C05},
\mathrm{AX\mbox{-}C06}
\nvdash
\mathrm{AX\mbox{-}C07}.
\]

A finite exhaustive analysis may be organized over all \(8^3\) triples \((f,g,h)\). The audit record reports 35 triples admitting both complete branches and one violating triple:

\[
(f,g,h)=(a,b,c),
\]

with:

\[
(u,v,w,z)=(p,r,q,s).
\]

The formal independence claim itself depends only on the explicit witness above.

---

# 12. Optional Structurality and Its Countermodel

## AX-C08. Universal structurality

The following axiom is optional and not part of TSI-CORE-1.0:

\[
\forall f\,
\operatorname{Structural}(f).
\]

Define:

\[
\mathfrak M_{\neg C08}.
\]

## 12.1 Carriers

\[
\mathsf{Rep}=\{0,1,2\},
\]

\[
\mathsf{Trans}=\{e,a\}.
\]

## 12.2 Structural equivalence

\(\equiv_{\mathsf S}\) has exactly two equivalence classes:

\[
\{0,1\},
\qquad
\{2\}.
\]

Equivalently:

\[
\equiv_{\mathsf S}
=
\{(0,0),(0,1),(1,0),(1,1),(2,2)\}.
\]

## 12.3 Application

The application relation is exactly:

\[
\operatorname{Apply}(e,0,0),
\]

\[
\operatorname{Apply}(e,1,1),
\]

\[
\operatorname{Apply}(e,2,2),
\]

\[
\operatorname{Apply}(a,0,0),
\]

\[
\operatorname{Apply}(a,1,2).
\]

No other application facts hold.

## 12.4 Composition

The composition relation is exactly:

\[
\operatorname{Comp}(e,e,e),
\]

\[
\operatorname{Comp}(e,a,a),
\]

\[
\operatorname{Comp}(a,e,a).
\]

No other composition facts hold.

## 12.5 Verification

All six mandatory axioms hold.

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
\mathrm{TSI\mbox{-}CORE\mbox{-}1.0}
\nvdash
\mathrm{AX\mbox{-}C08}.
\]

---

# 13. Independence of the Mandatory Axioms

Each mandatory axiom is independent of the other five.

TH-C00 is not treated as an additional premise in the independence tests. Whenever AX-C06 and AX-C07 both hold, TH-C00 follows automatically.

## 13.1 Countermodel for AX-C01

Define \(\mathfrak M_{\neg C01}\).

\[
\mathsf{Rep}=\{0,1\},
\qquad
\mathsf{Trans}=\{e\}.
\]

\[
\equiv_{\mathsf S}:=\varnothing.
\]

\[
\operatorname{Apply}
=
\{(e,0,0),(e,1,1)\}.
\]

\[
\operatorname{Comp}
=
\{(e,e,e)\}.
\]

AX-C01 is false. AX-C02, AX-C04, AX-C05, AX-C06, and AX-C07 are true.

## 13.2 Countermodel for AX-C02

Define \(\mathfrak M_{\neg C02}\).

\[
\mathsf{Rep}=\{0,1\},
\qquad
\mathsf{Trans}=\{e\}.
\]

\[
X\equiv_{\mathsf S}Y\iff X=Y.
\]

\[
\operatorname{Apply}
=
\{(e,0,0),(e,0,1),(e,1,1)\}.
\]

\[
\operatorname{Comp}
=
\{(e,e,e)\}.
\]

AX-C02 is false because \(e\) maps \(0\) to both \(0\) and \(1\). All other mandatory axioms are true.

## 13.3 Countermodel for AX-C04

Define \(\mathfrak M_{\neg C04}\).

\[
\mathsf{Rep}=\{0,1\},
\qquad
\mathsf{Trans}=\{e,f\}.
\]

\[
X\equiv_{\mathsf S}Y\iff X=Y.
\]

\[
\operatorname{Apply}
=
\{(e,0,0),(e,1,1),(f,0,1),(f,1,1)\}.
\]

\[
\operatorname{Comp}
=
\{(e,e,e),(e,f,f),(f,e,f),(f,f,e)\}.
\]

AX-C04 fails for \(\operatorname{Comp}(f,f,e)\). At \(X=0,Z=0\), \(\operatorname{Apply}(e,0,0)\) is true, but there is no \(Y\) such that both \(\operatorname{Apply}(f,0,Y)\) and \(\operatorname{Apply}(f,Y,0)\) hold. All other mandatory axioms are true.

## 13.4 Countermodel for AX-C05

Define \(\mathfrak M_{\neg C05}\).

\[
\mathsf{Rep}=\{0\},
\qquad
\mathsf{Trans}=\{e\}.
\]

\[
0\equiv_{\mathsf S}0.
\]

\[
\operatorname{Apply}:=\varnothing.
\]

\[
\operatorname{Comp}
=
\{(e,e,e)\}.
\]

AX-C05 is false. AX-C01, AX-C02, AX-C04, AX-C06, and AX-C07 are true.

## 13.5 Countermodel for AX-C06

Define \(\mathfrak M_{\neg C06}\).

\[
\mathsf{Rep}=\{0\},
\qquad
\mathsf{Trans}=\{e\}.
\]

\[
0\equiv_{\mathsf S}0.
\]

\[
\operatorname{Apply}
=
\{(e,0,0)\}.
\]

\[
\operatorname{Comp}:=\varnothing.
\]

AX-C06 is false. AX-C01, AX-C02, AX-C04, AX-C05, and AX-C07 are true.

## 13.6 Countermodel for AX-C07

The model \(\mathfrak M_{\neg C07}\) from Section 11 satisfies AX-C01, AX-C02, AX-C04, AX-C05, and AX-C06, but violates AX-C07.

---

# 14. Independence Summary

| Formula | Status | Witness |
|---|---|---|
| AX-C01 | INDEPENDENT | \(\mathfrak M_{\neg C01}\) |
| AX-C02 | INDEPENDENT | \(\mathfrak M_{\neg C02}\) |
| AX-C04 | INDEPENDENT | \(\mathfrak M_{\neg C04}\) |
| AX-C05 | INDEPENDENT | \(\mathfrak M_{\neg C05}\) |
| AX-C06 | INDEPENDENT | \(\mathfrak M_{\neg C06}\) |
| AX-C07 | INDEPENDENT | \(\mathfrak M_{\neg C07}\) |
| Former AX-C03 / TH-C00 | DERIVABLE | AX-C06 and AX-C07 |
| AX-C08 | OPTIONAL / NOT DERIVABLE | \(\mathfrak M_{\neg C08}\) |

The six mandatory axioms are mutually independent relative to the present signature.

No claim is made that this is the unique possible minimal presentation or that no definitionally equivalent basis exists.

---

# 15. Why AX-C04 Is One-Directional

Consider the stronger principle:

\[
\operatorname{Comp}(f,g,h)
\leftrightarrow
\forall X\,\forall Z
\Bigg(
\operatorname{Apply}(h,X,Z)
\leftrightarrow
\exists Y
\big[
\operatorname{Apply}(g,X,Y)
\land
\operatorname{Apply}(f,Y,Z)
\big]
\Bigg).
\]

Call this AX-C04*.

Assume:

\[
g\approx_{\mathrm{ext}}k.
\]

By AX-C06:

\[
\operatorname{Comp}(e,g,g).
\]

Because \(g\) and \(k\) have the same application graph, AX-C04* also yields:

\[
\operatorname{Comp}(e,g,k).
\]

By TH-C00:

\[
g=k.
\]

Therefore:

\[
\mathrm{AX\mbox{-}C04^*}
+
\mathrm{AX\mbox{-}C06}
+
\mathrm{AX\mbox{-}C07}
\vdash
\forall g\,\forall k
\left(
g\approx_{\mathrm{ext}}k
\rightarrow
g=k
\right).
\]

Thus the biconditional form would force extensional identity and eliminate the intended possibility of distinct transformations with the same application graph.

For this reason AX-C04 remains one-directional.

---

# 16. Extension Policy

## MOD-C01. Preservation of primitive sorts

A module may use \(\mathsf{Rep}\) and \(\mathsf{Trans}\), but may not silently change their meaning.

## MOD-C02. Preservation of the primitive signature

A module may not redefine:

\[
\equiv_{\mathsf S},
\qquad
\operatorname{Apply},
\qquad
\operatorname{Comp},
\qquad
e.
\]

## MOD-C03. Reduct condition

Every model of an extension module, when reduced to the kernel signature, must satisfy all six mandatory axioms.

## MOD-C04. Explicit dependencies

Any module requiring one or more of the following must state them as explicit additional axioms:

- universal structurality;
- extensional identity;
- total application;
- total composition;
- a distinguished empty transformation;
- domain closure under structural equivalence;
- inverses;
- cancellation;
- commutativity;
- idempotence;
- probabilistic structure;
- temporal structure;
- metric or topological structure.

## MOD-C05. Conservativity claims

If an extension \(E\) is claimed to be conservative over the kernel \(K\), the required statement is:

\[
\forall\varphi\in\operatorname{Sent}(L_K),
\qquad
E\vdash\varphi
\Rightarrow
K\vdash\varphi.
\]

Such conservativity must be proved separately for each module.

## MOD-C06. Version discipline

Any alteration of primitive sorts, primitive signature, mandatory axioms, theorem TH-C00, or extension policy requires a new version identifier.

## MOD-C07. No silent import

No future proof may use an extension-level principle as though it were a theorem of TSI-CORE-1.0.

---

# 17. Optional Extension Schemes

## EXT-C01. Extensional identity

\[
\forall f\,\forall g
\left(
f\approx_{\mathrm{ext}}g
\rightarrow
f=g
\right).
\]

## EXT-C02. Total composition

\[
\forall f\,\forall g\,\exists h\,
\operatorname{Comp}(f,g,h).
\]

## EXT-C03. Empty transformation

Introduce:

\[
\bot_{\mathsf T}:\mathsf{Trans}
\]

with:

\[
\operatorname{EmptyAction}(\bot_{\mathsf T}).
\]

## EXT-C04. Domain closure

\[
\forall f\,\forall X\,\forall X'
\Big[
X\equiv_{\mathsf S}X'
\land
\operatorname{DefinedAt}(f,X)
\rightarrow
\operatorname{DefinedAt}(f,X')
\Big].
\]

## EXT-C05. Universal structurality

\[
\forall f\,
\operatorname{Structural}(f).
\]

These extensions are not part of the frozen kernel.

---

# 18. Metatheoretic Status

## 18.1 Established in this edition

1. The formal language is many-sorted and type-correct.
2. The mandatory kernel is finitely satisfiable.
3. TH-C00 is derivable from AX-C06 and AX-C07.
4. TH-C01 is derivable from AX-C05 and AX-C02.
5. TH-C02 holds extensionally by AX-C04.
6. AX-C01 is independent.
7. AX-C02 is independent.
8. AX-C04 is independent.
9. AX-C05 is independent.
10. AX-C06 is independent.
11. AX-C07 is independent.
12. AX-C08 is not derivable from the mandatory kernel.
13. A biconditional strengthening of AX-C04 forces extensional identity in the presence of AX-C06 and AX-C07.
14. The mandatory six-axiom basis is minimal relative to the present signature and the stated target properties.

## 18.2 Not established in this edition

The following are not claimed:

- categoricity;
- model completeness;
- quantifier elimination;
- decidability;
- finite-model property;
- completeness of any future applied theory;
- conservativity of future modules;
- equivalence with a category-theoretic, semigroup-theoretic, or restriction-theoretic presentation;
- uniqueness of the present axiom basis;
- physical interpretation;
- empirical validation;
- computational implementation;
- machine-checked proof in Lean, Isabelle, Coq, or another proof assistant.

---

# 19. Open Problems

## OP-C01. Decidability

Determine whether the first-order theory generated by the mandatory kernel is decidable.

## OP-C02. Finite-model behavior

Determine which kernel-language sentences valid in all models are already witnessed or refuted by finite models.

## OP-C03. Alternative minimal bases

Classify definitionally or Morita-equivalent minimal presentations of the same target structure.

## OP-C04. Conservative extensions

For each future module, prove or refute conservativity over TSI-CORE-1.0.

## OP-C05. Extensional quotient

Study the quotient:

\[
\mathsf{Trans}/{\approx_{\mathrm{ext}}}
\]

and determine which additional assumptions are required for composition to descend to the quotient.

## OP-C06. Algebraic comparison

Investigate possible relationships with partial transformation structures, partial monoids, categories with partial composition, restriction categories, and ordered algebras of partial maps.

No equivalence with these structures is claimed here.

## OP-C07. Automated verification

Formalize the kernel, its theorems, and all finite countermodels in at least one proof assistant.

---

# 20. Audit Summary

Independent audit reports conducted on precursor versions identified the following decisive points.

## 20.1 Redundancy of former AX-C03

The former functionality axiom:

\[
\forall f\,\forall g\,\forall h_1\,\forall h_2
\Big[
\operatorname{Comp}(f,g,h_1)
\land
\operatorname{Comp}(f,g,h_2)
\rightarrow
h_1=h_2
\Big]
\]

is derivable from AX-C06 and AX-C07.

It is therefore retained as TH-C00 rather than as a primitive axiom.

## 20.2 Invalid countermodels from earlier audit attempts

Some earlier proposed countermodels allowed two distinct results for the same declared composition while retaining unit compositions.

Such structures violate AX-C07.

For example, if:

\[
\operatorname{Comp}(a,a,e)
\]

and:

\[
\operatorname{Comp}(a,a,a),
\]

then AX-C06 gives:

\[
\operatorname{Comp}(e,e,e),
\qquad
\operatorname{Comp}(a,e,a).
\]

An appropriate instance of AX-C07 forces:

\[
e=a.
\]

Thus these structures do not witness independence of the former AX-C03.

## 20.3 Independence of the remaining axioms

Explicit finite countermodels establish independence of:

\[
\mathrm{AX\mbox{-}C01},
\mathrm{AX\mbox{-}C02},
\mathrm{AX\mbox{-}C04},
\mathrm{AX\mbox{-}C05},
\mathrm{AX\mbox{-}C06},
\mathrm{AX\mbox{-}C07}.
\]

## 20.4 Editorial corrections incorporated

All countermodels now explicitly interpret both carriers, structural equivalence, application, composition, and the unit constant.

No model description relies on an unstated default interpretation.

---

# 21. Machine-Verification Roadmap

This section is a roadmap, not a claim of completed machine verification.

## Stage MV-C01. Signature

Declare opaque non-empty types or sorts:

```text
Rep
Trans
```

Declare:

```text
equivS : Rep → Rep → Prop
Apply  : Trans → Rep → Rep → Prop
Comp   : Trans → Trans → Trans → Prop
e      : Trans
```

## Stage MV-C02. Core structure

Package AX-C01, AX-C02, AX-C04, AX-C05, AX-C06, and AX-C07 as fields of one formal structure.

## Stage MV-C03. Derived theorems

Formalize and check TH-C00, TH-C01, and TH-C02.

TH-C00 should require only AX-C06 and AX-C07.

## Stage MV-C04. Satisfiability model

Encode \(\mathfrak M_0\) as a one-element finite instance and discharge all six axioms.

## Stage MV-C05. Independence witnesses

Encode:

\[
\mathfrak M_{\neg C01},
\mathfrak M_{\neg C02},
\mathfrak M_{\neg C04},
\mathfrak M_{\neg C05},
\mathfrak M_{\neg C06},
\mathfrak M_{\neg C07}.
\]

For each model prove:

1. the target axiom fails;
2. all other mandatory axioms hold.

## Stage MV-C06. Optional structurality witness

Encode \(\mathfrak M_{\neg C08}\) and prove:

\[
\neg\operatorname{Structural}(a).
\]

## Stage MV-C07. Release tag

After successful machine checking, create a separately identified release, for example:

```text
TSI-CORE-1.0-MV
```

or:

```text
TSI-CORE-1.1
Machine-Verified Edition
```

The machine-verified release must include proof-assistant source, toolchain version, dependency versions, build instructions, and cryptographic hashes of released files.

---

# 22. Version and Freeze Policy

TSI-CORE-1.0 is frozen as the baseline of the TSI research program.

“Frozen” means:

1. future modules may import the kernel;
2. future modules may add explicit axioms;
3. future modules may not silently alter the kernel;
4. correction of a mathematical error requires a new numbered release;
5. editorial changes that affect no formula should still be tracked by a revision identifier;
6. machine verification produces a separately identified release.

Suggested module names include:

- TSI-STRUCT;
- TSI-TIME;
- TSI-DYNAMICS;
- TSI-INFORMATION;
- TSI-MEMORY;
- TSI-PROBABILITY.

These names are organizational only and introduce no present commitments.

---

# 23. Canonical Kernel Summary

The canonical signature is:

\[
\left\langle
\mathsf{Rep},
\mathsf{Trans},
\equiv_{\mathsf S},
\operatorname{Apply},
\operatorname{Comp},
e
\right\rangle.
\]

The canonical mandatory theory is:

\[
\boxed{
\mathrm{AX\mbox{-}C01},
\mathrm{AX\mbox{-}C02},
\mathrm{AX\mbox{-}C04},
\mathrm{AX\mbox{-}C05},
\mathrm{AX\mbox{-}C06},
\mathrm{AX\mbox{-}C07}
}
\]

with:

\[
\boxed{
\mathrm{TH\mbox{-}C00}
}
\]

derived from:

\[
\mathrm{AX\mbox{-}C06}
\land
\mathrm{AX\mbox{-}C07}.
\]

The six mandatory axioms are mutually independent relative to the present signature.

---

# 24. Final Resolution

TSI-CORE-1.0 is adopted as the formally audited baseline kernel of the TSI research program.

The established claims are limited to:

- type correctness;
- satisfiability;
- the stated theorem derivations;
- the stated finite independence witnesses;
- minimality relative to the present signature and target properties.

No stronger mathematical, empirical, physical, computational, or certification claim is implied.

Future work proceeds through separately versioned modules that reduce to, and do not alter, TSI-CORE-1.0.

---

**End of TSI-CORE-1.0**
