# T5: Arithmetic Major–Minor Target After OFI Reconstruction

**Status:** exact reduction and proof target; no new binary-Goldbach estimate is claimed.  
**Purpose:** state the unique arithmetic inequality that must be proved after the B-spline / OFI representation and local-dual extraction are in place.

---

## 1. Work first with Mangoldt weights

For a branch \(\sigma\in\{+,-\}\), define
\[
\Lambda_\sigma(n)=\Lambda(n)\mathbf 1_{n\equiv\sigma\pmod 6},
\]
where the finitely many exceptional values supported at \(2\) and \(3\) are tracked separately.

For a cutoff \(N\), define the sector exponential sums
\[
T_{\sigma,N}(\alpha)
=
\sum_{n\le N}\Lambda_\sigma(n)e(\alpha n),
\qquad e(x)=e^{2\pi i x}.
\]

The exact sector correlation is
\[
R^{(N)}_{\sigma,\tau}(E)
=
\int_0^1
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

The corresponding prime-only correlation is
\[
G^{(N)}_{\sigma,\tau}(E)
=
\sum_{a+b=E}\theta_\sigma(a)\theta_\tau(b).
\]

The OFI spline field may be built from either sequence, but the analytic input naturally enters through \(\Lambda\) and the logarithmic derivatives
\[
-\frac{\zeta'}{\zeta}(s),
\qquad
-\frac{L'}{L}(s,\chi_3).
\]

---

## 2. Character-sector form

Put
\[
A_\Lambda=\Lambda-\Lambda_3,
\qquad
B_\Lambda=\chi_3\Lambda,
\]
with \(\Lambda_3\) carrying the multiples of \(3\). Then away from the exceptional coordinates,
\[
\Lambda_+=\frac{A_\Lambda+B_\Lambda}{2},
\qquad
\Lambda_-=\frac{A_\Lambda-B_\Lambda}{2}.
\]

Thus the three mod-\(6\) Goldbach channels are linear combinations of exactly two spectral objects:

\[
R_0=\frac14(A_\Lambda*A_\Lambda-B_\Lambda*B_\Lambda),
\]
\[
R_2=\frac14(A_\Lambda*A_\Lambda+2A_\Lambda*B_\Lambda+B_\Lambda*B_\Lambda),
\]
\[
R_4=\frac14(A_\Lambda*A_\Lambda-2A_\Lambda*B_\Lambda+B_\Lambda*B_\Lambda).
\]

This is the only legitimate V4-style compression in the proof spine: ordinary and \(\chi_3\)-twisted additive correlations. No topological packaging may substitute for those coefficients.

---

## 3. Major/minor decomposition

Choose a standard finite major-arc set \(\mathfrak M(Q,N)\subset\mathbb T\) around reduced rationals \(a/q\) with \(q\le Q\), and let
\[
\mathfrak m(Q,N)=\mathbb T\setminus\mathfrak M(Q,N).
\]

For every sector pair,
\[
R^{(N)}_{\sigma,\tau}(E)
=
R^{\mathfrak M,(N)}_{\sigma,\tau}(E)
+
R^{\mathfrak m,(N)}_{\sigma,\tau}(E),
\]
where each term is the same Fourier integrand restricted to the indicated arcs.

The major arc term is the location of the singular series and the positive order-\(E\) main contribution. The minor arc term is the cancellation problem.

---

## 4. Insert OFI only through the exact local functional

For a stable fractional order \(u>1/2\), let \(H_{u,j}\) be the spline synthesis of the relevant sector correlation, and let
\[
\mathcal C_{u,R,E}[H]
=
\langle H,\widetilde{\mathsf B}_{u,R}(\cdot-(E+1))\rangle
\]
be the compact local dual window from T3.

By linearity,
\[
\mathcal C_{u,R,E}[H_{u,j}]
=
\mathcal C_{u,R,E}[H^{\mathfrak M}_{u,j}]
+
\mathcal C_{u,R,E}[H^{\mathfrak m}_{u,j}].
\]

This is the correct place to test an OFI order: not on a raw smoothed Fourier norm, but on the **post-extraction** major and minor pieces.

---

## 5. Required major-arc lower bound

The proof must establish constants \(c_0>0\), \(E_0\), and a positive arithmetic factor \(\mathfrak S_j(E)\) such that for every admissible even \(E\ge E_0\),
\[
\boxed{
\mathcal C_{u,R,E}[H^{\mathfrak M}_{u,j}]
\ge c_0\,\mathfrak S_j(E)E
-\mathcal E^{\mathfrak M}_{u,R,j}(E).
}
\]

The factor \(\mathfrak S_j(E)\) is not assumed away: the local congruence structure must remain explicit in every sector.

---

## 6. Required minor-arc upper bound

The decisive new theorem would be a uniform estimate
\[
\boxed{
\left|
\mathcal C_{u,R,E}[H^{\mathfrak m}_{u,j}]
\right|
\le
\mathcal E^{\mathfrak m}_{u,R,j}(E),
}
\]
with
\[
\mathcal E^{\mathfrak m}_{u,R,j}(E)
=o\!\bigl(\mathfrak S_j(E)E\bigr)
\]
uniformly in the admissible even targets.

This is the actual Goldbach bottleneck. A claim that OFI solves Goldbach must reduce this quantity, after reconstruction, below the major-arc main term.

---

## 7. Prime-power subtraction ledger

Let
\[
P(n)=\Lambda(n)-\theta(n).
\]
Then
\[
R_\Lambda-G=(\theta*P)+(P*\theta)+(P*P).
\]

The final descent from Mangoldt positivity to actual-prime positivity must include an explicit bound
\[
\left|R_j(E)-G_j(E)\right|
\le \mathcal E^{\mathrm{pp}}_j(E).
\]

A safe first target is an elementary order no worse than
\[
\mathcal E^{\mathrm{pp}}_j(E)=O\!\left(\sqrt E\log^3E\right).
\]
The exact constants and sector exceptions must be proved in a dedicated lemma; they are not supplied by the spline machinery.

---

## 8. The complete positivity certificate

Combine T3, the major/minor split, and prime-power stripping. A sufficient theorem for an admissible target \(E\) is
\[
\begin{aligned}
&c_0\mathfrak S_j(E)E \\
&>\mathcal E^{\mathfrak M}_{u,R,j}(E)
+\mathcal E^{\mathfrak m}_{u,R,j}(E)
+\eta_u(N)\|\widetilde{\mathsf B}_{u,R}\|_2
+\|H_{u,j}\|_2\varepsilon_u(R)
+\mathcal E^{\mathrm{pp}}_j(E).
\end{aligned}
\]

Then
\[
G_j(E)>0,
\]
which gives an actual prime-pair representation in the required residue sector.

This is the complete OFI-native Goldbach certificate. Every term has an assigned origin:

| term | origin |
|---|---|
| \(c_0\mathfrak S_j(E)E\) | major arcs / arithmetic density |
| \(\mathcal E^{\mathfrak M}\) | major-arc approximation error |
| \(\mathcal E^{\mathfrak m}\) | minor-arc cancellation |
| \(\eta_u\|\widetilde{\mathsf B}_{u,R}\|_2\) | external field approximation |
| \(\|H_u\|_2\varepsilon_u(R)\) | compact dual-window truncation |
| \(\mathcal E^{\mathrm{pp}}\) | prime-power removal |

---

## 9. Where the proposed extra structures can legally enter

- **Trig/Euler splines:** a basis for estimating the oscillatory \(T_{\sigma,N}\) fields.
- **Heat/Poisson semigroups:** controlled multiscale arc windows, provided extraction cost is charged.
- **Ruelle transfer:** only if it yields a bound on an explicit weighted exponential sum or correlation.
- **T1/countable compactness:** compact local-window exhaustion and finite arc covers; not prime positivity.
- **Smash products:** optional quotient bookkeeping for the ordinary/twisted channel pair; not a replacement for the displayed convolution formulas.
- **Ricci flow / Perelman:** excluded from the proof spine until an arithmetic observable is defined and proved stable under the proposed geometric flow.
- **Satterthwaite / degrees of freedom:** numerical branch ranking only.

---

## 10. Next theorem to attack

The next nontrivial deliverable is not another representation theorem. It is one explicit bound of the form
\[
\left|
\mathcal C_{u,R,E}[H^{\mathfrak m}_{u,j}]
\right|
\le C_u E^{1-\delta_u}
\]
for some \(\delta_u>0\), with the local dual, sector projection, and OFI order all retained in the constants.

If such a theorem cannot be proved, the current framework remains a rigorous encoding and certification architecture but not a solution of binary Goldbach.