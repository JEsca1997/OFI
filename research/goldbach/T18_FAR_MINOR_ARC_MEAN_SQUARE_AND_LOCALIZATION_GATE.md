# T18: Far Minor-Arc Mean Square and the Localization Gate

**Status:** exact Parseval reduction, conditional exceptional-set consequence, and a sharp statement of the missing upgrade to pointwise control.  
**Purpose:** extract the strongest honest consequence available from a weighted far-minor mean-square estimate, while separating it from the unproved P1 supremum.

---

## 1. Restricted Fourier coefficients

Fix a sector \(j\in\{0,2,4\}\). For any Type-I/II pair from T17, write
\[
H_{\ell,r}(\alpha)
:=\mathbf 1_{\mathfrak F}(\alpha)
\Omega_K(\alpha)
\mathcal B_{\sigma_j,\ell}(\alpha)
\mathcal B_{\tau_j,r}(\alpha).
\]

Its additive Fourier coefficients are
\[
\mathcal J_{\ell,r}(E)
=
\int_0^1H_{\ell,r}(\alpha)e(-E\alpha)\,d\alpha.
\]

This is exactly the T17 far-minor bilinear contribution.

---

## 2. Exact Parseval identity

Since \(H_{\ell,r}\in L^2(\mathbb T)\), Parseval gives
\[
\boxed{
\sum_{E\in\mathbb Z}|\mathcal J_{\ell,r}(E)|^2
=
\int_{\mathfrak F}
\Omega_K(\alpha)^2
|\mathcal B_{\sigma_j,\ell}(\alpha)|^2
|\mathcal B_{\tau_j,r}(\alpha)|^2\,d\alpha.
}
\]

Therefore, for a dyadic target block
\[
\mathcal E_X:=\{E\in[X,2X]\cap(j+6\mathbb Z)\},
\]
we have the immediate inequality
\[
\sum_{E\in\mathcal E_X}|\mathcal J_{\ell,r}(E)|^2
\le
\int_{\mathfrak F}
\Omega_K^2
|\mathcal B_{\sigma_j,\ell}|^2
|\mathcal B_{\tau_j,r}|^2.
\]

Thus a weighted fourth-moment estimate on the frequency side is precisely an additive-coefficient mean-square estimate. No heuristic conversion is needed.

---

## 3. Correct density-one target

The natural density-one target is
\[
\boxed{
\int_{\mathfrak F}
\Omega_K(\alpha)^2
|\mathcal B_{\sigma_j,\ell}(\alpha)|^2
|\mathcal B_{\tau_j,r}(\alpha)|^2\,d\alpha
\ll X^{3-\eta_{\ell,r}}
}
\]
for some \(\eta_{\ell,r}>0\), after all decomposition parameters have been tied to \(X\asymp N\).

The exponent \(3\) is the relevant coefficient-energy scale for an additive convolution with \(O(X)\) target coefficients of natural size \(O(X)\). A target of scale \(X^{2-2\delta}\) is not the generic mean-square benchmark.

Summing over finitely many decomposition pieces, assume
\[
\sum_{\ell,r}
\sum_{E\in\mathcal E_X}
|\mathcal J_{\ell,r}(E)|^2
\le C X^{3-\eta}.
\]

---

## 4. Exact exceptional-set consequence

Fix a threshold \(X^{1-\delta}\). By Chebyshev,
\[
\begin{aligned}
\#\left\{E\in\mathcal E_X:
\sum_{\ell,r}|\mathcal J_{\ell,r}(E)|>X^{1-\delta}
\right\}
&\ll
X^{-2+2\delta}
\sum_{E\in\mathcal E_X}
\left(\sum_{\ell,r}|\mathcal J_{\ell,r}(E)|\right)^2\\
&\ll X^{1+2\delta-\eta},
\end{aligned}
\]
where the finite number of \((\ell,r)\) pairs is absorbed into the constant.

Hence, whenever
\[
2\delta<\eta,
\]
the far-minor contribution is \(O(X^{1-\delta})\) for all but \(o(X)\) targets in the sector block.

Combined with the T15 major-arc package and compatible transition mean-square bounds, this is the correct route to a **density-one Fejér-windowed statement**.

---

## 5. Why this does not prove the P1 supremum

A mean-square estimate allows a sparse exceptional set. To upgrade it to
\[
\sup_{E\in\mathcal E_X}
\left|\mathcal I_{j,K}^{\mathfrak F}(E)\right|
=o(X),
\]
one needs a further localization principle.

A generic discrete derivative estimate is too weak. From the Fourier definition,
\[
\mathcal J(E+1)-\mathcal J(E)
=
\int_0^1H(\alpha)e(-E\alpha)(e(-\alpha)-1)\,d\alpha,
\]
so only
\[
|\mathcal J(E+1)-\mathcal J(E)|
\le2\int_0^1|H(\alpha)|\,d\alpha
\]
follows automatically.

For far-minor bilinear products this bound is generally much larger than the \(X^{1-\delta}\) scale needed for deficit propagation. Smoothness of the Fejér multiplier does not fix this, because the rough factor \(\mathbf 1_{\mathfrak F}\) and the prime bilinear product remain.

---

## 6. The localization gate

To turn the T18 exceptional-set statement into a pointwise P1 theorem, one needs at least one independently proved statement of one of the following types.

### L1. Pointwise Fourier coefficient theorem
\[
\sup_{E\in\mathcal E_X}
\left|\mathcal I_{j,K}^{\mathfrak F}(E)\right|
\le cX
\]
with \(c\) strictly below the remaining major-term margin.

### L2. Anti-spike / local propagation theorem
For every \(E_0\in\mathcal E_X\),
\[
|\mathcal I_{j,K}^{\mathfrak F}(E_0)|\ge cX
\Longrightarrow
\sum_{|h|\le H(X)}
|\mathcal I_{j,K}^{\mathfrak F}(E_0+h)|^2
\ge c'X^2H(X),
\]
with a block length large enough to contradict the global T18 budget.

### L3. Stronger high moment plus a valid maximal inequality
A higher-moment estimate together with a maximal/Fourier localization theorem that controls the supremum over target coefficients.

No generic B-spline, Riesz, or semigroup identity supplies L1–L3 by itself.

---

## 7. What OFI can legitimately target

The OFI branch can be tested against the Fejér baseline through the exact weighted fourth moment
\[
\mathfrak Q_{\ell,r}^{(K)}
:=
\int_{\mathfrak F}
\Omega_K^2
|\mathcal B_{\sigma_j,\ell}|^2
|\mathcal B_{\tau_j,r}|^2.
\]

A candidate fractional sector-preserving kernel \(\Omega_u\) is useful only if it proves
\[
\mathfrak Q_{\ell,r}^{(u)}
\le X^{-\varepsilon}
\mathfrak Q_{\ell,r}^{(K)}
\]
for a sufficient collection of bilinear pieces, while its major-model and extraction ledgers remain favorable.

Even such a theorem would first advance the T8 density-one branch. It does not automatically solve the localization gate.

---

## 8. Revised proof map

\[
\text{T15: small major arcs}
\to
\text{T16: transition bands}
\to
\text{T18: weighted fourth moment / almost all}
\to
\text{T9 + localization gate: every target}.
\]

The far-minor P1 supremum remains the hardest analytic route. The density-one route is narrower but mathematically reachable in principle once a genuine weighted fourth-moment saving is supplied.