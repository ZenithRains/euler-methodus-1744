# 来源与制作说明

最后核查：2026-10-03。

## 原书与拉丁文底本

Leonhard Euler, *Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes sive solutio problematis isoperimetrici latissimo sensu accepti*. Lausannae & Genevae: apud Marcum-Michaelem Bousquet & Socios, 1744. Eneström 编号 E65。

正文校录使用用户保存的 Euler Archive E65 扫描件；[University of the Pacific 目录页](https://scholarlycommons.pacific.edu/euler-works/65/)为来源入口。当地文件名缩略为 `Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf`。它有 331 个 PDF 页面、47,861,933 字节，SHA-256：

```text
eeaa387cfcfa6056e6aebc592d12cd65675ebb8620ab955216421ffc1d1414c8
```

PDF 第 1 页为档案封面，第 2 页为原扉页，第 3 页为空白，第 4 页起为正文。原书正文与两附录的原页标记覆盖 1 至 320，另含原目录、装订说明和五张图版。档案目录采用的书名存在 `lattissimo` 拼写，工程书名按原扉页及 ETH 目录使用 `latissimo`。当前目录链接与本地文件哈希分别记录；未断言今后重新下载的文件必然具有同一哈希。

公开副本提供来源链接及哈希，不附带该扫描 PDF。目录页的“免费开放访问”说明与具体的再分发许可分别理解；未把 ETH 对其馆藏的授权套用到 Euler Archive 文件。

## ETH 扉页图饰

来源为同书 1744 年印本的 ETH-Bibliothek Zürich 馆藏，索书号 **Rar 4999**，持久标识符 [doi:10.3931/e-rara-1490](https://doi.org/10.3931/e-rara-1490)。[e-rara 记录](https://www.e-rara.ch/zut/content/titleinfo/433675)标注 **Public Domain Mark**。详见 [RIGHTS.md](RIGHTS.md) 和原制作记录 `editorial/ornament-source.md`。

- [IIIF Manifest](https://www.e-rara.ch/i3f/v20/433675/manifest)
- [扉页原图](https://www.e-rara.ch/i3f/v20/433682/full/full/0/default.jpg)
- [图饰裁切](https://www.e-rara.ch/i3f/v20/433682/535,1700,1230,840/full/0/default.jpg)

原图和裁切保存在 `sources/e-rara/`。图饰经过局部亮度分离及 Potrace 描摹；`tex/figures/title-ornament.svg` 是批准的 SVG 试稿，`title-ornament.pdf` 是用于排版的矢量 PDF。它们保留可见图形、题字与署名，局部淡线可能丢失，没有补造缺失笔画。PDF 是 SVG 的格式转换结果，仓库不承诺重新转换后的 PDF 字节与现有文件一致。

编号插图依据底本五张图版重绘为 49 个 TikZ 文件：正文 `fig01` 至 `fig21`，附录 `addfig01` 至 `addfig28`。轮廓与坐标为排版示意，点名及几何关联依据原图核对；它们没有度量精度或原铜版无损复原的主张。

## 模板与字体

版式改编自 [Foadsf/vintage-latex](https://github.com/Foadsf/vintage-latex)，固定提交 [559011918849a3da819912a7c26493071d542df5](https://github.com/Foadsf/vintage-latex/tree/559011918849a3da819912a7c26493071d542df5)，主要参考 `examples/01-early-modern-page.tex`。署名保留 Foadsf 与 repository contributors。变更包括书名、页边距、暖纸色 `#FAF6ED`、页眉、原页标记、公式排版、内容组织及矢量图装配。改编模板保留 CC BY-SA 4.0，原授权文本位于 `LICENSES/vintage-latex-CC-BY-SA-4.0.txt`。本工程未使用 fiziko。

正文使用 [EB Garamond](https://github.com/octaviopardo/EBGaramond12)，数学使用 [Garamond-Math](https://github.com/YuanshengZhao/Garamond-Math)，均为 SIL OFL 1.1。当前本机实际字体版本、文件 SHA-256 及版权元数据在 `sources/font-manifest.json`；它们与上游 README 中的版本号可能不同。公开副本不附带字体文件。

## OCR、校录与编辑层

原始 OCR 使用 Tesseract 5.5.3、`lat` 数据、PSM 3，以及 300 dpi 灰度页面。逐页记录为 `ocr/page-manifest.csv`，合并识别文本为 `ocr/full-raw.txt`，扫描和参数记录为 `sources/source-manifest.json`。原始 OCR 的公式及置信度不宜直接作为可靠正文。

整理者为 Ruiyi Zhang。制作由 GPT-6 辅助，早期清点、初稿转录及部分检查由 GPT-5.6 Luna 辅助。拉丁文采用扫描对照的 AI 辅助校录，公式逐项检查，疑点保存在 `editorial/`。这份工作稿尚未获得独立学者对全书逐字逐式的审校认证。

重排按现有编辑规则归一化长 s、跨行断词及部分标题缩写，保留历史数学记法、原节号和原页标记。疑似原印错误与现代录入错误分别记录，修改应能回溯到底本。中文译稿独立维护，未包含在当前公开副本中。

## 已发布 PDF

文件名：`Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes.pdf`；212 页；1,451,058 字节。2026-10-03 核验 SHA-256：

```text
0ec2d3570b1510cd392ac937e0a87d9abd2a4f72cb6cd16ba19f4154037f45e1
```

[个人站点下载](https://zenithrains.github.io/files/euler-e65-latin-working-draft.pdf)。重新构建可能因 PDF 创建时间等元数据产生不同哈希；本工程另行保留已发布文件的字节和记录。
