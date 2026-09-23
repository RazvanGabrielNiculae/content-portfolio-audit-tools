import json,subprocess,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class Expansion(unittest.TestCase):
 def runj(self,*args):
  r=subprocess.run([sys.executable,*map(str,args)],cwd=R,capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr);return json.loads(r.stdout)
 def test_internal_link_graph(self): self.assertEqual(self.runj(R/'tools/audit_internal_links.py',R/'examples/internal-links.csv')['edges'],3)
 def test_overlap(self): self.assertEqual(len(self.runj(R/'tools/audit_content_overlap.py',R/'examples/content-text.csv')['potential_overlap_pairs']),1)
 def test_unicode_novelty(self):
  x=self.runj(R/'tools/audit_lexical_novelty.py',R/'examples/novelty-base.txt',R/'examples/novelty-candidate.txt');self.assertGreater(x['novel_term_ratio'],0)
if __name__=='__main__':unittest.main()
