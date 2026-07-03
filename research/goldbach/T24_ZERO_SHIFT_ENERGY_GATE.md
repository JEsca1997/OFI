# T24: Zero-Shift Energy Gate

**Status:** exact isolation of the \(s=0\) obstruction in the T20–T23 density-one route; no energy estimate is claimed.  
**Purpose:** prevent nonzero-shift divisor sparsity from being misapplied to the zero-shift multiplicative-collision energy.

---

## 1. The smooth far-minor energy is nonnegative

For one Type-I/II pair, let
\[
W^{\rm sm}_{\mathfrak F,K}(\alpha)
=
\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2,
\qquad 0\le W^{\rm sm}_{\mathfrak F,K}\le1.
\]

With
\[
\mathcal B_1(\alpha)\mathcal B_2(\alpha)=\sum_tC(t)e(\alpha t),
\]
the weighted fourth moment is
\[
\mathfrak Q_{\mathfrak F,K}
=
\int_0^1W^{\rm sm}_{\mathfrak F,K}(\alpha)
|\mathcal B_1(\alpha)\mathcal B_2(\alpha)|^2d\alpha
\ge0.
\]

Its Fourier expansion from T19 is
\[
\mathfrak Q_{\mathfrak F,K}
=
\sum_h\widehat W^{\rm sm}_{\mathfrak F,K}(h)\mathcal C_C(h),
\qquad
\mathcal C_C(h)=\sum_tC(t)\overline{C(t-h)}.
\]

Although this expansion has signed off-zero Fourier coefficients, the original integral is an energy. A proof of smallness must come from frequency localization and arithmetic control, not from treating the total as an arbitrary signed sum.

---

## 2. The central coefficient

The zero Fourier coefficient of the smooth weight is
\[
\lambda_0
:=
\widehat W^{\rm sm}_{\mathfrak F,K}(0)
=
\int_0^1\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2d\alpha
\ge0.
\]

The corresponding correlation is
\[
\boxed{
\mathcal C_C(0)=\sum_t|C(t)|^2.
}
\]

Equivalently, by Parseval on the full circle,
\[
\mathcal C_C(0)
=
\int_0^1|\mathcal B_1(\alpha)\mathcal B_2(\alpha)|^2d\alpha.
\]

Thus the zero shift measures the complete additive collision energy of the two bilinear image sequences before far-minor localization.

---

## 3. Exact factorization through T22

Since \(C=A*B\), T22 gives
\[
\mathcal C_C(0)
=
(\mathcal R_A*\mathcal R_B)(0)
=
\sum_s\mathcal R_A(s)\mathcal R_B(-s).
\]

Because
\[
\mathcal R_F(-s)=\overline{\mathcal R_F(s)},
\]
this may be written as
\[
\boxed{
\mathcal C_C(0)
=
\sum_s\mathcal R_A(s)\overline{\mathcal R_B(s)}.
}
\]

This identity is exact. It does not justify replacing the right side by an absolute-value bound unless that extra loss is explicitly accepted.

---

## 4. Why nonzero-shift sparsity does not resolve it

T23 shows that for fixed \(s\ne0\), only gcd strata \(d\mid s\) contribute to
\[
\mathcal R_A(s).
\]

At \(s=0\), every admissible gcd stratum contributes. In normalized variables,
\[
a n=b n',
qquad (a,b)=1,
\]
forces
\[
n=b\ell,
\qquad n'=a\ell,
\]
but does not force \(a=b=1\).

Hence the zero-shift energy includes all multiplicative collision families
\[
(m,n)=(da,b\ell),
qquad
(m',n')=(db,a\ell),
]
across coprime slope pairs \((a,b)\). The literal tuple diagonal is only one subfamily.

Therefore:
\[
\boxed{
\text{divisor sparsity for }s\ne0\text{ gives no direct saving for the zero-shift energy.}
}
\]

---

## 5. Two legitimate ways to handle the zero-shift contribution

### Z1. Direct far-minor energy estimate

Prove the localized bound directly:
\[
\boxed{
\int_0^1\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2
|\mathcal B_1(\alpha)\mathcal B_2(\alpha)|^2d\alpha
\ll X^{3-\eta}.
}
\]

This is the cleanest form because it retains the frequency localization that is lost when \(\mathcal C_C(0)\) is isolated on the full circle.

### Z2. A coefficient-energy estimate plus controlled kernel interaction

Prove a sufficient estimate for
\[
\mathcal C_C(0)=\sum_t|C(t)|^2,
\]
together with bounds for the nonzero correlations strong enough to control the full kernel-weighted sum in T19.

This route is usually more expensive because the full-circle energy ignores the far-minor suppression encoded by \(\chi_{\mathfrak F}\Omega_K^2\).

---

## 6. What cannot be claimed

It is invalid to argue:

\[
\text{nonzero shifts are sparse}
\Longrightarrow
\mathfrak Q_{\mathfrak F,K}\text{ is small}.
\]

The central multiplicative-collision energy remains. Likewise, a finite-shift Fejér identity does not by itself lower the positive integral in Section 1.

A window can help only by proving that the bilinear product has small energy on the region where the weight is supported, or by giving a controlled kernel interaction estimate that implies the same conclusion.

---

## 7. Refined T20/T22 theorem target

For each required Type-I/II pair, the density-one branch now requires a coupled estimate:
\[
\boxed{
\int_0^1\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2
|\mathcal B_1(\alpha)\mathcal B_2(\alpha)|^2d\alpha
\ll X^{3-\eta},
}
\]
with the collar/tail bookkeeping of T20 and the decomposition remainders included.

The gcd-lattice expansion in T23 remains valuable for understanding nonzero short correlations and for a possible kernel-side proof, but it does not replace this zero-shift energy requirement.

---

## 8. OFI decision rule

A fractional sector-preserving multiplier can beat Fejér only if it produces a provably smaller **localized positive energy**
\[
\int\chi_{\mathfrak F}\Omega_u^2|\mathcal B_1\mathcal B_2|^2,
\]
not merely a more attractive finite-shift kernel on the nonzero \(6\mathbb Z\) correlations.

This is the main obstruction left by the zero-shift geometry.