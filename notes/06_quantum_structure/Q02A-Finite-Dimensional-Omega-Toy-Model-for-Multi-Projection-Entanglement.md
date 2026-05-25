# QM EXT 002A Finite Dimensional Omega Toy Model For Multi Projection Entanglement

path: 06_quantum_structure/QM-EXT-002A-Finite-Dimensional-Omega-Toy-Model-for-Multi-Projection-Entanglement.md
folder: 06_quantum_structure
filename: QM-EXT-002A-Finite-Dimensional-Omega-Toy-Model-for-Multi-Projection-Entanglement.md
repository: DDF
type: research_note

# Note ID
DDF-QM-EXT-002A

# Title
Finite-Dimensional \(\Omega\) Toy Model for Multi-Projection Entanglement

# Folder
06_quantum_structure/entanglement_projection/

# Status
Active mathematical development

# Version
v0.1

# Date
2026-03-15

# Depends On
- DDF-QM-EXT-002
- 01_foundations F1–F4
- 02_operator_notes (Dirac factorisation, spin)

# Establishes
- A concrete finite-dimensional toy model for the generative domain \(\Omega\).
- Explicit projection operators \(P_A^{(1)}, P_B^{(1)}, P^{(2)}\) that map a single generative state to an entangled Bell state in \(U\).

# Excludes
- Bell inequality violations (deferred to 002B).
- Derivation of the full infinite-dimensional fibre bundle.

---

## 1. Setup and Hilbert spaces

To demonstrate multi-projection entanglement from a single generative configuration without postulating superluminal influences in \(U\), we construct a minimal finite-dimensional model.

We define the generative domain \(\Omega\) as a four-dimensional complex vector space:
$$
\Omega \cong \mathbb{C}^4
$$
In the observable universe \(U\), we consider two local subsystems A and B, each modelled by a two-dimensional Hilbert space (e.g., spin-\(1/2\) particles):
$$
\mathcal{H}_A \cong \mathcal{H}_B \cong \mathbb{C}^2
$$
The joint two-body state space in \(U\) is constructed via the standard tensor product:
$$
\mathcal{H}_U^{(2)} = \mathcal{H}_A \otimes \mathcal{H}_B \cong \mathbb{C}^4
$$

---

## 2. Definition of projections

We require a single generative state \(\Psi_\Omega \in \Omega\) to project into a maximally entangled state in \(\mathcal{H}_U^{(2)}\). Let \(\{ |e_i\rangle \}_{i=1}^4\) be the computational basis for \(\Omega\), and \(\{ |00\rangle, |01\rangle, |10\rangle, |11\rangle \}\) be the standard basis for \(\mathcal{H}_U^{(2)}\).

We define the joint projection \(P^{(2)}: \Omega \to \mathcal{H}_U^{(2)}\) simply as the identity isomorphism:
$$
P^{(2)} = \sum_{i,j \in \{0,1\}} |ij\rangle \langle e_{2i+j+1}|
$$
Now, choose a specific generative state:
$$
\Psi_\Omega = \frac{1}{\sqrt{2}} \left( |e_1\rangle + |e_4\rangle \right)
$$
Applying the joint projection yields a standard Bell state in \(U\):
$$
\psi_U^{(2)} = P^{(2)}(\Psi_\Omega) = \frac{1}{\sqrt{2}} \left( |00\rangle + |11\rangle \right) = |\Phi^+\rangle
$$

The single-body marginal projections \(P_A^{(1)}\) and \(P_B^{(1)}\) map \(\Psi_\Omega\) to the local effective states in A and B. They are defined via the partial trace over the joint projection:
$$
\rho_A = P_A^{(1)}(\Psi_\Omega) = \mathrm{Tr}_B \left( |\psi_U^{(2)}\rangle\langle \psi_U^{(2)}| \right) = \frac{1}{2}I_A
$$
$$
\rho_B = P_B^{(1)}(\Psi_\Omega) = \mathrm{Tr}_A \left( |\psi_U^{(2)}\rangle\langle \psi_U^{(2)}| \right) = \frac{1}{2}I_B
$$
Thus, the single generative state \(\Psi_\Omega\) produces maximally mixed local marginals but a perfectly correlated joint state.

---

## 3. Admissibility and joint region \(\mathcal{A}_\Omega^{(2)}\)

In the DDF framework, not all states in \(\Omega\) map to physically realizable particle configurations in \(U\). The subset of \(\Omega\) that yields valid multi-body projections is the admissible region \(\mathcal{A}_\Omega^{(2)}\).

In this toy model, \(\mathcal{A}_\Omega^{(2)}\) is constrained to the subspace of \(\Omega\) that maps to antisymmetric (fermionic) or symmetric (bosonic) states under \(P^{(2)}\), reflecting the topological constraints from `F6-fermionic_and_bosonic_sectors`. The non-factorised geometry of \(\mathcal{A}_\Omega^{(2)}\) ensures that \(P^{(2)}(\Psi_\Omega) \neq P_A^{(1)}(\Psi_\Omega) \otimes P_B^{(1)}(\Psi_\Omega)\).

---

## 4. Open questions

1. How do spin measurement settings \(a\) and \(b\) interact with the marginal projections \(P_A^{(1)}\) and \(P_B^{(1)}\)?
2. Does the non-factorised geometry of \(\mathcal{A}_\Omega^{(2)}\) naturally lead to Bell inequality violations without non-local signalling?
3. How is the distribution measure \(\mu\) over \(\Omega\) defined to reproduce Born rule probabilities?

*(These questions are addressed in Note DDF-QM-EXT-002B).*

---

## 5. Next step

- Derive Bell correlations \(\mathbb{P}(x,y \mid a,b)\) for spin measurements using this toy model (002B).
- Formally verify that \(\sum_y \mathbb{P}(x,y \mid a,b)\) is independent of \(b\) (no-signalling constraint).