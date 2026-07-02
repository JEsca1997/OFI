# OFI--Ruelle Discriminant Barrier Route for RH

## Purpose

This note records the selected RH route after the zero-locking investigation:

```math
\text{Riesz / Ruelle spectral pressure}
\Longrightarrow
\text{renormalized discriminant barrier}
\Longrightarrow
\text{no zero collision}
\Longrightarrow
\text{no complex escape}
\Longrightarrow
\mathrm{RH}.
```

This replaces the earlier tentative idea of a literal `1/12` charge jump at zero escape.  The charge-jump picture is dangerous because analytic deformation usually makes local zero data continuous through a double-zero collision.  The stronger and more natural target is therefore a collision barrier.

---

## De Bruijn heat-flow setting

Let

```math
\Xi_t(x)=e^{t\partial_x^2}\Xi_0(x)
```

be the de Bruijn deformation of the Riemann Xi function.

The known anchor is:

```math
\Xi_t\in LP \quad\text{for}\quad t\ge 1/2.
```

The goal is to prove:

```math
\Xi_t\in LP \quad\text{for}\quad 0\le t\le 1/2.
```

It is enough to rule out zero collisions while moving backward from `t=1/2` to `t=0`.

---

## Zero dynamics

For a finite zero system under the heat equation, the zeros satisfy the Dyson-type dynamics

```math
\dot z_k
=
2\sum_{j\ne k}\frac{1}{z_k-z_j}.
```

Near a collision of two zeros, set

```math
d=z_i-z_j.
```

The dominant pair interaction is

```math
\dot z_i\sim \frac{2}{d},
\qquad
\dot z_j\sim -\frac{2}{d},
```

hence

```math
\dot d\sim \frac{4}{d}.
```

Therefore

```math
\frac{d}{dt}\log d^2
=
2\frac{\dot d}{d}
\sim
\frac{8}{d^2}>0
```

forward in time.  Forward heat flow repels zeros away from collision; backward heat flow can drive them toward collision.  Hence RH requires a global lower barrier preventing the backward collision.

---

## Finite discriminant model

For a polynomial or finite truncation with zeros `z_i`, define

```math
\Delta(t)=\prod_{i<j}(z_i(t)-z_j(t))^2.
```

Then

```math
\log\Delta(t)=2\sum_{i<j}\log(z_i(t)-z_j(t)).
```

Differentiating gives

```math
\partial_t\log\Delta
=
2\sum_{i<j}\frac{\dot z_i-\dot z_j}{z_i-z_j}.
```

The local collision computation above shows that `log Delta` has the correct singular behavior: a collision corresponds to

```math
\Delta(t_*)=0,
\qquad
\log\Delta(t_*)=-\infty.
```

Thus the desired global theorem is not merely a monotonicity statement but a finite-pressure/noncollision statement.

---

## Infinite Xi discriminant

The Xi function has infinitely many zeros, so the discriminant must be renormalized.  The target object is an OFI-renormalized discriminant

```math
\Delta_{\mathrm{OFI}}(\Xi_t)
```

or equivalently an OFI--Ruelle pressure

```math
\mathcal P_{\mathrm{OFI}}(t)
=
-\log\Delta_{\mathrm{OFI}}(\Xi_t)
+
\frac{1}{12}\mathcal V(t),
```

where `V(t)` is the Bernoulli / Euler--Maclaurin / triangular vacuum subtraction required to make the infinite pair interaction finite.

The `1/12` term should be treated as a renormalization floor or vacuum subtraction, not as an instantaneous discontinuous jump at zero escape.

---

## Main theorem target

```math
\boxed{
\Delta_{\mathrm{OFI}}(\Xi_t)>0
\quad\text{for all}\quad
0\le t\le 1/2.
}
```

Equivalently:

```math
\boxed{
\mathcal P_{\mathrm{OFI}}(t)<\infty
\quad\text{for all}\quad
0\le t\le 1/2.
}
```

This is the OFI--Ruelle discriminant barrier.

---

## Why this implies zero-locking

Assume `Xi_{1/2} in LP` and suppose, for contradiction, that some zero leaves the real axis for a smaller time.

Because zeros of an analytic family move continuously, a nonreal conjugate pair must be born from a real collision at some first escape time `t_*`:

```math
z_i(t_*)=z_j(t_*).
```

Then the discriminant vanishes:

```math
\Delta_{\mathrm{OFI}}(\Xi_{t_*})=0.
```

But the discriminant barrier says

```math
\Delta_{\mathrm{OFI}}(\Xi_{t_*})>0.
```

Contradiction.

Therefore no complex escape occurs, and

```math
\Xi_t\in LP
\quad
(0\le t\le1/2).
```

In particular:

```math
\Xi_0\in LP,
```

which is RH.

---

## Ruelle interpretation

The pairwise logarithmic interaction

```math
-\sum_{i<j}\log |z_i-z_j|^2
```

is a Coulomb / free-energy / pressure term.  Ruelle thermodynamic formalism is the correct language for a global pressure barrier because it is designed to control weighted orbit/interaction sums through transfer operators and pressure.

The intended pressure form is schematic:

```math
\mathcal P_{\mathrm{OFI}}(t)
=
\operatorname{Pressure}_{\mathrm{Ruelle}}
\left(
-2\log|z_i-z_j| + \text{OFI vacuum subtraction}
\right).
```

The rigorous task is to define this pressure directly from Xi's zero set and the Riesz/OFI kernel, not merely from finite truncations.

---

## Lean4 abstraction target

The formal scaffold should isolate the hard theorem as follows:

```lean
axiom ofi_ruelle_discriminant_barrier :
  forall t : Real,
    t \in Set.Icc 0 (1/2 : Real) ->
    Delta_OFI (Xi t) > 0
```

Then zero-locking becomes:

```lean
theorem zero_locking_from_discriminant
    (t : Real)
    (ht : t \in Set.Icc 0 (1/2 : Real)) :
    InLaguerrePolya (Xi t) := by
  -- If not LP, then a first escape time gives collision.
  -- Collision implies Delta_OFI = 0.
  -- Barrier gives Delta_OFI > 0.
  -- Contradiction.
  sorry
```

The real mathematical work is to remove the axiom by proving the OFI--Ruelle pressure remains finite on `[0,1/2]`.

---

## Immediate proof obligations

1. Define `Delta_OFI(Xi_t)` as a renormalized infinite discriminant.
2. Prove finite truncations have the correct Dyson/discriminant derivative.
3. Prove the Bernoulli `1/12` vacuum subtraction cancels the divergent tail.
4. Express the renormalized interaction as a Ruelle pressure.
5. Prove pressure finiteness on `0 <= t <= 1/2`.
6. Prove pressure finiteness implies `Delta_OFI(Xi_t)>0`.
7. Prove any complex escape requires a prior real zero collision.

This is now the selected boss fight.
