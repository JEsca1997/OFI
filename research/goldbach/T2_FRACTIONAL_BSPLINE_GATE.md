# T2: Fractional B-Spline Stability Gate

**Status:** exact design plus explicit proof obligations.  
**Purpose:** extend the boxcar/triangular Goldbach encoding continuously in OFI order without losing stable recovery of the discrete coefficient sequence.

---

## 1. Reparameterize by semigroup order

The usual fractional B-spline notation uses a degree-like parameter \(\alpha\) with Fourier factor
\[
\widehat{\beta^\alpha}(\xi)
=
\left(\frac{1-e^{-i\xi}}{i\xi}\right)^{\alpha+1}.
\]

For Goldbach, use the **semigroup order**
\[
s=\alpha+1>0
\]
and write the centered symmetric kernel as \(\mathsf B_s\), normalized by
\[
\widehat{\mathsf B_s}(\xi)
=
\left|\frac{2\sin(\xi/2)}{\xi}\right|^s.
\]

At integer values:
\[
\mathsf B_1=b_1\quad\text{(boxcar)},
\qquad
\mathsf B_2=b_2\quad\text{(triangle)}.
\]

The advantage of \(s\) is the exact convolution law
\[
\boxed{\mathsf B_s*\mathsf B_t=\mathsf B_{s+t}.}
\]
This is the fractional continuation of \(B_m*B_n=B_{m+n}\).

---

## 2. Half-shift prime synthesis at arbitrary order

For a finite cutoff \(N\) and branch \(\sigma\in\{+,-\}\), define
\[
\Phi^{(s)}_{\sigma,N}(x)
=
\sum_{r\le N}\theta_\sigma(r)
\mathsf B_s\!\left(x-\left(r+\frac12\right)\right).
\]

For sector \((\sigma,\tau)\), convolution gives the exact synthesis identity
\[
\boxed{
\Phi^{(s)}_{\sigma,N}*\Phi^{(t)}_{\tau,N}(x)
=
\sum_E\mathfrak G^{(N)}_{\sigma,\tau}(E)
\mathsf B_{s+t}(x-(E+1)).
}
\]

The arithmetic coefficient does not change with \(s,t\). Only the reconstruction atom changes.

This is the proper OFI continuation of T1: integer B-splines were not discarded; they are the anchor points in a continuous semigroup.

---

## 3. The real obstruction: stable translate recovery

For noninteger \(s+t\), \(\mathsf B_{s+t}\) is generally not compactly supported, so the finite tridiagonal Gram calculation from the triangular case no longer applies.

Define the bi-infinite translate Gram symbol
\[
P_u(\omega)
=
\sum_{k\in\mathbb Z}
\left|\widehat{\mathsf B_u}(\omega+2\pi k)\right|^2,
\qquad u=s+t.
\]

The required stability statement is
\[
\boxed{
0<A_u\le P_u(\omega)\le B_u<\infty
\quad\text{for all }\omega\in[-\pi,\pi].
}
\]

When this holds, the integer translates of \(\mathsf B_u\) form a stable Riesz sequence in the generated shift-invariant space, and the dual extractor is defined spectrally by
\[
\widehat{\widetilde{\mathsf B}_u}(\omega)
=
\frac{\widehat{\mathsf B_u}(\omega)}{P_u(\omega)}.
\]

Then
\[
\left\langle
\mathsf B_u(\cdot-E),
\widetilde{\mathsf B}_u(\cdot-k)
\right\rangle
=\delta_{Ek}.
\]

### Gate T2-A

Prove the lower bound \(A_u>0\) over an admissible interval of orders \(u\). The Goldbach route cannot use a fractional order merely because it looks OFI-compatible; it must pass this frame-stability condition.

---

## 4. Fractional exact extraction theorem

Assume T2-A for \(u=s+t\). Let
\[
H^{(s,t)}_{\sigma,\tau,N}
=
\Phi^{(s)}_{\sigma,N}*\Phi^{(t)}_{\tau,N}.
\]

Then the coefficient extractor is
\[
\boxed{
\mathfrak G^{(N)}_{\sigma,\tau}(E)
=
\left\langle
H^{(s,t)}_{\sigma,\tau,N},
\widetilde{\mathsf B}_{s+t}(\cdot-(E+1))
\right\rangle.
}
\]

This is exact. No asymptotic prime claim is hidden in it.

---

## 5. Fractional Ostrowski constant

Define the dual-weighted local averaging functional
\[
\mathcal C_{u,E}[H]
=
\langle H,\widetilde{\mathsf B}_u(\cdot-(E+1))\rangle.
\]

A usable local descent inequality is
\[
\left|
\mathcal C_{u,E}[H]-H(E+1)
\right|
\le
\operatorname{Lip}(H)\,M_u,
\]
with
\[
M_u
:=
\int_{\mathbb R}|x|\,
\left|\widetilde{\mathsf B}_u(x)\right|\,dx.
\]

### Gate T2-B

Show \(M_u<\infty\) and obtain a quantitative upper bound on it for the chosen order range. In the triangular base case \(u=2\), the primal-weighted estimate supplied \(M_2=1/3\); for a general dual fractional extractor, the constant must be calculated rather than assumed.

---

## 6. OFI order selection

The order choices serve distinct jobs:

| order | role | status |
|---|---|---|
| \(s=t=1\), \(u=2\) | exact compact triangular base case | proved finite-dimensional |
| \(s=t=3/2\), \(u=3\) | first smoother compact integer comparison | next benchmark |
| \(s=t=1/2\), \(u=1\) | boundary/roughness stress test | diagnostic |
| \(s=t=1+1/24\) | small OFI perturbation near boxcar chain | experimental |
| \(s=t=1+1/12\) | vacuum-marked OFI perturbation | experimental only |
| variable \(s,t\) | optimize stability versus oscillation | after T2-A/T2-B |

The number \(1/12\) is not inserted as a proof weight. It is a designated perturbative order to test against the Bernoulli residual ledger.

Negative orders are excluded from the first proof spine: they amplify high frequencies and can destroy the local stability required for coefficient extraction.

---

## 7. Riesz limit: what is and is not allowed

The OFI PDF gives the structural chain
\[
B_1\to B_n\to\beta^\alpha\xrightarrow[h\to0]\text{Riesz OFI},
\]
and identifies the symmetric fractional limit with a two-sided Riesz kernel.

For Goldbach, the Riesz limit is admissible only after the following commuting-diagram problem is solved:
\[
\begin{array}{ccc}
\text{prime coefficients} &\xrightarrow{\text{spline synthesis}}& H_u\\
\downarrow\text{identity} && \downarrow h\to0\\
\text{same coefficients} &\xleftarrow{\text{stable extraction}}& \text{Riesz-limited field}
\end{array}
\]

The lower horizontal arrow must remain stable, or the continuum limit may erase the discrete coefficient information. The Riesz kernel is therefore a late-stage asymptotic tool, not a replacement for the fractional spline extractor.

---

## 8. Computational falsification matrix

For each \(u\) in a selected compact interval:

1. sample \(P_u(\omega)\) densely on \([-\pi,\pi]\);
2. estimate \(A_u=\inf P_u\), \(B_u=\sup P_u\), and \(B_u/A_u\);
3. construct the finite-section dual extractor;
4. test exact recovery of random sparse nonnegative sequences;
5. test exact recovery of \(\theta_\pm\) coefficients at finite cutoffs;
6. compute \(M_u\) or an upper envelope for it;
7. reject any order whose recovery is ill-conditioned or whose local constant becomes too large.

This identifies a safe fractional-order corridor before attaching any prime-distribution estimate.

---

## 9. What T2 earns

Once T2-A and T2-B are proved, the Goldbach program has a valid OFI continuum of exact arithmetic encodings:
\[
\mathfrak G_j(E)
\longleftrightarrow
\text{fractional B-spline coefficient at every stable order }u.
\]

That makes it legitimate to ask whether a special OFI order improves the major/minor-arc or character-sector estimates. Before T2, such an improvement could be an artifact of noninvertible smoothing.

T2 is therefore the last representation theorem before the genuinely number-theoretic bottleneck begins.