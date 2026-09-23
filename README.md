# Content Portfolio Audit Tools

Dependency-free QA for page portfolios: one primary task per URL, explicit information gain, parent/hub ownership, and duplicate-intent detection.

## Quick start

Additional deterministic portfolio checks:
- `tools/audit_internal_links.py` — graph edges, zero-incoming nodes and anchor-pattern diagnostics.
- `tools/audit_lexical_novelty.py` — Unicode-aware lexical novelty/Jaccard comparison.
- `tools/audit_content_overlap.py` — pairwise lexical-overlap candidates; diagnostic only, not a ranking claim.
```bash
python3 tools/audit_portfolio.py examples/pages.csv
python3 -m unittest discover -s tests -v
```

The tool validates editorial architecture; it does not predict rankings, AI citations, or traffic.

Research basis:
- https://niculae.info/blog/information-gain-seo/
- https://niculae.info/blog/google-ai-mode-query-fan-out/
- https://niculae.info/blog/ai-citation-coverage/
- https://github.com/RazvanGabrielNiculae/ai-search-frameworks
