import argparse,csv,json,re,itertools
def tok(s): return set(re.findall(r"\w+",(s or '').casefold(),flags=re.UNICODE))
def audit(path,threshold=.6):
 if not 0 <= threshold <= 1: raise ValueError('threshold must be between 0 and 1')
 with open(path,newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
 out=[]
 for a,b in itertools.combinations(rows,2):
  x=tok(a.get('text','')); y=tok(b.get('text','')); union=x|y; score=(len(x&y)/len(union)) if union else 0.0
  if score>=threshold: out.append({'a':a.get('url'),'b':b.get('url'),'jaccard':round(score,4)})
 return {'pages':len(rows),'potential_overlap_pairs':out}
def main():
 p=argparse.ArgumentParser();p.add_argument('csv');p.add_argument('--threshold',type=float,default=.6);a=p.parse_args();print(json.dumps(audit(a.csv,a.threshold),indent=2,ensure_ascii=False))
if __name__=='__main__':main()
