import argparse,json,re
from pathlib import Path
def tok(s): return set(re.findall(r"\w+",s.casefold(),flags=re.UNICODE))
def audit(base,candidate):
 a=tok(Path(base).read_text(encoding='utf-8')); b=tok(Path(candidate).read_text(encoding='utf-8')); new=b-a; union=a|b
 return {"base_terms":len(a),"candidate_terms":len(b),"novel_terms":sorted(new),"novel_term_ratio":round(len(new)/max(1,len(b)),4),"jaccard":round(len(a&b)/max(1,len(union)),4)}
def main():
 p=argparse.ArgumentParser();p.add_argument('base');p.add_argument('candidate');x=p.parse_args();print(json.dumps(audit(x.base,x.candidate),indent=2,ensure_ascii=False))
if __name__=='__main__':main()
