# T17: Far Minor-Arc Fourier-Coefficient Gate

**Status:** exact pointwise target and Type-I/II reduction; no far-minor-arc cancellation estimate is claimed.  
**Purpose:** state the final analytic obstruction after the small-denominator major arcs and transition bands have been isolated.

---

## 1. Far minor arcs

Let
\[
\mathfrak F
:=
\mathbb T\setminus
\left(
\mathfrak M(Q_0,W;N)
\cup
\bigcup_{Q_0<R\le Q_1}\mathfrak T(R;W,N)
\right),
\]
where \(Q_0=(\log N)^B\), the union is over dyadic transition bands, and \(Q_1\le N^\vartheta\).

For a sector \(j\in\{0,2,4\}\), define the Fejér-weighted far-minor coefficient
\[
\mathcal I^{\mathfrak F}_{j,K}(E)
:=
\int_{\mathfrak F}
\Omega_K(\alpha)
T_{\sigma_j,N}(\alpha)T_{\tau_j,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

This is an individual Fourier coefficient of a restricted product. It is the pointwise P1 quantity.

---

## 2. The exact sufficient far-minor theorem

Assign a remaining positive major-term allowance \(\rho_{\mathfrak F}c_jN\), after the small-major and transition ledgers have been paid. A sufficient theorem is
\[
\boxed{
\sup_{\substack{E\asymp N\\E\equiv j\,({\rm mod}\,6)}}
\left|
\mathcal I^{\mathfrak F}_{j,K}(E)
\right|
\le\rho_{\mathfrak F}c_jN,
\qquad 0<\rho_{\mathfrak F}<1.
}
\]

Together with the T13 major lower bound and the T16 transition budget, this would give positivity of the **Fejér-windowed Mangoldt coefficient**.

It would still not complete unwindowed Goldbach because the T9 descent gate remains separate.

---

## 3. Why global \(L^2\) is not enough

The elementary estimate gives
\[
\left|
\mathcal I^{\mathfrak F}_{j,K}(E)
\right|
\le
\left(\int_0^1|T_{\sigma_j,N}|^2\right)^{1/2}
\left(\int_0^1|T_{\tau_j,N}|^2\right)^{1/2}
\ll N\log N.
\]

The Fejér inequality \(0\le\Omega_K\le1\) does not improve this to \(o(N)\). This is the T7 energy barrier in its far-minor form.

Likewise, a one-sided pointwise bound
\[
\sup_{\alpha\in\mathfrak F}|T_{\sigma,N}(\alpha)|\le B
\]
only gives
\[
|\mathcal I^{\mathfrak F}_{j,K}(E)|
\ll B\sqrt{N\log N}.
\]

To force \(o(N)\) by this crude route would require
\[
B=o\!\left(\sqrt{\frac N{\log N}}\right),
\]
which is far stronger than the pointwise estimates normally available from a bare minor-arc treatment. A genuine bilinear/Fourier-coefficient argument is required.

---

## 4. Exact additive-window identity

Because the sector Fejér multiplier has Fourier expansion
\[
\Omega_K(\alpha)=\sum_{|k|\le K}\nu_k^{(K)}e(6k\alpha),
\]
we have the exact identity
\[
\boxed{
\mathcal I^{\mathfrak F}_{j,K}(E)
=
\sum_{|k|\le K}\nu_k^{(K)}
\mathcal I^{\mathfrak F}_{j,0}(E-6k),
}
\]
where
\[
\mathcal I^{\mathfrak F}_{j,0}(u)
:=
\int_{\mathfrak F}
T_{\sigma_j,N}(\alpha)T_{\tau_j,N}(\alpha)e(-u\alpha)\,d\alpha.
\]

Thus the multiplier averages **nearby additive Fourier coefficients**. It does not insert a multiplicative factor into a Type-II variable product.

This identity also explains why the far-minor problem cannot be solved by declaring Fejér positivity: averaging may reduce oscillation, but it can also mask a large center coefficient. Any claimed benefit has to be a proved bound for this weighted Fourier coefficient.

---

## 5. Type-I/II decomposition with sector bookkeeping

A valid combinatorial identity for \(\Lambda\), restricted afterward to the \(+\) or \(-\) residue class, gives a finite decomposition
\[
T_{\sigma,N}(\alpha)
=
\sum_{\ell\in\mathcal L_{\sigma}}
\mathcal B_{\sigma,\ell}(\alpha)
+
\mathcal E_{\sigma}^{\mathrm{comb}}(\alpha),
\]
where each \(\mathcal B_{\sigma,\ell}\) is a Type-I or Type-II exponential sum, schematically
\[
\mathcal B_{\sigma,\ell}(\alpha)
=
\sum_{m\sim M}\sum_{n\sim L}
a_{\ell,m}b_{\ell,n}e(\alpha mn),
\qquad ML\asymp N,
\]
with explicit congruence restrictions inherited from the sector.

Substitution into the far-minor coefficient produces finitely many terms
\[
\mathcal J_{\ell,r}(E)
:=
\int_{\mathfrak F}
\Omega_K(\alpha)
\mathcal B_{\sigma_j,\ell}(\alpha)
\mathcal B_{\tau_j,r}(\alpha)e(-E\alpha)\,d\alpha,
\]
plus terms containing \(\mathcal E^{\mathrm{comb}}\).

A sufficient Type-I/II theorem is therefore
\[
\boxed{
\sum_{\ell,r}\sup_{E\asymp N}|\mathcal J_{\ell,r}(E)|
+
\mathcal E_{\mathrm{comb},j}(N)
\le
\rho_{\mathfrak F}c_jN.
}
\]

This is the correct statement of the far-minor analytic task.

---

## 6. Legitimate weighted bilinear improvement targets

The OFI/Fejér branch can contribute only through a theorem that controls one of the following genuinely weighted objects:

\[
\sup_{E\asymp N}
\left|
\int_{\mathfrak F}
\Omega_K\mathcal B_{\sigma,\ell}\mathcal B_{\tau,r}e(-E\alpha)d\alpha
\right|,
\]

or an averaged precursor strong enough to recover that supremum after an independently proved concentration/large-sieve step.

For example, a usable intermediate estimate would be a weighted correlation inequality of the form
\[
\sum_{E\in\mathcal E_X}
|\mathcal J_{\ell,r}(E)|^2
\le X^{3-\eta_{\ell,r}},
\]
which feeds T8's exceptional-set route. It does **not** by itself establish the P1 supremum in Section 2.

This keeps the hierarchy explicit:
\[
\text{weighted mean square}\Rightarrow\text{almost all},
\qquad
\text{uniform weighted Fourier coefficient}\Rightarrow\text{pointwise Fejér output}.
\]

---

## 7. No free use of transfer operators or spline order

A Ruelle/transfer operator, Riesz multiplier, fractional B-spline order, or extended-trigonometric family is relevant here only when it yields a stated estimate for one of the \(\mathcal J_{\ell,r}(E)\) terms, their weighted energy, or their required coefficient norms.

A formal semigroup identity for the window does not create cancellation in
\[
e(\alpha mn)
\]
or in the final Fourier phase \(e(-E\alpha).

---

## 8. Final analytic ledger before descent

The complete Fejér-windowed P1 target is now:

\[
\mathcal A_{j,K}^{(N)}(n)
\ge
\underbrace{c_jN}_{\text{weighted major model}}
-
\underbrace{\mathcal E_{j,K}^{\mathfrak M}}_{\text{polylog major residual}}
-
\underbrace{\sum_R|\mathcal I_{j,K,R}|}_{\text{transition bands}}
-
\underbrace{|\mathcal I_{j,K}^{\mathfrak F}|}_{\text{far minor coefficient}}.
\]

T15 makes the first error controllable at the polylogarithmic scale. T16 allocates the second. T17 states the third and hardest analytic theorem.

Only after this ledger is positive does T9's separate descent problem become relevant.