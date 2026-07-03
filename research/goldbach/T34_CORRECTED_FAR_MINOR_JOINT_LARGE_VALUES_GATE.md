# T34: Corrected Far-Minor Joint Large-Values Gate

**Status:** exact dyadic reduction of the pure T33 far-minor Goldbach energy; no large-values estimate is claimed.  
**Purpose:** state the first genuinely proof-moving theorem in terms of the actual sector prime sums, rather than prime-gap correlations or a major-model residual.

---

## 1. Pure far-minor Goldbach energy

Fix sector labels \(\sigma,\tau\in\{+,-\}\). By T33, the far-minor contribution is exactly
\[
\mathfrak Q_{\mathfrak F,\Omega}^{\rm GB}
=
\int_0^1
w(\alpha)
|S_\sigma(\alpha)|^2|S_\tau(\alpha)|^2d\alpha,
\]
where
\[
w(\alpha):=\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2,
\qquad 0\le w\le1.
\]

The density-one target is
\[
\boxed{
\mathfrak Q_{\mathfrak F,\Omega}^{\rm GB}
\ll X^{3-\eta}.
}
\]

---

## 2. Weighted joint large-value sets

For dyadic levels \(U,V>0\), define
\[
\mathfrak E_{U,V}
:=
\left\{
\alpha\in\operatorname{supp}(w):
U<|S_\sigma(\alpha)|\le2U,
\quad
V<|S_\tau(\alpha)|\le2V
\right\}.
\]

Write the weighted measure
\[
\mu_w(E):=\int_Ew(\alpha)d\alpha.
\]

The sets \(\mathfrak E_{U,V}\), together with harmless lower-level pieces, partition the far-minor support according to the two actual prime-sum magnitudes.

---

## 3. Exact dyadic energy reduction

On \(\mathfrak E_{U,V}\),
\[
|S_\sigma|^2|S_\tau|^2\le16U^2V^2.
\]

Therefore
\[
\boxed{
\mathfrak Q_{\mathfrak F,\Omega}^{\rm GB}
\ll
\sum_{U,V}^{\rm dyadic}
U^2V^2\mu_w(\mathfrak E_{U,V})
+
\mathcal E_{\rm low},
}
\]
where \(\mathcal E_{\rm low}\) consists of the finitely many bands below chosen base thresholds \(U_0,V_0\).

Conversely, since \(|S_\sigma|>U\) and \(|S_\tau|>V\) on \(\mathfrak E_{U,V}\),
\[
\boxed{
U^2V^2\mu_w(\mathfrak E_{U,V})
\le
\mathfrak Q_{\mathfrak F,\Omega}^{\rm GB}.
}
\]

Thus the dyadic expression records the exact joint-concentration content of the far-minor energy.

---

## 4. Low-level ledger

Let
\[
\mathfrak E_{\le U_0,\le V_0}
:=
\{\alpha\in\operatorname{supp}(w):|S_\sigma|\le U_0,\ |S_\tau|\le V_0\}.
\]

Then
\[
\int_{\mathfrak E_{\le U_0,\le V_0}}
 w|S_\sigma|^2|S_\tau|^2
\le
U_0^2V_0^2\int_0^1w(\alpha)d\alpha.
\]

The mixed low/high bands are controlled similarly, e.g.
\[
\int_{\{|S_\sigma|\le U_0\}}
 w|S_\sigma|^2|S_\tau|^2
\le
U_0^2\int_0^1w|S_\tau|^2.
\]

Hence base thresholds are not cosmetic. They must be selected so that all low-level ledgers fit inside a prescribed fraction of \(X^{3-\eta}\).

---

## 5. A sufficient joint large-values theorem

A direct sufficient result is the summable bound
\[
\boxed{
\sum_{U,V}^{\rm dyadic}
U^2V^2\mu_w(\mathfrak E_{U,V})
\ll X^{3-\eta}.
}
\]

A stronger per-stratum form is
\[
\boxed{
\mu_w(\mathfrak E_{U,V})
\ll
X^{3-\eta}U^{-2}V^{-2}(\log X)^{-A}
}
\]
for enough logarithmic slack \(A\) to absorb the \(O((\log X)^2)\) dyadic strata.

Neither estimate is asserted here.

---

## 6. Why one-factor bounds are not enough

Separate estimates for
\[
\mu_w\{\alpha:|S_\sigma(\alpha)|>U\}
\quad\text{and}\quad
\mu_w\{\alpha:|S_\tau(\alpha)|>V\}
\]
do not automatically control \(\mu_w(\mathfrak E_{U,V})\) at the required scale. The obstruction is possible joint concentration of the two sector sums on the same far-minor frequencies.

The exact missing arithmetic statement is therefore:
\[
\boxed{
\text{large values of }S_\sigma\text{ and }S_\tau
\text{ cannot overlap too often on the weighted far-minor set.}
}
\]

This is the corrected analogue of the joint-concentration issue from the former T29--T30 route, now attached to the right Goldbach product.

---

## 7. Connection to Type-I/II decomposition

A Vaughan/Heath--Brown decomposition may be inserted only after the joint-large-values object is fixed:
\[
S_\rho(\alpha)
=
\sum_{\ell}\mathcal B_{\rho,\ell}(\alpha)+\mathcal E_{\rho,\rm comb}(\alpha).
\]

Then a proof must show that the dyadic sets \(\mathfrak E_{U,V}\) are controlled by the corresponding Type-I/II component pairs plus all combinatorial remainders. It is not valid to replace \(S_\sigma S_\tau\) by a single generic correlation sum.

The correct proof order is
\[
\text{joint large values of }S_\sigma,S_\tau
\to
\text{component-pair reduction}
\to
\text{bilinear/spectral/dispersion estimate}.
\]

---

## 8. OFI comparison rule

An OFI multiplier \(\Omega_u\) improves the far-minor gate only if, under the same output-locality and collar ledger, it proves a smaller weighted joint-large-values functional:
\[
\sum_{U,V}U^2V^2\mu_{\chi_{\mathfrak F}|\Omega_u|^2}(\mathfrak E_{U,V})
\]
than the benchmark multiplier by a quantitatively sufficient amount.

Pointwise decay of \(\Omega_u\) alone is not enough; T25 already records the radius cost of trying to obtain a power saving solely by that route.

---

## 9. Outcome

The corrected far-minor branch is now:
\[
\boxed{
\int_{\mathfrak F}|\Omega|^2|S_\sigma|^2|S_\tau|^2
}
\to
\boxed{
\sum_{U,V}U^2V^2\mu_w(\mathfrak E_{U,V})
}
\to
\text{joint Type-I/II large-values theorem}.
\]

This is a direct arithmetic target for Goldbach. No prime-gap autocorrelation identity is used.