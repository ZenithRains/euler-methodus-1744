# Appendix figures 1–15

Source: the supplied E65 scan, Tabula III (PDF329, appendix figures1–7) and Tabula IV (PDF330, appendix figures8–15). Both complete plates were inspected at 3800-pixel render size; individual crops of all 15 figures were viewed for lettering and crossings.

Files: tex/figures/addfig01.tex through addfig15.tex. Each is a self-contained TikZ picture matching the edition's .35 pt rule and small Garamond mathematical lettering. These are manual geometric redrawings with schematic coordinates, not exact facsimiles. Curves are hand-drawn Bézier paths following the scan; no replacement analytic elastic-curve solution is asserted. Paper damage and engraving shading are omitted. The integration template supplies addfig:1 through addfig:15 hyperlink targets.

## Individual checks

1. A–M–m–B curve and separate ray MR retained.
2. A–M–m–B inflected curve, baseline AD, ordinate MP retained.
3. Tangent T–N–M–B, curved AM, horizontal T–C–A–P, vertical ND and MP, oblique NQ, suspended body D and endpoint clamp B retained. The weight is an unshaded circle.
4. Vertical R–N–C–D–E, horizontal C–A–P, tangent NM and ordinate MP retained. Curve passes through D and A to M.
5. Lowercase a,b,d,f distinguished from uppercase A,B,D,E,F. Curve continues through f,D,F,B,A,M. Oblique branches Aa, Bb, Dd and vertical DE retained.
6. Upper/lower case point pairs retained: b/B,c/C,d/D,e/E,m/M,n/N,p/P,q/Q. The S-shaped elastic curve and both transverse ordinate systems are retained.
7. The upper r and lower R are distinct labels. The curve crosses the central axis at b,A,B; left n,m and right M,N mark the corresponding ordinate ends. Labels n,m were moved off the curve after rendering. Both outer continuations remain open.
8. Two lobes cross at A. Lowercase c,p,m are on the left; uppercase C,P,M,N are on the right. No spurious ordinate through N is added.
9. Two separated self-crossing loops have upper O and lower o; the main central crossing is A. B and b label the outer endpoints. Upper and lower coordinate systems are retained with their case differences. Cubic segments explicitly pass through C,c,M,N,m,n and both crossings.
10. Single right loop with crossing O, outer A and B endpoints, baseline DC, and MN ordinate through Q retained.
11. All three loops and their o/O/o crossings retained. Central D,F,O,Q,C lettering retained, with G and H on the connecting left-hand branches. Upper and lower repeated lowercase labels retained. The vertical ordinate endpoints and adjacent letters were adjusted after rendering to avoid touching the curve.
12. A is common to the curved AC, tangent AT and suspended load P. Load rendered as an unshaded circle.
13. Column AB, base and separate loading body P retained. The characteristic weight outline is approximated in vector form; fine engraved shading is omitted.
14. Deflected member A–m–F, horizontal HF, baseline AG, ordinate mp, masonry support GK and load P retained. Brick joints are schematic decorative structure, without introducing mechanical constraints absent from the original.
15. Symmetric tapered outline from A to f and f, central AF and transverse m–M–m retained. Both repeated lowercase f and m labels are deliberate source readings.

## Verification

Temporary wrapper tex/addfig1-15-proof.tex compiles with LuaLaTeX to 15 pages. All 15 rendered figure crops were inspected at 1400-pixel page resolution. Label/curve collisions in 7 and 11 were corrected and re-rendered. No overfull boxes were reported. The wrapper PDF is tmp/addfig1-15-proof.pdf. Final full-book sizing is controlled by tex/e65-complete.tex.
