# Explicit-Formula Bridge: From Prime-Only Goldbach to Zeta and \(L(s,\chi_3)\)

**Status:** exact reduction and quantitative certification criterion. This document does not prove the required lower bound.

---

## 1. Why \(\Lambda\) is the spectral entry point

The prime-only weight \(\theta\) is the correct final observable for strong Goldbach, but the von Mangoldt weight \(\Lambda\) is the one directly encoded by standard spectral/Dirichlet data:
\[
-\frac{\zeta'}{\zeta}(s)=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad \Re s>1.
\]

For the nontrivial real Dirichlet character modulo \(3\),
\[
\chi_3(n)=
\begin{cases}
0,&3\mid n,\\
1,&n\equiv1\pmod3,\\
-1,&n\equiv2\pmod3,
\end{cases}
\]
one likewise has
\[
-\frac{L'}{L}(s,\chi_3)=\sum_{n\ge1}\frac{\chi_3(n)\Lambda(n)}{n^s},
\qquad \Re s>1.
\]

Thus the two arithmetic sequences
\[
\Lambda(n),\qquad \chi_3(n)\Lambda(n)
\]
are the exact ordinary and twisted spectral observables relevant to the mod-\(3\) sector split.

---

## 2. Additive Goldbach correlation with \(\Lambda\)

Define
\[
R_\Lambda(E):=\sum_{a+b=E}\Lambda(a)\Lambda(b).
\]
At finite cutoff \(N\ge E\), set
\[
T_N(\alpha):=\sum_{n\le N}\Lambda(n)e(\alpha n).
\]
Then Fourier inversion gives the exact identity
\[
R_\Lambda(E)=\int_0^1T_N(\alpha)^2e(-\alpha E)\,d\alpha.
\]

The role of the analytic machinery is now precise: it may work through \(\zeta\), \(L(s,\chi_3)\), Mellin transforms, Riesz multipliers, or a transfer operator, but it must eventually deliver a lower bound for this additive coefficient or its sector-refined analogue.

---

## 3. Prime powers are the only gap between \(\Lambda\) and \(\theta\)

Set
\[
P(n):=\Lambda(n)-\theta(n).
\]
Then \(P(n)\ne0\) precisely at non-prime prime powers \(n=p^k\) with \(k\ge2\), and
\[
0\le P(n)\le\log n.
\]
Consequently,
\[
R_\Lambda(E)-G(E)
=(\theta*P)(E)+(P*\theta)(E)+(P*P)(E),
\]
where
\[
G(E):=(\theta*\theta)(E).
\]

This identity is exact.

---

## 4. Prime-power stripping lemma

Let \(Q(E)\) denote the number of non-prime prime powers at most \(E\). For \(E\ge16\), the elementary bound
\[
Q(E)\le2\sqrt E
\]
is sufficient for the present purpose: squares contribute at most \(\sqrt E\), and all higher powers contribute at most a further \(\sqrt E\).

Since every nonzero term in \(\theta\), \(P\), or \(\Lambda\) is at most \(\log E\),
\[
0\le R_\Lambda(E)-G(E)\le 8\sqrt E(\log E)^2
\qquad(E\ge16).
\]

The constant \(8\) is deliberately loose; only the \(O(\sqrt E\log^2E)\) scale matters here.

### Consequence

If one proves
\[
R_\Lambda(E)>8\sqrt E(\log E)^2
\]
for every sufficiently large even \(E\), then
\[
G(E)>0,
\]
and therefore every such \(E\) is a sum of two primes.

This is the correct way to turn a \(\Lambda\)-weighted analytic estimate into a strong-Goldbach certificate. Mere positivity of \(R_\Lambda(E)\) is not enough, because it could be supported only by prime powers.

---

## 5. Character-sector version

The character decomposition from `CHARACTER_SECTOR_REDUCTION.md` is prime-only. The same analytic plan must control the ordinary and twisted Mangoldt sums
\[
T_N(\alpha)=\sum_{n\le N}\Lambda(n)e(\alpha n),
\qquad
T_{\chi,N}(\alpha)=\sum_{n\le N}\chi_3(n)\Lambda(n)e(\alpha n).
\]

A sector theorem must therefore do two things:

1. prove a positive main term for the relevant ordinary/twisted combination; and
2. bound its error strongly enough to exceed both the minor-arc contribution and the prime-power stripping allowance \(8\sqrt E\log^2E\).

For the mixed branch, the necessary output can be written schematically as
\[
\frac14\,[A*A-B*B](E)>0,
\]
where \(A=\theta-\theta_3\) and \(B=\chi_3\theta\). A \(\Lambda\)-based route must first establish the analogous bound, then subtract the prime-power error explicitly.

---

## 6. OFI compatibility test

The continuous Riesz potential in the existing OFI derivation has Fourier multiplier \(|\xi|^{-\alpha}\). That multiplier does not by itself encode \(\Lambda\), \(\theta\), \(\zeta\), or the Dirichlet character. Therefore its admissible role here is limited:

- it may regularize or reweight a transform of \(T_N\) or \(T_{\chi,N}\);
- it may not be treated as a prime detector; and
- any claimed OFI advance must prove a quantitative inequality for these exact exponential sums after the reweighting.

The minimal theorem to target is:
\[
\left|\operatorname{Err}_{\mathrm{OFI}}(E)\right|
\le \operatorname{Main}_{\mathrm{OFI}}(E)-8\sqrt E(\log E)^2-\varepsilon_E,
\qquad \varepsilon_E>0.
\]
Only then does the OFI route pass from a spectral regularization to a strong-Goldbach proof.

---

## 7. Research status after this bridge

The proof problem is now reduced to a familiar but fully explicit analytic demand: obtain a sufficiently strong lower bound for a binary additive \(\Lambda\)-correlation, including the mod-\(3\) character sector, and beat the stated prime-power remainder. No geometric vocabulary can replace that inequality.
