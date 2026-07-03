# Goldbach Operator Core: Exact Identities and the Remaining Global Inequality

**Status:** rigorous reduction plus finite-verification interface. This document proves exact identities. It does **not** prove the global positive lower bound required for Goldbach.

---

## 1. Prime-only observable

Define the Chebyshev prime weight
\[
\theta(n)=
\begin{cases}
\log n,& n\text{ is prime},\\
0,&\text{otherwise}.
\end{cases}
\]

For primes larger than \(3\), split it into the two mod-\(6\) branches
\[
\theta_+(n)=\theta(n)\mathbf 1_{n\equiv1\,(\mathrm{mod}\,6)},
\qquad
\theta_-(n)=\theta(n)\mathbf 1_{n\equiv-1\,(\mathrm{mod}\,6)}.
\]

The exceptional prime \(3\) is handled separately. Define
\[
\theta_3(n)=(\log 3)\mathbf 1_{n=3},
\qquad
\theta=\theta_3+\theta_++\theta_-.
\]

This is the non-negotiable arithmetic input: the operator begins from an observable that is supported **exactly** on primes, not merely on \(6n\pm1\) candidates.

---

## 2. The sector convolution operator

Let \(\ell^1(\mathbb N)\) carry additive convolution
\[
(f*g)(E):=\sum_{a+b=E}f(a)g(b).
\]

Define the three admissible Goldbach-sector observables
\[
\mathfrak G_0:=\theta_+*\theta_-,
\qquad
\mathfrak G_2:=\theta_+*\theta_+,
\qquad
\mathfrak G_4:=\theta_-*\theta_-.
\]

For every even \(E>6\):

\[
\mathfrak G_0(E)>0
\Longleftrightarrow
E=p+q\text{ for primes }p\equiv1,\ q\equiv-1\pmod6,
\quad E\equiv0\pmod6,
\]
\[
\mathfrak G_2(E)>0
\Longleftrightarrow
E=p+q\text{ for primes }p,q\equiv1\pmod6,
\quad E\equiv2\pmod6,
\]
\[
\mathfrak G_4(E)>0
\Longleftrightarrow
E=p+q\text{ for primes }p,q\equiv-1\pmod6,
\quad E\equiv4\pmod6.
\]

### Proof

Every summand in a sector convolution is nonnegative. It is positive exactly when both indices are prime and lie on the specified branches. Thus a positive sum is equivalent to at least one matching prime pair. Conversely, any matching prime pair contributes \((\log p)(\log q)>0\). The residue identities force the stated target class. \(\square\)

This proposition supplies the previously missing “prime indicator bridge,” but only by explicitly using \(\theta\). It is an exact bookkeeping identity, not yet an asymptotic lower bound.

---

## 3. Circle/Fourier realization

For a finitely supported sequence \(f\), write
\[
\widehat f(\alpha)=\sum_{n\ge1}f(n)e(\alpha n),
\qquad e(x)=e^{2\pi i x},
qquad \alpha\in\mathbb T=\mathbb R/\mathbb Z.
\]

Then Fourier inversion gives the exact coefficient identity
\[
(f*g)(E)=\int_0^1\widehat f(\alpha)\widehat g(\alpha)e(-\alpha E)\,d\alpha.
\]

Applying this to the three sectors yields
\[
\mathfrak G_0(E)=\int_0^1 S_+(\alpha)S_-(\alpha)e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_2(E)=\int_0^1 S_+(\alpha)^2e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_4(E)=\int_0^1 S_-(\alpha)^2e(-\alpha E)\,d\alpha,
\]
where
\[
S_\pm(\alpha)=\sum_{n\ge1}\theta_\pm(n)e(\alpha n)
\]
with the sums truncated at any \(N\ge E\) when evaluating the coefficient at \(E\).

This is an exact operator-level bridge: the Goldbach problem is equivalent to positivity of explicit Fourier coefficients of the sector products.

---

## 4. A concrete \(V_4\) realization

Let
\[
\mathcal H=\ell^2(W_+)\oplus\ell^2(W_-),
\]
where \(W_+=\{n:n\equiv1\pmod6\}\) and \(W_-=\{n:n\equiv-1\pmod6\}\). Define the branch involution \(J\) on coefficient labels by
\[
J(6k+1)=6k-1,
\qquad
J(6k-1)=6k+1
\]
where the index ranges are adjusted to stay in positive integers. Let \(\varepsilon\) be the sign involution on the two summands. Then the commuting involutions \(J\) and \(\varepsilon\) generate a representation of \(V_4\).

The sector products \((+,-),(+,+),(-,-)\) are the three branch-pair channels. This gives a precise algebraic sorting action, but it does not generate primality: primality is carried by \(\theta_\pm\).

---

## 5. OFI-compatible smoothing: what can be proved immediately

Let \(m_t(n)\) be any real multiplier satisfying
\[
0<m_t(n)\le1,
\qquad m_t(n)\to1\quad(t\downarrow0).
\]
Define a diagonal smoothing semigroup on sequences,
\[
(\mathcal K_t f)(n)=m_t(n)f(n).
\]
For example, the heat multiplier is \(m_t(n)=e^{-tn^2}\). Define the smoothed sector coefficient
\[
\mathfrak G_{j,t}(E):=((\mathcal K_t\theta_{\sigma})*(\mathcal K_t\theta_{\tau}))(E).
\]

Because every summand is nonnegative,
\[
\mathfrak G_{j,t}(E)>0
quad\Longleftrightarrow\quad
\mathfrak G_j(E)>0
\]
for every fixed \(t>0\), provided \(m_t(n)>0\) on the finite range \(1\le n<E\).

Thus positive diagonal smoothing preserves the **existence** of a Goldbach representation. It does not create one, and it does not prove a lower bound uniform in \(E\). This is the valid entry point for an OFI/Riesz-style multiplier: it must retain coefficientwise positivity and then supply quantitative estimates.

---

## 6. The one theorem still needed for a proof

A complete proof above a threshold \(E_0\) would follow from the following explicitly falsifiable statement:

> **Uniform sector lower bound.** There exist \(E_0\) and constants \(c>0\), \(\delta>0\) such that for every even \(E\ge E_0\), in its admissible sector \(j\),
> \[
> \mathfrak G_j(E)
> \ge cE-CE^{1-\delta}>0.
> \]
> Equivalently, in a major/minor-arc decomposition,
> \[
> \mathfrak G_j(E)=\operatorname{Main}_j(E)+\operatorname{Err}_j(E),
> \]
> with \(\operatorname{Main}_j(E)\ge cE\) and \(|\operatorname{Err}_j(E)|\le CE^{1-\delta}\).

The exact magnitude of the main term can be normalized differently depending on the weight and truncation; the decisive feature is a strictly positive main term that dominates the error uniformly.

---

## 7. Honest status after this reduction

The prime-observable and coefficient-identity gates are now specified exactly. What remains is the hardest part of Goldbach: a uniform estimate proving the relevant Fourier coefficient cannot vanish for arbitrarily large even \(E\).

No Riesz, Ruelle, Bell, Ricci-flow, or vacuum argument may be credited toward completion unless it proves a bound of the form in Section 6 for this exact \(\mathfrak G_j(E)\).
