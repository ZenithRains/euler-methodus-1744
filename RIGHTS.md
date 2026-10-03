# 版权与许可边界

本工程包含多种来源的材料，授权按组成部分分别说明。下表记录已查证的上游授权及本工程现代新增内容的许可。

| 材料 | 来源与当前状态 | 使用说明 |
| --- | --- | --- |
| Euler 1744 年拉丁原文及原书图版 | 历史公有领域作品；[ETH 同版记录](https://www.e-rara.ch/zut/content/titleinfo/433675)标注 Public Domain Mark | 整理者不对原文主张新增版权。忠实转录的原文不因进入现代 TeX 文件而整体变为模板作者的作品。 |
| 用户保存的 Euler Archive 扫描 PDF | [University of the Pacific E65](https://scholarlycommons.pacific.edu/euler-works/65/)；当前查阅目录未见该文件的明确 CC 再分发许可 | 公开副本提供链接和文件哈希，扫描 PDF 留在本地。没有将 ETH 的馆藏标记移植到这份文件。 |
| ETH 扉页原图与裁切 | ETH-Bibliothek Zürich，Rar 4999，[doi:10.3931/e-rara-1490](https://doi.org/10.3931/e-rara-1490)；Public Domain Mark | 保留作者、馆藏、索书号、DOI 和图饰改编说明。此标记与 CC BY-SA 许可证有不同用途。 |
| 改编的排版模板 | Foadsf/vintage-latex 及其 contributors，提交 `559011918849a3da819912a7c26493071d542df5`；CC BY-SA 4.0 | 保留署名、上游链接、许可和修改说明；发布改编模板时采用相同许可。 |
| EB Garamond 字体 | EB Garamond Project Authors；SIL OFL 1.1 | 不打包字体文件。许可证副本与字体实际元数据保留在工程中。 |
| Garamond-Math 字体 | Yuansheng Zhao 与 Xiangdong Zeng；SIL OFL 1.1 | 不打包字体文件。OFL 不要求使用该字体制作的文档整体采用 OFL。 |
| 现代校录说明、独立 TikZ 图形代码、版式贡献 | Ruiyi Zhang；披露 AI 辅助制作 | 在可受版权保护的范围内按 CC BY-SA 4.0 授权；见 `LICENSE` 和 `LICENSES/CC-BY-SA-4.0.txt`。原文及上游材料依其自身状态处理。 |
| 独立 Python 和 shell 脚本 | Ruiyi Zhang；披露 AI 辅助制作 | MIT，见文件头及 `LICENSES/MIT.txt`。此许可不改变它们所处理的历史文本、扫描件或模板的权利状态。 |
| 中文译稿 | 独立进行的未完成译稿 | 当前公开副本不收录；授权另行确定。 |

## 原作者和整理者

原书作者为 **Leonhard Euler**。现代整理、排版与工程维护署名为 **Ruiyi Zhang**。不得将现代校录或译稿归为 Euler 本人写作，也不得把历史原文署为整理者的原创。机构来源和模板署名表示来源与致谢，未表示其审定或背书本版本。

## 上游许可

- [vintage-latex 固定提交的 LICENSE](https://github.com/Foadsf/vintage-latex/blob/559011918849a3da819912a7c26493071d542df5/LICENSE)，本地逐字副本为 `LICENSES/vintage-latex-CC-BY-SA-4.0.txt`。
- [CC BY-SA 4.0 许可说明](https://creativecommons.org/licenses/by-sa/4.0/)及[法律文本](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)。
- [Public Domain Mark 1.0 说明](https://creativecommons.org/publicdomain/mark/1.0/)及[e-rara 使用条件](https://www.e-rara.ch/wiki/termsOfUse)。
- 字体许可见 `LICENSES/EB-Garamond-OFL-1.1.txt` 和 `LICENSES/Garamond-Math-OFL-1.1.txt`。

## 现代新增内容的许可范围

现代 README、PROVENANCE、PUBLICATION、CONTRIBUTING、引用与来源清单、`editorial/` 校录说明及检查记录、`tex/` 中可受保护的现代标记、版式和独立图形代码，采用 **CC BY-SA 4.0**。Ruiyi Zhang 的现代贡献署名与 Foadsf/vintage-latex 的上游署名分别保留。重排 PDF 的可受保护的现代编辑和排版部分同样采用 CC BY-SA 4.0。

公开副本 `scripts/` 内的六个独立工具 `ocr.py`、`assemble_ocr.py`、`trace_ornament.py`、`build-complete.sh`、`check-complete.py` 和 `prepare-public-repo.py` 采用 **MIT**。

上述授权自 2026-10-03 起用于本工程公开的现代新增内容。原文的公有领域地位、第三方材料的授权和纯机械转换的权利状态保持独立；这些许可不扩张到整理者无权重新授权的内容。自动描摹图饰的路径和历史图像不新增版权主张。中文译稿未包含在本次发布范围中，其授权另行确定。
