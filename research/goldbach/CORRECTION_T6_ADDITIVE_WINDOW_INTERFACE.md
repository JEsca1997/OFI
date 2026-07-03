# Correction: OFI Local Window Acts on the Additive Output Coordinate

**Scope:** This correction supersedes the product-weight claim in `T6_OFI_VAUGHAN_TYPEII_INTERFACE.md`.

## 1. The issue

A Goldbach coefficient is an **additive** convolution coefficient:
\[
g_E=(a*b)(E)=\sum_{r+s=E}a_r b_s.
\]

The B-spline/dual-window functional is applied after this convolution. Therefore it weights the output coordinate \(r+s\), not the product coordinate \(mn\) appearing inside a Vaughan or Heath--Brown decomposition of a single Mangoldt exponential sum.

It is incorrect to write the OFI-localized Type-II object directly as
\[
\sum_{m\sim M}\sum_{n\sim L}a_m b_n W(mn)e(\alpha mn)
\]
without deriving such a product weight from a separate identity.

## 2. Exact additive-window identity

Let
\[
H_u(x)=\sum_{q\in\mathbb Z}g_q\,\gamma_u(x-(q+1))
\]
be the corrected centered cardinal fractional B-spline synthesis of an additive coefficient sequence \(g\). Let \(\psi\in C_c^\infty(\mathbb R)\) be a local approximation to the dual extractor.

Define the discrete output kernel
\[
K_{u,\psi}(\ell)
:=\left\langle\gamma_u(\cdot),\psi(\cdot-\ell)\right\rangle,
\qquad \ell\in\mathbb Z.
\]
Then the local functional at target \(E\) is exactly
\[
\mathcal J^{\psi}_{u,E}[H_u]
=
\sum_{q\in\mathbb Z}g_qK_{u,\psi}(E-q).
\]

Thus the OFI/local-dual layer is a controlled smoothing or extraction in the **Goldbach sum variable**.

## 3. Correct Fourier-side multiplier

Define the periodic multiplier
\[
\Omega_{u,\psi}(\alpha)
:=\sum_{\ell\in\mathbb Z}K_{u,\psi}(\ell)e(\alpha\ell).
\]
For finite exponential sums
\[
A(\alpha)=\sum_r a_r e(\alpha r),
\qquad
B(\alpha)=\sum_s b_s e(\alpha s),
\]
we have
\[
\boxed{
\mathcal J^{\psi}_{u,E}[H_u]
=
\int_0^1
\Omega_{u,\psi}(\alpha)A(\alpha)B(\alpha)e(-E\alpha)\,d\alpha.
}
\]

The OFI window is therefore a bounded periodic **frequency multiplier on the product of the two additive exponential sums**.

## 4. Correct relation to Vaughan / Type-I / Type-II sums

A Vaughan- or Heath--Brown-type identity may still decompose each Mangoldt sum into bilinear pieces of the form
\[
\sum_{m\sim M}\sum_{n\sim L}c_m d_n e(\alpha mn).
\]

But the OFI window remains outside those individual pieces, as the factor
\[
\Omega_{u,\psi}(\alpha)
\]
in the outer minor-arc integral. The valid minor-arc target is consequently
\[
\boxed{
\left|
\int_{\mathfrak m}
\Omega_{u,\psi}(\alpha)
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)
\,d\alpha
\right|
\le \mathcal E_{u,\psi,j}(E).
}
\]

The Type-I/II bounds are used to control one or both factors \(T_{\sigma,N}\), uniformly on the minor arcs, or to control appropriate mean values over those arcs. They are not automatically replaced by a product-weight estimate.

## 5. Legitimate OFI contribution after correction

The fractional/order/window branch can help only if \(\Omega_{u,\psi}\) improves a valid minor-arc integral estimate after all extraction errors are included. Examples of legitimate gains would be:

1. \(\Omega_{u,\psi}\) suppresses a region of the minor arcs where available Type-II bounds are weakest, while preserving a positive major-arc contribution;
2. \(\Omega_{u,\psi}\) has a Fourier expansion that allows a sharper additive-shift average of Type-II estimates;
3. \(\Omega_{u,\psi}\) makes a weighted mean-square estimate stronger than the unweighted counterpart and the dual-window tail remains smaller than that gain.

None of these gains follows from smoothing alone.

## 6. Corrected next theorem

The next theorem worth attacking is:
\[
\boxed{
\text{For some stable order }u\text{ and local dual approximation }\psi,
\quad
\int_{\mathfrak m}
|\Omega_{u,\psi}(\alpha)T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)|\,d\alpha
\le C_uN^{1-\delta}
}
\]
for a positive \(\delta\), uniformly in the required sector channels, together with a major-arc lower bound for the same multiplier.

This is still a very hard binary-Goldbach estimate. The correction does not claim it.

## 7. Effect on status

- T1 exact B-spline encoding: unchanged.
- T2 fractional frame stability: unchanged.
- T3 compact local dual-window certificate: unchanged.
- T5 major/minor certificate: unchanged after replacing its OFI local functional by the multiplier \(\Omega_{u,\psi}\).
- T6 must be read through this additive-window correction.

This correction makes the arithmetic interface faithful to the additive nature of Goldbach and prevents an invalid shortcut through product-weight notation.