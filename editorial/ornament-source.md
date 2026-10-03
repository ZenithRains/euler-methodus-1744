# 扉页图饰来源与描摹试稿

2026-09-17，从 ETH-Bibliothek Zürich 的 e-rara 馆藏取得1744年同书扉页。馆藏号 Rar 4999，永久标识 https://doi.org/10.3931/e-rara-1490 。馆藏许可标记为 Public Domain Mark。

目录：https://www.e-rara.ch/zut/content/titleinfo/433675
IIIF清单：https://www.e-rara.ch/i3f/v20/433675/manifest
扉页图像：https://www.e-rara.ch/i3f/v20/433682/full/full/0/default.jpg
原始尺寸：2583 × 3136 像素。
图饰区域：https://www.e-rara.ch/i3f/v20/433682/535,1700,1230,840/full/0/default.jpg

已目视比较用户底本扉页与此图。中央树木和卷轴、椭圆框、两侧器物、卷草构图一致，可作为同一图饰的更清晰见证。此处的“同一图饰”是图像比较判断，尚未进行原铜版状态的专业鉴定。彩色图像保留了用户底本中大量丢失的细线，上方 SUPRA INVIDIAM 及底部署名亦可辨认。

`sources/e-rara/page-5.jpg`与`title-ornament.jpg`保存馆方原始响应，无生成式补绘。`output/figures/title-ornament-trace-draft.svg`为自动矢量描摹试稿，尚待逐区域审校。通过局部亮度差阈值与Potrace轮廓拟合产生，参数见`scripts/trace_ornament.py`。不增添猜测线条。细线、题字和署名仍可能在二值化中断裂，不能称作完成的忠实复原；正式版本应以彩色原图逐区复核。

首次SVG渲染已检查。试稿保留整体构图和多数排线，但部分淡线细节有损失。目前不自动替换正式样张扉页。

## 第一章入版检查

2026-09-17，主智能体将彩色原图与白底SVG渲染逐区比较，检查上方题字 SUPRA INVIDIAM、底部两组署名、中央卷轴及树木、左右器物和排线。保留原图笔画，不另行重排或补写署名。图像可读作 Delamonce del、Daudet Sculp.，此处仅记录图像读数，未做人物身份考证。部分浅色排线及署名的细笔仍有断裂；说明中明确保留该限制。

用户已认可描摹试稿，现将同一SVG转为`tex/figures/title-ornament.pdf`纳入第一章扉页。上面的“目前不自动替换”描述属于此前试稿阶段。PDF制作说明保留ETH馆藏号、DOI、Public Domain标记和现代描摹说明。
