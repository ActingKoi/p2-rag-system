"""Ablation: dense retrieval with potion-retrieval-32M instead of bge-small-en-v1.5.

See EVAL.md section 5 for the pre-registered hypothesis. Everything else about the
dense retriever (chunking, cosine similarity via unit vectors, ChunkScorer plumbing)
stays identical; only the embedding model changes.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers.dense import Dense

NEEDS_CLAUDE = False


class DensePotion(Dense):
    model = embed.POTION


def build(corpus, cfg):
    return DensePotion(corpus, cfg)
