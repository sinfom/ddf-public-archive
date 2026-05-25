# QM EXT 002B Bell Correlations And No Signalling

path: 06_quantum_structure/QM-EXT-002B-bell-correlations-and-no-signalling.md
folder: 06_quantum_structure
filename: QM-EXT-002B-bell-correlations-and-no-signalling.md
repository: DDF
type: research_note

# Note ID
DDF-QM-EXT-002B

# Title
Bell Correlations and No-Signalling in Multi-Projection Entanglement

# Folder
06_quantum_structure/entanglement_projection/

# Status
Active mathematical development

# Version
v0.1

# Date
2026-03-15

# Depends On
- DDF-QM-EXT-002A
- DDF-QM-EXT-002

# Establishes
- Calculation of CHSH correlations \(E(a,b)\) from the DDF finite-dimensional toy model.
- Explicit verification of the no-signalling constraint on marginal projections.
- Clarification that \(\Psi_\Omega\) is not a classical local hidden variable, but a quantum generative state.

# Excludes
- Generalisation to curved spacetimes (Gravity limit).

---

## 1. Measurement settings and outcome maps

Using the toy model from Note DDF-QM-EXT-002A, we define spin measurement settings \(a, a'\) for subsystem A and \(b, b'\) for subsystem B as unit vectors in \(\mathbb{R}^3\). These correspond to local Hermitian observables \(\sigma \cdot a\) and \(\sigma \cdot b\) on \(\mathcal{H}_A\) and \(\mathcal{H}_B\).

The outcome maps for local measurements on the projected states take values \(x, y \in \{-1, +1\}\). In the DDF ontology, the joint probability distribution is given by the Born rule applied to the joint projection:
$$
\mathbb{P}(x,y \mid a,b) = \mathrm{Tr}\left( \left( \Pi_A^x(a) \otimes \Pi_B^y(b) \right) P^{(2)}(\Psi_\Omega) \langle P^{(2)}(\Psi_\Omega) | \right)
$$
where \(\Pi_A^x(a) = \frac{1}{2}(I + x \, \sigma \cdot a)\) and \(\Pi_B^y(b) = \frac{1}{2}(I + y \, \sigma \cdot b)\) are local projection operators representing measurement settings.

---

## 2. Bell correlations

For the generative state \(\Psi_\Omega\) that projects to the Bell state \(|\Phi^+\rangle\), the joint probability evaluates to:
$$
\mathbb{P}(x,y \mid a,b) = \frac{1}{4} \left( 1 + x y (a_z b_z - a_x b_x - a_y b_y) \right)
$$
The correlation function \(E(a,b) = \sum_{x,y} x y \, \mathbb{P}(x,y \mid a,b)\) yields the standard quantum mechanical prediction. By choosing the standard CHSH angles (e.g., \(a\) and \(a'\) along the Z and X axes; \(b\) and \(b'\) at \(\pm \pi/4\) in the XZ plane), we evaluate the CHSH parameter:
$$
S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')| = 2\sqrt{2}
$$
The violation of the classical Bell bound (\(S \le 2\)) occurs because the joint projection \(P^{(2)}(\Psi_\Omega)\) over the admissible region \(\mathcal{A}_\Omega^{(2)}\) does not factorise into independent states. The structural property of \(\Omega\) responsible for this is the holistic mapping of a single generative vector into a non-separable tensor product structure.

---

## 3. No-signalling check

A critical constraint of the DDF framework is that multi-projection must not violate causality (propagation rigidity) in \(U\). This requires the marginal probability at A to be independent of the choice of measurement setting \(b\) at B. 

We sum over the outcomes \(y\) at B:
$$
\sum_{y \in \{-1, 1\}} \mathbb{P}(x,y \mid a,b) = \sum_y \mathrm{Tr}\left( \left( \Pi_A^x(a) \otimes \Pi_B^y(b) \right) |\psi_U^{(2)}\rangle\langle\psi_U^{(2)}| \right)
$$
Since \(\sum_y \Pi_B^y(b) = I_B\), this simplifies to:
$$
\mathbb{P}(x \mid a,b) = \mathrm{Tr}_A\left( \Pi_A^x(a) \, \mathrm{Tr}_B(|\psi_U^{(2)}\rangle\langle\psi_U^{(2)}|) \right) = \mathrm{Tr}_A\left( \Pi_A^x(a) \rho_A \right)
$$
Because \(\rho_A = P_A^{(1)}(\Psi_\Omega) = \frac{1}{2}I_A\), the marginal probability is:
$$
\mathbb{P}(x \mid a) = \frac{1}{2}
$$
This demonstrates explicitly that \(\mathbb{P}(x \mid a,b) = \mathbb{P}(x \mid a)\), confirming that the choice of \(b\) has no statistical influence on the outcomes at A. The no-signalling condition is structurally enforced by the compatibility of the marginal projections \(P_A^{(1)}\) and the joint projection \(P^{(2)}\).

---

## 4. Relation to Bell-local hidden variables

In standard interpretations, a local hidden variable \(\lambda\) must satisfy \(\mathbb{P}(x,y \mid a,b, \lambda) = \mathbb{P}(x \mid a, \lambda)\mathbb{P}(y \mid b, \lambda)\). 

If we attempt to treat \(\Psi_\Omega\) as a classical hidden variable, the non-factorisability of \(P^{(2)}(\Psi_\Omega)\) means that \(\Psi_\Omega\) fails the factorisation condition. Therefore, \(\Psi_\Omega\) acts as a Bell-nonlocal generative state. However, because \(\Psi_\Omega\) resides in the generative domain \(\Omega\) and all interactions in \(U\) strictly obey the propagation cone, this non-locality is purely kinematical (geometric constraints on multi-projection) rather than dynamical (superluminal signaling in \(U\)).

---

## 5. Next step

- Integrate this geometric non-factorisability with the fibre bundle structure (DDF-QM-EXT-003) to show how degeneracy labels encode joint projection branches.
- Map the admissible region \(\mathcal{A}_\Omega^{(2)}\) onto product phase space using the Dirac null cone framework (DDF-QM-EXT-004).