# T16: Transition-Arc Cancellation Budget

**Status:** exact denominator-band decomposition and sufficient analytic targets; no new exponential-sum bound is claimed.  
**Purpose:** quantify the large-denominator/transition problem left after the polylogarithmic major-arc package.

---

## 1. Transition bands

Fix the polylogarithmic cutoff
\[
Q_0=(\log N)^B,
\]
and a larger transition endpoint \(Q_1\le N^{\vartheta}\), where \(\vartheta>0\) is to be selected by the later Type-I/II analysis.

For dyadic \(R\) with
\[
Q_0<R\le Q_1,
\]
define the rational transition neighborhood
\[
\mathfrak T(R;W,N)
:=
\bigcup_{R<q\le2R}\ \bigcup_{\substack{1\le a\le q\\(a,q)=1}}
\left\{\frac aq+\beta:\ |\beta|\le\frac{W}{qN}\right\}.
\]

The union over the dyadic values of \(R\) is the transition region. Arc overlaps must either be excluded by the parameter choice or counted explicitly; every bound below remains valid with an overlap multiplicity inserted.

For a target sector \(j\), set
\[
\mathcal I_{j,K,R}(E)
:=
\int_{\mathfrak T(R;W,N)}
\Omega_K(\alpha)
T_{\sigma_j,N}(\alpha)T_{\tau_j,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

---

## 2. Measure of one denominator band

The elementary estimate
\[
\sum_{R<q\le2R}\varphi(q)\ll R^2
\]
gives
\[
\begin{aligned}
|\mathfrak T(R;W,N)|
&\ll
\sum_{R<q\le2R}\varphi(q)\frac{W}{qN}\\
&\ll \frac{WR}{N}.
\end{aligned}
\]

This is the geometric factor that every transition-arc estimate must beat.

---

## 3. Baseline pointwise-times-energy inequality

Let
\[
B_{\sigma}(R):=
\sup_{\alpha\in\mathfrak T(R;W,N)}|T_{\sigma,N}(\alpha)|.
\]

Since \(0\le\Omega_K\le1\), Cauchy–Schwarz and Parseval yield
\[
\begin{aligned}
|\mathcal I_{j,K,R}(E)|
&\le B_{\sigma_j}(R)
\int_{\mathfrak T(R;W,N)}|T_{\tau_j,N}(\alpha)|\,d\alpha\\
&\le B_{\sigma_j}(R)
|\mathfrak T(R;W,N)|^{1/2}
\left(\int_0^1|T_{\tau_j,N}(\alpha)|^2d\alpha\right)^{1/2}\\
&\ll
B_{\sigma_j}(R)\sqrt{WR\log N}.
\end{aligned}
\]

The same bound holds after exchanging \(\sigma_j\) and \(\tau_j\). Hence
\[
\boxed{
|\mathcal I_{j,K,R}(E)|
\ll
\min\{B_{\sigma_j}(R),B_{\tau_j}(R)\}
\sqrt{WR\log N}.
}
\]

This formula is only a baseline. It makes the required pointwise saving transparent.

---

## 4. A sufficient pointwise target per band

Assign a positive error allowance \(\rho_R\) to each dyadic band, with
\[
\sum_R\rho_R<\frac14c_j,
\]
where \(c_jN\) is the positive major-model lower budget sought in T13.

A sufficient condition for the band is
\[
\boxed{
\min\{B_{\sigma_j}(R),B_{\tau_j}(R)\}
\le
\frac{\rho_R N}{C\sqrt{WR\log N}}
}
\]
for a fixed absolute constant \(C\) absorbing the prior inequalities.

Then
\[
|\mathcal I_{j,K,R}(E)|\le\rho_RN.
\]

This is not asserted to be available across the full transition range. It is the precise cancellation target required by the most elementary route.

---

## 5. Weighted-energy refinement: where the Fejér/OFI kernel can matter

Define the weighted sector energy on the band
\[
\mathfrak W_{\tau,K}(R)
:=
\int_{\mathfrak T(R;W,N)}
\Omega_K(\alpha)^2|T_{\tau,N}(\alpha)|^2\,d\alpha.
\]

Then
\[
\begin{aligned}
|\mathcal I_{j,K,R}(E)|
&\le B_{\sigma_j}(R)
\int_{\mathfrak T(R;W,N)}\Omega_K(\alpha)|T_{\tau_j,N}(\alpha)|\,d\alpha\\
&\le B_{\sigma_j}(R)
|\mathfrak T(R;W,N)|^{1/2}
\mathfrak W_{\tau_j,K}(R)^{1/2}.
\end{aligned}
\]

Therefore
\[
\boxed{
|\mathcal I_{j,K,R}(E)|
\ll
B_{\sigma_j}(R)
\left(\frac{WR}{N}\right)^{1/2}
\mathfrak W_{\tau_j,K}(R)^{1/2}.
}
\]

This is the first rigorous location where a sector-preserving OFI multiplier can improve a transition estimate: it must prove that \(\mathfrak W_{\tau,K}(R)\) is smaller than the corresponding unweighted energy by enough to offset all other ledgers.

The mere inequality \(0\le\Omega_K\le1\) only shows non-enlargement; it does not establish a saving.

---

## 6. Type-I/II interface

After a legitimate Vaughan- or Heath–Brown-type decomposition of each sector sum, the transition contribution is reduced to finite combinations of sums schematically of the forms
\[
\sum_{m\sim M}a_m\sum_{n\sim L}b_n e(\alpha mn),
\qquad ML\asymp N,
\]
and Type-I variants where one variable is short.

The OFI/Fejér multiplier remains outside the individual bilinear phase:
\[
\int_{\mathfrak T(R;W,N)}
\Omega_K(\alpha)
\mathcal B_1(\alpha)\mathcal B_2(\alpha)e(-E\alpha)d\alpha.
\]

It is invalid to rewrite this automatically as a product-weighted sum with an unexplained factor \(W(mn)\). The additive-window correction from T6 remains in force.

A valid transition theorem must bound either:

\[
\sup_{\alpha\in\mathfrak T(R;W,N)}|\mathcal B_i(\alpha)|,
\]

or a mean-square/bilinear correlation that feeds \(\mathfrak W_{\tau,K}(R)\), with all dyadic decompositions and coefficient norms explicit.

---

## 7. Transition-band theorem target

A pointwise P1 package through \(Q_1\) would follow from estimates
\[
|\mathcal I_{j,K,R}(E)|\le\rho_RN
\]
for every dyadic \(R\in(Q_0,Q_1]\), all admissible target sectors, and all target values in the chosen range, together with
\[
\sum_{Q_0<R\le Q_1}\rho_R<\frac14c_j.
\]

The remaining far region must then satisfy a separate bound with the other quarter of the major budget. The constants are placeholders; the point is that every denominator band has a finite, preassigned error allowance.

---

## 8. What T16 settles

T16 does not prove cancellation. It proves the bookkeeping fact that the large-denominator problem is quantitatively reducible to one of two explicit deliverables:

\[
\boxed{
\text{pointwise sector exponential-sum cancellation}
\quad\text{or}\quad
\text{a weighted transition-energy saving.}
}
\]

This is the correct place to test any OFI, Riesz, transfer-operator, or extended-trigonometric input. It earns a role only by improving one of these two quantities relative to the Fejér baseline.