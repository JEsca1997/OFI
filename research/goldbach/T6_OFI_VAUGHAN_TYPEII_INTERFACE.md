# T6: OFI-Weighted Vaughan / Type-II Interface

**Status:** precise next arithmetic target; no new exponential-sum bound is claimed.  
**Purpose:** identify the first place where an OFI-local window could contribute to a genuine binary-Goldbach minor-arc estimate rather than merely rewriting the coefficient.

---

## 1. The unavoidable arithmetic input

After T1--T5, the remaining term is a sector minor-arc correlation built from Mangoldt sums:
\[
\mathcal I^{\mathfrak m}_{j}(E)
=
\int_{\mathfrak m}
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

The first standard reduction of a Mangoldt exponential sum is a Vaughan- or Heath--Brown-type identity. It decomposes the coefficients into finite combinations of Type-I and Type-II bilinear sums of the schematic form
\[
\sum_{m\sim M}\sum_{n\sim L}
a_m b_n\,e(\alpha mn),
\qquad ML\asymp N.
\]

For the \(\chi_3\)-twisted channel, the same forms appear with one or both coefficient sequences multiplied by \(\chi_3\).

**This bilinear cancellation estimate—not the spline synthesis—is the first theorem that could move the proof percentage materially.**

---

## 2. A smooth local substitute for the dual

Let \(u>1/2\), and let \(\widetilde\gamma_u\) be the dual of the corrected centered fractional cardinal B-spline family.

T3 used a compact truncation \(\chi_R\widetilde\gamma_u\). For arithmetic estimates, use a further smooth approximation
\[
\psi_{u,R,\varepsilon}\in C_c^\infty(\mathbb R)
\]
chosen so that
\[
\|\widetilde\gamma_u-\psi_{u,R,\varepsilon}\|_2
\le
\delta_u(R,\varepsilon),
\qquad
\delta_u(R,\varepsilon)\to0
\quad(R\to\infty,\;\varepsilon\to0).
\]

This is always possible because \(C_c^\infty(\mathbb R)\) is dense in \(L^2(\mathbb R)\). It creates a genuinely smooth, compact local test window while retaining a separately charged reconstruction error.

Its Fourier transform obeys, for every integer \(A\ge0\),
\[
|\widehat\psi_{u,R,\varepsilon}(\xi)|
\le C_{u,R,\varepsilon,A}(1+|\xi|)^{-A}.
\]

The constants are part of the ledger; no free smoothing is claimed.

---

## 3. OFI-localized additive correlation

Define the local test functional
\[
\mathcal J^{\psi}_{u,R,\varepsilon,E}[F]
=
\langle F,\psi_{u,R,\varepsilon}(\cdot-(E+1))\rangle.
\]

For the spline field built from a sector correlation, this evaluates a compact local average around the Goldbach coordinate. The exact coefficient obeys
\[
\left|
 g_E-
\mathcal J^{\psi}_{u,R,\varepsilon,E}[H_u]
\right|
\le
\|H_u\|_2\,\delta_u(R,\varepsilon).
\]

Thus the minor-arc task can be localized without replacing the coefficient by an uncontrolled smoothed proxy.

---

## 4. The OFI-weighted Type-I / Type-II target

After inserting the smooth local functional and a Vaughan-type identity, the new required estimate is of the form
\[
\boxed{
\sup_{\alpha\in\mathfrak m}
\left|
\sum_{m\sim M}\sum_{n\sim L}
 a_m b_n\,
 W_{u,R,\varepsilon,E}(mn)
 e(\alpha mn)
\right|
\le
C_{u,R,\varepsilon}
N^{1-\delta}
}
\]
for a positive \(\delta\), suitable dyadic ranges \(ML\asymp N\), and coefficient bounds produced by the chosen Mangoldt identity.

Here \(W_{u,R,\varepsilon,E}\) is the explicit finite-difference/localization weight induced by \(\psi_{u,R,\varepsilon}\) and the corrected cardinal fractional spline synthesis.

The proof must show—not assume—that this weight has the derivative, variation, and support properties required by the chosen bilinear-sum method.

---

## 5. What OFI could potentially improve

The fractional order can only help through a demonstrable improvement in one of these quantities:

\[
\|W_{u,R,\varepsilon,E}\|_\infty,
\qquad
\operatorname{Var}(W_{u,R,\varepsilon,E}),
\qquad
\|W_{u,R,\varepsilon,E}^{(k)}\|_1,
\qquad
\text{or a usable Fourier-decay norm.}
\]

That can improve a partial-summation, van der Corput, large-sieve, or bilinear-form estimate.

It cannot help merely because \(\gamma_u\) looks smoother. The reconstruction error
\[
\|H_u\|_2\delta_u(R,\varepsilon)
\]
and any inverse-frame conditioning cost must be included at the end.

---

## 6. Sector structure is retained throughout

The arithmetic experiment must be carried out separately for
\[
(\sigma,\tau)\in\{(+,-),(+,+),(-,-)\}.
\]

Equivalently, it must track both
\[
A_\Lambda=\Lambda-\Lambda_3
\qquad\text{and}\qquad
B_\Lambda=\chi_3\Lambda.
\]

The \(\chi_3\)-twisted Type-II sums are not optional bookkeeping: they are the exact content of the nonzero mod-\(6\) sectors.

---

## 7. A falsifiable OFI advantage criterion

Fix a baseline order \(u_0=2\) (the triangle case). An order \(u\) earns promotion to the proof spine only if one proves a bound such as
\[
\mathcal E^{\mathfrak m}_{u,R,\varepsilon,j}(E)
+
\|H_{u,j}\|_2\delta_u(R,\varepsilon)
\le
\rho
\left[
\mathcal E^{\mathfrak m}_{u_0,R,\varepsilon,j}(E)
+
\|H_{u_0,j}\|_2\delta_{u_0}(R,\varepsilon)
\right]
\]
with a uniform \(\rho<1\) on the required target range.

Anything less is an exploratory parameterization, not a proof improvement.

---

## 8. Why this is the right location for Ruelle, heat, and trig branches

- **Heat/Poisson semigroups:** may generate smooth arc cutoffs or multiscale decompositions of \(W\).
- **Ruelle transfer:** may enter only as a rigorous bound on a specified weighted exponential or bilinear sum.
- **Trigonometric/Euler splines:** may provide a basis for analyzing the oscillatory phase or for constructing explicit smooth windows.
- **Gudermannian/hyperbolic branches:** may parameterize a real-to-circular cutoff family, but must still deliver the same bilinear estimate.

These structures are now allowed as alternate ways to prove the displayed Type-I/II bound. They are not separate proof engines.

---

## 9. The next theorem, in one line

The next theorem worth attacking is:
\[
\boxed{
\text{An OFI-localized, sector-uniform Type-II minor-arc estimate with a positive power saving.}
}
\]

Proving that theorem would be new mathematical progress. Merely defining the OFI window, running numerical tests, or observing smoother plots would not.
