# 合版前半视觉 QA

检查对象：tmp/build/complete-front-proof.pdf，2026-09-20 22:02:55 生成的 146 页样稿，开始检查时文件大小 1,175,220 字节。

范围：PDF 物理第 1 至 80 页。每页以 1100 像素长边渲染，逐一查看四十张双页并排检查图。另以 1800 像素长边放大检查物理第 21、33、37、40、42、43、49、51、52、54、65、66、74、76、77 页。

检查包括扉页、制作说明、临时目录、页眉、原页码边注、长公式、分式与上下标，以及章节之间的连续阅读。检查图在 tmp/pdfs/front-qa/。

## 明确发现

- **物理第 79 页**：第四章起页直接从“Propositio I. Problema.”开始，缺少“CAPUT IV”及第四章章题。第一至第三章均有章标题，第四章 body 文件有意不含总模板所负责的章题，合版模板需要补入。该问题已向主代理报告。添加章题后需复查第 79 页及其后重新分页。

## 其余结论

第 1 至 78 页及当前第 80 页未发现明确的文本裁切、行间叠压、公式越出版心、边注与正文碰撞或错误章节页眉。第一章至第二章的 20/21 页交界、第二章至第三章的 49/50 页交界正常。公式密集页放大检查未发现新增明确版面缺陷。临时目录准确列出当前前三章起页 4、21、50 以及第四章起页 79；最终加入附录与图版后仍需核验完整目录。

本记录属于版面与阅读连续性的视觉 QA，未重新执行逐字拉丁文校勘或数学推导审查。未修改正文、图或排版文件。

## Second pass: complete-text-proof.pdf, physical pages 79–148

The 187-page combined proof was reviewed at 1100 pixels per page, with every physical page 79–148 viewed in paired spreads. Formula-dense physical pages 85, 96, 109, 119, 122, 130, 135 and 145 were additionally inspected at 1800 pixels. The previously reported missing chapter IV heading is resolved on physical p. 79. Chapter V begins correctly on p. 104; chapter VI begins on p. 137 and ends on p. 146; Additamentum I starts on p. 147. No new definite layout defect was found in these pages. Long displays, prime and roman derivative superscripts, margin source-page labels, running heads, and section transitions remain legible without clipping or overlap. This pass checks layout, not a renewed source transcription.
