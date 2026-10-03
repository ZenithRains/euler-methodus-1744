#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
"""Resumeable per-page Latin OCR. Raw output is uncorrected, including mathematics."""
from pathlib import Path
import subprocess, concurrent.futures, os, json, hashlib
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf'
def page(n):
    stem=f'page-{n:03d}'
    out=ROOT/'ocr/raw'/stem
    if out.with_suffix('.txt').exists(): return n
    image=ROOT/'ocr/images'/stem
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','300','-gray','-png',str(SOURCE),str(image)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    env=dict(os.environ,OMP_THREAD_LIMIT='1')
    subprocess.run(['tesseract',str(image)+'.png',str(out),'-l','lat','--psm','3','txt','tsv'],check=True,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    image.with_suffix('.png').unlink()
    return n
if __name__=='__main__':
 import argparse
 a=argparse.ArgumentParser();a.add_argument('--start',type=int,default=2);a.add_argument('--end',type=int,default=331);a.add_argument('--workers',type=int,default=4);args=a.parse_args()
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
  for n in pool.map(page,range(args.start,args.end+1)): print(f'completed {n}',flush=True)
