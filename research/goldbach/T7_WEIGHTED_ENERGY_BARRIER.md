# T7: Weighted Energy Barrier and Correlation Target

**Status:** elementary barrier theorem plus exact next target.  
**Purpose:** show why a bounded OFI multiplier and Parseval alone cannot prove binary Goldbach, and isolate the correlation estimate that must replace them.

---

## 1. The corrected weighted minor-arc integral

Let
\[
T_{\sigma,N}(\alpha)=\sum_{n\le N}\Lambda_\sigma(n)e(\alpha n)
\]
and let \(\Omega(\alpha)=\Omega_{u,\psi}(\alpha)\) be the periodic multiplier induced by the corrected OFI local output window. The weighted minor-arc term is
\[
\mathcal I^{\mathfrak m}_{\Omega,\sigma,\tau}(E)
=
\int_{\mathfrak m}
\Omega(\alpha)T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

The phase has modulus one, so it plays no role in the elementary absolute-value estimate.

---

## 2. The elementary weighted energy bound

Cauchy--Schwarz yields
\[
\left|\mathcal I^{\mathfrak m}_{\Omega,\sigma,\tau}(E)\right|
\le
\|\Omega\|_\infty
\left(\int_{\mathfrak m}|T_{\sigma,N}(\alpha)|^2d\alpha\right)^{1/2}
\left(\int_{\mathfrak m}|T_{\tau,N}(\alpha)|^2d\alpha\right)^{1/2}.
\]

Extending the integrals to the full torus and applying Parseval gives
\[
\int_0^1|T_{\sigma,N}(\alpha)|^2d\alpha
=
\sum_{n\le N}\Lambda_\sigma(n)^2.
\]

The elementary estimate \(\Lambda(n)^2\le (\log N)\Lambda(n)\) for \(n\le N\), together with \(\sum_{n\le N}\Lambda(n)=O(N)\), gives
\[
\sum_{n\le N}\Lambda_\sigma(n)^2=O(N\log N).
\]

Hence
\[
\boxed{
\left|\mathcal I^{\mathfrak m}_{\Omega,\sigma,\tau}(E)\right|
=O\!\left(\|\Omega\|_\infty N\log N\right).
}
\]

---

## 3. The barrier

The major-arc Goldbach main term is expected at order \(E\), up to a singular-series factor. The bound
\[
O(N\log N)
\]
is therefore too large even before one accounts for the dual-window truncation, major-arc approximation, or prime-power removal.

### Barrier theorem

A bounded OFI/local-window multiplier together with global Parseval and Cauchy--Schwarz cannot by itself establish the required binary-Goldbach minor-arc inequality.

In particular, merely choosing an order \(u\) for which \(\Omega_{u,\psi}\) has a smaller sup norm does not solve the arithmetic problem unless the same choice yields cancellation beyond global energy.

---

## 4. The first viable replacement: weighted correlation control

Squaring the weighted integral or studying its mean over targets produces additive correlations of the prime exponential sums. The meaningful target is a bound of the form
\[
\boxed{
\int_{\mathfrak m}
|\Omega(\alpha)|^2
|T_{\sigma,N}(\alpha)|^2
|T_{\tau,N}(\alpha)|^2
\,d\alpha
\le
C_{u,\psi}N^{2-2\delta}
}
\]
for some \(\delta>0\), or another estimate strong enough to give a pointwise coefficient bound after a legitimate amplification/descent argument.

This is not supplied by Parseval. It is a fourth-moment/additive-correlation statement.

---

## 5. Fourier-coefficient interpretation of the window

Write
\[
\Omega(\alpha)=\sum_{h\in\mathbb Z}\omega_h e(\alpha h).
\]
Then
\[
\mathcal I_{\Omega,\sigma,\tau}(E)
=
\sum_{h\in\mathbb Z}\omega_h
(\Lambda_\sigma*\Lambda_\tau)(E-h).
\]

Thus the local OFI window averages nearby additive correlations. It cannot create positivity out of a zero coefficient; it can only help if the correlation sequence is already controlled sufficiently uniformly over the window scale.

This makes the desired arithmetic improvement precise:

- obtain cancellation or a lower bound uniformly over an additive neighborhood of \(E\);
- choose \(\omega_h\) so the window emphasizes the portion with a provable advantage;
- pay the dual/window reconstruction tail.

---

## 6. Where compactness and covers can now enter

Let \(\mathfrak m\) be decomposed into finitely many arc families on which different Type-I/II estimates apply:
\[
\mathfrak m=\bigcup_{r=1}^{R(N)}\mathfrak m_r.
\]

The valid compact-cover task is to prove an estimate on every member of this finite cover and sum the resulting bounds:
\[
\left|\mathcal I^{\mathfrak m}_{\Omega}(E)\right|
\le
\sum_{r=1}^{R(N)}
\left|\int_{\mathfrak m_r}\Omega T_\sigma T_\tau e(-E\alpha)d\alpha\right|.
\]

T1/countable compactness language can organize a limiting exhaustion of such covers, but it cannot replace the needed Type-I/II inequality on each piece.

---

## 7. OFI advantage criterion, strengthened

Let \(u_0=2\) be the triangular baseline and let \(\Omega_u\) be a candidate OFI multiplier. A real advance requires a theorem of one of these forms:

\[
\int_{\mathfrak m}|\Omega_u|^2|T_\sigma|^2|T_\tau|^2
\ll N^{2-2\delta_u}
\]
with \(\delta_u>0\),

or a pointwise weighted estimate
\[
\left|\int_{\mathfrak m}\Omega_uT_\sigma T_\tau e(-E\alpha)d\alpha\right|
\ll N^{1-\delta_u},
\]

and, after adding the local-dual tail, a strict improvement over the baseline order.

The research question is now no longer vague:
\[
\boxed{
\text{Can an OFI-derived additive multiplier improve a provable Type-II or fourth-moment minor-arc bound?}
}

---

## 8. What this closes

T7 closes the easy-energy route as insufficient and prevents a false claim that the OFI window plus compactness automatically yields the desired power saving.

The remaining path is narrower but real:
\[
\text{Vaughan/Heath--Brown decomposition}
\to
\text{sector-aware Type-I/II estimates}
\to
\text{weighted fourth moment or pointwise minor-arc bound}
\to
\text{T3 local-dual certificate}
\to
\text{prime-power stripping}.
