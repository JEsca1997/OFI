# Correction: Two-Sample Amplifier and Near-Diagonal Gate

**Status:** exact correction to the phase-amplified expansions in T30/T36, plus an exact near-diagonal combinatorial bound.  
**Effect:** a phase-amplified first moment is governed by a two-sample kernel; it does not collapse directly to a one-variable difference kernel.

---

## 1. The one-sample identity that is correct

Let
\[
T(\alpha)=\sum_r C(r)e(\alpha r)
\]
be any finite Fourier polynomial and let
\[
\mathcal A=\{\alpha_1,\ldots,\alpha_J\}.
\]

The unamplified sampled energy satisfies
\[
\begin{aligned}
\sum_{j=1}^{J}|T(\alpha_j)|^2
&=
\sum_{r,s}C(r)\overline{C(s)}
\sum_{j=1}^{J}e\bigl(\alpha_j(r-s)\bigr)\\
&=
\boxed{
\sum_{r,s}C(r)\overline{C(s)}K_{\mathcal A}(r-s),
}
\end{aligned}
\]
where
\[
K_{\mathcal A}(h):=\sum_{j=1}^{J}e(\alpha_jh).
\]

This is a one-variable difference kernel and is the valid starting point for sampled energy/large-sieve arguments.

---

## 2. The amplified identity is a two-sample kernel

For \(|z_j|\le1\), define
\[
\Phi_{\mathcal A,z}
:=
\sum_{j=1}^{J}z_jT(\alpha_j).
\]

Then
\[
\begin{aligned}
|\Phi_{\mathcal A,z}|^2
&=
\sum_{j,k}z_j\overline{z_k}
T(\alpha_j)\overline{T(\alpha_k)}\\
&=
\sum_{r,s}C(r)\overline{C(s)}
\mathcal K_{\mathcal A,z}(r,s),
\end{aligned}
\]
with
\[
\boxed{
\mathcal K_{\mathcal A,z}(r,s)
:=
\sum_{j,k}z_j\overline{z_k}
e(\alpha_jr-\alpha_ks).
}
\]

Equivalently,
\[
\mathcal K_{\mathcal A,z}(r,s)
=
\left(\sum_jz_je(\alpha_jr)\right)
\overline{\left(\sum_kz_ke(\alpha_ks)\right)}.
\]

It is generally **not** of the form
\[
K_{\mathcal A,z}(r-s).
\]

Therefore the direct phase-amplified one-variable kernel claims in T30 and T36 must be read as superseded by this correction.

---

## 3. Correct Type-II specialization

For
\[
T(\alpha)=\mathcal B_1(\alpha)\mathcal B_2(\alpha)
=
\sum_tC(t)e(\alpha t),
\]
where
\[
C(t)=
\sum_{mn+uv=t}a_{m,n}b_{u,v},
\]
the amplified square is
\[
\begin{aligned}
&\left|
\sum_jz_j\mathcal B_1(\alpha_j)\mathcal B_2(\alpha_j)
\right|^2\\
&\quad=
\sum_{m,n,u,v\atop m',n',u',v'}
 a_{m,n}b_{u,v}\overline{a_{m',n'}b_{u',v'}}\\
&\qquad\qquad\times
\sum_{j,k}z_j\overline{z_k}
 e\!\left(
\alpha_j(mn+uv)-\alpha_k(m'n'+u'v')
\right).
\end{aligned}
\]

A phase depending only on \(\alpha_j-\alpha_k\) appears only after an additional, explicitly justified differencing/Cauchy step that aligns the two output frequencies. It is not present in this raw expansion.

---

## 4. Near-diagonal packing lemma

Let \(\mathcal A\subset\mathbb T\) be \(\delta\)-separated, and let
\[
\mathcal N_H
:=
\{(j,k):\|\alpha_j-\alpha_k\|_{\mathbb T}\le H\}.
\]

For every fixed \(j\), the arc of radius \(H\) around \(\alpha_j\) contains at most
\[
1+2\left\lfloor\frac H\delta\right\rfloor
\]
points of \(\mathcal A\). Hence
\[
\boxed{
|\mathcal N_H|
\le
J\left(1+2\left\lfloor\frac H\delta\right\rfloor\right).
}
\]

This is exact up to the harmless endpoint convention on the circle.

---

## 5. Near-diagonal weighted bound

For arbitrary complex numbers \(x_1,\ldots,x_J\), the inequality
\[
2|x_jx_k|\le|x_j|^2+|x_k|^2
\]
gives
\[
\boxed{
\sum_{(j,k)\in\mathcal N_H}|x_j||x_k|
\le
\left(1+2\left\lfloor\frac H\delta\right\rfloor\right)
\sum_{j=1}^{J}|x_j|^2.
}
\]

Taking
\[
x_j=\mathcal B_1(\alpha_j)\mathcal B_2(\alpha_j)
\]
yields
\[
\boxed{
\sum_{(j,k)\in\mathcal N_H}
|\mathcal B_1(\alpha_j)\mathcal B_2(\alpha_j)
\mathcal B_1(\alpha_k)\mathcal B_2(\alpha_k)|
\le
\left(1+2\left\lfloor\frac H\delta\right\rfloor\right)
\mathscr L(\mathcal A).
}
\]

---

## 6. What the near-diagonal attack achieves

At the natural output-frequency resolution \(H\asymp X^{-1}\), if the sampling scale satisfies
\[
\delta\gg X^{-1},
\]
then
\[
1+2\left\lfloor\frac H\delta\right\rfloor=O(1).
\]

Thus close sample pairs create at most a constant-multiplicity loss. This resolves the **combinatorial clustering** issue.

But it does not create a power saving, because the right-hand side remains
\[
\mathscr L(\mathcal A)=\sum_j|\mathcal B_1(\alpha_j)|^2|\mathcal B_2(\alpha_j)|^2.
\]

The diagonal \(j=k\) is included and is positive. It cannot be removed by oscillation.

---

## 7. Correct consequence for the proof program

The near-diagonal portion is now under control in the only valid sense available from spacing:
\[
\text{it costs bounded local multiplicity at resolution }X^{-1}.
\]

The remaining hard inputs are distinct:

\[
\text{(A) a direct bound for the diagonal sampled energy }\mathscr L(\mathcal A),
\]
\[
\text{(B) an explicitly derived differencing step producing a difference-phase sum},
\]
\[
\text{(C) rational- and far-difference estimates for that derived sum}.
\]

Spacing alone proves none of (A)--(C). It only prevents a new blow-up from a dense near-zero cluster.

---

## 8. Outcome

The attempted near-zero attack succeeds as a cleanup lemma, not as the missing exponent:
\[
\boxed{
\text{near-diagonal pairs }\le O(1+H/\delta)\times\text{ diagonal sampled energy}.
}
\]

The next genuine analytic target is to bound that diagonal sampled energy for each Type-II component pair, or to derive a valid differencing inequality whose off-diagonal terms possess exploitable arithmetic cancellation.