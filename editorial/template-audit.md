# E65 拉丁文重排模板审查

审查对象是 `reference/vintage-latex` 的固定提交 `559011918849a3da819912a7c26493071d542df5`。README 说明二十个示例各自独立。纯 LaTeX 示例为 01、02、04 至 06、10 至 14，均使用 LuaLaTeX。示例 03、07 至 09 是独立 MetaPost 文件。示例 15 至 20 还需要 `fiziko`。

## 建议的最小方案

E65 的第一张拉丁文样张建议从示例 01 复制，并吸收示例 04 的 `\incipit` 与 TikZ 装饰。先只保留以下依赖：

```tex
\documentclass[11pt,twoside]{article}
\usepackage{iftex}
\ifLuaTeX\else
  \PackageError{e65}{This document requires LuaLaTeX}{Run lualatex.}
\fi
\usepackage{fontspec}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage[tracking=true,protrusion=false,expansion=false]{microtype}
\usepackage{tikz} % 仅在需要段首花饰或矢量图时保留
\defaultfontfeatures{Renderer=HarfBuzz}
\setmainfont{EB Garamond}[
  Numbers={OldStyle,Proportional},
  Ligatures={TeX,Common,Historic,Rare}
]
```

页面尺寸、内外边距、段首大写、页眉页脚和暖色纸张沿用示例 01。扉页或章节开头再加入示例 04 的 `\incipit` 与普通 TikZ 路径。数学公式先用 E65 原有数学排版方案单独测试，正文样张无需引入 `unicode-math`。需要在图内用同一套数学字体时，再加入 `unicode-math` 和 `\setmathfont{Garamond-Math.otf}`，此时应记录字体文件来源与版本。

可复现编译命令如下：

```sh
mkdir -p build
lualatex -interaction=nonstopmode -halt-on-error \
  -output-directory=build e65-latin-sample.tex
```

编译器应固定为 LuaLaTeX。参考 README 明确指出 pdfLaTeX 不支持这些 OpenType 控制。参考仓库的 `build.sh` 可用于批量检查，首张样张仍建议保留独立源文件和独立输出目录。

## 示例取舍

示例 01 适合正文页，提供 EB Garamond、旧式数字、历史连字、段首大写、边注和印刷线。示例 04 适合扉页及章首，提供框式首字和无外部依赖的矢量花饰。示例 02 适合将来重绘几何图版，图中文字保持可搜索。示例 10 只在需要表格数字对齐或编译期计算时采用。

首个 E65 MWE 不应依赖 `fiziko`。它是单独的 GPL 3.0 依赖，需要额外检出并设置 `MPINPUTS`。只有当某个图版确实需要其 MetaPost 宏时，才将该依赖加入对应图形子工程，并在发布材料中单独列出。

## 授权与署名

参考仓库的源代码、说明文字和生成示例采用 CC BY SA 4.0，许可证文件标注 SPDX 为 `CC-BY-SA-4.0`。改编 E65 模板时，在制作说明或项目许可证页保留以下信息：

```text
排版模板改编自 Foadsf/vintage-latex，固定参考提交
559011918849a3da819912a7c26493071d542df5。
原项目采用 Creative Commons Attribution ShareAlike 4.0 International。
项目链接：https://github.com/Foadsf/vintage-latex
许可证：https://creativecommons.org/licenses/by-sa/4.0/
本项目对页面尺寸、文字内容、字体设置和图形作了修改。
```

若继续分发由该模板形成的模板改编部分，应按 CC BY SA 4.0 说明改动并采用相同协议。Euler 的 1744 年拉丁原文属于公共领域，原文来源和扫描版本仍需另行记录。E65 的现代汉译、校订、译注及编辑工作有独立的授权记录，不能由参考模板许可证自动覆盖。EB Garamond、Garamond Math、TeX Live 宏包和 TikZ 各自遵循其上游许可证，应在发行包的依赖清单中记录名称、版本和许可证。`fiziko` 若使用，按其上游 GPL 3.0 条款单独处理。

## 字体依赖清单

必需字体是 EB Garamond，参考 README 建议使用 TeX Live 或 MiKTeX 中的 `ebgaramond`。LuaLaTeX 通过 `fontspec` 读取 OpenType 特性，因此应在构建记录中写明 LuaLaTeX、TeX 发行版、EB Garamond 版本，并检查拉丁扩展字符、长 s、旧式数字和数学符号是否齐全。

Garamond Math 仅在采用 `unicode-math` 的公式或 MetaPost 图内数学标签时需要。中文译本另有中文字体方案，不能把中文字体混入这张拉丁文 MWE 的必需依赖。最终 PDF 应检查字体嵌入、缺字和文本可搜索性。

## 建议的验收点

先编译一页包含标题、段首大写、一个公式、一个 TikZ 图和一条内部引用的样张。确认输出 PDF 为矢量文本，拉丁字符和公式可复制，字体已嵌入，图中文字没有变成位图。固定模板提交与字体版本后，再开始逐章排版。
