# Character-Sector Reduction for the Goldbach Dream Kernel

**Status:** exact algebraic reduction. It isolates the three \(6n\pm1\) sectors as ordinary and mod-\(3\)-twisted prime correlations. It does not bound those correlations.

---

## 1. The nontrivial character modulo \(3\)

Define the real Dirichlet character
\[
\chi_3(n)=
\begin{cases}
0,&3\mid n,\\
1,&n\equiv1\pmod3,\\
-1,&n\equiv2\pmod3.
\end{cases}
\]

Let
\[
A(n):=\theta(n)-\theta_3(n),
\qquad
B(n):=\chi_3(n)\theta(n).
\]
Since every prime \(p>3\) is odd and is congruent to either \(1\) or \(-1\pmod6\),
\[
\theta_+(n)=\frac{A(n)+B(n)}2,
\qquad
\theta_-(n)=\frac{A(n)-B(n)}2.
\]

### Proof

For a prime \(p>3\), \(\chi_3(p)=+1\) precisely when \(p\equiv1\pmod6\), and \(\chi_3(p)=-1\) precisely when \(p\equiv-1\pmod6\). At \(p=3\), both \(A\) and \(B\) vanish. \(\square\)

---

## 2. Exact sector identities

Using commutativity of additive convolution,
\[
\mathfrak G_0=\theta_+*\theta_-=\frac14\bigl(A*A-B*B\bigr),
\]
\[
\mathfrak G_2=\theta_+*\theta_+=\frac14\bigl(A*A+2A*B+B*B\bigr),
\]
\[
\mathfrak G_4=\theta_-*\theta_-=\frac14\bigl(A*A-2A*B+B*B\bigr).
\]

These are identities of finitely truncated sequences, hence coefficientwise identities at every fixed target \(E\).

The \(V_4\) branch language can therefore be read as the simultaneous decomposition into the trivial and nontrivial \(\mathbb Z/3\mathbb Z\)-character components. This makes the branch split arithmetic rather than merely pictorial.

---

## 3. Fourier form

For cutoff \(N\), let
\[
S_{A,N}(\alpha)=\sum_{n\le N}A(n)e(\alpha n),
\qquad
S_{B,N}(\alpha)=\sum_{n\le N}B(n)e(\alpha n).
\]
Then for \(N\ge E\),
\[
\mathfrak G_0(E)=\frac14\int_0^1\left(S_{A,N}(\alpha)^2-S_{B,N}(\alpha)^2\right)e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_2(E)=\frac14\int_0^1\left(S_{A,N}(\alpha)+S_{B,N}(\alpha)\right)^2e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_4(E)=\frac14\int_0^1\left(S_{A,N}(\alpha)-S_{B,N}(\alpha)\right)^2e(-\alpha E)\,d\alpha.
\]

This identifies the actual analytic task: control both an ordinary prime exponential sum and its \(\chi_3\)-twist, with a lower bound that survives their possible cancellation in the mixed channel \(\mathfrak G_0\).

---

## 4. What this removes—and what it does not

### Removed ambiguity

- The exact meaning of the \(+\) and \(-\) tracks.
- The exceptional role of the prime \(3\).
- The claim that \(V_4\) needs to “detect” primes: the prime support is already in \(\theta\), while \(V_4\)/characters sort it.

### Still open

The identities do **not** imply positivity. In particular, even though \(A*A\) and \(B*B\) are individually structured, their coefficientwise difference need not be positive without a quantitative estimate. The Goldbach difficulty is exactly the needed uniform lower bound for these coefficients.

---

## 5. Next admissible OFI target

An OFI/Riesz/Ruelle operator can now be judged against a concrete target. It must yield a bound on the pair
\[
(S_{A,N},S_{B,N})
\]
strong enough to prove, in the appropriate residue class,
\[
\frac14[A*A-B*B](E)>0,
\]
or the corresponding \((A\pm B)^2/4\) coefficient. Any proposed “spectral gap,” smoothing, or pressure invariant that does not enter these two explicit character components is external to the Goldbach proof.
