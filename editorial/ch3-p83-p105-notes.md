# Chapter III, original pp. 83–105, §§1–30

The previous OCR-derived file was replaced in full by direct image collation on 2026-09-20. All 23 source-page images (PDF86–108) were viewed. Latin prose and displayed intermediate computations were transcribed, including the full §30 at the end of p105. This is AI-assisted working transcription, not independent scholarly verification.

Long s normalized; æ retained; page headers, signatures, and catchwords removed; line-end divisions joined. The large integral quantity is represented by `\Pi`; the second, distinct quantity introduced in §29 is `\pi`. Successive-value superscripts above iii use roman iv, v, vi, etc. These are not derivative orders. Original `pp`, `dd`, colon exponents, and logarithm `l` retained.

## Printed anomalies retained for review

- P84, the last numerator in `d.[Z^iv]dx` visibly reads `5[Z^iv]`; the surrounding pattern requires T. Retained Z.
- P89, long combined increment: the R numerator ends `3L'''dd[R'']`, whereas summation suggests `3L^v dd[R'']`. Retained the source's triple-prime reading.
- P90 prose calls the remaining terms `L^vi dx + L^vii dx`, although the summands being differentiated are Z terms. Retained L.
- P91 §7 twice prints AZ for the remaining segment of length a−x; the preceding proof calls this HZ or NZ. Retained AZ.
- P92 §10 prints `x=AH=a`; retained.
- P92 §12 lists `[N]=0, [R]=0`; retained R.
- P96 §18 first displayed inline double integral lacks y in its inner integrand. The subsequent restatement includes y. Retained this difference.
- P97 §18 altered functional has dx multiplying a bracket containing both the radical and a differential fraction; this appears inconsistent with the immediately preceding variation. Kept the printed placement and supplied balanced grouping for typesetting.
- P101 §27 first stationarity formula has a positive `1/dx` differential term, whereas the following equality implies a negative term. Retained the printed positive sign.
- P101 §27 says `ad gradum sextum` and `sex constantes` after describing a second-order equation differentiated twice. These words are retained.
- P103 §29 prints `xy−π=Πy/x`, whereas the following expression for Π would require denominator π. Retained x.
- P104 final logarithmic denominators are unparenthesized in the source: `l(g/c)(1−l(g/c))` and `lg(1−l(g/c))−lc`. The transcription preserves this historical grouping ambiguity instead of adding a modern interpretation.
- P105 §30 table visibly prints a plus sign before `2nν/dx²` in `d.q'`; standard successive second differences suggest minus. The printed plus is retained.

## Remaining verification boundary

Dense formulas were entered from the images, including source inconsistencies, and require independent formula-by-formula scholarly collation. Build checks establish TeX validity and visible typesetting only.

## Build verification

Full `tex/e65-caput-iii.tex` compiled with LuaLaTeX, exit 0, producing 32 pages in `tmp/e65-caput-iii.pdf`. After converting two long inline expressions to displays, the log contains no overfull boxes and no missing-character reports. Dense formula pages 4–5 rendered and visually inspected; formula groups fit, brackets and superscripts appear legibly.

The displacement point was standardized to Latin `v`, consistent with Fig. 4 and the earlier chapters; the initial reading as Greek nu was based only on the similar historical type shape. A Fig. 4 link was added to §1.

Full rendered-layout pass: every page 1–32 of the complete Chapter III PDF was viewed, including title page, editorial notice, all body pages, and the final figures. No visible formula clipping, text occlusion, orphaned standalone formula page, or overlapping figure labels was found. The short final prose page 31 is the normal chapter ending before the figure plate. A first-pass original-p97 marginal-note position was flagged for a further LaTeX pass to stabilize stored page coordinates. Layout inspection of §§31–47 does not constitute new source collation of that segment.

Final repeated LuaLaTeX run again passed (32 pages; no overfull boxes or missing-character reports). Page 11 was re-rendered and the original-p97 marginal note now sits correctly outside the text block.
