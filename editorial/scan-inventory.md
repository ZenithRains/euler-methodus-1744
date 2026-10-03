# 扫描件页序核验

核验对象：`Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf`

核验日期：2026-09-17

文件页数：331 页。`pdfinfo` 与 `pypdf` 均报告 331 页。核验文件 SHA-256 为 `eeaa387cfcfa6056e6aebc592d12cd65675ebb8620ab955216421ffc1d1414c8`。

## 前置页与原序

1. PDF 第 1 页是 University of the Pacific Scholarly Commons 的档案封面，含年份 1744、Euler Archive 信息、推荐引文及开放获取说明。E65 是本项目使用的 Eneström 编号，封面上的 1744 是作品年份。
2. PDF 第 2 页是原书扉页，题名为 `METHODUS INVENIENDI LINEAS CURVAS Maximi Minimive proprietate gaudentes, sive solutio problematis isoperimetrici latissimo sensu accepti`，署名 Leonhardo Eulero。
3. PDF 第 3 页为空白页。
4. PDF 第 4 页顶部直接出现 `CAPUT PRIMUM`，正文印刷页码为 1。

据此，在本 PDF 的前置页中没有发现独立的原序、献词或序言页。这个结论限于本文件所收页序。PDF 第 4 页开始正文，支持“原序未收录或未置于此扫描件前部”的判断。尚未取得另一份底本或档案元数据来判断原版是否曾有另页序言。

## 正文、附录与印刷页码

PDF 页码是文件页码，括号内为书内印刷页码。章节起始位置由逐页 OCR 标题及页眉页码核对。

| 部分 | PDF 起始页 | 印刷起始页 | 核验状态 |
| --- | ---: | ---: | --- |
| Caput I，De Methodo maximorum & minimorum ad lineas curvas inveniendas applicata in genere | 4 | 1 | 已核验，OCR 与页眉 |
| Caput II，De Methodo maximorum & minimorum ad lineas curvas inveniendas absoluta | 34 | 31 | 已核验，PDF 图像页眉 |
| Caput III，De inventione curvarum maximi minimive proprietate praeditarum | 86 | 83 | 已核验，OCR 与目录 |
| Caput IV，De usu Methodi hactenus traditae in resolutione varii generis quaestionum | 132 | 129 | 已核验，OCR 与目录 |
| Caput V，Methodus inter omnes curvas eadem proprietate praeditas | 174 | 171 | 已核验，OCR 与页眉 |
| Caput VI，Methodus inter omnes curvas pluribus proprietatibus communibus gaudentes | 230 | 227 | 已核验，OCR 与目录 |
| Additamentum I，De Curvis Elasticis | 248 | 245 | 已核验，OCR 与正文页码 |
| Additamentum II，De Motu Projectorum in medio non resistente | 314 | 311（目录逻辑页码）；页图实印 [309] | 已核验，目录与 PDF 图像分别记录 |

附录 II 的目录条目在 PDF 第 325 页明确给出印刷页码 311。正文起始页 PDF 第 314 页的页顶图像实际印有 `[309]`。本记录保留两个直接观察值，不把 OCR 或推算改写成单一页码。后续引用时应注明采用的是目录逻辑页码 311，还是该页图像上的实印页码 309。

正文末尾：PDF 第 323 页为印刷页 320 的正文末页。PDF 第 324 至 325 页为两页目录，印刷页码 321 至 322。PDF 第 326 页是给装订者的说明页，要求将五张图版置于书末，并附法文说明。页面随后进入图版。

## 图版

已视觉检查 PDF 第 327 至 331 页，确认共有 5 个连续图版页：

| PDF 页 | 图版标题 | 页面可见内容 |
| ---: | --- | --- |
| 327 | Tabula I，页眉标 `pag. 140` | Fig. 1 至 Fig. 10 |
| 328 | Tabula II，页眉标 `pag. 244` | Fig. 11 至 Fig. 21 |
| 329 | Tabula III，页眉标 `pag. 262`，并见 `Additamentum` | Fig. 1 至 Fig. 8 |
| 330 | Tabula IV，并见 `Additamentum` | Fig. 9 至 Fig. 15 |
| 331 | Tabula V，并见 `Additamentum` | Fig. 16 至 Fig. 28 |

Fig. 1 位于 PDF 第 327 页，即第一张图版 Tabula I 的左上区域。附录图版的编号重新从 Fig. 1 开始，因此全书存在正文图版编号与 Additamentum 图版编号的重复，这是版面原貌所见现象。

## 已验证与未验证

已验证：PDF 总页数；第 1 至第 4 页的前置页序；正文八个部分的起始页；PDF 第 323 至 326 页的正文末尾、目录与装订说明顺序；末尾五张图版；Fig. 1 的 PDF 页号。

未验证：逐页视觉检查全 331 页；所有正文页的 OCR 字符准确性；原始出版物是否另有未收入本 PDF 的序言、献词、勘误或不同图版装订方案；目录逻辑页码 311 与正文起始页图像实印 309 不一致的原因。
