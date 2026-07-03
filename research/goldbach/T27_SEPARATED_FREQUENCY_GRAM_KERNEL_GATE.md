# T27: Separated-Frequency Gram Kernel Gate

**Status:** exact dual/Gram reduction for the T26 large-values route; no large-sieve improvement is claimed.  
**Purpose:** identify the precise matrix kernel whose norm must be improved to obtain the Z-L far-minor large-values bound.

---

## 1. Coefficient form of the localized bilinear product

Write
\[
F(\alpha)=\mathcal B_1(\alpha)\mathcal B_2(\alpha)
=\sum_{n\in\mathbb Z}C(n)e(\alpha n),
\]
with \(C(n)\) supported in an interval of length \(O(X)\) after the dyadic ranges are fixed.

Let
\[
\mathcal A=\{\alpha_1,\dots,\alpha_J\}
\subset\operatorname{supp}(w)
\]
be a \(\delta\)-separated set in \(\mathbb T\):
\[
\|\alpha_i-\alpha_j\|_{\mathbb T}\ge\delta
\qquad(i\ne j).
\]

The discrete large-values quantity is
\[
\sum_{j=1}^J|F(\alpha_j)|^2.
\]

---

## 2. Exact primal Gram expansion

Expanding the square gives
\[
\begin{aligned}
\sum_{j=1}^J|F(\alpha_j)|^2
&=
\sum_{n,m}C(n)\overline{C(m)}
\sum_{j=1}^Je\bigl(\alpha_j(n-m)\bigr)\\
&=
\boxed{
\sum_{n,m}C(n)\overline{C(m)}\,K_{\mathcal A}(n-m),
}
\end{aligned}
\]
where
\[
K_{\mathcal A}(h):=\sum_{j=1}^Je(\alpha_j h).
\]

This is the exact Gram form in coefficient coordinates.

The diagonal \(n=m\) contributes
\[
J\sum_n|C(n)|^2.
\]
The off-diagonal terms require cancellation in the sampling kernel \(K_{\mathcal A}(h)\) against the actual additive coefficient correlations.

---

## 3. Exact dual Gram expansion

For arbitrary complex \(z_1,\dots,z_J\), define
\[
\mathcal G(z)
:=
\sum_n\left|\sum_{j=1}^Jz_je(\alpha_j n)\right|^2.
\]

If the \(n\)-sum runs over an interval \(I\) of length \(N_I\asymp X\), then
\[
\mathcal G(z)
=
\sum_{i,j}z_i\overline{z_j}\,D_I(\alpha_i-\alpha_j),
\]
where
\[
D_I(\theta):=\sum_{n\in I}e(\theta n)
\]
is the interval Dirichlet kernel.

Thus the sampling operator norm is exactly the spectral norm of the matrix
\[
\boxed{
\mathbf D_{ij}=D_I(\alpha_i-\alpha_j).
}
\]

The standard large-sieve bound controls this norm by the spacing scale:
\[
\sum_{j=1}^J|F(\alpha_j)|^2
\ll (X+\delta^{-1})\sum_n|C(n)|^2.
\]

This is a baseline inequality, not the required density-one saving.

---

## 4. Why the baseline large sieve does not close Z-L

The baseline estimate retains the full coefficient energy
\[
\sum_n|C(n)|^2,
\]
which is precisely the zero-shift collision quantity isolated in T24. If that energy is of natural order \(X^3\), then multiplying it by \(X+\delta^{-1}\) is far too costly for the target
\[
\sum_{\alpha_j\in\mathcal A}|F(\alpha_j)|^2
\ll X^{3-\eta}\delta^{-1}.
\]

Therefore ordinary frequency spacing alone does not produce the needed result. The proof must use additional structure in \(C=A*B\), the far-minor placement of the \(\alpha_j\), or both.

---

## 5. Bilinear expansion of the Gram form

For
\[
C(n)=\sum_{x+y=n}A(x)B(y),
\]
the primal Gram form becomes
\[
\sum_{j=1}^J|F(\alpha_j)|^2
=
\sum_{x,y,x',y'}
A(x)B(y)\overline{A(x')B(y')}
K_{\mathcal A}(x+y-x'-y').
\]

Equivalently, in Type-II variables,
\[
\boxed{
\sum_{j=1}^J|F(\alpha_j)|^2
=
\sum_{m,n,u,v\atop m',n',u',v'}
 a_{m,n}b_{u,v}\overline{a_{m',n'}b_{u',v'}}
 K_{\mathcal A}(mn+uv-m'n'-u'v').
}
\]

This is the separated-frequency analogue of T21. The difference is that the shift is now weighted by the sampling kernel \(K_{\mathcal A}\), rather than by a fixed finite Fejér coefficient.

---

## 6. Far-minor geometry must enter the kernel estimate

The condition \(\alpha_j\in\operatorname{supp}(w)\) says that each sample point avoids the rational neighborhoods used in T20. That information is absent from the generic bound
\[
|D_I(\alpha_i-\alpha_j)|\le\min\{X,\|\alpha_i-\alpha_j\|_{\mathbb T}^{-1}\}.
\]

A proof-moving estimate must exploit more than pairwise separation. It needs a statement of the schematic type
\[
\boxed{
\sum_{i,j}z_i\overline{z_j}
\mathcal K_{\rm bil}(\alpha_i,\alpha_j)
\ll X^{3-\eta}\delta^{-1}\sum_i|z_i|^2,
}
\]
where \(\mathcal K_{\rm bil}\) is the coefficient-sensitive bilinear kernel obtained after the Type-I/II and gcd-lattice structure is inserted.

This is stronger than the ordinary Dirichlet-kernel large sieve because it must see the cancellation of the actual arithmetic coefficients on far-minor frequency differences.

---

## 7. Concrete operator target

For a chosen dyadic Type-II block, define the bilinear sampling operator
\[
(\mathsf T_{\mathcal A}c)_j
:=
\sum_{m\sim M}\sum_{n\sim L}
c_{m,n}e(\alpha_jmn).
\]

A useful estimate has the form
\[
\boxed{
\|\mathsf T_{\mathcal A}c\|_{\ell^2(\mathcal A)}^2
\ll
\delta^{-1}X^{1-\eta_1}\|c\|_2^2
+
\mathcal R_{\rm structured}(c;\mathcal A),
}
\]
where the remainder is small enough after the second bilinear factor and the chosen decomposition are restored.

The precise normalization depends on the coefficient ranges and must be checked in the implementation. The point is structural: the gain must occur before the full \(C=A*B\) collision energy is formed.

---

## 8. Relation to the T23 lattice fibers

The product-difference kernel in Section 5 can be reorganized through T23 as
\[
mn-m'n'=s
\quad\Longrightarrow\quad
(m,m')=(da,db),\quad an-bn'=s/d.
\]

A legitimate dispersion proof may therefore seek cancellation in
\[
\sum_{d,a,b,\ell}
\gamma_{d,a,b,\ell}
K_{\mathcal A}(\text{corresponding output difference}),
\]
using the oscillation of \(K_{\mathcal A}\) across the coprime slope/lattice parameters.

This is where an actual spectral, Kloosterman, or OFI-derived transfer estimate would have to attach. The T23 parametrization is a coordinate system for the kernel; it is not itself a norm bound.

---

## 9. Outcome

T27 gives the exact next gate:
\[
\text{T23 lattice coefficients}
\to
\text{far-minor sampling Gram matrix}
\to
\text{coefficient-sensitive operator norm gain}
\to
\text{T26 Z-L large-values bound}.
\]

The ordinary large sieve is a benchmark. The missing theorem is a genuinely bilinear, arithmetic improvement over that benchmark on the far-minor frequency set.