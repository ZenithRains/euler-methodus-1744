# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
"""Structural checks complement, but do not replace, scan collation and visual QA."""
from pathlib import Path
from pypdf import PdfReader
import re,json,hashlib,argparse
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,help='Path to the original Euler Archive scan; optional for build-only checks')
parser.add_argument('--require-source',action='store_true',help='Fail if the original scan is unavailable')
args=parser.parse_args()
groups=[('I',66,'opening-p1 opening-p2-p4 opening-p5-p8 formula-specimen ch1-p10-p16 ch1-p17-p23 ch1-p24-p31'),('II',71,'ch2-p31-p56 ch2-p57-p82'),('III',47,'ch3-p83-p105 ch3-p106-p129'),('IV',42,'ch4-p129-p171'),('V',76,'ch5-p171-p227'),('VI',25,'ch6-p227-p244'),('Add. I',97,'add1-p245-p310'),('Add. II',16,'add2-p311-p320')]
report={'chapters':{},'errors':[]}
allpages=set()
for name,expected,files in groups:
 s='\n'.join((root/f'tex/chapters/{f}.tex').read_text() for f in files.split())
 nums=re.findall(r'\\originalsection\{(\d+(?:bis)?)\}',s)
 expected_sequence=[str(i) for i in range(1,expected+1)]
 if name=='Add. I':expected_sequence=[str(i) for i in range(1,91)]+['90bis','91']+[str(i) for i in range(93,98)]
 pages=list(map(int,re.findall(r'\\sourcepage\{(\d+)\}',s)));allpages.update(pages)
 report['chapters'][name]={'expected_sections':expected,'observed_sections':len(nums),'sequence_ok':nums==expected_sequence,'source_markers':pages}
 if nums!=expected_sequence: report['errors'].append(f'{name}: section sequence differs')
report['missing_body_source_markers']=sorted(set(range(1,321))-allpages)
if report['missing_body_source_markers']:report['errors'].append('missing original-page markers')
report['figure_files']=[f'{prefix}{i:02}.tex' for prefix,n in [('fig',21),('addfig',28)] for i in range(1,n+1) if (root/f'tex/figures/{prefix}{i:02}.tex').exists()]
if len(report['figure_files'])!=49:report['errors'].append('49 figure files required')
source=args.source or root/'Methodus inveniendi lineas curvas maximi minimive proprietate gau.pdf'
report['expected_source_sha256']=json.loads((root/'sources/source-manifest.json').read_text())['source_sha256']
if source.exists():
 report['source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
 report['source_status']='verified' if report['source_sha256']==report['expected_source_sha256'] else 'hash_mismatch'
 if report['source_status']=='hash_mismatch':report['errors'].append('original scan hash differs from source manifest')
else:
 report['source_status']='not_provided'
 if args.require_source:report['errors'].append('original scan required but unavailable')
pdf=root/'output/pdf/Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes.pdf'
if pdf.exists():
 r=PdfReader(pdf); report['pdf_pages']=len(r.pages);report['named_destinations']=len(r.named_destinations)
 report['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
 fonts={};images=[]
 def resources(res):
  res=res.get_object()
  for _,ref in res.get('/Font',{}).items():
   f=ref.get_object();name=str(f.get('/BaseFont'))
   desc=f.get('/FontDescriptor')
   if desc is None and '/DescendantFonts' in f:desc=f['/DescendantFonts'][0].get_object().get('/FontDescriptor')
   desc=desc.get_object() if desc else {}
   fonts[name]=any(k in desc for k in ['/FontFile','/FontFile2','/FontFile3'])
  for _,ref in res.get('/XObject',{}).items():
   o=ref.get_object()
   if o.get('/Subtype')=='/Image': images.append(str(ref))
   if '/Resources' in o:resources(o['/Resources'])
 for p in r.pages:resources(p['/Resources'])
 report['fonts_embedded']=fonts;report['raster_image_count']=len(images)
 if not all(fonts.values()):report['errors'].append('unembedded font')
 logpath=root/'tmp/build/e65-complete.log'
 report['build_log_status']='checked' if logpath.exists() else 'not_provided'
 if not logpath.exists():report['errors'].append('build log unavailable; build the book before auditing compilation')
 log=logpath.read_text() if logpath.exists() else ''
 report['layout_warnings']=[l for l in log.splitlines() if any(w in l for w in ['Overfull','Missing character','undefined references','multiply defined','duplicate ignored'])]
 if report['layout_warnings']:report['errors'].append('layout warnings')
 for prefix,n in [('fig',21),('addfig',28),('chi:sec',66),('chii:sec',71),('chiii:sec',47),('chiv:sec',42),('chv:sec',76),('chvi:sec',25),('addi:sec',97),('addii:sec',16)]:
  expected_numbers=list(range(1,n+1))
  if prefix=='addi:sec':expected_numbers=list(range(1,91))+['90bis',91]+list(range(93,98))
  missing=[f'{prefix}:{i}' for i in expected_numbers if f'{prefix}:{i}' not in r.named_destinations]
  if missing:report['errors'].append({'missing_destinations':missing})
else:report['errors'].append('full-book PDF missing; run scripts/build-complete.sh first')
(root/'editorial/complete-qa.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['chapters','figure_files']},indent=2,ensure_ascii=False))
raise SystemExit(1 if report['errors'] else 0)
