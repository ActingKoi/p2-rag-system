"""Your hybrid retriever (stage 1): fuse the rankings of two systems into one.

This file is yours to write. Until you write it, build() raises NotImplementedError, and p2 skips
the system and lists it as to do.

Where the idea is:
- the 13 lab's pipeline.py in the course repo (class/13-rag-pipeline/lab/starter/pipeline.py):
  rrf() is reciprocal rank fusion with k = 60, where each document scores the sum of 1 / (60 + rank)
  over the rankings it appears in, and command_fuse() fuses bm25 with an embedder;
- get the two systems you fuse with p2.retrievers.build("bm25", corpus, cfg) and
  build("dense", corpus, cfg), so each index is built once per run;
- fuse full rankings, not top-10 lists (ask each system for len(corpus.docs) documents), because a
  document that is 11th in both lists can belong in the fused top 10;
- order the fused documents with p2.runfile.order(), so equal scores fall in document id order.

If you want `p2 answer` to work with hybrid, also give it search_chunks(text, k): the same fusion over chunk rankings.
"""

from __future__ import annotations

import p2.retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

RRF_K = 60


def _rrf(rankings: list[list[str]], k: int = RRF_K) -> list[tuple[str, float]]:
    """Fuse full rankings (best first, ids) by reciprocal rank: each id scores sum(1 / (k + rank))."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item_id in enumerate(ranking, 1):
            scores[item_id] = scores.get(item_id, 0.0) + 1 / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.bm25 = p2.retrievers.build("bm25", corpus, cfg)
        self.dense = p2.retrievers.build("dense", corpus, cfg)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        n = len(self.corpus.docs)
        bm25_ids = [docid for docid, _ in self.bm25.search(text, n)]
        dense_ids = [docid for docid, _ in self.dense.search(text, n)]
        return _rrf([bm25_ids, dense_ids])[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        n = len(self.bm25.chunks)
        bm25_ids = [chunk_id for chunk_id, _ in self.bm25.search_chunks(text, n)]
        dense_ids = [chunk_id for chunk_id, _ in self.dense.search_chunks(text, n)]
        return _rrf([bm25_ids, dense_ids])[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
