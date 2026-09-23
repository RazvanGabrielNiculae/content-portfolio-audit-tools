import csv,importlib.util,pathlib,tempfile,unittest
P=pathlib.Path(__file__).parents[1]/'tools'/'audit_portfolio.py'; s=importlib.util.spec_from_file_location('m',P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
class T(unittest.TestCase):
 def f(self,rows):
  q=tempfile.NamedTemporaryFile('w',delete=False,newline=''); w=csv.DictWriter(q,fieldnames=['url','primary_task','information_gain','parent_url']); w.writeheader(); w.writerows(rows); q.close(); return q.name
 def test_valid(self): self.assertEqual(m.audit(self.f([{'url':'/a','primary_task':'A','information_gain':'x','parent_url':''},{'url':'/b','primary_task':'B','information_gain':'y','parent_url':'/a'}])),[])
 def test_duplicate_intent(self): self.assertTrue(any('duplicate' in x for x in m.audit(self.f([{'url':'/a','primary_task':'A','information_gain':'x','parent_url':''},{'url':'/b','primary_task':'A','information_gain':'y','parent_url':'/a'}]))))
 def test_missing_parent(self): self.assertTrue(any('parent_url' in x for x in m.audit(self.f([{'url':'/a','primary_task':'A','information_gain':'x','parent_url':'/missing'}]))))
if __name__=='__main__': unittest.main()
