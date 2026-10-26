"""Your reranker (stage 1): ask Claude to reorder a first-stage system's top 20.

This file is yours to write. Until you write it, build() raises NotImplementedError, and p2 skips
the system and lists it as to do. NEEDS_CLAUDE = True tells p2 that searching calls claude -p, so
CI never regenerates this system's runs; you produce them on your machine and commit them.

Where the idea is:
- the 13 lab's pipeline.py in the course repo (class/13-rag-pipeline/lab/starter/pipeline.py):
  rerank_one() shows the top 20 as numbered passages, RERANK_SCHEMA forces the reply into
  {"order": [20 numbers]}, a reply that is not each number once keeps the original order, and the
  documents below the 20 keep their order underneath;
- when you port RERANK_SCHEMA, also give its items "minimum": 1 and "maximum": 20 (the number of
  passages), so Claude cannot answer with a number that names no passage: the lab's schema only
  fixes how many numbers come back, and a reply such as [12, 2, 60, ...] silently keeps the first-stage order;
- make every call through p2.claude.call(prompt, schema, model=cfg.model,
  cache_dir=p2.claude.cache_folder(cfg)), which launches claude -p the way the lab does, caches
  replies, and records the tokens in the run's trace (traces/, which you commit with the run file:
  p2 check reads it, because CI never calls Claude to run this system again);
- get the first stage with p2.retrievers.build("hybrid", corpus, cfg).

`p2 answer --system rerank` also needs search_chunks(text, k): the same reranking over the first
stage's top 20 chunks (hybrid's search_chunks gives them).

A reranker over 20 candidates is one call per query: 20 calls for the practice queries, 40 for the
test queries. Try two queries first, and look at what Claude sees, before the full run.
"""

from __future__ import annotations

import p2.claude
import p2.retrievers

NEEDS_CLAUDE = True

CANDIDATES = 20
PASSAGE_CHARS = 600

RERANK_SCHEMA = {
    "type": "object",
    "properties": {
        "order": {
            "type": "array",
            "items": {"type": "integer", "minimum": 1, "maximum": CANDIDATES},
            "minItems": CANDIDATES,
            "maxItems": CANDIDATES,
        }
    },
    "required": ["order"],
}

RERANK_PROMPT = """Below are {n} passages, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.first_stage = p2.retrievers.build("hybrid", corpus, cfg)
        self.cache_dir = p2.claude.cache_folder(cfg)

    def _rerank(self, text: str, candidates: list[str], texts: dict[str, str]) -> list[str]:
        n = len(candidates)
        passages = "\n\n".join(f"[{i}] {texts[item_id][:PASSAGE_CHARS]}" for i, item_id in enumerate(candidates, 1))
        prompt = RERANK_PROMPT.format(n=n, query=text, passages=passages)
        reply = p2.claude.call(prompt, RERANK_SCHEMA, model=self.cfg.model, cache_dir=self.cache_dir)
        order_nums = (reply.output or {}).get("order") if reply.output else None
        if reply.error or not isinstance(order_nums, list) or sorted(order_nums) != list(range(1, n + 1)):
            return candidates
        return [candidates[i - 1] for i in order_nums]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        first = self.first_stage.search(text, max(k, CANDIDATES))
        ids = [docid for docid, _ in first]
        candidates, rest = ids[:CANDIDATES], ids[CANDIDATES:]
        texts = {docid: self.corpus.docs[docid].text for docid in candidates}
        new_order = self._rerank(text, candidates, texts) + rest
        return [(docid, float(len(new_order) - i)) for i, docid in enumerate(new_order)][:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        first = self.first_stage.search_chunks(text, max(k, CANDIDATES))
        ids = [chunk_id for chunk_id, _ in first]
        candidates, rest = ids[:CANDIDATES], ids[CANDIDATES:]
        chunk_by_id = {c.id: c for c in self.corpus.chunks(self.cfg.chunk_words, self.cfg.chunk_overlap)}
        texts = {chunk_id: chunk_by_id[chunk_id].text for chunk_id in candidates}
        new_order = self._rerank(text, candidates, texts) + rest
        return [(chunk_id, float(len(new_order) - i)) for i, chunk_id in enumerate(new_order)][:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
