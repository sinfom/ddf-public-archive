# N5a Gauge Algebra Selection From Projection Structure

path: 02_operator_notes/N5a-Gauge-Algebra-Selection-from-Projection-Structure.md
folder: 02_operator_notes
filename: N5a-Gauge-Algebra-Selection-from-Projection-Structure.md
repository: DDF
type: research_note

# N5a — Gauge Algebra Selection from Projection Structure

## Status

Partial derivation (structure + minimality constraints)

------

# 1. Purpose

Constrain the gauge algebra

[
\mathfrak{g}
]

derived in N5 to the form:

[
\mathfrak{u}(1)\oplus \mathfrak{su}(2)\oplus \mathfrak{su}(3)
]

using structural and minimality arguments.

------

# 2. Starting Point

From N5:

[
\mathfrak{g} = \mathrm{Comm}(H_{\text{int}})
]

with:

[
\mathfrak{g} \subset \mathfrak{u}(N)
]

------

# 3. Structural Constraints

We impose:

### (C1) Compactness

[
G \subset U(N)
]

### (C2) Finite-dimensional decomposition

[
\mathcal{H}_{\text{int}} = \bigoplus_i V_i
]

### (C3) Minimal non-trivial symmetry

- exclude trivial symmetry
- avoid unnecessary enlargement

### (C4) Interaction irreducibility

- sectors remain distinct but coupled

------

# 4. Minimal Internal Decomposition

The smallest non-trivial decomposition satisfying these constraints is:

[
\mathcal{H}_{\text{int}} =
\mathbb{C}^1 \oplus \mathbb{C}^2 \oplus \mathbb{C}^3
]

------

# 5. Resulting Commutant

This yields:

[
\mathfrak{g} =
\mathfrak{u}(1) \oplus \mathfrak{u}(2) \oplus \mathfrak{u}(3)
]

------

# 6. Algebra Decomposition

Using:

[
\mathfrak{u}(n) =
\mathfrak{u}(1) \oplus \mathfrak{su}(n)
]

we obtain:

[
\mathfrak{g} =
\mathfrak{u}(1) \oplus
\mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus
\mathfrak{u}(1) \oplus \mathfrak{su}(3)
]

------

# 7. Reduction of Abelian Factors

Multiple (\mathfrak{u}(1)) factors lead to:

- redundant gauge fields
- unphysical charge duplication

Impose:

### (C5) Single charge constraint

Only one (\mathfrak{u}(1)) is retained.

------

# 8. Final Gauge Algebra

[
\boxed{
\mathfrak{g} =
\mathfrak{u}(1)\oplus \mathfrak{su}(2)\oplus \mathfrak{su}(3)
}
]

------

# 9. Interpretation

- (\mathfrak{u}(1)): abelian charge sector
- (\mathfrak{su}(2)): doublet structure
- (\mathfrak{su}(3)): triplet structure

------

# 10. Status of Result

## Established

- gauge algebra arises from commutant of (H_{\text{int}})
- decomposition follows from internal space structure

## Assumed

- minimality of decomposition
- single-charge constraint

------

# 11. Limitations

Not yet derived:

- why decomposition is exactly (1,2,3)
- fermion representation content
- coupling constants

------

# 12. Next Step

- derive structure of (H_{\text{int}})
- connect representation theory to physical particles
- derive coupling hierarchy

------

# 13. Summary

The Standard Model gauge algebra arises as the minimal compact symmetry algebra compatible with:

- internal decomposition of the projection generator
- commutant structure
- localisation
- charge consistency

------