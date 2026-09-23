#!/usr/bin/env python3
import argparse,csv
from pathlib import Path
REQ=('url','primary_task','information_gain','parent_url')
def audit(path):
 with Path(path).open(encoding='utf-8',newline='') as fh:
  rows=list(csv.DictReader(fh))
 errors=[]
 if not rows: return ['empty portfolio']
 missing=[x for x in REQ if x not in (rows[0].keys() if rows else ())]
 if missing:return ['missing columns: '+','.join(missing)]
 tasks={}; urls={r['url'].strip() for r in rows}
 for i,r in enumerate(rows,2):
  u=r['url'].strip(); t=r['primary_task'].strip().casefold(); g=r['information_gain'].strip(); p=r['parent_url'].strip()
  if not u or not t or not g: errors.append(f'row {i}: required value missing')
  if t: tasks.setdefault(t,[]).append(u)
  if p and p not in urls: errors.append(f'row {i}: parent_url not in portfolio: {p}')
 for t,us in tasks.items():
  if len(us)>1: errors.append('duplicate primary_task: '+t+' -> '+', '.join(us))
 return errors
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('csv'); ns=ap.parse_args(); e=audit(ns.csv)
 print(f'errors={len(e)}'); [print('ERROR',x) for x in e]; return 1 if e else 0
if __name__=='__main__': raise SystemExit(main())
