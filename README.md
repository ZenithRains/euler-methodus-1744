# Euler · Methodus inveniendi (1744)

**拉丁文扫描校录、LaTeX 重排与矢量图工程，Eneström 编号 E65。**

整理者：Ruiyi Zhang。工程包含 Euler 1744 年 E65 的拉丁文 OCR、扫描对照校录、LaTeX 重排和矢量图。中文翻译在 `translation/zh-Hans/` 独立进行，尚未完成；当前公开副本以拉丁文工程为范围。

**版本性质：AI 辅助校录工作稿。** 全书结构和版面已检查，仍欢迎独立的扫描对照复核。构建成功、OCR 置信度和模型复核均不能证明每个字或公式完全正确。

English: A source-traceable, AI-assisted Latin transcription and LaTeX retypesetting of Leonhard Euler's *Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes sive solutio problematis isoperimetrici latissimo sensu accepti* (1744, E65). This is a working edition, with editorial queries and schematic vector redrawings. Independent scholarly proofreading remains welcome. The incomplete Chinese translation is maintained separately.

## 阅读与来源

[GitHub 仓库](https://github.com/ZenithRains/euler-methodus-1744) · [工作稿 Release](https://github.com/ZenithRains/euler-methodus-1744/releases/tag/v0.1.0-latin-draft)

- [重排版介绍](https://zenithrains.github.io/zh/notes/2026/09/euler-e65/)
- [已发布的拉丁文 PDF](https://zenithrains.github.io/files/euler-e65-latin-working-draft.pdf)
- [Euler Archive E65 原书目录页](https://scholarlycommons.pacific.edu/euler-works/65/)
- [ETH-Bibliothek Zürich 同版馆藏，Rar 4999](https://doi.org/10.3931/e-rara-1490)

详细底本、图饰与模板来源见 [PROVENANCE.md](PROVENANCE.md)。各部分版权与许可见 [RIGHTS.md](RIGHTS.md)。公开仓库的范围与版本约定见 [PUBLICATION.md](PUBLICATION.md)。

## 当前交付

全书主文件为 `tex/e65-complete.tex`，合并交付为 `output/pdf/Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes.pdf`，共212页。包含六章、两附录、原书目录、拉丁文及法文装订说明，以及正文21图和附录28图。八部分分别为66、71、47、42、76、25、97、16节，共440节。统一 EB Garamond、Garamond-Math、暖纸色 `#FAF6ED`，单一扉页、连续页码、章节目录及两套独立图号。早期分章PDF继续保留。

实际编译及内容结构检查见 `editorial/complete-qa.json`，校录和图形说明位于 `editorial/*-notes.md`。本版为AI辅助全书校录工作稿，保留可追溯疑点，独立学术复核尚待进行。

以下分章 PDF、旧样张和逐页 OCR 保留于完整本地工程；公开副本只导出当前合版依赖、合并 OCR、页面清单及校录记录。


- `output/pdf/e65-caput-i.pdf`：完整第一章校录工作稿，共20页，§§1–66，对应原书第1至31页。采用 EB Garamond＋Garamond-Math，扉页纳入 ETH 馆藏图饰的矢量描摹，附图1至3。
- `tex/e65-caput-i.tex`：完整第一章主文件。
- `output/pdf/e65-caput-ii.pdf`：完整第二章校录工作稿，§§1–71，对应原书第31至82页，附图4、5。
- `output/pdf/e65-caput-iii.pdf`：完整第三章校录工作稿，§§1–47，对应原书第83至129页，附图4、6。
- 第二、三章采用已确认的轻微暖纸色 `#FAF6ED`；主文件为 `tex/e65-caput-ii.tex` 和 `tex/e65-caput-iii.tex`。
- `editorial/chapters23-qa.md`：第二、三章范围、复核和交付检查记录；分段 notes 保存原印疑点。
- `output/pdf/e65-latin-sample.pdf` 与 `e65-latin-sample-garamond.pdf`：保留的早期字体比较样张。
- `ocr/full-raw.txt`：全书原始 OCR 合并文本，未校订，公式识别不可靠。
- `ocr/raw/page-NNN.txt` 与 `.tsv`：PDF第2至331页的330组原始OCR文件。
- `ocr/page-manifest.csv`：逐页类别、顺序页号、OCR状态、引擎置信度及文本哈希。置信度不代表真实准确率。
- `sources/source-manifest.json`：底本SHA-256、页数及OCR参数。
- `editorial/scan-inventory.md`：六章、两附录、五图版的定位，明确核验边界。
- `editorial/editorial-policy.md` 与 `errata-and-queries.md`：编辑规则、实际复核范围和疑点。

## 底本

用户提供的 `Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf`，来源为 Euler Archive E65，331个PDF页面。PDF1为档案封面，2为原扉页，3为空白，4起为正文；末尾含目录、装订说明与5张图版。

来源页面：https://scholarlycommons.pacific.edu/euler-works/65/

原PDF保持不变，SHA-256为 `eeaa387cfcfa6056e6aebc592d12cd65675ebb8620ab955216421ffc1d1414c8`。全书文字与图版按所提供扫描进行AI辅助逐页校录；不把这一工作等同于独立学术校勘或对其他馆藏印本的完整性鉴定。

## 构建

需要 TeX Live 2026 或兼容环境、LuaLaTeX、EB Garamond、Garamond-Math、fontspec、unicode-math、babel拉丁语、TikZ、adjustbox、amsmath、geometry、microtype、marginnote、needspace、fancyhdr、titlesec、hyperref、xurl。

```sh
sh scripts/build-complete.sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check-complete.py
./scripts/build-chapter1.sh
sh scripts/build-chapters23.sh
```

PDF输出至 `output/pdf/`，日志在 `tmp/build/`。本机验证使用 LuaHBTeX 1.24.0（TeX Live 2026）。正文和公式可搜索，全部49幅编号插图为TikZ矢量路径，扉页图饰以矢量PDF嵌入。字体版本与文件哈希见 `sources/font-manifest.json`；字体本身不打包。

编译不需要扫描 PDF。结构检查在扫描文件缺席时明确记录 `not_provided`；若要强制核验底本，运行 `python3 scripts/check-complete.py --require-source`。不同 TeX 或字体版本可能影响分页。原始扫描件未随公开副本分发，请从上述来源页面自行获取；下载遇到限制时可以手工保存，脚本不会绕过访问限制。

OCR需要 Python 3、Poppler的pdftoppm、Tesseract及拉丁语数据：

```sh
python3 scripts/ocr.py --workers 4
python3 scripts/assemble_ocr.py
```

OCR可断点续跑，已存在的TXT会被跳过。参数为300dpi灰度、Tesseract 5.5.3、lat、PSM3。复跑OCR时先将需要重识别的TXT和TSV移至单独备份目录，勿覆盖已校录TeX。

## 版式与授权

借鉴 Foadsf/vintage-latex，固定提交 `559011918849a3da819912a7c26493071d542df5`，本地参考位于 `reference/vintage-latex`。改编模板采用 CC BY-SA 4.0，保留原作者与贡献者署名、上游链接和修改说明；见TeX头注、PDF制作说明及 `editorial/template-audit.md`。

1744年拉丁原文属于公共领域；扫描来源独立记录，不新增扫描权利主张。EB Garamond与Garamond-Math遵循SIL OFL 1.1。未引入fiziko。现代校录说明与独立图形代码采用 CC BY-SA 4.0；独立脚本采用 MIT。中文译稿的公开授权另行确定。原文与第三方材料的权利状态分别保留。

制作由GPT-6辅助，部分初步检查和校录由GPT-5.6 Luna辅助。模型参与已在样张中披露。现代说明、校录记录、版式及图形代码采用 CC BY-SA 4.0，独立脚本采用 MIT；完整许可分别位于 `LICENSE` 与 `LICENSES/MIT.txt`，范围见 `RIGHTS.md`。

## 后续

字体、图饰及暖纸方案已获确认，全书已完成统一合版。49 幅编号图统一置于书末。后续可依据校录记录进行独立学术复核，逐项解决原印疑误和模糊字形，再确定拉丁定本。中文译稿独立推进；2026-10-03 检查其进度文件时，记录为 258/440 个文本单元，尚无完整译本交付。

## 仓库整理

`tex/e65-complete.tex` 是当前全书入口，`tex/chapters/` 为校录正文，`tex/figures/` 为矢量图。`editorial/` 保留校录疑点及各阶段检查记录，早期记录按其形成时的范围理解；当前状态以本 README 为准。`ocr/full-raw.txt` 是未校订的识别层。`sources/` 保存来源及环境元数据。

`python3 scripts/prepare-public-repo.py` 将当前材料复制到 `publication/euler-methodus-1744/`，按白名单导出，保留文件哈希。它保留本地扫描、缓存、样张和中文译稿，导出期间不移动或删除它们。旧样张、完整参考项目和临时文件不进入公开副本。已发布 PDF 的字节保持原样，存入公开副本的 `release/`，用于 GitHub Release 上传。该导出脚本绑定已批准 PDF 的哈希，适用于完整本地工程的发布整理。

如要协助校录，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，给出原页、节号、扫描证据和修改理由。

## 字体比较与图饰试稿（2026-09-17）

`output/pdf/e65-latin-sample-garamond.pdf`为Garamond-Math数学字体比较版，其余内容与版式沿用现有样张。TeX源为`tex/e65-latin-sample-garamond.tex`，在tex目录用LuaLaTeX连续编译两次即可。原Pagella样张保持可用。比较重点为第6至7页的公式。

更清晰的同书扉页来自ETH Zürich Rar 4999，详见`editorial/ornament-source.md`。图饰SVG已检查细线、题字和底部署名并收入第一章扉页；局部淡线仍有损失，详见来源说明，不作原铜版无损复原的主张。
