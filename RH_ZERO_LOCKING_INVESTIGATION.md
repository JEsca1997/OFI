# RH Zero-Locking Investigation

## Purpose

This note records the current proof-engineering decision for the Riemann Hypothesis route through OFI.  It is meant to separate what is already structurally useful from what still requires a proof-level derivation.

The current target is not to restate RH directly.  The target is the zero-locking implication:

```math
E_{\mathrm{OFI}}(f)=0 \quad\Longrightarrow\quad f\in LP,
```

for even real entire functions of Xi type, where `LP` denotes the Laguerre--Polya class.

Equivalently, the missing positive-defect lemma is:

```math
\text{nonreal zero of }f \quad\Longrightarrow\quad E_{\mathrm{OFI}}(f)>0.
```

Once this implication is proved and conserved along the de Bruijn heat flow, the backward descent closes:

```math
\Xi_{1/2}\in LP,
\qquad
E_{\mathrm{OFI}}(\Xi_t)=E_{\mathrm{OFI}}(\Xi_{1/2})=0,
\qquad
0\le t\le 1/2,
```

hence

```math
\Xi_t\in LP \quad (0\le t\le 1/2),
```

and in particular `Xi_0 in LP`, which is RH.

---

## Operator decision

For the RH-facing proof, the preferred primary operator stack is:

```math
\text{Riesz potential / fractional Laplacian}
\quad+\quad
\text{Ruelle / thermodynamic formalism when a spectral monotone is needed}.
```

Caputo and Riemann--Liouville remain useful as coordinate or boundary-realization operators, but they should not be treated as superior to the Riesz/Ruelle route for RH zero geometry.

Reason:

- The Riesz potential is Fourier-native and isotropic.
- The de Bruijn/Newman flow is heat-kernel/spectral in nature.
- The Laguerre--Polya problem is global zero geometry, not an initial-value boundary problem.
- Ruelle-style transfer operators are plausible candidates for spectral positivity or monotonicity.
- Caputo/Riemann--Liouville are still valuable, but they introduce boundary-directional data that does not automatically encode the global zero set of `Xi`.

Thus the RH proof should use Riesz/Ruelle as the core and treat Caputo/Riemann--Liouville as auxiliary realizations unless a specific theorem requires them.

---

## Important algebra erratum in the kinetic-symbol derivation

The current kinetic-symbol derivation contains a point that should be corrected before it is used downstream.

The text computes the OFI-filtered kinetic integrand as

```math
|p|^k\,|p|^{-\alpha}\,|p|^{-\alpha}
=|p|^{k-2\alpha}.
```

It then states that equality with the original kinetic term `|p|^k` implies

```math
\alpha=k/2.
```

But the displayed equality

```math
k-2\alpha=k
```

actually implies

```math
\alpha=0.
```

Therefore the present argument does **not** prove the stated kinetic-symbol principle as written.

A corrected version must change the fixed-point condition.  Possible repairs include:

1. Compare the filtered kinetic order to a normalized vacuum/order-zero sector rather than to the original order `k`.
2. Define `alpha=k/2` as the order that half-integrates each side of a quadratic kinetic bilinear down to a balanced order-zero density.
3. Recast the condition as a square-root factorization of the kinetic symbol:

```math
|p|^k = |p|^{k/2}\,|p|^{k/2},
```

so the natural OFI order is the half-order of the kinetic operator, not the solution of `k-2 alpha = k`.

Until this is repaired, the RH zero-locking path should not rely on the kinetic-symbol theorem.

---

## Current RH proof skeleton

Use the de Bruijn heat-flow family:

```math
\Xi_t=e^{t\partial_x^2}\Xi_0.
```

Known/deployed anchor:

```math
\Xi_t\in LP \quad\text{for}\quad t\ge 1/2.
```

Needed conservation:

```math
\partial_t E_{\mathrm{OFI}}(\Xi_t)=0,
\qquad 0\le t\le 1/2.
```

Needed zero-locking:

```math
E_{\mathrm{OFI}}(\Xi_t)=0
\quad\Longrightarrow\quad
\Xi_t\in LP.
```

Then:

```math
\Xi_{1/2}\in LP
\Rightarrow
E_{\mathrm{OFI}}(\Xi_{1/2})=0
\Rightarrow
E_{\mathrm{OFI}}(\Xi_t)=0
\Rightarrow
\Xi_t\in LP
\Rightarrow
\Xi_0\in LP.
```

---

## Positive-defect target

The concrete missing theorem is:

```math
\boxed{
\text{If }f\text{ is even real entire of Xi type and has a nonreal zero, then }
E_{\mathrm{OFI}}(f)>0.
}
```

A nonreal zero appears with the quartet

```math
\{\rho,\overline{\rho},-\rho,-\overline{\rho}\}.
```

The local escaping-pair factor is

```math
(x-a-ib)(x-a+ib)=(x-a)^2+b^2,
\qquad b\ne0.
```

A real collision has `b=0`; off-axis escape has `b^2>0`.  Therefore the desired spectral defect should detect the positive transverse term `b^2`.

A future formula may have the schematic form

```math
E_{\mathrm{OFI}}(f)
=
\sum_{\operatorname{Im}\rho>0}
W_{\mathrm{OFI}}(\rho),
\qquad
W_{\mathrm{OFI}}(\rho)>0\text{ if }\operatorname{Im}\rho\ne0.
```

The role of Gudermannian / Wronskian / spline / moonshine / Ricci-flow structures should be to prove positivity of this weight, not to replace the zero-locking lemma.

---

## Lean4 abstraction target

The Lean formalization should begin with the abstract theorem rather than the full analytic proof:

```lean
axiom off_axis_positive_defect :
  forall f : EntireFunction,
    EvenEntire f ->
    HasNonrealZero f ->
    E_OFI f > 0
```

Everything else can then be scaffolded cleanly.  The real mathematical work is to remove this axiom by proving the spectral defect formula from explicit OFI/Riesz/Ruelle definitions.

---

## Next task

Derive or locate an explicit formula for `E_OFI` such that:

1. `E_OFI` is conserved under the de Bruijn heat flow on `0 <= t <= 1/2`.
2. `E_OFI(f)=0` for Laguerre--Polya functions of Xi type.
3. Every nonreal zero contributes a strictly positive weight.

Until all three are proved, the RH proof remains a structured reduction, not a completed proof.
