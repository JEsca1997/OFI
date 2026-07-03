# T31: Corrected Goldbach Coefficient-Energy Gate

**Status:** exact Fourier/Parseval identities for the reflected Goldbach product and its localized residual energy; no arithmetic saving is claimed.  
**Purpose:** recover the valid energy technology after the Hankel-versus-Toeplitz correction, while keeping clear what is being autocorrelated.

---

## 1. Correct Goldbach coefficients

Fix sector labels \(\sigma,\tau\in\{+,-\}\). Let
\[
S_{\sigma,N}(\alpha)=\sum_{n\le N}\theta_\sigma(n)e(\alpha n),
\qquad
S_{\tau,N}(\alpha)=\sum_{n\le N}\theta_\tau(n)e(\alpha n).
\]

Define
\[
F_{\sigma,\tau}(\alpha)
:=S_{\sigma,N}(\alpha)S_{\tau,N}(\alpha).
\]

Its Fourier coefficients are the reflected/additive Goldbach coefficients
\[
\boxed{
\Gamma_{\sigma,\tau;N}(E)
:=
\sum_{\substack{m+n=E\\m,n\le N}}
\theta_\sigma(m)\theta_\tau(n).
}
\]

Thus exactly
\[
\boxed{
F_{\sigma,\tau}(\alpha)
=
\sum_E\Gamma_{\sigma,\tau;N}(E)e(\alpha E).
}
\]

The word “autocorrelation” below refers only to correlations of the **Goldbach coefficient sequence** \(E\mapsto\Gamma(E)\), never to the prime-gap function \(h\mapsto\sum_n\theta(n)\theta(n+h)\).

---

## 2. Full-circle Parseval identity

Parseval gives
\[
\boxed{
\int_0^1|S_{\sigma,N}(\alpha)S_{\tau,N}(\alpha)|^2d\alpha
=
\sum_E|\Gamma_{\sigma,\tau;N}(E)|^2.
}
\]

This is an exact positive fourth-moment identity for the Goldbach product.

It does **not** prove Goldbach positivity: a positive total mean square is compatible with zeros at individual even \(E\).

---

## 3. Major model and exact residual

Let \(P_{\sigma,N}(\alpha)\) denote an explicitly chosen major-arc model and define
\[
M_{\sigma,\tau}(\alpha)
:=P_{\sigma,N}(\alpha)P_{\tau,N}(\alpha).
\]

Write its coefficients as
\[
M_{\sigma,\tau}(\alpha)
=
\sum_E\mathcal M_{\sigma,\tau;N}(E)e(\alpha E).
\]

Define the Fourier-side residual
\[
\mathcal R_{\sigma,\tau}(\alpha)
:=F_{\sigma,\tau}(\alpha)-M_{\sigma,\tau}(\alpha)
=
\sum_Er_{\sigma,\tau;N}(E)e(\alpha E),
\]
where
\[
\boxed{
r_{\sigma,\tau;N}(E)
=
\Gamma_{\sigma,\tau;N}(E)-\mathcal M_{\sigma,\tau;N}(E).
}
\]

This is the residual whose size matters for a Goldbach theorem.

---

## 4. Correct localized far-minor energy

Let
\[
w(\alpha):=\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2,
\qquad0\le w\le1,
\]
where \(\chi_{\mathfrak F}\) is a smooth far-minor cutoff and \(\Omega\) is a sector-preserving output multiplier.

The correct localized residual energy is
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
:=
\int_0^1w(\alpha)|\mathcal R_{\sigma,\tau}(\alpha)|^2d\alpha.
}
\]

For \(w\equiv1\), Parseval gives
\[
\mathfrak Q^{\rm GB}_{\mathbb T,1}
=
\sum_E|r_{\sigma,\tau;N}(E)|^2.
\]

Hence the density-one target has the natural scale
\[
\boxed{
\sum_{E\asymp X\atop E\equiv j(6)}
|r_{\sigma_j,\tau_j;N}(E)|^2
\ll X^{3-\eta}.
}
\]

This target is unproved.

---

## 5. Exact kernel expansion of localized energy

Define the Fourier coefficients of the localized weight
\[
\widehat w(h):=\int_0^1w(\alpha)e(-h\alpha)d\alpha.
\]

Expanding \(|\mathcal R|^2\) gives
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
=
\sum_{E,E'}
r(E)\overline{r(E')}
\widehat w(E'-E).
}
\]

Equivalently, with the Goldbach-residual autocorrelation
\[
\mathcal C_r(h):=\sum_Er(E)\overline{r(E-h)},
\]
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
=
\sum_h\widehat w(h)\mathcal C_r(h).
}
\]

This identity is valid and useful. Its diagonal is
\[
\widehat w(0)\sum_E|r(E)|^2,
\]
which is nonnegative. The off-diagonal terms are not a substitute for bounding that positive diagonal mass unless the entire positive localized integral is estimated directly.

---

## 6. What can transfer from the previous energy technology

The following framework transfers after replacing the coefficient sequence by \(r(E)\):

\[
\text{smooth far-minor partitions},
\qquad
\text{Fourier-tail accounting for }\widehat w,
\qquad
\text{Chebyshev transfer from mean square to exceptional sets},
\qquad
\text{output-window extraction ledgers}.
\]

The old lattice/product-difference analysis transfers only after a new derivation of the coefficients of \(r(E)\) from the chosen Type-I/II decomposition of
\[
S_\sigma(\alpha)S_\tau(\alpha)-P_\sigma(\alpha)P_\tau(\alpha).
\]

No previous prime-gap autocorrelation formula is imported.

---

## 7. Density-one transfer, conditional on the correct residual estimate

Suppose for \(E\asymp X\), \(E\equiv j\pmod6\),
\[
\mathcal M_j(E)\ge c_jX,
\]
and
\[
\sum_{E\asymp X\atop E\equiv j(6)}|r_j(E)|^2
\le C X^{3-\eta}.
\]

For a threshold \(X^{1-\delta}\), Chebyshev yields
\[
\#\{E\asymp X:E\equiv j(6),\ |r_j(E)|>X^{1-\delta}\}
\ll X^{1+2\delta-\eta}.
\]

If \(2\delta<\eta\), this is density zero. For all remaining sufficiently large \(E\),
\[
\Gamma_j(E)
=
\mathcal M_j(E)+r_j(E)
>0
\]
provided \(X^{1-\delta}<c_jX\).

This is a correct conditional density-one Goldbach implication. The hard missing input is the stated mean-square residual estimate.

---

## 8. Outcome

The corrected energy branch is
\[
S_\sigma S_\tau
\to
\Gamma_{\sigma,\tau}(E)
\to
r_{\sigma,\tau}(E)
\to
\sum_E|r(E)|^2
\to
\text{Chebyshev density-one transfer}.
\]

It reuses valid harmonic-analysis machinery without confusing prime-gap correlations with Goldbach representations.