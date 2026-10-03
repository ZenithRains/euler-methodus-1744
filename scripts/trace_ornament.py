# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
"""Conservative automated vector tracing trial; no invented replacement strokes."""
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np, subprocess
root=Path(__file__).resolve().parents[1]
im=Image.open(root/'sources/e-rara/title-ornament.jpg').convert('L')
a=np.asarray(im,dtype=float);background=np.asarray(im.filter(ImageFilter.GaussianBlur(9)),dtype=float)
mask=Image.fromarray(np.uint8(np.where(a<background-9,0,255))).convert('1')
path=root/'tmp/ornament-mask.pbm';path.parent.mkdir(parents=True,exist_ok=True);mask.save(path)
(root/'output/figures').mkdir(parents=True,exist_ok=True)
subprocess.run(['potrace',str(path),'-s','--turdsize','2','--alphamax','0.8','--opttolerance','0.15','-o',str(root/'output/figures/title-ornament-trace-draft.svg')],check=True)
