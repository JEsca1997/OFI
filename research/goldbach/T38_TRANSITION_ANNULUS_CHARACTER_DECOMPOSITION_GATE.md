# T38: Transition-Annulus Character Decomposition Gate

**Status:** exact algebraic reduction of sector prime sums near rational points; the needed analytic estimate remains open in this program.  
**Purpose:** expose the denominator-sensitive object inside the transition annuli and prevent any claim that a radial OFI multiplier alone controls it.

---

## 1. Rational point and modulus

Fix a reduced rational point
\[
\alpha=\frac aq+\beta,
\qquad (a,q)=1,
\]
and set
\[
L=[q,6].
\]

For \(\sigma\in\{+1,-1\}\), define the sector sum
\[
S_{\sigma,X}(\alpha)
:=
\sum_{n\le X}\theta(n)\mathbf 1_{n\equiv\sigma\ (6)}e(\alpha n).
\]

Split it as
\[
S_{\sigma,X}(\alpha)
=
S^{\times}_{\sigma,X}(\alpha)+\mathcal P_{\sigma,L}(\alpha),
\]
where
\[
S^{\times}_{\sigma,X}(\alpha)
:=
\sum_{\substack{n\le X\\n\equiv\sigma\ (6)\\(n,L)=1}}
\theta(n)e(\alpha n)
\]
and \(\mathcal P_{\sigma,L}\) contains the finitely many prime terms with \(p,L)>1\).

Since \(\theta\) is supported on primes,
\[
|\mathcal P_{\sigma,L}(\alpha)|
\le \sum_{p\mid L}\log p
\le \log L.
\]
Thus the non-unit contribution is explicit and negligible at the scales considered here; it is nevertheless retained in any exact final ledger.

---

## 2. Twisted prime sums

For each Dirichlet character \(\chi\pmod L\), define
\[
\Psi_X(\chi;\beta)
:=
\sum_{n\le X}\theta(n)\chi(n)e(\beta n).
\]

Let
\[
\mathcal U_\sigma(L)
:=
\{r\pmod L:(r,L)=1,\ r\equiv\sigma\pmod6\}.
\]
For every unit residue \(r\pmod L\), character orthogonality gives
\[
\mathbf 1_{n\equiv r\ (L)}\mathbf 1_{(n,L)=1}
=
\frac1{\varphi(L)}
\sum_{\chi\, (L)}\overline{\chi(r)}\chi(n).
\]

Consequently,
\[
\boxed{
S^{\times}_{\sigma,X}\!\left(\frac aq+\beta\right)
=
\frac1{\varphi(L)}
\sum_{\chi\, (L)}
\mathcal G_\sigma(\chi;a,q)
\Psi_X(\chi;\beta),
}
\]
where the finite rational coefficient is
\[
\mathcal G_\sigma(\chi;a,q)
:=
\sum_{r\in\mathcal U_\sigma(L)}
 e\!\left(\frac{ar}{q}\right)\overline{\chi(r)}.
\]

This is an exact reduction. No prime-distribution theorem has been used.

---

## 3. Coefficient energy: no automatic denominator saving

Because the phases \(e(ar/q)\) have modulus one, character orthogonality yields
\[
\begin{aligned}
\sum_{\chi\, (L)}|\mathcal G_\sigma(\chi;a,q)|^2
&=
\sum_{r,s\in\mathcal U_\sigma(L)}
 e\!\left(\frac{a(r-s)}q\right)
\sum_{\chi\, (L)}\overline{\chi(r)}\chi(s)\\
&=\varphi(L)\,|\mathcal U_\sigma(L)|.
\end{aligned}
\]

Since \(6\mid L\), multiplication by \(-1\) exchanges the two sector classes among units, so
\[
|\mathcal U_+(L)|=|\mathcal U_-(L)|=\frac{\varphi(L)}2.
\]
Hence
\[
\boxed{
\sum_{\chi\, (L)}|\mathcal G_\sigma(\chi;a,q)|^2
=\frac{\varphi(L)^2}{2}.
}
\]

Therefore the coefficient system itself supplies no power saving in \(q\). Any useful annular saving must come from nontrivial control of the twisted prime sums \(\Psi_X(\chi;\beta)\), their averages over characters/moduli, or cancellation after combining the two sectors.

---

## 4. The transition-annulus energy in character variables

For a dyadic rational annulus \(\mathcal A(Q)\), the exact identity above converts
\[
\mathfrak E_{\sigma,\tau}(Q)
=
\int_{\mathcal A(Q)}|S_\sigma(\alpha)|^2|S_\tau(\alpha)|^2d\alpha
\]
into a weighted fourth moment of \(\Psi_X(\chi;\beta)\):
\[
\mathfrak E_{\sigma,\tau}(Q)
=
\sum_{Q<q\le2Q}\ \sum_{(a,q)=1}
\int_{|\beta|\le W/(qX)}
\left|
\frac1{\varphi([q,6])}
\sum_{\chi\,([q,6])}
\mathcal G_\sigma(\chi;a,q)\Psi_X(\chi;\beta)
+\mathcal P_{\sigma,L}
\right|^2
\]
\[
\hspace{22mm}\times
\left|
\frac1{\varphi([q,6])}
\sum_{\chi\,([q,6])}
\mathcal G_\tau(\chi;a,q)\Psi_X(\chi;\beta)
+\mathcal P_{\tau,L}
\right|^2d\beta.
\]

The displayed formula is not yet an estimate. It identifies the exact analytic input required.

---

## 5. Principal and nonprincipal channels

Separate the principal character \(\chi_0\pmod L\):
\[
\Psi_X(\chi;\beta)
=
\mathbf 1_{\chi=\chi_0}\,\mathsf M_L(\beta)
+\mathsf R_X(\chi;\beta),
\]
where \(\mathsf M_L\) is an explicit candidate main term and \(\mathsf R_X\) is the residual.

Then the transition analysis splits into:

\[
\text{principal channel: rational/singular-series model},
\]

\[
\text{nonprincipal channel: averaged twisted-prime residual},
\]

\[
\text{cross channel: interaction of the two.}
\]

Any proof claiming a power saving must bound these three channels separately with the same stated ranges in \(q\), \(\beta\), and \(X\).

---

## 6. Concrete missing theorem

A denominator-sensitive estimate sufficient to move the program would have the shape
\[
\boxed{
\sum_{Q<q\le2Q}\ \sum_{\chi\,([q,6)}^{\!*}
\int_{|\beta|\le W/(qX)}
|\mathsf R_X(\chi;\beta)|^4d\beta
\ll X^{3-\eta}\,\mathcal L(X,Q),
}
\]
for an explicit admissible loss \(\mathcal L\), uniformly in the transition range \(Q_0<Q\le Q_1\).

The star denotes the intended nonprincipal or primitive restriction, which must be defined precisely in any theorem statement.

This is not established here. It is the point at which classical zero-density and large-sieve technology ordinarily enters.

---

## 7. OFI relevance test

An OFI operator has a genuine role at this gate only if it yields a proved inequality that improves one of:

\[
\text{the character average},
\qquad
\text{the }\beta\text{-average},
\qquad
\text{the principal/nonprincipal separation},
\qquad
\text{or the reconstruction cost after localization}.
\]

A multiplier depending only on geometric distance in \(\alpha\) does not automatically improve any of these denominator/character quantities.

---

## 8. Outcome

The transition annulus is now reduced to a standard but precise arithmetic object:
\[
\boxed{
\text{fourth moments of additively twisted prime sums over characters of moduli }[q,6].
}
\]

This is progress in localization, not a proof of the missing estimate. It gives the exact location where any new OFI theorem must intervene.