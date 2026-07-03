# T19: Weighted Fourth Moment as a Shifted-Correlation Problem

**Status:** exact Fourier expansion and cutoff-regularity correction; no shifted-correlation estimate is claimed.  
**Purpose:** turn the T18 weighted fourth-moment target into a concrete arithmetic off-diagonal problem, while recording the loss of finite spline locality caused by a sharp far-minor cutoff.

---

## 1. Bilinear product coefficients

Fix one Type-I/II pair from T17 and abbreviate
\[
\mathcal B_1(\alpha)=\sum_x c_x e(\alpha x),
\qquad
\mathcal B_2(\alpha)=\sum_y d_y e(\alpha y).
\]

Their product has the exact additive coefficient expansion
\[
\mathcal B_1(\alpha)\mathcal B_2(\alpha)
=
\sum_n C(n)e(\alpha n),
\qquad
C(n):=\sum_{x+y=n}c_xd_y.
\]

No multiplicative reweighting is introduced. The arithmetic object is the additive convolution coefficient \(C(n)\).

---

## 2. The weighted fourth moment

Let
\[
W_{\mathfrak F,K}(\alpha)
:=\mathbf1_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2,
\]
and define its Fourier coefficients
\[
\kappa_{\mathfrak F,K}(h)
:=
\int_0^1W_{\mathfrak F,K}(\alpha)e(\alpha h)\,d\alpha.
\]

Then the T18 energy is
\[
\mathfrak Q_{\mathfrak F,K}(\mathcal B_1,\mathcal B_2)
:=
\int_{\mathfrak F}\Omega_K(\alpha)^2
|\mathcal B_1(\alpha)|^2|\mathcal B_2(\alpha)|^2d\alpha.
\]

Substitution of the coefficient expansion gives the exact identity
\[
\boxed{
\mathfrak Q_{\mathfrak F,K}
=
\sum_{n,n'}C(n)\overline{C(n')}
\kappa_{\mathfrak F,K}(n-n').
}
\]

Equivalently, grouping by shift \(h=n-n'\),
\[
\boxed{
\mathfrak Q_{\mathfrak F,K}
=
\sum_{h\in\mathbb Z}
\kappa_{\mathfrak F,K}(h)
\sum_n C(n)\overline{C(n-h)}.
}
\]

Thus the weighted fourth moment is a kernel-weighted sum of shifted additive correlations of the bilinear convolution sequence.

---

## 3. Diagonal and off-diagonal split

The diagonal is
\[
\kappa_{\mathfrak F,K}(0)
\sum_n|C(n)|^2,
\qquad
\kappa_{\mathfrak F,K}(0)
=
\int_{\mathfrak F}\Omega_K(\alpha)^2d\alpha\ge0.
\]

The off-diagonal term is
\[
\sum_{h\ne0}
\kappa_{\mathfrak F,K}(h)
\mathcal C_C(h),
\qquad
\mathcal C_C(h):=\sum_nC(n)\overline{C(n-h)}.
\]

A saving below the natural \(X^3\) scale must come from one or both of:

\[
\text{reduced weighted diagonal mass},
\qquad
\text{or cancellation/control in the shifted correlations }\mathcal C_C(h).
\]

This is the exact arithmetic content hidden inside the phrase “weighted fourth-moment improvement.”

---

## 4. Full-circle Fejér locality versus sharp-arc nonlocality

Without the far-minor cutoff, the Fejér square has finite Fourier support. Indeed,
\[
\Omega_K(\alpha)
=
\sum_{|k|\le K}\nu_k^{(K)}e(6k\alpha),
\]
so
\[
\Omega_K(\alpha)^2
=
\sum_{|r|\le2K}\eta_r^{(K)}e(6r\alpha),
\]
where
\[
\eta_r^{(K)}
:=
\sum_{k\in\mathbb Z}\nu_k^{(K)}\nu_{r-k}^{(K)}.
\]

Thus on the full circle,
\[
\int_0^1\Omega_K^2|\mathcal B_1\mathcal B_2|^2
=
\sum_{|r|\le2K}\eta_r^{(K)}\mathcal C_C(6r).
\]

This is a genuinely finite-range B-spline/Fejér shifted-correlation identity.

But after multiplying by the sharp indicator \(\mathbf1_{\mathfrak F}\),
\[
\kappa_{\mathfrak F,K}(h)
\]
is generally not finitely supported. Therefore:

\[
\boxed{
\text{a sharp far-minor cutoff destroys the finite shift locality of the Fejér square.}
}
\]

This must be paid for explicitly. It cannot be ignored while invoking a local-spline argument.

---

## 5. Smooth-partition replacement

A legitimate repair is to replace a sharp arc indicator by a smooth periodic partition
\[
1=\chi_{\mathfrak M}+\chi_{\mathfrak T}+\chi_{\mathfrak F},
\]
with \(0\le\chi_\bullet\le1\), each cutoff supported in a controlled enlargement of its intended region.

For the far region use
\[
W^{\mathrm{sm}}_{\mathfrak F,K}(\alpha)
:=\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2.
\]
If \(\chi_{\mathfrak F}\) has \(s\) controlled derivatives, its Fourier coefficients obey a decay estimate of the schematic form
\[
|\widehat{W^{\mathrm{sm}}_{\mathfrak F,K}}(h)|
\ll_s
\frac{\mathcal N_{s,K}}{(1+|h|)^s},
\]
where \(\mathcal N_{s,K}\) depends on cutoff transition widths and the Fejér degree.

This restores summable or rapidly decaying shift weights, but creates boundary collars between regions. Their contribution must be added to the T15/T16/T17 ledger; smoothing does not erase it.

---

## 6. Concrete shifted-correlation theorem target

For a smooth far-minor partition, a sufficient density-one input is an estimate of the form
\[
\boxed{
\sum_{h\in\mathbb Z}
\left|\widehat{W^{\mathrm{sm}}_{\mathfrak F,K}}(h)\right|
\left|\mathcal C_C(h)\right|
\ll X^{3-\eta}.
}
\]

A stronger but easier-to-state sufficient package is:
\[
\sum_n|C(n)|^2\ll X^{3-\eta_0}
\]
for the diagonal part, together with
\[
\sum_{h\ne0}
(1+|h|)^{-s}|\mathcal C_C(h)|
\ll X^{3-\eta_1}
\]
for some \(s>1\), with \(\eta=\min(\eta_0,\eta_1)\) after cutoff constants are paid.

These are not asserted. They are the exact bilinear correlation estimates needed to make T18 operational.

---

## 7. OFI decision rule

A fractional sector-preserving OFI kernel is genuinely better than Fejér only if its squared multiplier, together with a specified smooth arc partition, yields a provably smaller weighted shifted-correlation functional:
\[
\sum_h|\widehat{\chi_{\mathfrak F}\Omega_u^2}(h)|\,|\mathcal C_C(h)|
<
\sum_h|\widehat{\chi_{\mathfrak F}\Omega_K^2}(h)|\,|\mathcal C_C(h)|,
\]
with sufficient margin to cover its major and extraction ledgers.

This is where spline order, Riesz control, or a semigroup construction can matter mathematically: by changing a stated shift kernel. It cannot matter merely by renaming the same unproved off-diagonal correlations.

---

## 8. Outcome

T19 turns the far-minor density-one branch into a precise research program:
\[
\text{smooth sector partition}
\to
\text{kernel-weighted shifted bilinear correlations}
\to
\text{weighted fourth-moment saving}
\to
\text{T18 exceptional-set bound}.
\]

The remaining task is arithmetic: prove a nontrivial estimate for the weighted shifted correlations of the actual Type-I/II coefficient sequences.