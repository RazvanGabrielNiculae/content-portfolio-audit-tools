import argparse,csv,json
from collections import Counter,defaultdict
def audit(path):
 ins=Counter(); outs=Counter(); nodes=set(); anchors=defaultdict(Counter); broken=[]
 with open(path,newline='',encoding='utf-8') as f:
  for i,r in enumerate(csv.DictReader(f),2):
   s=(r.get("source") or "").strip(); t=(r.get("target") or "").strip(); a=(r.get("anchor") or "").strip()
   if not s or not t: broken.append({'row':i,'source':s,'target':t}); continue
   nodes|={s,t}; outs[s]+=1; ins[t]+=1
   if a: anchors[t][a]+=1
 zero_incoming=sorted(n for n in nodes if ins[n]==0)
 repetitive={n:c.most_common(1)[0] for n,c in anchors.items() if sum(c.values())>=3 and c.most_common(1)[0][1]/sum(c.values())>=.8}
 return {"nodes":len(nodes),"edges":sum(outs.values()),"zero_incoming_nodes":zero_incoming,"malformed_edges":broken,"repetitive_anchor_targets":repetitive}
def main():
 p=argparse.ArgumentParser();p.add_argument('csv');a=p.parse_args();print(json.dumps(audit(a.csv),indent=2,sort_keys=True,ensure_ascii=False))
if __name__=='__main__':main()
