# T13: Sector Fejér Major-Arc Approximation Gate

**Status:** exact model/error decomposition and required lower-bound target; no prime-distribution estimate is claimed.  
**Purpose:** state the first genuinely arithmetic theorem needed after the sector-preserving Fejér/B-spline construction.

---

## 1. Sector Mangoldt sums

For \(\sigma\in\{+,-\}\), put
\[
\Lambda_\sigma(n)=\Lambda(n)\mathbf 1_{n\equiv\sigma\pmod6},
\qquad
T_{\sigma,N}(\alpha)=\sum_{n\le N}\Lambda_\sigma(n)e(\alpha n).
\]

For the Goldbach target channel \(j\in\{0,2,4\}\), choose
\[
(\sigma_j,\tau_j)=
\begin{cases}
(+,-),&j=0,\\
(+,+),&j=2,\\
(-,-),&j=4.
\end{cases}
\]

The unwindowed Mangoldt coefficient is
\[
R_j^{(N)}(E)=
\int_0^1T_{\sigma_j,N}(\alpha)T_{\tau_j,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

On the rescaled lattice \(E=6n+j\), the Fejér-windowed output is
\[
\mathcal A_{j,K}^{(N)}(n)
=
\sum_{|k|\le K}\nu_k^{(K)}R_j^{(N)}(6(n-k)+j).
\]

Equivalently,
\[
\boxed{
\mathcal A_{j,K}^{(N)}(n)
=
\int_0^1
\Omega_K(\alpha)
T_{\sigma_j,N}(\alpha)T_{\tau_j,N}(\alpha)e(-(6n+j)\alpha)\,d\alpha,
}
\]
where \(\Omega_K(\alpha)=\widehat\nu_K(6\alpha)\).

---

## 2. Major-arc parametrization

Let \(Q\ge1\) and let \(W>0\). Define
\[
\mathfrak M(Q,W;N)
=
\bigcup_{q\le Q}\ \bigcup_{\substack{1\le a\le q\\(a,q)=1}}
\left\{\alpha=\frac aq+\beta:\ |\beta|\le\frac{W}{qN}\right\}.
\]

The choices of \(Q,W\) must later be made so that these arcs are disjoint or are handled by an explicitly bounded overlap argument. This document does not assume an optimal choice.

Write
\[
V_N(\beta)=\sum_{m\le N}e(\beta m).
\]

---

## 3. Sector arithmetic amplitudes

For each reduced rational \(a/q\), define the formal sector amplitude
\[
\mathfrak a_\sigma(a,q)
:=
\frac{1}{\varphi([q,6])}
\sum_{\substack{r\bmod [q,6]\\(r,[q,6])=1\\r\equiv\sigma\,({\rm mod}\,6)}}
 e\!\left(\frac{ar}{q}\right),
\]
where \([q,6]\) denotes the least common multiple.

This is the local residue-density factor predicted by a prime number theorem in arithmetic progressions. The major-arc approximation target is
\[
T_{\sigma,N}\!\left(\frac aq+\beta\right)
=
\mathfrak a_\sigma(a,q)V_N(\beta)
+\mathcal R_{\sigma}(a,q,\beta;N).
\]

The two sector amplitudes may equivalently be organized through the ordinary and \(\chi_3\)-twisted channels:
\[
\Lambda_\pm=\frac12(A_\Lambda\pm B_\Lambda),
\qquad
A_\Lambda=\Lambda-\Lambda_3,
\quad B_\Lambda=\chi_3\Lambda.
\]

Thus the \(\chi_3\) component is not an optional correction; it is part of the amplitude required for the \(2\) and \(4\pmod6\) sectors.

---

## 4. Exact Fejér-weighted major model

Insert only the principal amplitudes into the major-arc integral. Define
\[
\begin{aligned}
\mathcal M_{j,K}^{(N)}(n;Q,W)
:={}&
\sum_{q\le Q}\sum_{\substack{1\le a\le q\\(a,q)=1}}
\mathfrak a_{\sigma_j}(a,q)\mathfrak a_{\tau_j}(a,q)
 e\!\left(-\frac{a(6n+j)}q\right)\\
&\times
\int_{|\beta|\le W/(qN)}
\Omega_K\!\left(\frac aq+\beta\right)
V_N(\beta)^2e(-(6n+j)\beta)\,d\beta.
\end{aligned}
\]

This is the correct Fejér-weighted major model. It retains the full multiplier \(\Omega_K(a/q+\beta)\); no false rational-preservation simplification is made.

Its associated finite weighted singular object is therefore the complete rational sum above, not merely the ordinary singular series times a scalar.

---

## 5. Exact major-arc error ledger

On each major arc write
\[
T_{\sigma_j,N}=P_{\sigma_j}+\mathcal R_{\sigma_j},
\qquad
P_{\sigma}(a/q+\beta)=\mathfrak a_\sigma(a,q)V_N(\beta).
\]

Then the difference between the actual Fejér-weighted major contribution and \(\mathcal M_{j,K}^{(N)}\) is exactly the integral of
\[
\Omega_K\bigl(
P_{\sigma_j}\mathcal R_{\tau_j}
+
\mathcal R_{\sigma_j}P_{\tau_j}
+
\mathcal R_{\sigma_j}\mathcal R_{\tau_j}
\bigr)e(-(6n+j)\alpha).
\]

Hence a sufficient absolute error bound is
\[
\begin{aligned}
\mathcal E_{j,K}^{\mathfrak M}
\le{}&
\int_{\mathfrak M}
|\Omega_K(\alpha)|
\bigl(
|P_{\sigma_j}(\alpha)|\,|\mathcal R_{\tau_j}(\alpha)|\\
&\qquad\qquad+
|\mathcal R_{\sigma_j}(\alpha)|\,|P_{\tau_j}(\alpha)|
+
|\mathcal R_{\sigma_j}(\alpha)|\,|\mathcal R_{\tau_j}(\alpha)|
\bigr)d\alpha.
\end{aligned}
\]

Because \(0\le\Omega_K\le1\), the Fejér multiplier does not enlarge this absolute major-arc error. It also does not automatically make it small; the required prime-distribution estimate remains in the residuals \(\mathcal R_\sigma\).

---

## 6. The sectorwise major-arc theorem required

A theorem sufficient for the Fejér branch is the following.

### Target T13

There exist admissible parameter choices \(Q(N),W(N),K(N)\), constants \(c_j>0\), and \(\delta>0\) such that for every sufficiently large rescaled target \(n\),
\[
\boxed{
\mathcal M_{j,K}^{(N)}(n;Q,W)
\ge c_jN,
}
\]
and
\[
\boxed{
\mathcal E_{j,K}^{\mathfrak M}(n;Q,W)
\le N^{1-\delta}.
}
\]

The comparison must be uniform in each sector \(j\) and compatible with the truncation relation between \(N\) and the target \(E=6n+j\).

This is a nontrivial arithmetic theorem. The B-spline/Fejér construction does not establish it.

---

## 7. Why positivity is global, not termwise

Even though \(\Omega_K\ge0\), the rational terms in \(\mathcal M_{j,K}^{(N)}\) contain complex phases
\[
e\!\left(-\frac{a(6n+j)}q\right)
\]
and complex local amplitudes. Positivity cannot be checked term-by-term.

The correct task is to prove that the fully assembled model is real and bounded below after the rational sum and \(\beta\)-integrals are combined. This is exactly the weighted-singular-series gate from the T10 correction, now written as a finite major-arc model.

---

## 8. Assembly with later gates

If T13 holds, the Fejér-windowed sector correlation obeys
\[
\mathcal A_{j,K}^{(N)}(n)
\ge
c_jN
-
\mathcal E_{j,K}^{\mathfrak M}
-
\mathcal E_{j,K}^{\mathfrak m}.
\]

A pointwise conclusion still additionally requires:

1. a minor-arc budget \(\mathcal E_{j,K}^{\mathfrak m}<c_jN\) with margin;
2. a justified descent from the Fejér-windowed output to the center coefficient, as required by T9; and
3. prime-power removal when passing from \(\Lambda\) to actual primes.

T13 therefore closes neither P1 nor T9. It supplies the first arithmetic major-term gate those later arguments must consume.

---

## 9. Immediate research priority

The immediate task is to derive usable bounds for \(\mathcal R_\sigma(a,q,\beta;N)\) in the sector decomposition, including the \(\chi_3\)-twisted component, on a quantitatively specified major-arc family.

Only after that is it meaningful to compare a fractional OFI window against the Fejér/B-spline baseline on the major arcs.