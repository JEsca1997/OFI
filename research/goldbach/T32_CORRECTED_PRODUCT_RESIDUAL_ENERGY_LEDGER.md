# T32: Corrected Product-Residual Energy Ledger

**Status:** exact product decomposition and rigorous energy reduction for the reflected Goldbach operator; no analytic bound is claimed.  
**Purpose:** isolate the three actual residual energies that replace the previous correlation-centered bottleneck.

---

## 1. Sector sums and a chosen major model

Fix sector labels \(\sigma,\tau\in\{+,-\}\). Write
\[
S_\sigma(\alpha)=P_\sigma(\alpha)+D_\sigma(\alpha),
\qquad
S_\tau(\alpha)=P_\tau(\alpha)+D_\tau(\alpha),
\]
where:

\[
S_\rho(\alpha)=\sum_{n\le N}\theta_\rho(n)e(\alpha n)
\]

is the exact prime sum, \(P_\rho\) is the chosen major-arc model, and
\[
D_\rho:=S_\rho-P_\rho
\]
is its exact discrepancy.

The Goldbach Fourier product is
\[
F_{\sigma,\tau}=S_\sigma S_\tau,
\]
and its model is
\[
M_{\sigma,\tau}=P_\sigma P_\tau.
\]

---

## 2. Exact three-term residual identity

The corrected Goldbach residual is
\[
R_{\sigma,\tau}(\alpha)
:=F_{\sigma,\tau}(\alpha)-M_{\sigma,\tau}(\alpha).
\]

Expanding gives
\[
\boxed{
R_{\sigma,\tau}
=
P_\sigma D_\tau
+
D_\sigma P_\tau
+
D_\sigma D_\tau.
}
\]

Define
\[
R^{(1)}:=P_\sigma D_\tau,
\qquad
R^{(2)}:=D_\sigma P_\tau,
\qquad
R^{(3)}:=D_\sigma D_\tau.
\]

This is an exact algebraic decomposition. The first two terms are linear in one prime-sum discrepancy; the third is genuinely bilinear.

---

## 3. Localized Goldbach residual energy

Let
\[
w(\alpha):=\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2,
\qquad 0\le w\le1,
\]
where \(\chi_{\mathfrak F}\) is the smooth far-minor cutoff and \(\Omega\) is sector preserving.

Define
\[
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
:=
\int_0^1w(\alpha)|R_{\sigma,\tau}(\alpha)|^2d\alpha.
\]

Since
\[
|x+y+z|^2\le3(|x|^2+|y|^2+|z|^2),
\]
we obtain the rigorous reduction
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
\le3\left(
\mathfrak Q_{P\!D}^{(\sigma,\tau)}
+
\mathfrak Q_{D\!P}^{(\sigma,\tau)}
+
\mathfrak Q_{D\!D}^{(\sigma,\tau)}
\right),
}
\]
where
\[
\mathfrak Q_{P\!D}^{(\sigma,\tau)}
:=
\int_0^1w|P_\sigma|^2|D_\tau|^2,
\]
\[
\mathfrak Q_{D\!P}^{(\sigma,\tau)}
:=
\int_0^1w|D_\sigma|^2|P_\tau|^2,
\]
\[
\boxed{
\mathfrak Q_{D\!D}^{(\sigma,\tau)}
:=
\int_0^1w|D_\sigma|^2|D_\tau|^2.
}
\]

---

## 4. Correct distribution of analytic responsibility

The three ledger entries have different mathematical meanings.

### L1. \(P\!D\) and \(D\!P\): one-discrepancy energies

These may be approachable from a combination of:
\[
\text{major-model control},
\qquad
\text{mean-square discrepancy estimates},
\qquad
\text{the precise support of }w.
\]

A crude but explicit bound is
\[
\mathfrak Q_{P\!D}^{(\sigma,\tau)}
\le
\|w^{1/2}P_\sigma\|_\infty^2
\int_0^1|D_\tau(\alpha)|^2d\alpha,
\]
and symmetrically for \(D\!P\). Whether this is useful depends on the actual model and partition; it is not asserted to save a power.

### L2. \(D\!D\): the genuine far-minor bilinear energy

\[
\mathfrak Q_{D\!D}^{(\sigma,\tau)}
=
\int_0^1w|D_\sigma|^2|D_\tau|^2.
\]

This is the corrected analogue of the old hard energy gate. It is positive and cannot be reduced by claiming arbitrary signed cancellation after the square has formed.

Any power saving must arise from a direct bilinear estimate for the discrepancies, from large-values information, or from an earlier oscillatory decomposition.

---

## 5. A sufficient three-budget theorem

To obtain the T31 density-one target
\[
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
\ll X^{3-\eta},
\]
it is sufficient to prove, for some nonnegative budgets \(\eta_1,\eta_2,\eta_3\) with a common positive saving, that
\[
\mathfrak Q_{P\!D}^{(\sigma,\tau)}
\ll X^{3-\eta},
\qquad
\mathfrak Q_{D\!P}^{(\sigma,\tau)}
\ll X^{3-\eta},
\qquad
\mathfrak Q_{D\!D}^{(\sigma,\tau)}
\ll X^{3-\eta}.
\]

More generally, a fixed allocation such as
\[
\mathfrak Q_{P\!D}\le\frac1{12}X^{3-\eta},
\qquad
\mathfrak Q_{D\!P}\le\frac1{12}X^{3-\eta},
\qquad
\mathfrak Q_{D\!D}\le\frac1{12}X^{3-\eta}
\]
would imply
\[
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
\le\frac14X^{3-\eta}.
\]

The numerical fractions are only a bookkeeping example.

---

## 6. Why this is better than the old autocorrelation spine

The old correlation-centered language obscured which quantity was being squared. Here the logic is exact:

\[
S_\sigma S_\tau
\to
P_\sigma P_\tau
\to
P_\sigma D_\tau+D_\sigma P_\tau+D_\sigma D_\tau
\to
\text{three positive weighted energies}.
\]

The product is the Goldbach product throughout. The only autocorrelation that may later appear is an autocorrelation of the coefficient sequence of one of these residual terms after Parseval/kernel expansion.

---

## 7. OFI decision rule

An OFI multiplier or fractional operator advances this gate only if it proves one of the following under the same partition:

\[
\mathfrak Q_{P\!D}^{\rm OFI}<\mathfrak Q_{P\!D}^{\rm benchmark},
\]
\[
\mathfrak Q_{D\!P}^{\rm OFI}<\mathfrak Q_{D\!P}^{\rm benchmark},
\]
\[
\boxed{
\mathfrak Q_{D\!D}^{\rm OFI}<\mathfrak Q_{D\!D}^{\rm benchmark}
}
\]

by a quantitatively sufficient amount after all extraction, collar, and major-model costs are charged.

A formal rearrangement of \(S_\sigma S_\tau\) or a statement about prime-gap correlations does not close any of these ledgers.

---

## 8. Outcome

The corrected density-one bottleneck is now sharply isolated:
\[
\boxed{
\int_0^1
\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2
|D_\sigma(\alpha)|^2|D_\tau(\alpha)|^2d\alpha
\ll X^{3-\eta}.
}
\]

The linear \(P\!D\) terms have their own checkable ledgers. The real hard theorem is the bilinear discrepancy energy \(D\!D\), not an autocorrelation identity.