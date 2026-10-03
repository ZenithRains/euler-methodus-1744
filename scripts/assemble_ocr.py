#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
"""Collect immutable OCR records and page QA metadata. Confidence is not accuracy."""
from pathlib import Path
import csv,json,hashlib,subprocess
root=Path(__file__).resolve().parents[1]
source=root/'Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf'
rows=[];parts=[]
for n in range(2,332):
 stem=f'page-{n:03d}'
 path=root/'ocr/raw'/f'{stem}.txt'
 text=path.read_text()
 with (root/'ocr/raw'/f'{stem}.tsv').open() as f:
  words=[r for r in csv.DictReader(f,delimiter='\t') if r.get('text','').strip() and float(r['conf'])>=0]
 conf=[float(w['conf']) for w in words]
 kind=('title' if n==2 else 'blank' if n==3 else 'body' if n<=323 else 'index' if n<=325 else 'binding_notice' if n==326 else 'plate')
 rows.append({'pdf_page':n,'sequence_page':n-3 if 4<=n<=325 else '', 'printed_page_observed':309 if n==314 else '', 'page_note':'Printed 309; sequence position 311; see editorial inventory' if n==314 else 'Page label not individually verified', 'kind':kind,'ocr_words':len(conf),'mean_engine_confidence':round(sum(conf)/len(conf),2) if conf else '', 'low_confidence_words':sum(x<60 for x in conf),'status':'raw_unverified','sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 parts.append(f'\n\n===== PDF PAGE {n:03d}; RAW UNVERIFIED OCR =====\n\n{text}')
(root/'ocr/full-raw.txt').write_text('EULER E65: UNCORRECTED LATIN OCR\nMathematical expressions are unreliable. Source page numbers are PDF pages.\n'+''.join(parts))
with (root/'ocr/page-manifest.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
metadata={'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_pdf_pages':331,'ocr_pages':len(rows),'excluded_pdf_pages':{'1':'Archive cover, born-digital text'},'engine':subprocess.check_output(['tesseract','--version'],text=True).splitlines()[0],'language':'lat','psm':3,'render_dpi':300,'render':'grayscale PNG using pdftoppm','warning':'Engine confidence does not certify transcription or mathematical accuracy.'}
(root/'sources/source-manifest.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(metadata,indent=2))
