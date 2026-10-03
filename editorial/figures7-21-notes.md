# 图 7 至 21 矢量重绘说明

## 来源与方法

直接依据本项目 E65 扫描件末尾 Tabula I、Tabula II，即 PDF 第 327、328 页。使用现有 3800 像素图版渲染 tmp/pdfs/remainder-source/plate-327.png 与 plate-328.png，逐图局部放大核对。各图手工构造为 TikZ 路径与数学字母，沿用前六图的细黑线及 Garamond 字体。未使用生成式图像修复。

这组文件保留各原图可见的点、连线、曲线、大小写与希腊标签关系。曲线采用手工贝塞尔近似，坐标与比例参照扫描；属于可缩放的示意性忠实重绘，不宣称恢复原版刻线的精确曲率。扫描破损处的断墨统一连接为连续细线，未将断墨误绘为数学虚线。原图中的墨斑、边框、邻图线条未收入。

## 文件与标签核对

- fig07.tex：A、B、C、P、Q、M、m、n、S、s，大小写分别保留。
- fig08.tex：A、B、C、P、M。
- fig09.tex：A、B、C、D、E、M、Q、S，保留两条相交弧与辅助线 SQ。
- fig10.tex：A、P、Q、M。
- fig11.tex：A、P、N、M。
- fig12.tex：A、B、C、D、P、M，保留开放圆弧。
- fig13.tex：A、C、E、F、M、O、P、R，F 点附近原刻线较淡，按可见弧线与斜边连接。
- fig14.tex：两侧重复 D、M，中央 C、P、G、A，重复字母未添加自拟下标。
- fig15.tex：A、Z 与 a、z；I 至 T 的原序列 I、K、L、M、N、O、P、Q、R、S、T；小写对应点以及扰动点 v、omega。v 依正文 nv 采用拉丁 v，omega 采用希腊字母。两条扰动高度略放大以保持辨识度。
- fig16.tex：A、Z、a、z、C、D、E，保留上下两条共端点曲线。
- fig17.tex：A、B、C、P、M。
- fig18.tex：A、B、C、D、E、F、G、H、I、O，以及小写 a、b、c。保留外围三角形、三条曲线、交叉辅助线及小三角形。
- fig19.tex：A、M、P、N、O。
- fig20.tex：A、B、P、a、b、M、m、alpha、beta，大写 M 为曲线上点，小写 m 为水平线点。
- fig21.tex：两侧重复 B、N、D、M；中央 Q、C、P、A。

## 排版检查

独立 wrapper 为 tex/figures7-21-proof.tex，输出 tmp/build/figures7-21-proof.pdf，共 15 页。LuaLaTeX 编译通过，无 Overfull、缺字或错误。全部 15 图的渲染页均逐图检查，随后复查图 7、13、16、18、20 的标签及局部曲线修订。图文件只使用基础 TikZ 命令，不要求额外 TikZ 库。图 15 原宽 12 cm，其他图原宽约 5.3 至 7 cm，适合总版按图组编排。
