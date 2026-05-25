# N Mass As Spectral Gap Core Derivation

path: 04_action_principle/N-Mass-as-Spectral-Gap-Core-Derivation.md
folder: 04_action_principle
filename: N-Mass-as-Spectral-Gap-Core-Derivation.md
repository: DDF
type: research_note

# N — Mass as Spectral Gap (Core Derivation)

## Dependency chain

admissibility  
→ propagation cone  
→ principal symbol  
→ wave operator  
→ mass operator  
→ spectral gap  
→ mass  
→ rest energy  

---

## Section 1 — Setup

### Definition — Wave operator
\[
\Box := \partial_t^2 - c^2 \nabla^2
\]

### Definition — Mass operator
\[
K := -\Box
\]

---

## Section 2 — Symbol

### Lemma — Cone symbol
\[
\sigma(\omega,k) = \omega^2 - c^2 |k|^2
\]

### Lemma — Operator realisation
\[
\sigma(\omega,k) \Rightarrow \Box
\]

---

## Section 3 — Positivity

### Statement
For admissible states:

\[
|\omega| \le c|k|
\]

so

\[
c^2|k|^2 - \omega^2 \ge 0
\]

### Quadratic form
\[
\langle \psi,K\psi\rangle
=
\int (c^2|k|^2 - \omega^2)\,|\hat\psi|^2 \ge 0
\]

---

## Section 4 — Spectral split

### Null sector
\[
\langle \psi,K\psi\rangle = 0
\]

→ support on

\[
c^2|k|^2 - \omega^2 = 0
\]

---

### Positive sector
\[
\langle \psi,K\psi\rangle > 0
\]

→ support where

\[
c^2|k|^2 - \omega^2 > 0
\]

---

## Section 5 — Spectral gap

### Definition
\[
\mu^2[\psi]
=
\frac{\langle \psi,K\psi\rangle}{\langle \psi,\psi\rangle}
\]

### Classification
\[
\mu^2 = 0 \;\text{(null)}, \quad \mu^2 > 0 \;\text{(massive)}
\]

---

## Section 6 — Mass

### Definition
\[
m = \frac{\hbar}{c^2}\mu
\]

\[
m^2 = \frac{\hbar^2}{c^4}\mu^2
\]

### General form
\[
m^2[\psi]
=
\frac{\hbar^2}{c^4}
\frac{\langle \psi,K\psi\rangle}{\langle \psi,\psi\rangle}
\]

---

## Section 7 — Rest energy

### Energy
\[
E = \hbar \omega
\]

### Rest condition
\[
k = 0
\]

### Identification
\[
\omega_0 = \mu
\]

### Result
\[
E_0 = mc^2
\]

---

## Section 8 — Dirac formulation

### Factorisation
\[
D^2 = \Box
\]

### Mass operator
\[
K = -D^2
\]

### First-order equation
\[
(D - \mu)\psi = 0
\]

---

## Final result

\[
m = \frac{\hbar}{c^2}\mu
\]

Mass is the spectral gap of the propagation operator.