# T33: Support-Separated Major Model and Pure Far-Minor Gate

**Status:** exact support-separation reduction; no far-minor arithmetic estimate is claimed.  
**Purpose:** remove the artificial \(P D\) and \(D P\) ledgers from the far-minor analysis when the major model is localized to the major side of the smooth partition.

---

## 1. Smooth partition with a genuine buffer

Let \(\chi_{\mathfrak M}\) and \(\chi_{\mathfrak F}\) be smooth nonnegative cutoffs on \(\mathbb T\) such that
\[
\operatorname{supp}(\chi_{\mathfrak M})
\cap
\operatorname{supp}(\chi_{\mathfrak F})
=\varnothing.
\]

The omitted region is a transition collar \(\chi_{\mathfrak T}\), so that one may arrange a smooth partition of unity
\[
\chi_{\mathfrak M}+\chi_{\mathfrak T}+\chi_{\mathfrak F}=1.
\]

The support disjointness, rather than merely pointwise small overlap, is the condition used below.

---

## 2. Localized major model

Start with an analytic major approximation \(\widetilde P_\rho(\alpha)\) for each sector prime sum \(S_\rho(\alpha)\). Define the localized model
\[
\boxed{
P_\rho(\alpha):=\chi_{\mathfrak M}(\alpha)\widetilde P_\rho(\alpha).
}
\]

Let
\[
D_\rho(\alpha):=S_\rho(\alpha)-P_\rho(\alpha).
\]

On the far-minor support,
\[
\chi_{\mathfrak F}(\alpha)P_\rho(\alpha)=0,
\]
and therefore
\[
\boxed{
\chi_{\mathfrak F}(\alpha)D_\rho(\alpha)
=
\chi_{\mathfrak F}(\alpha)S_\rho(\alpha).
}
\]

This is exact.

---

## 3. Exact collapse of the T32 residual on far minors

For the Goldbach product residual
\[
R_{\sigma,\tau}
=
S_\sigma S_\tau-P_\sigma P_\tau,
\]
we have on \(\operatorname{supp}(\chi_{\mathfrak F})\)
\[
P_\sigma=P_\tau=0.
\]

Hence
\[
\boxed{
\chi_{\mathfrak F}R_{\sigma,\tau}
=
\chi_{\mathfrak F}S_\sigma S_\tau
=
\chi_{\mathfrak F}D_\sigma D_\tau.
}
\]

Equivalently, the two linear T32 pieces vanish after multiplication by the far-minor cutoff:
\[
\chi_{\mathfrak F}P_\sigma D_\tau=0,
\qquad
\chi_{\mathfrak F}D_\sigma P_\tau=0.
\]

---

## 4. Pure far-minor energy identity

Let \(\Omega\) be any sector-preserving multiplier and define
\[
w_{\mathfrak F,\Omega}(\alpha)
:=
\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2.
\]

Then the corrected far-minor residual energy is exactly
\[
\begin{aligned}
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
&:=
\int_0^1w_{\mathfrak F,\Omega}(\alpha)
|R_{\sigma,\tau}(\alpha)|^2d\alpha\\
&=
\boxed{
\int_0^1
\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2
|S_\sigma(\alpha)|^2|S_\tau(\alpha)|^2d\alpha.
}
\end{aligned}
\]

Thus the far-minor task is a single positive bilinear prime-sum energy:
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
\ll X^{3-\eta}.
}
\]

No \(P D\) or \(D P\) error ledger is needed in this region when the partition is set up this way.

---

## 5. Where the model-error ledgers go

The support-separation simplification does not discard the model errors. It assigns them to the correct regions:

\[
\text{major model approximation }\widetilde P_\rho
quad\longrightarrow\quad
\mathfrak M\text{ and collar }\mathfrak T,
\]

\[
\text{far-minor energy }
quad\longrightarrow\quad
\mathfrak F\text{ only, with the exact sums }S_\sigma,S_\tau.
\]

This avoids double counting. The total proof ledger is therefore:
\[
\mathcal E_{\rm total}
=
\mathcal E_{\mathfrak M}
+
\mathcal E_{\mathfrak T}
+
\mathcal E_{\mathfrak F}
+
\mathcal E_{\rm extraction}
+
\mathcal E_{\rm prime\ powers},
\]
where
\[
\mathcal E_{\mathfrak F}
\text{ is controlled through }
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}.
\]

---

## 6. Consequence for the role of OFI

A sector-preserving OFI multiplier can help the far-minor gate only through a provable bound on
\[
\int
\chi_{\mathfrak F}|\Omega|^2|S_\sigma|^2|S_\tau|^2.
\]

It cannot claim a far-minor gain by improving the major model, because the major model is absent there by construction.

Likewise, a putative OFI improvement must survive the locality/extraction costs of the output multiplier. The exact support identity does not turn a windowed coefficient estimate into an unwindowed pointwise Goldbach theorem.

---

## 7. Transition collar warning

A smooth cutoff cannot generally make the major and far regions touch without a collar. Any collar contribution must be assigned explicitly:
\[
\mathcal I_{\mathfrak T}(E)
:=
\int_0^1
\chi_{\mathfrak T}(\alpha)
S_\sigma(\alpha)S_\tau(\alpha)e(-E\alpha)d\alpha.
\]

Support separation transfers difficulty from cross-terms to this transition ledger; it does not erase it.

The advantage is exact bookkeeping:
\[
\text{major model error belongs to }\mathfrak M\cup\mathfrak T,
\qquad
\text{far-minor analysis sees only }S_\sigma S_\tau.
\]

---

## 8. Outcome

T33 sharpens the corrected spine to
\[
\text{major model on }\mathfrak M
\quad+\quad
\text{transition collar on }\mathfrak T
\quad+\quad
\boxed{
\int_{\mathfrak F}|\Omega|^2|S_\sigma|^2|S_\tau|^2
}
\text{ on }\mathfrak F.
\]

The far-minor bottleneck is therefore one pure arithmetic energy estimate. This is the right place to test any Type-I/II, large-values, spectral, or OFI mechanism.