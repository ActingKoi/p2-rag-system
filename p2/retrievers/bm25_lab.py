"""Second ablation: BM25 with the 12 lab's tokenizer instead of the "codes" tokenizer.

See EVAL.md section 8 for the pre-registered hypothesis. Everything else about BM25
(k1, b, chunking) stays identical; only the tokenizer changes.
"""

from __future__ import annotations

from p2.retrievers.bm25 import BM25

NEEDS_CLAUDE = False


class BM25Lab(BM25):
    def __init__(self, corpus, cfg):
        cfg = cfg.replace(tokenizer="lab")
        super().__init__(corpus, cfg)


def build(corpus, cfg):
    return BM25Lab(corpus, cfg)
