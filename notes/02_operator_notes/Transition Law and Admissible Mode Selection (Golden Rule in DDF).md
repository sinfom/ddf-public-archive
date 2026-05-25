# Transition Law and Admissible Mode Selection (Golden Rule in DDF)

## Purpose
To reinterpret transition rates using admissibility constraints.

---

## 1. Standard Transition Law

Fermi’s Golden Rule:

    Γ ∝ |⟨m|V|n⟩|² ρ(ω)

---

## 2. DDF Reformulation

Define admissible density:

    ρ_adm(ω) = ρ(ω) χ_adm(ω)

where:
- χ_adm = 1 if mode is admissible
- χ_adm = 0 otherwise

---

## 3. Transition Law (DDF Form)

    Γ_DDF ∝ |⟨ψ_m, Vψ_n⟩|² ρ_adm(Δω)

---

## 4. Interpretation

Transition requires:

1. Non-zero coupling:
   ⟨ψ_m, Vψ_n⟩ ≠ 0

2. Admissible output mode:
   ρ_adm(Δω) > 0

---

## 5. Selection Rules

Standard selection rules become:

> admissibility constraints on coupling

---

## 6. Forbidden Transitions

A transition is forbidden if:

- coupling = 0
- OR output mode is non-admissible

---

## 7. Spontaneous Emission

    Γ_sp ∝ |⟨m|V_vac|n⟩|² ρ_adm(ω)

Vacuum provides perturbation, admissibility selects outcome.

---

## 8. Summary

- Transition = coupling + admissible channel
- Emission = admissibility restoration
- Selection = admissibility filtering