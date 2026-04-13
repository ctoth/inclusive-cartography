---
title: "Institutions: Abstract Model Theory for Specification and Programming"
authors: "Joseph A. Goguen, Rod M. Burstall"
year: 1992
venue: "Journal of the ACM, 39(1), 95-146"
doi_url: "https://doi.org/10.1145/147508.147524"
pages: "95-146 (JACM); 73pp in UCSD preprint reading copy"
---

# Institutions: Abstract Model Theory for Specification and Programming

## One-Sentence Summary
Introduces **institutions** — an abstract formalization (4-tuple of signatures, sentences, models, and satisfaction) of the informal notion of "a logical system", capturing the Tarski-style satisfaction relation in a way that is parameterized over signatures, so that specification-language machinery (theories, structuring/combination operators, parameterization, implementation, duplex/multiplex constructions) can be developed once and reused across any logic whose satisfaction is invariant under signature change. *(p.1–3)*

## Problem Addressed
- "Population explosion" of logical systems in computer science: first-order, higher-order, Horn-clause, equational (many-sorted, order-sorted, conditional), temporal, dynamic, modal, intuitionistic, polymorphic lambda calculus, process logics, etc. *(p.2)*
- Each specification or programming-language community reinvents a theory of signatures, theories, colimits of theories, parameterization, implementation morphisms, and correctness proofs — all glued to one logic. *(p.2–3)*
- Goal: develop these structuring mechanisms **once**, parameterized over an arbitrary underlying logic, provided the logic satisfies a minimal abstract condition (the satisfaction condition). This enables logic-independent specification theory, lets one combine heterogeneous logics via *duplex* / *multiplex* institutions, and justifies modular specification even for artificial/natural languages. *(p.1–3)*

## Key Contributions
- Definition of an **institution** as a 4-tuple $(\text{Sign},\ \text{Sen},\ \text{Mod},\ \models)$ with a satisfaction condition expressing "truth is invariant under change of notation". *(p.2, Definition 1)*
- Catalog of example institutions: many-sorted first-order logic with equality, unsorted FOL, equational logic, Horn-clause, conditional equational, partial-algebra variants, order-sorted, higher-order, and others. *(p.2, summary)*
- Definition of **theories** and **theory morphisms** purely within an arbitrary institution; proof that the category of theories has colimits whenever the category of signatures does. *(p.2)*
- **Institution morphisms** and **duplex / multiplex institutions** — systematic combination of logics for programming-in-the-large (e.g. combining equational logic with first-order logic). *(p.2–3)*
- Applications: specification-language structure, parameterized programming, module systems, verification of constraints, and data-type "data" / "hierarchy" constraint extensions. *(p.2–3)*

## Context / Prior Work Motivation
- Fills a gap between:
  - Clear (Burstall & Goguen, [15]) and the 1980–84 "putting theories together" work, which only handled equational logic. *(p.3)*
  - Specific model-theoretic / algebraic-specification work like OBJ, ACT ONE, Larch, PLUSS, ASL, Ehrig–Mahr, Extended ML — each committed to one logic. *(p.3)*
- Barwise's "abstract model theory" [6] is cited as philosophically related but classical model-theoretic, not oriented to parameterization over notation / signature change. *(p.3, and elsewhere)*

## The Four Components of an Institution (§2, Definition 1) — *(p.4–6)*

An institution **I** consists of:

1. **Sign** — a category of *signatures* $\Sigma$. Objects are signatures; arrows are *signature morphisms* $\phi: \Sigma \to \Sigma'$ (rename/embed symbols consistently). *(p.4, bullet 1)*
2. **Sen: Sign → Set** — a functor assigning to each signature $\Sigma$ the set $\text{Sen}(\Sigma)$ of *$\Sigma$-sentences*, and to each signature morphism $\phi$ a *sentence translation* $\text{Sen}(\phi): \text{Sen}(\Sigma) \to \text{Sen}(\Sigma')$. *(p.4, bullet 2)*
3. **Mod: Sign^op → Cat** — a (contravariant) functor assigning to each signature $\Sigma$ a category $\text{Mod}(\Sigma)$ of *$\Sigma$-models*, with model morphisms as arrows; and to each $\phi: \Sigma \to \Sigma'$ a *reduct* functor $\text{Mod}(\phi): \text{Mod}(\Sigma') \to \text{Mod}(\Sigma)$ (often written $\_|_\phi$ or $U_\phi$). *(p.4, bullet 3)*
4. **$\models_\Sigma \subseteq |\text{Mod}(\Sigma)| \times \text{Sen}(\Sigma)$** — a *satisfaction relation* for each signature. *(p.4, bullet 4)*

### The Satisfaction Condition *(p.4–5, Theorem 2 / (1))*

For every signature morphism $\phi: \Sigma \to \Sigma'$, every $\Sigma'$-model $M'$, and every $\Sigma$-sentence $e$:

$$
M' \models_{\Sigma'} \text{Sen}(\phi)(e) \quad\Longleftrightarrow\quad \text{Mod}(\phi)(M') \models_\Sigma e
$$

Plain reading: "**truth is invariant under change of notation**". Translating a sentence along $\phi$ and then asking whether $M'$ satisfies it gives the same answer as reducing $M'$ along $\phi$ back to a $\Sigma$-model and asking whether *that* satisfies the original sentence. *(p.4–5)*

## Definitions and Basic Machinery (reading so far — §1.1, §2 opening) — *(p.1–5)*

- **Signature:** collection of non-logical symbols (function/relation symbols with arities, sort names). In many-sorted FOL a signature is $(S, F, P)$ with sorts $S$, function symbols $F_{w,s}$, and predicate symbols $P_w$. *(p.2, and §2)*
- **Signature morphism:** consistent renaming/embedding between two such vocabularies. *(p.2, bullet)*
- **$\Sigma$-sentence:** a sentence built over $\Sigma$ using the logic's sentence-forming apparatus. *(p.2)*
- **$\Sigma$-model:** an interpretation giving meaning to all symbols in $\Sigma$. *(p.2)*
- **Reduct of a model along $\phi$:** take a $\Sigma'$-model $M'$ and forget / rename back to produce a $\Sigma$-model $M'|_\phi$. In model-theoretic terms this is the *$\phi$-reduct*. *(p.4)*
- **Specification vs. programming distinction:** specifications are theories (sentences over a signature), programs are *denotations* of theories (models). Programming-language semantics is just the "forgetful" side, and specification semantics is both: theories AND their model classes. *(p.5)*

## Running Examples (§2 onward, anticipated)

- **EQ** — many-sorted equational logic; sentences are universally quantified equations, models are $\Sigma$-algebras. *(p.2, p.4)*
- **FOEQ** — first-order logic with equality, many-sorted. *(p.2, p.4)*
- Variants: unsorted FOL, Horn-clause logic, conditional equational logic, partial algebras, order-sorted, higher-order. *(p.2)*

## Key Equations / Definitions (LaTeX)

### (1) Satisfaction condition *(p.4–5)*

$$
M' \models_{\Sigma'} \text{Sen}(\phi)(e) \iff \text{Mod}(\phi)(M') \models_{\Sigma} e
$$

Where:
- $\phi: \Sigma \to \Sigma'$ is any signature morphism
- $e \in \text{Sen}(\Sigma)$
- $M' \in |\text{Mod}(\Sigma')|$
- $\text{Sen}(\phi)$ is the sentence-translation functor action
- $\text{Mod}(\phi)$ is the model-reduct functor action (contravariant)

## §2.2 Theories and Presentations *(p.11–15)*

### Definition 2 (presentation, model, theory — all relative to a fixed institution $\mathcal{I}$)

Let $\Sigma$ be a signature.

1. A **$\Sigma$-presentation** is a pair $\langle \Sigma, E\rangle$ where $E \subseteq \text{Sen}(\Sigma)$. *(p.12)*
2. A **$\Sigma$-model satisfies** $\langle \Sigma, E\rangle$ iff it satisfies every sentence in $E$. *(p.12)*
3. Given $E \subseteq \text{Sen}(\Sigma)$, define $E^* \subseteq |\text{Mod}(\Sigma)|$ to be the class of all $\Sigma$-models satisfying every sentence in $E$. Dually, given a class $M$ of $\Sigma$-models, $M^*$ is the set of sentences satisfied by every model in $M$. Also: $\mathbf{Mod}\langle\Sigma,E\rangle$ is the **theory** of $\langle \Sigma, E\rangle$. *(p.12)*
4. The **closure** of a presentation $\langle \Sigma, E\rangle$ is $\langle \Sigma, E^{**}\rangle$, denoted $E^{**}$. *(p.12)*
5. $\langle \Sigma, E\rangle$ is **closed** iff $E = E^{**}$. *(p.12)*
6. The closure of $\langle \Sigma, E\rangle$ is **the $\Sigma$-theory presented by** $E$, written $\langle\Sigma, E^{**}\rangle$. *(p.12)*
7. A **$\Sigma$-theory** is a presentation $\langle \Sigma, E\rangle$ with $E$ closed. *(p.12)*
8. The $\Sigma$-theory **presented by** a presentation is $\langle\Sigma, E^{**}\rangle$. *(p.12)*
9. A **$\Sigma$-sentence $e$ is semantically entailed by** a collection $E$ of $\Sigma$-sentences, written $E \models e$, iff $e \in E^{**}$. *(p.12)*

### Proposition 3 (Galois connection) *(p.13)*

The two $(-)^*$ maps form a **Galois connection**. For any $E, E' \subseteq \text{Sen}(\Sigma)$ and $M, M' \subseteq |\text{Mod}(\Sigma)|$:

1. $E \subseteq E' \Rightarrow E'^* \subseteq E^*$
2. $M \subseteq M' \Rightarrow M'^* \subseteq M^*$
3. $E \subseteq E^{**}$
4. $M \subseteq M^{**}$
5. $E^* = E^{***}$
6. $M^* = M^{***}$
7. There is a dual (inclusion-reversing) isomorphism between closed sets of sentences and closed classes of models; unions $\leftrightarrow$ intersections. *(p.13)*
8. $\bigcap_n E_n^* = (\bigcup_n E_n)^*$ (and the dual identities for model collections) *(p.13)*

### Proposition 4 (translation preserves closure under morphisms) *(p.14)*

Given signature morphism $\phi: \Sigma \to \Sigma'$ and a $\Sigma'$-model $m'$, $m' \in \phi(E)^*$ iff $\mathbf{Mod}(\phi)(m') \in E^*$. Translation along $\phi$ respects $(-)^*$: for $E \subseteq \text{Sen}(\Sigma)$, $\phi(E)^{**} \subseteq \phi(E^{**})$ (and stronger equalities under certain conditions). *(p.14)*

### Definition 5 (theory morphism) *(p.14)*

If $T = \langle \Sigma, E\rangle$ and $T' = \langle \Sigma', E'\rangle$ are theories, a **theory morphism** $\phi: T \to T'$ is a signature morphism $\phi: \Sigma \to \Sigma'$ such that $\phi(e) \in E'^{**}$ for every $e \in E$, equivalently $\phi(E) \subseteq E'^{**}$. The category of all $\mathcal{I}$-theories and theory morphisms is denoted $\mathbf{Th}$. *(p.14)*

### Definition 6 (forgetful functor on models of a theory) *(p.14)*

Given a theory morphism $\phi: T \to T'$, the **forgetful functor** $\phi^*: \mathbf{Mod}(T') \to \mathbf{Mod}(T)$ sends a $T'$-model $m'$ to $\mathbf{Mod}(\phi)(m')$. Well-defined because satisfaction is preserved under reduction along $\phi$ (by satisfaction condition + $\phi$ being a theory morphism). *(p.14)*

### Lemmas 7 and 8 *(p.15)*

- **Lemma 7 (closure):** $\phi(E^{**}) \subseteq \phi(E)^{**}$. Proof via satisfaction condition applied pointwise. *(p.15)*
- **Lemma 8 (presentation):** Given presentations $\langle \Sigma, E\rangle$ and $\langle \Sigma', E'\rangle$ and a signature morphism $\phi: \Sigma \to \Sigma'$ with $\phi(E) \subseteq E'^{**}$, the induced map is a theory morphism of the closures. So you can present theory morphisms using just a generating set $E$ — you do not need $E$ itself to be closed. *(p.15)*

## §2.4 Putting Theories Together — Clear-style colimits *(p.15–16)*

- Core insight (from Clear [15]): **build big theories as colimits of small theories connected by theory morphisms** (subtheory inclusions). *(p.16)*
- Example (p.16): a theory `NAT + BOOL` is built from subtheories `NAT`, `BOOL` both inclusions into a common bigger theory. Colimit gives minimal shared enrichment.
- The *sum* $T$ of subtheories $T_1, T_2$ with a shared subtheory $T_0$ is a pushout in $\mathbf{Th}$. *(p.16)*
- `enrich T by … / apply P to …` (Clear operators) are pushouts of theory morphisms. *(p.16)*
- For this to work, $\mathbf{Th}$ must have (finite) colimits. Upcoming Theorem 9 (§3): it does, as soon as $\mathbf{Sign}$ does — lifted via the sentence functor. *(p.16)*
- Parameterized specifications: formal parameter is a theory $P$, body is a theory $B$ with $P \hookrightarrow B$; instantiation is pushout along an *actual-argument theory morphism* $f: P \to A$. The instantiated body is the theory $A +_P B$. *(p.16)*

## §2.5 Diagrams and colimits (categorical machinery needed) *(p.17–19)*

### Definition 9 (diagram) *(p.17)*

A **diagram** $D$ in a category $\mathbf{C}$ consists of a graph $G$ together with a labelling of each node $n \in G$ by an object $D_n \in \mathbf{C}$ and each edge $e: n \to n'$ by a morphism $D(e) \in \mathbf{C}$. Calls $G$ the **shape**, $D$ the **base**, $D(e)$ the **apex** of an edge. A **morphism of cones** $\alpha \to \beta$ is a morphism $f: A \to B$ in $\mathbf{C}$ such that $\alpha_n \cdot f = \beta_n$ for every node $n$.

### Definition 10 (finite cocompleteness) *(p.18)*

A category $\mathbf{C}$ is **finitely cocomplete** iff every diagram of finite shape in $\mathbf{C}$ has a colimit. A functor $F: \mathbf{C} \to \mathbf{C}'$ **reflects (creates) colimits** iff whenever $D$ is a diagram in $\mathbf{C}$ such that $FD$ has a colimit in $\mathbf{C}'$ there is a (unique) colimit cone $\alpha$ for $D$ in $\mathbf{C}$ with $F\alpha$ the given colimit cone in $\mathbf{C}'$.

### Theorem 11 (the forgetful functor reflects colimits) *(p.18)*

**$\mathbf{Sign}: \mathbf{Th} \to \mathbf{Sign}$ reflects colimits.** So whenever $\mathbf{Sign}$ has finite colimits, $\mathbf{Th}$ does too. Proof sketch: given a diagram $D$ in $\mathbf{Th}$, take a colimit of its underlying $\mathbf{Sign}$-diagram, then define $E$ as the union of translated axioms from each theory in the diagram. Then $\langle \Sigma, E\rangle$ is a $\Sigma$-theory and the cone is a colimit cone in $\mathbf{Th}$. *(p.18)*

**Corollary 12 (informal, §2.5):** The category $\mathbf{Th}$ of theories in an institution is finitely cocomplete iff its category $\mathbf{Sign}$ of signatures is. *(p.19)*

### §2.5 more-categorical formulation of an institution *(p.19–21)*

"Twisted relations" view: in $\mathbf{Rel}$, a morphism between relations $R \subseteq A \times B$ and $R' \subseteq A' \times B'$ is a pair $(f, g)$ with $f: A \to A'$ and $g: B' \to B$ such that $aRb$ implies $f(a) R' g^{-1}(b)$ (note the reverse direction on the second component) — this matches the contravariance of $\mathbf{Mod}$ against the covariance of $\mathbf{Sen}$. *(p.19–20)*

### Definition 13 (institution morphism — provisional) *(p.20)*

An **institution morphism** $\mathcal{I} \to \mathcal{I}'$ consists of a functor $\Phi: \mathbf{Sign} \to \mathbf{Sign}'$ and a natural transformation $\eta: \Phi; \text{Sen}' \to \text{Sen}$ together with a natural transformation $\mu: \mathbf{Mod} \to \Phi^{op}; \mathbf{Mod}'$ (models are pushed forward, sentences are pulled back), such that the (satisfaction) composition is defined and a natural transformation with a twisted flavor. Institutions and institution morphisms form the category $\mathbf{INS}$. *(p.20–21)*

### Lemma 14 *(p.22)*

If $\mathbf{C}$ has pullbacks, then $\mathbf{Rel}(\mathbf{C})$ (the category of relations over $\mathbf{C}$) is a category. Used to set up a comma-category formulation of institutions and of institution morphisms. *(p.22)*

## §3 Constraints *(p.23 onward)*

### Motivation
- Ordinary specifications are too loose: a theory like NAT admits non-standard models (non-isomorphic algebras with "junk" elements or different representations). *(p.23)*
- Remedy: a **constraint** is a theory morphism $\theta: T' \to T$ declared within a specification such that the models of $T$ that are considered "acceptable" must be **free**/**initial** along $\theta$ — i.e., the reduct of such a model along $\theta$ determines the rest uniquely. *(p.23)*

### Definition 15 (liberal institution, free extension) *(p.26)*

- A theory morphism $F: T \to T'$ is **liberal** iff for every $T$-model $A$, the forgetful functor $F^*: \mathbf{Mod}(T') \to \mathbf{Mod}(T)$ has a *left adjoint* $F^\sharp$ — i.e. every $T$-model $A$ has a free extension $F^\sharp(A)$ along $F$.
- An institution is **liberal** iff every theory morphism in it is liberal. *(p.26, Definition 15)*

### Definition 16 (extensive morphism) *(p.27)*

Let $F: T \to T'$ be a theory morphism. $F$ is **extensive** iff for every $B \in \mathbf{Mod}(T')$ and every $A \in \mathbf{Mod}(T)$, if $A$ is free on $B$'s reduct, then the induced comparison map out of $F^\sharp(A)$ is a monomorphism. (Rules out pathological "collapsing" constructions.) *(p.27)*

## Examples of Institutions (§2.3+)

- **EQ / $\mathrm{EQ}^-$:** many-sorted equational logic with or without sorts-as-variables; signatures are $(S, F)$; sentences are universal equations $\forall X.\ t_1 = t_2$; models are $\Sigma$-algebras; $\models$ is standard algebraic satisfaction. *(§2.3 and App. A.1)*
- **FOEQ:** many-sorted first-order logic with equality. *(p.9, §2)*
- **Horn-clause logic** (conditional equations): limit to sentences of the form $(\bigwedge_i p_i) \Rightarrow q$. *(p.9)*
- **Lawvere-Sets** institution: signatures are $S$-sorted sets of operators, models are functors into **Set**; illustrates a "more abstract" signature-as-category presentation. *(p.24–25)*
- **LSET[X]**, **SET[X]**: parameterized theories for indexed/parameterized data structures, used throughout as running constraint examples. *(p.23)*

## Status notes
- Paper is 73 pages in UCSD preprint (`https://cseweb.ucsd.edu/~goguen/pps/ins.pdf`); JACM page numbering is 95–146.
- Directly reading all 73 page images (no chunking) per parent instructions.
- **All 73 pages read.** Paper ends on p.72 (refs [101]–[107]); p.73 is the TOC.
- **Commit:** `2d862365c32ee4e9c9c7dec06781a8c7897dde47` ("add: Goguen_1992_InstitutionsAbstractModelTheory via paper-process"). 5 files committed (abstract.md, citations.md, description.md, metadata.json, notes.md). `paper.pdf` and `pngs/` are in `.gitignore` (`*.pdf`, `*.png`) so they are deliberately not tracked — they stay on disk as local build artifacts.
- No blockers. Task complete.

## Appendix A.1 — General Algebra as an Institution *(p.50–55)*

### Definition 48 (equational signature)
$\Sigma = (S, \Omega)$ where $S$ is a set of **sorts** and $\Omega$ is a family of sets $\Omega_{w,s}$ (indexed by $w \in S^*, s \in S$) of **operator symbols** of arity $w$ and sort $s$. Constants live in $\Omega_{\varepsilon, s}$ where $\varepsilon$ is the empty string. *(p.50)*

### Definition 49 (equational signature morphism)
$\sigma: (S, \Omega) \to (S', \Omega')$ is a pair: a function $\sigma: S \to S'$ and an $S^* \times S$-indexed family of maps $\sigma_{w,s}: \Omega_{w,s} \to \Omega'_{\sigma^*(w), \sigma(s)}$. Composition is component-wise. The **category of equational signatures** is $\mathbf{Sig}$. *(p.51)*

### Definition 50 ($\Sigma$-algebra)
Given $\Sigma = (S, \Omega)$, a $\Sigma$-algebra $A$ consists of an $S$-indexed family $|A| = \{A_s \mid s \in S\}$ (the **carriers** of $A$) together with, for each $\sigma \in \Omega_{w,s}$, a function $\sigma_A: A_w \to A_s$. Homomorphisms preserve operators. A morphism $\phi: \Sigma \to \Sigma'$ induces a reduct functor $\mathbf{Alg}(\phi): \mathbf{Alg}_{\Sigma'} \to \mathbf{Alg}_{\Sigma}$ computed pointwise: for $A' \in \mathbf{Alg}_{\Sigma'}$, define $\mathbf{Alg}(\phi)(A')_s = A'_{\phi(s)}$ and $\sigma \mapsto \phi(\sigma)_{A'}$. *(p.52–53)*

### Term algebra $T_\Sigma(X)$ *(p.53)*
Given a variable $S$-sorted set $X$, $T_\Sigma(X)$ is the free $\Sigma$-algebra on $X$: smallest $S$-sorted set closed under sorts (generators from $X$) and operator application, with initial-$\Sigma$-algebra structure. Key fact *(Theorem 55)*: $T_\Sigma(X)$ is initial in the category of $\Sigma$-algebras equipped with an assignment of $X$ — i.e. the free algebra construction is a left adjoint to the forgetful functor. *(p.53)*

### Definition 56 ($\Sigma$-equation), Definition 57 (satisfaction), Definition 58 (equation translation) *(p.54)*
- A $\Sigma$-**equation** $e$ is a triple $(X, t_1, t_2)$ where $X$ is an $S$-sorted set of variables and $t_1, t_2 \in T_\Sigma(X)_s$ for some sort $s$.
- $A \models_\Sigma (X, t_1, t_2)$ iff for every assignment $\alpha: X \to A$, the unique homomorphic extensions satisfy $\alpha^*(t_1) = \alpha^*(t_2)$.
- A signature morphism $\phi: \Sigma \to \Sigma'$ acts on equations by translating terms: $\phi((X, t_1, t_2)) = (\phi(X), \phi^\sharp(t_1), \phi^\sharp(t_2))$. *(p.54)*

### Definition 59 (Eqs functor) and Proposition 60 (satisfaction condition for EQ) *(p.55)*
- $\text{Eqs}: \mathbf{Sig} \to \mathbf{Set}$ sends $\Sigma$ to the set of $\Sigma$-equations and acts on morphisms via the above translation.
- **Proposition 60 (Satisfaction Condition):** For $\phi: \Sigma \to \Sigma'$, $\Sigma'$-algebra $A'$, and $\Sigma$-equation $e$: $A' \models_{\Sigma'} \phi(e) \iff \mathbf{Alg}(\phi)(A') \models_\Sigma e$. Straightforward from the fact that the reduct preserves assignments.
- **Example 61:** Many-sorted Equational Logic is an institution. **FoSig**, **FoSigEq**, **FoModEq** are introduced as variants where the sentence functor is built over first-order formulas rather than equations, and the model functor stays the same for the Equational side but is restricted to the sub-class respecting the formula structure for the first-order side. *(p.55)*

## Appendix A.2 — First-Order Logic and Related Institutions *(p.55–60)*

### Definition 62 (first-order signature) *(p.55–56)*
A **first-order signature** $\Omega$ is a triple $(S, \Omega, \Pi)$ where:
1. $S$ is a set of sorts.
2. $\Omega = \{\Omega_{w,s} \mid w \in S^*, s \in S\}$ is an $S^* \times S$-indexed family of **operator/function symbols**.
3. $\Pi = \{\Pi_w \mid w \in S^*\}$ is an $S^*$-indexed family of **predicate/relation symbols**.

A morphism of first-order signatures is a triple $(\phi_1, \phi_2, \phi_3)$: a sort-map, an operator-map, and a predicate-map, consistent with arities. Call **FoSig** the category of first-order signatures, **FoSig$_{eq}$** the variant with equality built in, and **FoSig$^-$** the variant without relation symbols.

### Definition 63 ($\Omega$-model) *(p.56)*
A **model** $A$ of an $\Omega$ consists of
1. An $S$-indexed family $|A| = \{A_s \mid s \in S\}$ of carrier sets called the **carriers** (one per sort).
2. For each $\sigma \in \Omega_{w,s}$, a function $\sigma_A: A_w \to A_s$.
3. For each $\pi \in \Pi_w$, a relation $\pi_A \subseteq A_w$.

A **morphism** of first-order $\Omega$-models is an $S$-sorted family of functions preserving operators and relations (but not required to reflect them). Call **FoMod** the functor $\Omega \mapsto \mathbf{FoMod}(\Omega)$.

### Definition 64 ($\Omega$-formulas, $\mathrm{TERM}_\Omega$, $\mathrm{WFF}_\Omega$) *(p.56–57)*
$\mathrm{TERM}_\Omega(X)$ is the usual set of terms over variables $X$. **Atomic $\Omega$-formulas** over $X$ are either of the form $\pi(t_1, \ldots, t_n)$ for $\pi \in \Pi_w$ and $t_i \in \mathrm{TERM}_\Omega(X)_{w_i}$, or of the form $t_1 = t_2$ for $t_1, t_2$ of the same sort (in FoSig$_{eq}$). Then:

1. $Var(true) = \emptyset$; $Var(t_1 = t_2) = Var(t_1) \cup Var(t_2)$; $Var(\pi(t_1, \ldots, t_n)) = \bigcup_i Var(t_i)$; $Var(\neg P) = Var(P)$; $Var(P \wedge Q) = Var(P) \cup Var(Q)$; $Var((\forall x) P) = Var(P) \setminus \{x\}$.
2. $Free(true) = \emptyset$ and dually for $=$, $\pi$; $Free((\forall x) P) = Free(P) \setminus \{x\}$.

A formula is **closed** ($\Omega$-formula, in the strict sense) iff it has no free variables. $\mathrm{WFF}_\Omega(X) \subseteq$ closed formulas. *(p.57)*

### Definition 65 (Tarski satisfaction) *(p.58)*
Given an assignment $\sigma: X \to |A|$ and any formula $P$ over variables $X$, define $A \models_\sigma P$ by induction on the formula tree. Key cases:
1. $A \models_\sigma true$;
2. $A \models_\sigma (t_1 = t_2)$ iff $\sigma^*(t_1) = \sigma^*(t_2)$ (where $\sigma^*$ is the unique homomorphic extension of $\sigma$);
3. $A \models_\sigma \pi(t_1, \ldots, t_n)$ iff $(\sigma^*(t_1), \ldots, \sigma^*(t_n)) \in \pi_A$;
4. $A \models_\sigma \neg P$ iff $A \not\models_\sigma P$;
5. $A \models_\sigma P \wedge Q$ iff $A \models_\sigma P$ and $A \models_\sigma Q$;
6. $A \models_\sigma (\forall x) P$ iff for every $a \in A_{\text{sort}(x)}$, $A \models_{\sigma[x \mapsto a]} P$.
For a closed formula $P$, $A \models P$ iff $A \models_\sigma P$ for some (equivalently every) $\sigma$. *(p.58)*

**Satisfaction Condition for $\mathcal{FOEQ}$:** derived in the same pattern as the equational case — translation commutes with reduct. *(p.58)*

### Examples 66–71 — packaging specific logical systems as institutions
- **Example 66** (many-sorted FOL): institution $\mathcal{FOL}$.
- **Example 67** (many-sorted FOL with equality, $\mathcal{FOEQ}$): same signatures, but formulas include equality; equivalent to FOL via axioms. *(p.58–59)*
- **Example 68** (many-sorted Horn-clause logic with equality): same signatures, sentences restricted to **universally quantified Horn clauses** $(\forall X)\ A_1 \wedge \ldots \wedge A_n \Rightarrow A$ where each $A_i$ is an atomic formula or equation. Institution **HornEq** is a subinstitution of $\mathcal{FOEQ}$. *(p.59–60)*
- **Example 69** (many-sorted conditional equational logic): Horn with equality restricted to equational atoms. Institution $\mathcal{CEQ}$; this is the basis for OBJ2/OBJ3 and Larch. *(p.60)*
- **Example 70** (many-sorted Horn-clause logic **without** equality): variant **HornRel** whose sentences are Horn clauses without equality. Basis for pure Prolog. *(p.60)*
- **Example 71** (loose-semantics $\mathcal{FOEQ}$): institution where models of a theory are **all** models satisfying the axioms (loose model class), not just initial/free ones. Used when treating "theories whose meaning is a model class, not a single canonical model". *(p.60)*

## Limitations / Caveats Noted by the Authors

- The formalization assumes a **set-theoretic** ambient universe; models and sentences are handled as sets/classes (p.7, p.13 footnote on Set vs Set$_0$ — some size issues, worked around by using Grothendieck universes where convenient). *(p.7, p.13 footnote)*
- **Liberal institution** property is not free — several institutions fail it (e.g. general FOL with explicit non-initial interpretations). Hence the explicit definition and careful theorem conditions. *(p.28, §3.1)*
- **Duplex/multiplex institutions** require an institution morphism $\Phi$ that is sufficiently well-behaved ("cordial") to propagate cocompleteness; otherwise you lose the ability to build colimits of theories. *(p.43, Theorem 39)*
- The "satisfaction condition" does not itself guarantee decidability or compactness of entailment — it is just the structural precondition for treating theories abstractly. *(p.49 / §5)*
- Abstract model theory in the Lindström/Barwise tradition (compactness, Löwenheim-Skolem generalizations) is acknowledged as related but **not** the focus — the institution definition is weaker and more structurally oriented. *(p.7, p.49)*

## Arguments Against Prior Work

- **Clear [15]** handled only equational logic; other specification languages (ACT ONE, OBJ, Larch, PLUSS, ASL, Ehrig–Mahr) were similarly committed to one underlying logic. Goguen/Burstall argue this forces every structuring theorem to be reproved per logic. *(p.3)*
- **Classical abstract model theory (Barwise [6], Lindström, Feferman)** treats a logic as a set of first-order sentences with a compactness/LöSk-generalization angle; Goguen/Burstall argue this misses the *signature/notation-change* dimension that matters in specification languages. *(p.3, p.7)*
- **Meseguer's general logics [76]** is cited as the closest contemporaneous reformulation and is argued to be more abstract (based on closure systems of consequence) but at the cost of losing the model-theoretic machinery; institutions retain models and therefore retain "data" / constraints / parameterization naturally. *(p.5, and summary §5)*
- Earlier formal specification approaches that relied on fixed higher-order or dependent-type logics lose modularity because they cannot rename/embed signatures without redoing the semantics each time. *(p.2–3)*

## Design Rationale

- Why **functorial** $\text{Sen}$ and $\text{Mod}$? Because specifications and models must be *translated* along signature morphisms (to rename, import, forget, or extend), and functoriality guarantees that such translations compose correctly and preserve composition of morphisms. *(p.4, Definition 1)*
- Why **contravariance** of $\text{Mod}$? A signature morphism $\phi: \Sigma \to \Sigma'$ expands a vocabulary, so a $\Sigma'$-model has at least as much structure as a $\Sigma$-model — the natural direction is to *forget* extra structure, hence $\text{Mod}(\phi): \mathbf{Mod}(\Sigma') \to \mathbf{Mod}(\Sigma)$. *(p.4)*
- Why a **satisfaction condition** as the axiom? It is the categorically cleanest way to say "truth is invariant under notation change", and it is the precise condition under which the central constructions (Galois connection between theories and model classes, closure of theories under translation, colimits of theories, lifting of theory morphisms) all go through. *(p.2, §2.1, Def 1)*
- Why build **theories** on top of presentations rather than syntactic closures alone? Because presentations enable modular construction (Lemma 8 lets you specify a theory by a *generating set*, which is how Clear and OBJ actually work). *(p.15, Lemma 8)*
- Why develop **institution morphisms** rather than just fixing one institution? To formalize the idea that one logic can *implement* another (e.g. encode first-order specifications as equational ones in a multi-sorted setting), and to justify duplex specifications that mix logics in practice. *(p.39, §4)*
- Why **constraints** as a *theory morphism with an initiality condition*, not as a new sentence constructor? Because it keeps the constraint mechanism *inside* the institution-theoretic framework, so all the structuring and colimit machinery automatically applies to constrained specifications. *(p.30, §3.2)*

## Testable Properties

- Every institution must satisfy the satisfaction condition *(p.4)*.
- If $\mathbf{Sign}$ is finitely cocomplete, then $\mathbf{Th}$ is too (Theorem 11). Test: in any implementation, a pushout of theory morphisms exists whenever a pushout of the underlying signature morphisms exists. *(p.18)*
- Galois connection properties: $E \subseteq E^{**}$, $M \subseteq M^{**}$, $E^* = E^{***}$ (Proposition 3). *(p.13)*
- $\mathcal{C}(\mathcal{I})$ is an institution iff $\mathcal{I}$ is an institution (Prop 23). Test: augmenting the sentence set with constraints preserves the satisfaction condition. *(p.32)*
- $\mathbf{Th}_{\mathcal{C}(\mathcal{I})}$ cocomplete iff $\mathcal{I}$'s signatures cocomplete (Thm 24). *(p.33)*
- If $\Phi: \mathcal{I} \to \mathcal{I}'$ is cordial, $\overline{\Phi}: \mathbf{Th}_{\mathcal{I}'} \to \mathbf{Th}_{\mathcal{I}}$ is cocontinuous (Thm 39). *(p.43–44)*
- $\mathcal{D}(\Phi)$ is an institution and cocomplete whenever $\mathcal{I}$ is (Thm 44, Cor 45). *(p.46)*
- Initial algebras $T_\Sigma$ exist and are unique up to iso in $\mathbf{Alg}_\Sigma$, and "generalised initiality" is the content of a data constraint (Thm 55 + Def 19). *(p.30, p.53)*

## Relevance to Project (inclusive-cartography, systematic-review protocol critique)

This is a foundational theoretical paper, not an empirical one. Its direct relevance to the inclusive-cartography project's current batch (critique of LLM-confidence-threshold selection in a systematic-review protocol) is **thematic rather than empirical**: it provides the canonical reference for the *institution-theoretic* abstraction of logical systems, which is useful if/when:

1. The cognitive-review protocol invokes the word "institution" in the sense of Goguen/Burstall — i.e., a logic-independent framework for theories and their semantics.
2. The protocol critique needs a formal framework for comparing heterogeneous evidence "logics" (e.g. qualitative assessment vs. quantitative scoring) under a shared abstract structure.
3. The project ever needs to discuss "satisfaction condition" / "change of notation" / "category of theories" as a point of comparison.

If the meeting discussion involves cross-logic specification, modular theory building, or formal abstractions of logical systems, this paper is the canonical citation.

## Open Questions

- [ ] Does the inclusive-cartography protocol actually invoke institutions in Goguen/Burstall's sense, or is the word being used in a different (e.g. social-institutional) sense? — to clarify with Q tomorrow.
- [ ] Is there a "light" institution-theoretic analogue for LLM-confidence-threshold analysis? (Probably no; but the *signature/sentence/model* framing could translate to "prompt-schema / assertion / answer distribution".)

## Related Work Worth Reading

- **Meseguer, "General logics" (1989, ref [76])** — rival but related reformulation based on closure systems.
- **Tarlecki et al. works on institution-independent model theory** (refs [97]–[100]) — subsequent development of institution theory.
- **Sannella & Tarlecki on parameterization** (refs [91]–[93]).
- **Barwise & Feferman, "Model-Theoretic Logics" (ref [6])** — the classical abstract model theory predecessor.

## §4 Institution Morphisms — Using More Than One Institution *(p.39–47)*

Motivation: to "implement" sentences in one institution via constructions in another. Example: relate first-order logic $\mathcal{FOEQ}$ to equational logic $\mathcal{EQ}$ by reflecting a first-order signature to a Horn-logic signature with the right amount of machinery.

### Definition 32 (institution morphism — expanded) *(p.40)*

An **institution morphism** $\Phi: \mathcal{I} \to \mathcal{I}'$ consists of:

1. A functor $\Phi: \mathbf{Sign} \to \mathbf{Sign}'$
2. A natural transformation $\alpha: \Phi; \text{Sen}' \to \text{Sen}$ (sentence translation goes **backwards**: from $\mathcal{I}'$ into $\mathcal{I}$)
3. A natural transformation $\beta: \mathbf{Mod} \to \Phi^{op}; \mathbf{Mod}'$ (model translation goes **forwards**)

satisfying the Satisfaction Condition for morphisms *(p.40)*:

$$
m \models_{\Sigma} \alpha_\Sigma(e') \iff \beta_\Sigma(m) \models'_{\Phi(\Sigma)} e'
$$

for every $\Sigma$-model $m$ from $\mathcal{I}$ and $\Phi(\Sigma)$-sentence $e'$ from $\mathcal{I}'$. *(p.40)*

### Proposition 33 (equational reformulation) *(p.41)*

Given an institution morphism $\Phi: \mathcal{I} \to \mathcal{I}'$, a set $M$ of $\Sigma$-models of $\mathcal{I}$, and a set $E'$ of $\Phi(\Sigma)$-sentences of $\mathcal{I}'$:

1. $(\beta_\Sigma M)^* = \alpha_\Sigma^{-1}(M^*)$
2. $(\alpha_\Sigma E')^* = \beta_\Sigma^{-1}(E'^*)$

### Definition 34 / Proposition 35 (sound / complete institution morphism) *(p.42)*

- An institution morphism $\Phi: \mathcal{I} \to \mathcal{I}'$ is **sound** iff $\mathcal{FOEQ} \Rightarrow \mathcal{EQ}$-style translation preserves entailment.
- It is **sound** iff for every $\Sigma$-theory in $\mathcal{I}'$ and every sentence $e \in E$: $\alpha(E) \models_{\mathcal{I}} \alpha(e)$ whenever $E \models'_{\mathcal{I}'} e$.

### Definition 36, Proposition 37, Definition 38, Theorem 39 — lifting institution morphisms to theory morphisms, cordiality, cocontinuity *(p.42–44)*

- **Definition 36 (lifted theory map):** Given an institution morphism $\Phi: \mathcal{I} \to \mathcal{I}'$ with $\Phi; \text{Sign}' = 1_{\mathbf{Sign}'}$, define $\overline{\Phi}: \mathbf{Th}_{\mathcal{I}'} \to \mathbf{Th}_{\mathcal{I}}$ by $\overline{\Phi}(\langle \Sigma', E'\rangle) = \langle \Psi(\Sigma'),\ (\alpha_{\Psi(\Sigma')}(E'))^*\rangle$ and $\overline{\Phi}(\phi) = \Psi(\phi)$. *(p.42)*
- **Proposition 37:** $\overline{\Phi}(\phi)$ defined above is indeed a theory morphism, and $\overline{\Phi}$ is a functor. Proof uses Presentation Lemma 8. *(p.43)*
- **Definition 38 (cordial morphism):** $\Phi$ is **(finitely) cordial** iff the underlying functor $\Phi$ on signatures has a left inverse $\Psi: \mathbf{Sign}' \to \mathbf{Sign}$ with $\Psi; \Phi = 1_{\mathbf{Sign}'}$ that is (finitely) cocontinuous. *(p.43)*
- **Theorem 39 (cordial implies cocontinuous lift):** If $\Phi: \mathcal{I} \to \mathcal{I}'$ is (finitely) cordial, then $\overline{\Phi}: \mathbf{Th}_{\mathcal{I}'} \to \mathbf{Th}_{\mathcal{I}}$ is (finitely) cocontinuous — i.e., you can push colimits of $\mathcal{I}'$-theories through to $\mathcal{I}$. Detailed colimit computation given p.43–44. *(p.43–44)*

## §4.2 Duplex Institutions *(p.45–47)*

Used when you want two logics at once: e.g., equational core (for data definitions) plus first-order shell (for further properties and constraints) — this is how Clear/OBJ/Larch informally combine equational definitions with additional first-order properties.

### Definition 40 (duplex constraint) *(p.45)*

Let $\Phi: \mathcal{I} \to \mathcal{I}'$ be an institution morphism and let $\Sigma$ be a signature in $\mathcal{I}'$. A **$\Sigma$-duplex constraint** is a pair $c = \langle F: T'' \to T',\ \theta: \text{Sign}(T'') \to \Phi(\Sigma)\rangle$ where $F$ is a theory morphism in $\mathcal{I}'$ and $\theta$ is a signature morphism in $\mathcal{I}'$. A $\Sigma$-model $m$ of $\mathcal{I}$ **satisfies** $c$ iff the reduct of $\beta(m) \in \mathbf{Mod}'(\Phi(\Sigma))$ along $\theta$ is in the category $\mathcal{A}$ of free $F$-extensions of some $T''$-model (up to iso). *(p.45)*

In other words: a duplex constraint expresses an "initial / free-extension" condition in $\mathcal{I}'$ but is attached to and satisfied by a model in $\mathcal{I}$, via $\Phi$'s model translation $\beta$.

### Definition 41 (translation of duplex constraint) *(p.46)*

Given $\phi: \Sigma \to \Sigma'$ in $\mathbf{Sign}$, the translation of a $\Sigma$-duplex constraint $c = \langle F, \theta \rangle$ along $\phi$ is $\phi(c) = \langle F,\ \phi \cdot \theta \rangle$ — analogous to Definition 20. *(p.46)*

### Lemma 42 (satisfaction) and Definition 43 (duplex institution) *(p.46)*

- **Lemma 42:** For $c$ a duplex constraint and $\phi$ a signature morphism, $m \models \phi(c)$ iff $\phi(m) \models c$.
- **Definition 43:** The **duplex institution** $\mathcal{D}(\Phi)$ associated with an institution morphism $\Phi: \mathcal{I} \to \mathcal{I}'$ has $\mathcal{I}$'s signatures and models but the sentence set enriched by $\mathcal{I}$-sentences **plus** $\mathcal{I}'$-sentences (translated via $\alpha$) **plus** duplex constraints. Satisfaction extends uniformly. *(p.46)*

### Theorem 44, Corollary 45, Definition 46, Proposition 47 *(p.46–47)*

- **Theorem 44:** If $\mathcal{I}$ is an institution and $\Phi: \mathcal{I} \to \mathcal{I}'$ is an institution morphism, then $\mathcal{D}(\Phi)$ is an institution. Proof is Proposition 23 (constraint institution) applied through $\Phi$.
- **Corollary 45:** If the category of signatures of $\mathcal{I}$ is (finitely) cocomplete then so is the category of theories of the duplex institution $\mathcal{D}(\Phi)$. Thus you can still do all the Clear-style structuring.
- **Definition 46 ($\mathcal{T}(\Phi)$, "theories of $\Phi$"):** The category whose objects are pairs $\langle T, T'\rangle$ with $T \in \mathbf{Th}_{\mathcal{I}}$ and $T' \in \mathbf{Th}_{\mathcal{I}'}$ linked appropriately and whose arrows are compatible theory-morphism pairs; a "multi-institution theory". *(p.46)*
- **Proposition 47:** $\mathcal{T}(\Phi)$ is an institution. *(p.47)*

## §4.3 Multiplex Institutions *(p.47–48)*

Generalizes duplex from two institutions to a **tower / diagram** of institutions linked by institution morphisms $\Phi_i: \mathcal{I}_i \to \mathcal{I}_{i+1}$ (or an arbitrary finite diagram shape). The definitions of multiplex constraint, translation, and the resulting institution $\mathcal{M}(\Phi_1, \ldots, \Phi_n)$ follow the duplex pattern.

Running example: `STRING-OF-NAT` is built using a multiplex institution where natural numbers are introduced equationally (in $\mathcal{EQ}$) and `string_of` is defined via first-order sentences (in $\mathcal{FOEQ}$), and existential quantifiers can be used from the target institution when convenient. *(p.47–48)*

Terminology glossary:

- `even(n)` can be formulated either equationally or via Horn/FOL — multiplex lets you pick.
- "Loosely" is meant in the $\mathcal{FOEQ}$ sense (existential quantifiers allowed).

## §5 Summary and Future Research *(p.48–49)*

- Formalized "logical system" / "abstract model theory" = institutions, specifically by requiring the satisfaction condition.
- Institutions give meaning to specification-language features *generically*: theories, structuring, theory morphisms, parameterization, implementation morphisms, constraints, data constraints, duplex / multiplex combinations of logics.
- Five directions for future research *(p.49)*:
  1. Connect to "algebraic-logic" work of Tarski (sharpen the Satisfaction Condition side).
  2. Characterize "strongly liberal" institutions (characterization of $F^*$ as free-generated).
  3. Work on thorough explorations of cocompleteness results (Tarlecki references 47 and 97).
  4. Study classical Tarski-style abstract model theory (Lindström, Barwise) inside the institution framework.
  5. Study more concrete examples (programming languages like pure Prolog, OBJ, Eqlog, Clear, LIL, program development LIL).

## §3.2 Constraining Theories — Constraint as Extra Sentence *(p.29–33)*

### Definition 19 (Σ-constraint) *(p.30)*

A **Σ-constraint** is a pair $(F: T' \to T'',\ \theta: \text{Sign}(T'') \to \Sigma)$ consisting of a theory morphism $F$ and a signature morphism $\theta$ landing in $\Sigma$. A $\Sigma$-model $M$ **satisfies** the constraint iff $\theta M$ ("reduct of $M$ along $\theta$") satisfies $T''$ and is $F$-free (i.e. initial in the fiber over its $T'$-reduct along $F$) up to iso.

The idea: the constraint says "the behavior of the symbols reached by $\theta$ from $T''$ should be freely generated by the behavior mapped in via $F$". Constraints encode "data" initiality (no junk, no confusion) without leaving the institutional framework.

### Definition 20 (translation of a constraint) *(p.30)*

Given $c = (F, \theta)$ a $\Sigma$-constraint and $\phi: \Sigma \to \Sigma'$ a signature morphism, the **translation** $\phi(c)$ is $(F,\ \phi \cdot \theta)$. That is: you compose the second component with $\phi$; $F$ is untouched.

### Lemma 21 (constraint satisfaction under translation) *(p.31)*

For a signature morphism $\phi: \Sigma \to \Sigma'$, a $\Sigma$-constraint $c$, and a $\Sigma'$-model $B$: $B \models \phi(c)$ iff $\phi(B) \models c$. This is the "satisfaction condition for constraints" — it is the analogue of the basic satisfaction condition.

### Definition 22 / Proposition 23 — the institution $\mathcal{C}(\mathcal{I})$ *(p.31–32)*

Given an institution $\mathcal{I}$, the institution $\mathcal{C}(\mathcal{I})$ has:

- Same signatures and same models as $\mathcal{I}$.
- $\text{Sen}_{\mathcal{C}(\mathcal{I})}(\Sigma) = \text{Sen}_{\mathcal{I}}(\Sigma) \cup (\text{set of } \Sigma\text{-constraints})$.
- Satisfaction is the union of $\mathcal{I}$-satisfaction and constraint-satisfaction.

**Proposition 23:** If $\mathcal{I}$ is an institution, then so is $\mathcal{C}(\mathcal{I})$. Proof is essentially Lemma 21 + functoriality of $\mathbf{Mod}$.

### Theorem 24 (C(I) cocomplete) *(p.33)*

Given an institution with a finitely cocomplete category of signatures, the institution $\mathcal{C}(\mathcal{I})$ of constraining theories has (finitely) cocomplete theories. This lets you use all the Clear-style structuring machinery on constrained theories.

### Running examples — **N**, **NP**, `SETCH` *(p.33–34)*

- **N** is natural numbers with `0: N` and `s: N -> N`.
- **NP** is **N** plus a unary predicate `p`.
- `SETCH` is a parameterized theory of sets over a data parameter; the constraint declared in `NAT` pinned natural numbers to their free/initial model (no junk natural numbers, no confusion).
- This gives the "initial model" interpretation that algebraic-specification practice needs, **without** leaving the institution-independent framework. *(p.33–34)*

## §3.3 Other kinds of constraint *(p.35–38)*

### Definition 25 (data/hierarchy constraint) *(p.35)*

A "data constraint" from $\mathcal{I}$ is a variant where we decorate a constraint with a selected category $\mathcal{A}$ of target models: only models in $\mathcal{A}$ are considered acceptable free extensions. *(Used for "junk-free, confusion-free" model-class filtering.)*

### Proposition 26 *(p.35)*

Modifying $\mathcal{C}(\mathcal{I})$ to use $\mathcal{A}$-satisfaction still yields an institution, and its theories are as cocomplete as $\mathcal{I}$.

### Definition 27 (image factorization situation) *(p.36)*

For a category $\mathbf{C}$, an **image factorization situation** is a pair $(\mathcal{E}, \mathcal{M})$: class $\mathcal{E}$ of epics, class $\mathcal{M}$ of monics, both closed under composition, all isos in both, and every $f$ factors as $e; m$ with $e \in \mathcal{E}, m \in \mathcal{M}$ uniquely up to a unique isomorphism of center objects.

### Proposition 28 (diagonal fill-in property) *(p.37)*

Given an image factorization situation on $\mathbf{C}$, the diagonal fill-in property holds: any commutative square with one edge in $\mathcal{E}$ and opposite edge in $\mathcal{M}$ has a unique diagonal. Also closure under pushouts/pullbacks.

### Definition 29 (institution with image factorization) *(p.37)*

An institution $\mathcal{I}$ has **image factorization** iff each category $\mathbf{Mod}(\Sigma)$ has one that is "preserved under reducts" (functors $\mathbf{Mod}(\phi)$ map $\mathcal{E}$ to $\mathcal{E}$ and $\mathcal{M}$ to $\mathcal{M}$).

### Definition 30 (F-generated model) *(p.37)*

Let $F: T \to T'$ be a theory morphism. A $T'$-model $B$ is **F-generated** iff the unit $\epsilon_B: F^\sharp(F^*(B)) \to B$ of the adjunction is in $\mathcal{E}$ (i.e., an epic in the factorization).

### Theorem 31 (closure properties) *(p.38)*

If $\mathcal{I}$ is liberal with image factorization and $F: T \to T'$ is a theory morphism with $A$ an $F$-free $T'$-model, then for every monic $m: B \hookrightarrow A$ in $\mathbf{Mod}(T')$ such that $m$ factors through $F^*$, $B$ is also $F$-free. In short: "subobjects of free models are free" under these assumptions — the machinery needed to make hierarchy constraints behave properly.
