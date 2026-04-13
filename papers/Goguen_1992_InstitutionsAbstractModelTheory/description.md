---
tags: [category-theory, model-theory, algebraic-specification, logical-frameworks, formal-methods]
---
Introduces **institutions** — a category-theoretic abstraction of a "logical system" as a 4-tuple $(\text{Sign}, \text{Sen}, \text{Mod}, \models)$ satisfying a satisfaction condition ("truth is invariant under change of notation"), so that specification-language machinery (theories, theory morphisms, colimits, parameterization, constraints) can be developed once and reused across arbitrary underlying logics.
Proves that the category of theories $\mathbf{Th}$ is cocomplete whenever its signature category is, defines institution morphisms / duplex / multiplex constructions for combining logics, and introduces "constraints" as a theory-morphism + initiality condition that captures data-type constraints inside the framework.
Foundational to algebraic specification (Clear, OBJ, Larch, CASL) and to any formal discussion of logic-independent specification, theory structuring, or cross-logic translation — canonical reference when the word "institution" appears in the Goguen/Burstall sense.
