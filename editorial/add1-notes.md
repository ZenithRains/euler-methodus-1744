# Additamentum I: transcription and source notes

## Coverage and workflow

Source PDF pages 248–313, logical and printed pages 245–310, were rendered at 1900 pixels and visually read sequentially. All 66 source pages are represented by sourcepage markers. The 97 numbered text units, all intermediate equations, and numerical calculation tables are transcribed into tex/chapters/add1-p245-p310.tex. The long s is normalized to s; ligatures, historical differential notation, repeated products, decimal commas, and &c. are retained. No translation has been added. Raw OCR was auxiliary only.

The opening paragraph is section 1, not an unnumbered preface. The section sequence is 1–90, 90bis, 91, 93–97. Original p. 289 prints 72 for the paragraph following 72; this edition uses 73 and discloses the change in a footnote. Original p. 305 repeats 90, retained as 90bis with a footnote. Original p. 306 prints 91 and p. 307 proceeds to 93; the absent number 92 is disclosed, without inventing a paragraph.

Required figures are Appendix figures 1–25. Figure calls use addfig destinations, distinct from main-text numbering. Source marginal topic rubrics present in the source have been retained where transcribed as species labels. Primary text and formula transcription is complete; this is not a critical edition and the mathematical claims have not been modernized or independently proved.

## Source readings and apparent printing errors retained

These are source-critical observations, not mathematical corrections. Formula strings below identify the passage; the TeX file contains complete formulas.

| Original page / section | Reading retained or editorial observation |
|---|---|
| 251 / 5 | Integrated P(xx+cx+f) has xx without the one-half appearing in the following formula. |
| 253 / 10 | The displayed sine relation has radicand E²k⁴−P²f, without f squared. |
| 254 / 11 | AF=nP is retained although the preceding construction uses mP. |
| 255 / 13 | The second squared factor has hqx−½rxx. |
| 259 / 24 | Integral of z⁷dx has denominator 2.4.6.6. |
| 262 / 27 | Numerical identities involving b, a, f and 1,1803206 are retained as printed despite mutual inconsistency. |
| 263 / 29 | MAN is first printed 81°,82′ and later 81°,22′. |
| 265 / 32 | Final node angle ends 42″, compared with 48″ in the preceding discussion. |
| 269 / 39 | f=g−37g⁵/(30c⁴) is retained. |
| 270 / 41 | P coefficient contains a final dp in its numerator. |
| 271 / 43 | First multiplied equation has −Qdq; the later equation has −qdQ. |
| 272 / 44 | Arc is called AN=s. |
| 273 / 46 | Faint numerator ydp in the long differentiated equation is read using the visible adjacent equality. This is a contextual reading rather than a wholly distinct printed glyph. |
| 274 / 47 | Applicata PM=s is retained. |
| 275 / 49 | Substitution prints c+Ekka/P. |
| 277 / 53 | y-series term s⁹ has denominator ending b³. |
| 279 / 57 | First moment sum has −yp; context elsewhere uses yq. |
| 280 / 59 | dq expression has ωdt in its second term; the first displayed nested derivative denominator on this page has dv. |
| 282 / 62 | Positive dr expression is retained following the preceding negative expression. |
| 289 / 73 | Original repeats number 72; visible PDF footnote identifies normalization to 73. |
| 290–291 / 74 | Entire calculation table retained; short and inconsistent 9,483130193 residual retained. |
| 294 / 78 | All table entries retained, including second-column u=4,6925559924. |
| 295 / 79 | Later exponential denominator prints exponent ½π where preceding approximation uses 5π/2. |
| 296 / 80 | Radius expression prints dy²/ddy. |
| 296 / 81 | Third condition prints 0=A−B−D. |
| 298 / 83 | Historical exclusion of odd-intersection free modes retained without modern correction. |
| 300 / 85 | Full table preserved, including u=4,7302983543, Error +636341 and +53145574. |
| 301 / 85 | n=2423/10000 and subsequent 39+7576/10000 retained. |
| 303 / 88 | Exponential sum with square root of cos(a/c) retained as printed. |
| 304 / 89 | In the equation defining zero ordinate the first exponential has exponent a/c, second −a/(2c). Numerical ratios 0,607815, 0,551685, 0,448315 retained. |
| 304–305 / 90 | l cot.φ retained without a half factor. |
| 305 / 90bis | Repeated original number 90 made distinct through bis, with visible explanatory footnote. |
| 306–307 / 91,93 | Source skips 92, disclosed in footnote. |
| 307 / 93 | Ratio 57 ad 160 retained following 2,807041 ad 1. |
| 309 / 96 | a/c=4,7300350232 retained. |

## Verification

Independent wrapper: tex/add1-proof.tex. Initial LuaLaTeX build succeeded, 33 pages, no overfull boxes or missing characters. A second build resolved marginal-position coordinates. All 33 proof pages were visually inspected. One collision at source p. 247 between source-page label and Fig. 1 was separated by an explicit marginal offset. A chapter heading was then added for independent reuse and the wrapper rebuilt. Final verification details are appended below.

Final independent build: three consecutive LuaLaTeX runs succeeded, 33 pages, no overfull boxes or missing characters. First two pages were re-rendered after the heading and Fig. 1 offset changes; the collision is resolved and the title is present. Figure links to targets defined only by the combined edition naturally remain unresolved in this standalone proof. Parent performs final combined-book layout and destination checks.

## Independent embedded-bitmap second check

All 35 source queries above were independently rechecked against original embedded bitmap crops on 2026-09-20, and compared with the chapter TeX. No definite transcription error was found among the queried passages. The contextual reading at p. 273 remains explicitly qualified. The p. 280 note now identifies the first displayed nested derivative more precisely. See `editorial/add1-source-queries-second-check.md` for the complete itemized result and evidence paths. This verification confirms the source readings; it does not independently certify the mathematical claims.
