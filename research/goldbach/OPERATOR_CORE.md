# Goldbach Operator Core: Exact Identities and the Remaining Global Inequality

**Status:** rigorous finite-cutoff reduction plus finite-verification interface. This document proves exact identities; it does **not** prove the global lower bound required for Goldbach.

---

## 1. Prime-only observable

Define the Chebyshev prime weight
\[
\theta(n)=
\begin{cases}
\log n,&n\text{ prime},\\
0,&\text{otherwise}.
\end{cases}
\]
For each cutoff \(N\), define the finitely supported sequence
\[
\theta^{(N)}(n):=\theta(n)\mathbf1_{1\le n\le N}.
\]

For primes larger than \(3\), split it into mod-\(6\) branches:
\[
\theta^{(N)}_+(n)=\theta^{(N)}(n)\mathbf1_{n\equiv1\,(\mathrm{mod}\,6)},
\qquad
\theta^{(N)}_-(n)=\theta^{(N)}(n)\mathbf1_{n\equiv-1\,(\mathrm{mod}\,6)}.
\]
The exceptional prime is
\[
\theta^{(N)}_3(n)=(\log3)\mathbf1_{n=3\le N},
\qquad
\theta^{(N)}=\theta^{(N)}_3+\theta^{(N)}_++\theta^{(N)}_-.
\]

This is the non-negotiable arithmetic input: the observable is supported **exactly** on primes, not on the full \(6n\pm1\) candidate lattice.

---

## 2. Sector convolution operator

For finitely supported sequences, let
\[
(f*g)(E):=\sum_{a+b=E}f(a)g(b).
\]
For \(N\ge E\), define
\[
\mathfrak G_{0,N}:=\theta^{(N)}_+*\theta^{(N)}_-,\qquad
\mathfrak G_{2,N}:=\theta^{(N)}_+*\theta^{(N)}_+,\qquad
\mathfrak G_{4,N}:=\theta^{(N)}_-*\theta^{(N)}_-.
\]
For fixed \(E\), these stabilize once \(N\ge E\); write the stable value as \(\mathfrak G_j(E)\).

For every even \(E>6\),
\[
\mathfrak G_0(E)>0\Longleftrightarrow E=p+q,\quad p\equiv1,\ q\equiv-1\pmod6,\quad E\equiv0\pmod6,
\]
\[
\mathfrak G_2(E)>0\Longleftrightarrow E=p+q,\quad p,q\equiv1\pmod6,\quad E\equiv2\pmod6,
\]
\[
\mathfrak G_4(E)>0\Longleftrightarrow E=p+q,\quad p,q\equiv-1\pmod6,\quad E\equiv4\pmod6.
\]

### Proof

Every summand is nonnegative, and is positive exactly when both indices are prime in the designated branches. Conversely a matching prime pair contributes \((\log p)(\log q)>0\). \(\square\)

This closes the **definition-level** prime-indicator gap, but supplies no uniform lower bound.

---

## 3. Exact circle/Fourier realization

For finitely supported \(f\), set
\[
\widehat f(\alpha)=\sum_{n\ge1}f(n)e(\alpha n),\qquad e(x)=e^{2\pi i x},\qquad \alpha\in\mathbb T=\mathbb R/\mathbb Z.
\]
Then
\[
(f*g)(E)=\int_0^1\widehat f(\alpha)\widehat g(\alpha)e(-\alpha E)\,d\alpha.
\]
Thus, for \(N\ge E\),
\[
\mathfrak G_{0,N}(E)=\int_0^1S_{+,N}(\alpha)S_{-,N}(\alpha)e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_{2,N}(E)=\int_0^1S_{+,N}(\alpha)^2e(-\alpha E)\,d\alpha,
\]
\[
\mathfrak G_{4,N}(E)=\int_0^1S_{-,N}(\alpha)^2e(-\alpha E)\,d\alpha,
\]
where \(S_{\pm,N}=\widehat{\theta^{(N)}_\pm}\).

This is the exact coefficient bridge. The global problem is proving these coefficients are positive for every admissible even \(E\).

---

## 4. Concrete \(V_4\) sorting representation

Let
\[
\mathcal H=\ell^2(\{6k+1:k\ge1\})\oplus\ell^2(\{6k-1:k\ge1\}).
\]
On basis vectors \(e_{k,+},e_{k,-}\), define
\[
Je_{k,+}=e_{k,-},\quad Je_{k,-}=e_{k,+},\qquad Ke_{k,\pm}=(-1)^ke_{k,\pm}.
\]
Then \(J^2=K^2=I\) and \(JK=KJ\), so \(\{I,J,K,JK\}\cong V_4\). The sectors \((+,-),(+,+),(-,-)\) are the branch-pair channels.

This is an exact sorting symmetry; it does not manufacture primality, which remains entirely in \(\theta_\pm\).

---

## 5. OFI-compatible positive smoothing

Let \(m_t(n)\) satisfy
\[
0<m_t(n)\le1,\qquad m_t(n)\to1\ (t\downarrow0),
\]
and define \((\mathcal K_tf)(n)=m_t(n)f(n)\). For example, \(m_t(n)=e^{-tn^2}\).

For a sector \(j=(\sigma,\tau)\), define
\[
\mathfrak G_{j,t}(E)=((\mathcal K_t\theta_\sigma)*(\mathcal K_t\theta_\tau))(E).
\]
Since every contributing summand is multiplied by a strictly positive factor,
\[
\mathfrak G_{j,t}(E)>0\Longleftrightarrow\mathfrak G_j(E)>0.
\]
Positive diagonal smoothing preserves the existence of representations, but cannot create a representation or prove a uniform lower bound.

---

## 6. The one theorem still needed

A proof above a threshold \(E_0\) follows from an explicit bound: there exist \(c,C,\delta>0\) such that for every sufficiently large admissible even \(E\),
\[
\mathfrak G_j(E)\ge cE-CE^{1-\delta}>0.
\]
Equivalently,
\[
\mathfrak G_j(E)=\operatorname{Main}_j(E)+\operatorname{Err}_j(E),
\]
with a positive uniform main term dominating the absolute error.

No Riesz, Ruelle, Bell, Ricci-flow, or vacuum component counts toward a Goldbach proof unless it proves this bound for the exact prime-only coefficients above.
