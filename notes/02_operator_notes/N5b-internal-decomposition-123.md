# N5b Internal Decomposition 123 From Projection Generator

path: 02_operator_notes/N5b-Internal-Decomposition-123-from-Projection-Generator.md
folder: 02_operator_notes
filename: N5b-Internal-Decomposition-123-from-Projection-Generator.md
repository: DDF
type: research_note

# N5b — Internal Decomposition (1,2,3) from Projection Generator

## Status

Structural derivation (minimality + spectral constraints)

------

# 1. Purpose

Derive the internal decomposition:

[
\mathcal{H}_{\text{int}} =
\mathbb{C}^1 \oplus \mathbb{C}^2 \oplus \mathbb{C}^3
]

from properties of the projection generator (L).

------

# 2. Starting Point

From N5:

[
L = D \otimes \mathbf{1} + \mathbf{1} \otimes H_{\text{int}}
]

with:

[
H_{\text{int}} = H_{\text{int}}^\dagger
]

------

# 3. Spectral Decomposition

By the spectral theorem:

[
H_{\text{int}} =
\bigoplus_i \lambda_i I_{n_i}
]

Thus:

[
\mathcal{H}_{\text{int}} =
\bigoplus_i \mathbb{C}^{n_i}
]

------

# 4. Structural Constraints

We impose:

### (C1) Non-trivial symmetry

At least one (n_i \ge 2)

### (C2) Scalar sector

At least one (n_i = 1)

### (C3) Multiple interaction sectors

At least two distinct non-abelian blocks

### (C4) Irreducibility

Blocks are minimal invariant subspaces

### (C5) Minimality

Choose smallest structure satisfying all constraints

------

# 5. Candidate Decompositions

| Structure | Issue                             |
| --------- | --------------------------------- |
| (1,1,1)   | purely abelian                    |
| (1,2)     | insufficient interaction richness |
| (2,3)     | missing scalar sector             |
| (1,2,2)   | redundant symmetry                |
| (1,3,3)   | non-minimal                       |

------

# 6. Minimal Valid Structure

The smallest decomposition satisfying all constraints is:

[
(1,2,3)
]

Thus:

[
\mathcal{H}_{\text{int}} =
\mathbb{C}^1 \oplus \mathbb{C}^2 \oplus \mathbb{C}^3
]

------

# 7. Resulting Gauge Algebra

From N5:

[
\mathfrak{g} =
\mathfrak{u}(1)\oplus \mathfrak{su}(2)\oplus \mathfrak{su}(3)
]

------

# 8. Interpretation

- (1): scalar / charge sector
- (2): doublet structure
- (3): triplet structure

------

# 9. Status of Result

## Established

- decomposition follows from spectral structure
- minimality selects (1,2,3)

## Assumed

- minimality principle
- irreducibility constraints

------

# 10. Limitations

Not yet derived:

- uniqueness of (1,2,3)
- fermion representations
- coupling constants

------

# 11. Summary

The internal structure of the projection generator admits a minimal decomposition:

[
(1,2,3)
]

which produces the Standard Model gauge algebra via the commutant construction.

------