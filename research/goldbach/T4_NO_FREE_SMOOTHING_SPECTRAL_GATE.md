# T4: No-Free-Smoothing Spectral Gate

**Status:** exact identity and proof criterion.  
**Purpose:** identify precisely what fractional B-spline/OFI smoothing can contribute to Goldbach, and rule out a false shortcut.

---

## 1. The exact finite Fourier coefficient

For a finite cutoff \(N\), write
\[
S_{\sigma,N}(\alpha)
=
\sum_{n\le N}\theta_\sigma(n)e(\alpha n),
\qquad e(x)=e^{2\pi i x}.
\]
Then the sector coefficient is exactly
\[
\mathfrak G^{(N)}_{\sigma,\tau}(E)
=
\int_0^1
S_{\sigma,N}(\alpha)
S_{\tau,N}(\alpha)
 e(-\alpha E)\,d\alpha.
\]

This is the arithmetic target. No change of representation may replace it.

---

## 2. Fractional spline synthesis in frequency

Let \(s,t>0\) and let \(\mathsf B_s,\mathsf B_t\) be the centered fractional spline kernels from T2. The half-shifted physical-space fields satisfy
\[
\widehat{\Phi^{(s)}_{\sigma,N}}(\xi)
=e^{i\xi/2}\widehat{\mathsf B_s}(\xi)
\sum_{n\le N}\theta_\sigma(n)e^{-i\xi n}.
\]

Thus the convolved spline field has multiplier
\[
\widehat{H^{(s,t)}_{\sigma,\tau,N}}(\xi)
=e^{i\xi}\widehat{\mathsf B_{s+t}}(\xi)
S_{\sigma,N}\!\left(-\frac{\xi}{2\pi}\right)
S_{\tau,N}\!\left(-\frac{\xi}{2\pi}\right).
\]

The spline factor has damped high-frequency magnitude
\[
\left|\widehat{\mathsf B_{s+t}}(\xi)\right|
\asymp |\xi|^{-(s+t)}
\]
at large frequency. This is genuine regularization of the represented field.

---

## 3. Exact reconstruction necessarily cancels the multiplier

T2-A gives a dual extractor \(\widetilde{\mathsf B}_{s+t}\) satisfying coefficientwise reconstruction. Consequently,
\[
\mathfrak G^{(N)}_{\sigma,\tau}(E)
=
\left\langle H^{(s,t)}_{\sigma,\tau,N},
\widetilde{\mathsf B}_{s+t}(\cdot-(E+1))
\right\rangle.
\]

On the Fourier side, the dual contains the reciprocal Gram factor needed to undo the aliasing and spline attenuation. Therefore:

\[
\boxed{
\text{exact reconstruction does not create a free minor-arc gain.}
}
\]

Any apparent decrease in a smoothed minor-arc norm must be compared with the norm or condition number of the reconstruction operator. A claim of improvement that omits this cost is incomplete.

---

## 4. The only legitimate OFI gain

An OFI spline order \(u=s+t\) is useful only if it yields a bound of the form
\[
\left|
\langle H_u,\widetilde{\mathsf B}_u(\cdot-(E+1))\rangle_{\mathfrak m}
\right|
\le
\mathcal E_u(E)
\]
whose right side is strictly better than the corresponding unsmoothed estimate **after** including the reconstruction cost.

A sufficient comparison target is
\[
\mathcal E_u(E)
\le
C_u E^{1-\delta_u}
\]
with \(\delta_u>0\), while the major term remains bounded below by a positive order-\(E\) contribution after the same extractor is applied.

The gain must survive this complete inequality:
\[
\mathcal M_{u,j}(E)
>
\mathcal E^{\mathrm{minor}}_{u,j}(E)
+
\mathcal E^{\mathrm{EM}}_{u,j}(E)
+
\mathcal E^{\mathrm{Ost}}_{u,j}(E)
+
\mathcal E^{\mathrm{pp}}_j(E).
\]

---

## 5. OFI order as a tunable spectral preconditioner

The correct interpretation of the order \(u\) is not “a special number proves Goldbach.” It is a spectral preconditioner balancing:

\[
\text{high-frequency damping}
\quad\text{against}\quad
\text{dual-extraction amplification}.
\]

Define the finite-cutoff conditioning cost
\[
\kappa_u(N)
=
\frac{\sup_{\omega\in[-\pi,\pi]}P_u(\omega)}
{\inf_{\omega\in[-\pi,\pi]}P_u(\omega)}.
\]

An order is admissible for the spectral experiment only when both quantities are controlled:
\[
\text{damping benefit}(u,N)
\quad\text{and}\quad
\kappa_u(N).
\]

The T2-A bounds provide a crude analytic ceiling:
\[
\kappa_u
le
\frac{1+2(2/\pi)^{2u}(1-2^{-2u})\zeta(2u)}{(2/\pi)^{2u}}
\]
for \(u>1/2\). It is a stability guarantee, not an optimization formula.

---

## 6. Major/minor arc experiment, correctly normalized

Let \(\mathbb T=\mathfrak M\cup\mathfrak m\) be a major/minor-arc split. For every stable order \(u\), evaluate the extracted terms
\[
\mathfrak G_j(E)
=
\mathcal I^{\mathfrak M}_{u,j}(E)
+
\mathcal I^{\mathfrak m}_{u,j}(E),
\]
where each term includes both the spline multiplier and the canonical dual extractor.

The mandatory controls are:

1. **Identity control:** at \(u=2\), extracted totals equal direct convolution exactly.
2. **Order invariance:** extracted totals agree across all stable \(u\), up to numerical precision.
3. **No-free-smoothing control:** compare raw minor-arc damping with extracted minor-arc magnitude after dual recovery.
4. **Sector control:** repeat separately for \(E\equiv0,2,4\pmod6\).
5. **Character control:** repeat for \(A\) and \(B=\chi_3\theta\) channels before recombination.
6. **Conditioning control:** report \(\kappa_u(N)\) with every claimed gain.

---

## 7. Where the \(1/12\) order belongs

The order
\[
u=2+\frac1{12}
\]
is a valid experiment point because it is within the stable corridor and is near the triangular base order. But it has no privileged arithmetic status until the complete extracted error bound improves.

Use it as a test point alongside
\[
\nu\in\left\{1,\frac32,2,2+\frac1{24},2+\frac1{12},3\right\}.
\]

The Bernoulli \(1/12\) correction remains in the Euler--Maclaurin residual ledger. The spline order \(2+1/12\) is a separate analytic choice; the two must not be identified without a theorem.

---

## 8. Consequence for the proof program

T1 and T2 establish a lossless OFI-native representation of Goldbach coefficients. T4 says exactly what still has to happen:

\[
\boxed{
\text{find a fractional order and sector estimate whose post-reconstruction error is smaller.}
}
\]

If no such order exists, fractional splines remain a stable representation and diagnostic tool, but they do not advance the number-theoretic proof. If one exists and yields a uniform quantitative major/minor inequality, it becomes the OFI-specific arithmetic contribution.

This is the correct transition from representation theory to the actual Goldbach bottleneck.