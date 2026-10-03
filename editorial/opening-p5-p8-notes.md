# opening p5 至 p8 校核说明

本段依据 `tmp/pdfs/source-008.png` 至 `source-011.png` 逐图查看，并与 `ocr/raw/page-008.txt` 至 `page-011.txt` 对读。范围从原印刷页 5 顶部第 9 节续文开始，至原印刷页 8 第 15 节末句 `absolvendæ`，`Hypothesis I` 及第 16 节未收入。

TeX 保留原节号和拉丁文段落层级，去除行末断词、页眉、页码、校样装饰和页底接排提示。长 s 按现有样张规范归一为普通 s，æ、œ 和数学拉丁语拼写保留。OCR 中明显的长 s、连字和字形误识已依据扫描图复核。第 15 节末词按扫描确认为 `absolvendæ`，并在 TeX 中写作 `absolvendæ`。

这是一份逐图校录稿，尚未完成第二位校读者复核，也未声称形成批校本。原页 5 至 8 的页码通过 `\sourcepage{5}`、`\sourcepage{6}`、`\sourcepage{7}`、`\sourcepage{8}` 标记；第 15 节跨越原页 7 至 8，文件末尾对应原页 8 的续行。
