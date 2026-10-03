# Additamentum I: second check of source queries

## Scope and evidence

2026-09-20. Independent review of all 35 listed source queries in `editorial/add1-notes.md`, followed by comparison with the corresponding passages in `tex/chapters/add1-p245-p310.tex`. The source was the original PDF `Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf`. Printed page p corresponds to physical PDF page p+3.

Images were extracted directly with `pypdf`, using `reader.pages[p+2].images[0].image`; the embedded images are approximately 2701 × 3777 pixels. Full pages and overlapping local crops were inspected, with particular attention to small fractions, superscripts, differential letters, signs, and numerical table entries. Working evidence is retained in `tmp/add1-query-check/pNNN.png` and `pNNN-0.png`, `pNNN-1.png`, `pNNN-2.png`. The 1900-pixel OCR previews were not the evidence for this check.

Result: no definite transcription error was found among these 35 queries. The queried TeX readings agree with the original bitmap, subject to the existing contextual qualification at p. 273. The repeated and skipped section numbers agree with the source and the visible editorial footnotes. No chapter TeX was changed. The wording locating the nested derivative at p. 280 was made more precise in the notes. This check establishes source readings only; it does not independently prove every mathematical claim or diagnose the origin of every inconsistency.

## Item-by-item result

| Original page / section | Query checked | Second-check result |
|---|---|---|
| 251 / 5 | Integrated P(xx+cx+f) has xx without the one-half appearing in the following formula. | Confirmed in embedded bitmap; matching TeX retained. |
| 253 / 10 | The displayed sine relation has radicand E²k⁴−P²f, without f squared. | Confirmed in embedded bitmap; matching TeX retained. |
| 254 / 11 | AF=nP is retained although the preceding construction uses mP. | Confirmed in embedded bitmap; matching TeX retained. |
| 255 / 13 | The second squared factor has hqx−½rxx. | Confirmed in embedded bitmap; matching TeX retained. |
| 259 / 24 | Integral of z⁷dx has denominator 2.4.6.6. | Confirmed in embedded bitmap; matching TeX retained. |
| 262 / 27 | Numerical identities involving b, a, f and 1,1803206 are retained as printed despite mutual inconsistency. | Confirmed in embedded bitmap; matching TeX retained. |
| 263 / 29 | MAN is first printed 81°,82′ and later 81°,22′. | Confirmed in embedded bitmap; matching TeX retained. |
| 265 / 32 | Final node angle ends 42″, compared with 48″ in the preceding discussion. | Confirmed in embedded bitmap; matching TeX retained. |
| 269 / 39 | f=g−37g⁵/(30c⁴) is retained. | Confirmed in embedded bitmap; matching TeX retained. |
| 270 / 41 | P coefficient contains a final dp in its numerator. | Confirmed in embedded bitmap; matching TeX retained. |
| 271 / 43 | First multiplied equation has −Qdq; the later equation has −qdQ. | Confirmed in embedded bitmap; matching TeX retained. |
| 272 / 44 | Arc is called AN=s. | Confirmed in embedded bitmap; matching TeX retained. |
| 273 / 46 | Faint numerator ydp in the long differentiated equation is read using the visible adjacent equality. This is a contextual reading rather than a wholly distinct printed glyph. | Faint first y remains a contextual reading; adjacent equality clearly supports ydp. Existing qualification retained. |
| 274 / 47 | Applicata PM=s is retained. | Confirmed in embedded bitmap; matching TeX retained. |
| 275 / 49 | Substitution prints c+Ekka/P. | Confirmed in embedded bitmap; matching TeX retained. |
| 277 / 53 | y-series term s⁹ has denominator ending b³. | Confirmed in embedded bitmap; matching TeX retained. |
| 279 / 57 | First moment sum has −yp; context elsewhere uses yq. | Confirmed in embedded bitmap; matching TeX retained. |
| 280 / 59 | dq expression has ωdt in its second term; the first displayed nested derivative denominator on this page has dv. | Confirmed in embedded bitmap; matching TeX retained. |
| 282 / 62 | Positive dr expression is retained following the preceding negative expression. | Confirmed in embedded bitmap; matching TeX retained. |
| 289 / 73 | Original repeats number 72; visible PDF footnote identifies normalization to 73. | Source numbering confirmed; disclosed editorial treatment matches TeX. |
| 290–291 / 74 | Entire calculation table retained; short and inconsistent 9,483130193 residual retained. | Confirmed in embedded bitmap; matching TeX retained. |
| 294 / 78 | All table entries retained, including second-column u=4,6925559924. | Confirmed in embedded bitmap; matching TeX retained. |
| 295 / 79 | Later exponential denominator prints exponent ½π where preceding approximation uses 5π/2. | Confirmed in embedded bitmap; matching TeX retained. |
| 296 / 80 | Radius expression prints dy²/ddy. | Confirmed in embedded bitmap; matching TeX retained. |
| 296 / 81 | Third condition prints 0=A−B−D. | Confirmed in embedded bitmap; matching TeX retained. |
| 298 / 83 | Historical exclusion of odd-intersection free modes retained without modern correction. | The exclusion of the odd-intersection modes is explicit in the source paragraph; matching text retained. No modern correction inferred. |
| 300 / 85 | Full table preserved, including u=4,7302983543, Error +636341 and +53145574. | Confirmed in embedded bitmap; matching TeX retained. |
| 301 / 85 | n=2423/10000 and subsequent 39+7576/10000 retained. | Confirmed in embedded bitmap; matching TeX retained. |
| 303 / 88 | Exponential sum with square root of cos(a/c) retained as printed. | Confirmed in embedded bitmap; matching TeX retained. |
| 304 / 89 | In the equation defining zero ordinate the first exponential has exponent a/c, second −a/(2c). Numerical ratios 0,607815, 0,551685, 0,448315 retained. | Confirmed in embedded bitmap; matching TeX retained. |
| 304–305 / 90 | l cot.φ retained without a half factor. | Confirmed in embedded bitmap; matching TeX retained. |
| 305 / 90bis | Repeated original number 90 made distinct through bis, with visible explanatory footnote. | Source numbering confirmed; disclosed editorial treatment matches TeX. |
| 306–307 / 91,93 | Source skips 92, disclosed in footnote. | Source numbering confirmed; disclosed editorial treatment matches TeX. |
| 307 / 93 | Ratio 57 ad 160 retained following 2,807041 ad 1. | Confirmed in embedded bitmap; matching TeX retained. |
| 309 / 96 | a/c=4,7300350232 retained. | Confirmed in embedded bitmap; matching TeX retained. |

## Notes on small readings

- P. 251: no one-half appears before the first integrated xx; the following formula does contain one-half.
- P. 253: the queried radicand ends in P²f, with no additional superscript on f.
- P. 277: the queried y-series exponent is visibly 3; the earlier cosine-series b⁸ provides a useful local comparison.
- P. 280: the queried denominator dv belongs to the first display after the dp/dq substitutions. Later displays have other denominators, which remain as printed.
- P. 295: the later exponential denominator visibly uses one-half π, whereas the preceding approximation uses five-halves π.
- P. 304: the first exponential in the zero-ordinate equation uses a/c, while the second uses −a/(2c); the mixed denominators are present in the original.

No recompilation was required for this read-only source review, since no TeX or figure changed. Combined-book layout verification remains recorded separately in `editorial/complete-front-visual-qa.md`.
