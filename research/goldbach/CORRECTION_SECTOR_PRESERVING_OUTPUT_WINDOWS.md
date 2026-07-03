# Correction: Sector-Preserving OFI Output Windows

**Scope:** This correction refines the local-output formulas in T3, T5, T8, and T10.

## 1. The issue

The Goldbach coefficient is split into three residue channels:
\[
G_0=\theta_+*\theta_-,\qquad
G_2=\theta_+*\theta_+,\qquad
G_4=\theta_-*\theta_-.
\]

A generic local output window
\[
(\omega*G_j)(E)=\sum_h\omega_hG_j(E-h)
\]
mixes target residues whenever \(h\not\equiv0\pmod6\). Then the label \(j\) at the center is no longer the label of the shifted coefficient.

Thus a scalar sector formula is invalid unless the window preserves the residue class or the proof explicitly carries the mixing.

## 2. First proof-spine convention: support on \(6\mathbb Z\)

For the scalar V4/character decomposition, impose
\[
\boxed{\omega_h=0\quad\text{unless}\quad h\equiv0\pmod6.}
\]

Write
\[
\omega_{6k}=\nu_k,
\qquad
\Omega(\alpha)=\sum_{k\in\mathbb Z}\nu_k e(6k\alpha).
\]

Then for \(E\equiv j\pmod6\),
\[
E-6k\equiv j\pmod6,
\]
and the exact local sector output is
\[
A_j(E)=\sum_k\nu_kG_j(E-6k).
\]

No residue channel is mixed. The same convention applies to the Mangoldt correlations \(R_j\).

## 3. Equivalent rescaled lattice formulation

Fix a sector residue \(j\in\{0,2,4\}\) and set
\[
\mathcal G_j(n):=G_j(6n+j).
\]

Then a sector-preserving OFI output window is an ordinary convolution on the rescaled integer lattice:
\[
\mathcal A_j(n)=(\nu*\mathcal G_j)(n).
\]

Its frequency variable is the sixfold circle coordinate. This is the cleanest setting for applying the B-spline/local-dual construction while retaining the mod-6 factorization.

## 4. General windows require a channel-mixing matrix

If arbitrary shifts are desired, define the vector
\[
\mathbf G(E)=
\begin{pmatrix}
G_0(E)\\G_2(E)\\G_4(E)
\end{pmatrix}
\]
with the convention that each component is extended by zero away from its residue class.

Decompose the kernel by residue:
\[
\omega^{(r)}_k:=\omega_{6k+r},\qquad r\in\{0,2,4\}.
\]

Then local extraction has the form
\[
\mathbf A(n)=\sum_{r\in\{0,2,4\}}M_r\,(\omega^{(r)}*\mathbf G)(n),
\]
where the matrices \(M_r\) implement the residue shift \(j\mapsto j-r\pmod6\).

This route is legal but more complicated: the weighted major term, minor-arc estimate, and singular series become matrix-valued. It is excluded from the first proof spine.

## 5. Consequences for the weighted singular series

Under the sector-preserving convention,
\[
\Omega(\alpha)=\Omega(\alpha+1/6),
\]
so the multiplier respects the mod-6 character decomposition. The weighted sector singular series must be defined separately on the rescaled lattice:
\[
\mathfrak S^{\Omega}_j(6n+j)
\]
and its positivity is tested in that fixed channel.

This removes hidden cross-sector cancellation from the major-arc ledger.

## 6. Consequences for locality

A support radius of \(K\) on the rescaled lattice means an additive target radius of \(6K\) in the original variable. Every T3 dual-tail and T10 uncertainty estimate must use that physical radius.

The sector constraint costs frequency flexibility, but it buys a correct scalar arithmetic target. That is the right trade for the initial theorem path.

## 7. Updated proof-spine rule

\[
\boxed{
\text{Use symmetric real OFI output kernels supported on }6\mathbb Z
\text{ until a full channel-mixing theorem is available.}
}
\]

This correction does not establish a new minor-arc or major-arc bound. It makes all later sectorwise statements mathematically well-typed.