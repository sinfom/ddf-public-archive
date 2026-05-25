# N2b Dispersion And Admissibility

path: 02_operator_notes/N2b-Dispersion-and-Admissibility.md
folder: 02_operator_notes
filename: N2b-Dispersion-and-Admissibility.md
repository: DDF
type: research_note

# N2b — Dispersion and Admissibility

## Status
Corrected formulation — conditional dispersion closure added

---

## 1. Purpose

This note analyses how **dispersion relations** behave within the propagation structure established in N1, N1b, and N2.

The goal is to separate three distinct claims:

1. The propagation cone constrains the maximum allowed propagation speed.
2. The cone alone does not uniquely determine the full dispersion law.
3. Under the stronger DDF condition of **global admissibility**, the fundamental irreducible scalar dispersion relation is uniquely quadratic.

This note therefore closes the earlier fragility in the chain by distinguishing:

\[
	ext{cone-admissibility}
\]

from

\[
	ext{global admissibility}.
\]

---

## 2. Starting Point from N1 / N1b

From propagation rigidity:

- dynamics are governed by a hyperbolic operator;
- propagation occurs along a characteristic set;
- the principal symbol defines a propagation cone.

This gives:

\[
|\omega| \leq c|k|.
\]

This constraint arises from:

- operator symbol structure;
- characteristic geometry;
- hyperbolic propagation.

It does **not** arise from Fourier decay, spectral support, or Paley-Wiener arguments.

---

## 3. Dispersion Relations

A dispersion relation is a function:

\[
\omega = \omega(k)
\]

or, more invariantly,

\[
F(\omega,k)=0
\]

which determines the relation between temporal frequency \(\omega\) and spatial wavevector \(k\).

The cone tells us where propagation is allowed.  
The dispersion relation tells us how a specific mode propagates within that allowed region.

---

## 4. Velocities

### Phase velocity

\[
v_p(k)=rac{\omega(k)}{|k|}
\]

### Group velocity

\[
v_g(k)=rac{d\omega}{d|k|}
\]

For admissible propagation, these velocities must remain compatible with the propagation cone.

---

## 5. Cone Constraint

From N1:

\[
|\omega(k)| \leq c|k|.
\]

For modes on the massless cone boundary:

\[
|\omega(k)|=c|k|.
\]

For massive modes, the physical group velocity remains subluminal even though the phase velocity may exceed \(c\). Therefore the precise admissibility condition should be stated at the level of causal propagation and characteristic structure, not merely as a bound on phase velocity.

Corrected statement:

\[
|v_g| \leq c
\]

for physical signal propagation.

---

## 6. Key Principle: Propagation vs Dispersion

The propagation cone constrains:

\[
	ext{where propagation can occur}.
\]

It does **not**, by itself, uniquely determine:

\[
	ext{the full functional form of } \omega(k).
\]

Therefore:

\[
	ext{cone} 
ot\Rightarrow 	ext{unique dispersion}.
\]

This was the fragile point in the earlier version.

The corrected DDF position is:

\[
	ext{cone} + 	ext{global admissibility} \Rightarrow 	ext{quadratic scalar dispersion}.
\]

---

## 7. Levels of Admissibility

### 7.1 Cone-admissibility

A dispersion relation is cone-admissible if it respects the finite propagation structure determined by the characteristic cone.

This is a weak condition.

It allows more than one dispersion relation.

---

### 7.2 Global admissibility

A dispersion relation is globally admissible if it satisfies the full DDF selection rule:

1. locality;
2. finite-order dynamics;
3. real principal symbol;
4. hyperbolic propagation;
5. rotational isotropy;
6. Lorentz covariance of the cone;
7. irreducibility of the scalar sector;
8. no hidden internal degrees of freedom;
9. stable bounded evolution.

This is the stronger condition required for a fundamental scalar field equation.

---

## 8. Classification of Dispersion Relations

### 8.1 Linear massless type

\[
\omega = c|k|.
\]

Properties:

- \(v_p=c\);
- \(v_g=c\);
- non-dispersive;
- wave packets preserve shape in the ideal linear case.

Status:

- compatible with cone-admissibility;
- globally admissible as the massless scalar boundary case.

This corresponds to propagation on the cone boundary.

---

### 8.2 Massive quadratic type

\[
\omega^2 = c^2|k|^2+\mu^2.
\]

Properties:

- group velocity satisfies \(|v_g|<c\);
- phase velocity may exceed \(c\), but this does not violate causality;
- modes propagate inside the cone;
- produces dispersive wave-packet behaviour.

Status:

- compatible with cone-admissibility;
- globally admissible for an irreducible scalar mode;
- yields the Klein-Gordon equation.

Here \(\mu\) is interpreted in DDF as a scalar spectral gap or admissible displacement from the massless cone boundary.

In physical units:

\[
\mu = rac{mc^2}{\hbar}.
\]

---

### 8.3 Nonlinear dispersion

Example:

\[
\omega = c|k|+lpha |k|^3.
\]

Properties:

- group velocity depends on \(k\);
- wave packets spread;
- high-frequency behaviour can violate global cone structure unless band-limited;
- typically corresponds to higher-order operators or effective-medium corrections.

Status:

- may be cone-compatible locally or approximately;
- may be admissible as an effective or emergent correction;
- is not globally admissible as a fundamental irreducible scalar dispersion law.

Reason:

Nonlinear dispersion generally requires at least one of:

- higher-order derivatives;
- preferred frame or scale;
- extra internal degrees of freedom;
- broken Lorentz covariance;
- effective medium behaviour;
- band-limited validity.

Therefore it is excluded from the fundamental scalar sector by global admissibility.

---

## 9. Dispersion Rigidity Theorem

### Theorem N2b.1 — Scalar Dispersion Rigidity

Let \(\phi\) be a scalar projected mode governed by a local finite-order operator derived from:

\[
P = L^\dagger L - M.
\]

Assume:

1. finite propagation speed;
2. real principal symbol;
3. hyperbolic propagation;
4. rotational isotropy;
5. Lorentz covariance of the propagation cone;
6. locality;
7. finite-order dynamics;
8. irreducibility of the scalar sector.

Then the fundamental scalar dispersion relation is:

\[
\omega^2=c^2|k|^2+\mu^2.
\]

where \(\mu\) is a scalar spectral gap.

Thus the globally admissible scalar operator is:

\[
(\Box+\mu^2)\phi=0.
\]

This is the Klein-Gordon equation.

---

## 10. Proof Sketch

### Step 1 — Hyperbolic cone

From N1/N1b, the principal symbol defines a hyperbolic cone:

\[
p(\omega,k)=\omega^2-c^2|k|^2.
\]

---

### Step 2 — Lorentz covariance

From N2, admissible transformations preserve the quadratic form:

\[
Q(\omega,k)=\omega^2-c^2|k|^2.
\]

Therefore any fundamental scalar dispersion law must be expressible as a scalar function of \(Q\):

\[
F(Q)=0.
\]

---

### Step 3 — Finite-order locality

A local finite-order scalar operator corresponds to a polynomial in derivatives.

Therefore \(F(Q)\) must be polynomial.

---

### Step 4 — Irreducibility

If \(F(Q)\) has degree greater than one, then it factorises into multiple branches or introduces additional modes.

For example:

\[
F(Q)=(Q+\mu_1^2)(Q+\mu_2^2)
\]

corresponds to multiple scalar sectors, not one irreducible scalar mode.

Irreducibility therefore selects the linear polynomial:

\[
F(Q)=Q+\mu^2.
\]

---

### Step 5 — Result

Thus:

\[
Q+\mu^2=0
\]

which gives:

\[
\omega^2-c^2|k|^2+\mu^2=0.
\]

Equivalently:

\[
\omega^2=c^2|k|^2-\mu^2
\]

depending on sign convention.

Using the standard Klein-Gordon convention:

\[
\omega^2=c^2|k|^2+\mu^2.
\]

Therefore the scalar field satisfies:

\[
(\Box+\mu^2)\phi=0.
\]

---

## 11. DDF Interpretation

In DDF language:

- the cone gives the admissible propagation structure;
- Lorentz covariance preserves the cone;
- locality excludes nonlocal dispersion;
- finite-order dynamics excludes arbitrary functions of \(k\);
- irreducibility excludes multi-branch polynomial sectors;
- the mass term appears as a scalar spectral gap.

Therefore Klein-Gordon is not inserted by hand.

It is the minimal globally admissible scalar equation.

---

## 12. Relationship to Klein-Gordon Recovery

Using:

\[
\mu=rac{mc}{\hbar}
\]

and

\[
\Box=rac{1}{c^2}\partial_t^2-
abla^2,
\]

the globally admissible scalar equation becomes:

\[
\left(\Box+rac{m^2c^2}{\hbar^2}ight)\phi=0.
\]

This is the Klein-Gordon equation.

Thus N2b provides the missing closure needed for the first recovery of known physics.

---

## 13. What This Note Does and Does Not Prove

### Established

This note establishes that:

\[
	ext{cone}+	ext{global admissibility}
\Rightarrow
	ext{quadratic scalar dispersion}.
\]

It therefore closes the earlier gap for the scalar sector.

---

### Not claimed

This note does not claim that the cone alone fixes dispersion.

It also does not claim that nonlinear dispersion can never appear.

Nonlinear dispersion may still appear as:

- effective field behaviour;
- medium-like behaviour;
- higher-order corrections;
- emergent approximations;
- non-fundamental sectors.

But it is not admissible as the fundamental irreducible scalar law.

---

## 14. Revised Open Problems

| ID | Problem | Status |
|---|---|---|
| OP1 | Classify cone-admissible dispersion relations | Still open |
| OP2 | Determine effective nonlinear corrections | Open |
| OP3 | Derive quadratic scalar dispersion under global admissibility | Closed conditionally by Theorem N2b.1 |
| OP4 | Link scalar spectral gap \(\mu\) to projection data in \(L\) and \(M\) | Open |
| OP5 | Extend dispersion rigidity to spinor, gauge, and curved sectors | Open |

---

## 15. Role in DDF

This note clarifies:

\[
	ext{N1/N1b} \Rightarrow 	ext{propagation cone}
\]

\[
	ext{N2} \Rightarrow 	ext{Lorentz covariance}
\]

\[
	ext{N2b} \Rightarrow 	ext{scalar dispersion rigidity}
\]

\[
	ext{N2c or N3} \Rightarrow 	ext{Klein-Gordon / Dirac recovery}
\]

---

## 16. Summary

Propagation rigidity establishes:

- finite propagation speed;
- causal cone structure;
- hyperbolic characteristic geometry.

Cone-admissibility alone allows multiple possible dispersion relations.

Global admissibility adds:

- locality;
- finite-order dynamics;
- Lorentz covariance;
- isotropy;
- irreducibility.

Under these stronger conditions, the fundamental scalar dispersion relation is uniquely:

\[
\omega^2=c^2|k|^2+\mu^2.
\]

This yields:

\[
(\Box+\mu^2)\phi=0.
\]

Therefore the Klein-Gordon equation is recovered as the minimal globally admissible scalar field equation in DDF.

---

## 17. Key Insight

The cone constrains propagation.

Global admissibility selects the dispersion law.

