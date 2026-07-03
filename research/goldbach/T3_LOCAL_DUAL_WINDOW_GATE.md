# T3: Local Dual-Window Descent Gate

**Status:** exact Hilbert-space certificate; arithmetic positivity estimate remains open.  
**Purpose:** replace the overly strong requirement of a global first moment for the fractional canonical dual with a controlled compact-window approximation.

---

## 1. Starting point: exact fractional extraction

Let \(u>1/2\) lie in the stable fractional-spline corridor. For a finite cutoff \(N\), the sector field has the form
\[
H_u(x)
=
\sum_{E\in I}g_E\,\mathsf B_u(x-(E+1)),
\qquad
 g_E=\mathfrak G^{(N)}_{\sigma,\tau}(E).
\]

Let \(\widetilde{\mathsf B}_u\) be the canonical dual. Exact extraction is
\[
g_E
=
\langle H_u,\widetilde{\mathsf B}_u(\cdot-(E+1))\rangle_{L^2}.
\]

This identity is lossless, but the dual need not be compactly supported. That is why a naive pointwise Ostrowski estimate may impose more decay than the proof actually needs.

---

## 2. Compact local dual windows

For \(R>0\), choose a compactly supported cutoff \(\chi_R\) with
\[
0\le\chi_R\le1,
\qquad
\chi_R(x)=1\ \text{for }|x|\le R,
\qquad
\chi_R(x)=0\ \text{for }|x|\ge R+1.
\]

Define the truncated dual window
\[
\widetilde{\mathsf B}_{u,R}(x)
:=
\chi_R(x)\widetilde{\mathsf B}_u(x).
\]

The computable local estimator is
\[
\mathcal C_{u,R,E}[H_u]
=
\langle H_u,
\widetilde{\mathsf B}_{u,R}(\cdot-(E+1))
\rangle.
\]

It depends only on the field inside a fixed local window around the target Goldbach coordinate.

---

## 3. Exact truncation certificate

By Cauchy--Schwarz,
\[
\begin{aligned}
|g_E-\mathcal C_{u,R,E}[H_u]|
&=
\left|
\langle H_u,
(1-\chi_R)\widetilde{\mathsf B}_u(\cdot-(E+1))
\rangle
\right|\\
&\le
\|H_u\|_{L^2}
\,\varepsilon_u(R),
\end{aligned}
\]
where
\[
\varepsilon_u(R)
:=
\|(1-\chi_R)\widetilde{\mathsf B}_u\|_{L^2}.
\]

Because the canonical dual belongs to \(L^2\),
\[
\varepsilon_u(R)\to0
\qquad(R\to\infty).
\]

Thus:

\[
\boxed{
 g_E\ge
 \mathcal C_{u,R,E}[H_u]
-
\|H_u\|_2\varepsilon_u(R).
}
\]

This is an unconditional finite-cutoff certificate. It does not use a global first moment or assert a pointwise sample approximation.

---

## 4. Adding an external approximation

Suppose a major/minor-arc, Ruelle, heat-kernel, or OFI calculation supplies an approximating field \(\widehat H_u\) with
\[
\|H_u-\widehat H_u\|_2\le\eta_u(N).
\]
Then
\[
\left|
\mathcal C_{u,R,E}[H_u]
-
\mathcal C_{u,R,E}[\widehat H_u]
\right|
\le
\eta_u(N)
\,\|\widetilde{\mathsf B}_{u,R}\|_2.
\]
Therefore
\[
\boxed{
 g_E\ge
\mathcal C_{u,R,E}[\widehat H_u]
-
\eta_u(N)\|\widetilde{\mathsf B}_{u,R}\|_2
-
\|H_u\|_2\varepsilon_u(R).
}
\]

A positive right side certifies \(g_E>0\), hence an actual prime-pair representation in the corresponding sector.

---

## 5. Relation to Ostrowski

This is the Hilbert-space version of the local-descent idea:

\[
\text{global spline field}
\to
\text{local window functional}
\to
\text{exact coefficient with explicit tail error}.
\]

A classical Ostrowski inequality can still be used when additional regularity is available, for example to estimate the local functional by a center sample or local average. But it is no longer a structural bottleneck.

The proof program should use the stronger of two valid routes:

1. **Lipschitz/Ostrowski route** for compact integer splines, where a first-moment constant is explicit.
2. **L2 local-dual route** for fractional splines, where the truncation error \(\varepsilon_u(R)\) is explicit and tends to zero.

---

## 6. Why this is the correct T1/compactness interface

For each fixed \(R\), the test window is compactly supported. The family of local windows indexed by target \(E\) is a countable translate cover of the coefficient lattice.

At finite cutoff, only finitely many windows are active. At the infinite level, the relevant control is not an unsupported claim that prime coefficients themselves form a compact set; it is the controlled exhaustion
\[
R\uparrow\infty,
\qquad
N\uparrow\infty,
\]
with
\[
\varepsilon_u(R)\to0.
\]

This gives the topology language a real analytic task: compact local supports and a convergent exhaustion of the dual tail.

---

## 7. The new arithmetic target

T3 reduces the OFI Goldbach problem to finding an approximating field \(\widehat H_u\) such that, uniformly for the required sectors,
\[
\mathcal C_{u,R,E}[\widehat H_u]
>
\eta_u(N)\|\widetilde{\mathsf B}_{u,R}\|_2
+
\|H_u\|_2\varepsilon_u(R).
\]

This is the precise post-reconstruction inequality.

The fractional spline machinery has now done all it can do structurally:

- exact encoding;
- stable extraction;
- compact local certificate;
- an explicit reconstruction-tail ledger.

The remaining issue is entirely arithmetic: construct a major-arc lower estimate and a minor-arc/character-error bound strong enough to make the displayed inequality positive.

---

## 8. Immediate experimental protocol

For each stable order \(u\) and cutoff \(N\):

1. compute the finite-sector coefficient sequence \(g\) directly;
2. construct a finite-section approximation to the canonical dual;
3. record \(\varepsilon_u(R)\) versus \(R\);
4. evaluate the local estimator \(\mathcal C_{u,R,E}\);
5. test the exact certificate against direct coefficients;
6. only then substitute a spectral approximation \(\widehat H_u\).

This keeps numerical experiments honest: the local window is permitted to approximate the dual, but its reconstruction tail is always charged to the error budget.
