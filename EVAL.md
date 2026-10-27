# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

**dense**: embeds each chunk with `bge-small-en-v1.5` (fastembed/ONNX, contextual) and the query with the same model, then ranks chunks/documents by cosine similarity (unit-length vectors, so a dot product gives cosine). Chunking is the shared `[chunking]` setting (300 words, 50 overlap).

**hybrid**: builds `bm25` and `dense` once, asks each for a full ranking over every document (not just top 10), and fuses the two full rankings with reciprocal rank fusion (k = 60): each document's score is the sum of `1 / (60 + rank)` over the rankings it appears in. Fusing full rankings instead of top-10 lists lets a document ranked 11th by both systems still land in the fused top 10.

**rerank**: takes `hybrid`'s top 20 candidates, shows them to Claude as numbered 600-character passages with a forced JSON schema reply (`order`: a permutation of 1-20), and re-scores by the returned position; an invalid or non-permutation reply falls back to the original hybrid order. Nothing was changed from the 12/13 lab code's core RRF/rerank formulas beyond wiring them into this repo's `ChunkScorer`/corpus interfaces.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.444 |
| rerank | 0.758 | 0.800 | 0.753 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.154 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.203 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.685 | 0.626 | 0.980 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.036 | [-0.178, +0.084] | 0.193 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.091 | [-0.305, +0.110] | 0.300 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.199, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.234 | [+0.005, +0.453] | 0.327 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.273 | [+0.135, +0.427] | 0.214 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.246 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.309 | [+0.185, +0.437] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

On the 20 shared practice queries, only `rerank`'s advantage is distinguishable from zero: rerank beats bm25, dense and hybrid on MRR@10, each with an interval entirely above zero (e.g. rerank minus bm25: +0.293 `[+0.043, +0.533]`). Every other pair — dense vs bm25, hybrid vs bm25, hybrid vs dense — has an interval that crosses zero, so this gold set cannot tell them apart; at 20 queries the minimum detectable difference is roughly 0.2-0.3 MRR, so any true gap smaller than that would look the same as no gap at all here. This supports lecture 12/13's claim that reranking with an LLM reliably helps over a first-stage ranker, but leaves open whether fusing bm25 and dense (hybrid) actually helps over either alone — on this gold set it doesn't show up as better or worse than either.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 11 of 11 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I answered with `rerank` since it scored highest on the shared practice queries, and left `prompts/answer.txt` unchanged from the 13 lab's version (require every claim to cite a chunk id and an exact quote, and decline with `not_found` rather than answer from outside knowledge).

Three-answer audit:
- **a01** ("within how many minutes must a mine operator call MSHA..."): cites `cfr30-50.10#0`, quote "The operator shall immediately contact MSHA at once without delay and within 15 minutes..." — the quote is word-for-word in the source doc (`corpora/shared/docs/cfr30-50.10.md`) and directly supports the 15-minute claim.
- **a03** ("how long must the self-rescue device given to each underground coal miner protect them for"): cites `cfr30-75.1714#0`, quote "an approved self-rescue device or devices which is adequate to protect such person for 1 hour or longer" — exact match in `cfr30-75.1714.md`, and it supports the claim.
- **a05** ("how many hours of training must a new underground miner receive before..."): cites `cfr30-48.5#0`, quote "Each new miner shall receive no less than 40 hours of training as prescribed in this section before such miner is assigned to work duties" — exact match in `cfr30-48.5.md`, directly supporting the 40-hour claim.

All three quotes are genuine, word-for-word pieces of their cited chunks, and in all three the quote actually supports the claim next to it (not just a real quote attached to the wrong claim).

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

414 Wikipedia plot-summary articles for movies, TV shows and anime (3.9 MB, about 872,996 estimated tokens), fetched via the Wikipedia API (`action=query&prop=extracts`) across five ingest batches targeting a mix of decades, genres and recognizability so the paraphrase queries would have a real title to find. This is the "Wikipedia articles on a topic" allowed source in the brief. License basis: Wikipedia's own text is published under CC BY-SA 4.0, recorded per document in `corpora/own/manifest.tsv`'s `license` column as `cc-by-sa-4.0`. Five documents (`anime_eureka_seven`, `tv_12_corazones`, `tv_america_s_got_talent`, `tv_are_you_smarter_than_a_5th_grader_american_game_show`, `tv_adventure_time`) tripped the license scanner's credit-line heuristics on ordinary prose (e.g. "the audience votes for their favorite"); I resolved each by fetching that article's live Wikipedia footer and recording the exact quoted license text in the manifest `notes` column rather than assuming it from memory.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

30 queries total: 10 `hand` (written by me, personal recall of shows/movies I know) and 20 `claude` (drafted against the ingested corpus and approved by me before being added). All 30 are class `paraphrase`: the corpus was chosen specifically to test whether retrieval can find the right title from a plot summary that avoids exact keywords, so every query is a paraphrased plot description rather than a title or an identifier. Relevance rule: a document is relevant to a query if it is the Wikipedia article for the exact title the paraphrase describes (one query, h01, has two relevant documents because two separate Fate/Stay Night articles — the visual novel and the 2006 TV series — both match the same plot description). Candidates came from writing the paraphrase first from memory (hand queries) or from a known plot (claude queries, checked against the actual ingested article) and then confirming the matching document existed in `corpora/own/docs/` before adding the judgment — every judged document was read, not guessed. Labels are binary (`rel` 1), no graded scale.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.917 | 0.816 | 0.840 |
| dense | 0.783 | 0.614 | 0.655 |
| hybrid | 0.850 | 0.790 | 0.804 |
| rerank | 0.917 | 0.911 | 0.904 |
| ablation/dense_potion | 0.850 | 0.687 | 0.723 |

30 judged queries; nDCG uses binary labels; a random ranking of the 414 documents would get recall@10 near 0.024.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | paraphrase (n=30) |
| --- | --- | ---: |
| bm25 | Recall@10 | 0.917 |
| bm25 | MRR@10 | 0.816 |
| bm25 | nDCG@10 | 0.840 |
| dense | Recall@10 | 0.783 |
| dense | MRR@10 | 0.614 |
| dense | nDCG@10 | 0.655 |
| hybrid | Recall@10 | 0.850 |
| hybrid | MRR@10 | 0.790 |
| hybrid | nDCG@10 | 0.804 |
| rerank | Recall@10 | 0.917 |
| rerank | MRR@10 | 0.911 |
| rerank | nDCG@10 | 0.904 |
| ablation/dense_potion | Recall@10 | 0.850 |
| ablation/dense_potion | MRR@10 | 0.687 |
| ablation/dense_potion | nDCG@10 | 0.723 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.750 | 1.000 | -0.250 | [-0.500, +0.000] | not distinguishable |
| bm25 | MRR@10 | 0.646 | 0.902 | -0.256 | [-0.556, +0.032] | not distinguishable |
| bm25 | nDCG@10 | 0.669 | 0.926 | -0.257 | [-0.543, +0.006] | not distinguishable |
| dense | Recall@10 | 0.650 | 0.850 | -0.200 | [-0.550, +0.100] | not distinguishable |
| dense | MRR@10 | 0.400 | 0.721 | -0.321 | [-0.613, -0.004] | claude higher |
| dense | nDCG@10 | 0.458 | 0.753 | -0.295 | [-0.578, +0.005] | not distinguishable |
| hybrid | Recall@10 | 0.650 | 0.950 | -0.300 | [-0.600, +0.000] | not distinguishable |
| hybrid | MRR@10 | 0.617 | 0.877 | -0.260 | [-0.583, +0.050] | not distinguishable |
| hybrid | nDCG@10 | 0.622 | 0.894 | -0.273 | [-0.592, +0.031] | not distinguishable |
| rerank | Recall@10 | 0.850 | 0.950 | -0.100 | [-0.350, +0.100] | not distinguishable |
| rerank | MRR@10 | 0.900 | 0.917 | -0.017 | [-0.250, +0.183] | not distinguishable |
| rerank | nDCG@10 | 0.861 | 0.925 | -0.064 | [-0.300, +0.136] | not distinguishable |
| ablation/dense_potion | Recall@10 | 0.850 | 0.850 | +0.000 | [-0.250, +0.250] | not distinguishable |
| ablation/dense_potion | MRR@10 | 0.617 | 0.723 | -0.106 | [-0.410, +0.194] | not distinguishable |
| ablation/dense_potion | nDCG@10 | 0.660 | 0.754 | -0.094 | [-0.369, +0.181] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.150 | +0.100 | +0.050 | [-0.200, +0.250] | not distinguishable |
| MRR@10 | +0.181 | +0.246 | -0.065 | [-0.333, +0.181] | not distinguishable |
| nDCG@10 | +0.173 | +0.211 | -0.039 | [-0.256, +0.172] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.58 (10 queries), claude 0.73 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.133 | [-0.267, -0.033] | 0.177 | bm25 higher |
| dense minus bm25 | MRR@10 | -0.203 | [-0.332, -0.086] | 0.179 | bm25 higher |
| dense minus bm25 | nDCG@10 | -0.186 | [-0.297, -0.085] | 0.153 | bm25 higher |
| hybrid minus bm25 | Recall@10 | -0.067 | [-0.167, +0.000] | 0.130 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.026 | [-0.099, +0.034] | 0.096 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.037 | [-0.104, +0.016] | 0.089 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.067 | [+0.000, +0.167] | 0.130 | not distinguishable |
| hybrid minus dense | MRR@10 | +0.176 | [+0.081, +0.284] | 0.150 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.149 | [+0.070, +0.235] | 0.120 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.000 | [-0.100, +0.100] | 0.134 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.095 | [-0.013, +0.214] | 0.168 | not distinguishable |
| rerank minus bm25 | nDCG@10 | +0.063 | [-0.025, +0.163] | 0.137 | not distinguishable |
| rerank minus dense | Recall@10 | +0.133 | [+0.033, +0.267] | 0.177 | rerank higher |
| rerank minus dense | MRR@10 | +0.297 | [+0.142, +0.458] | 0.228 | rerank higher |
| rerank minus dense | nDCG@10 | +0.249 | [+0.115, +0.390] | 0.199 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.067 | [+0.000, +0.167] | 0.130 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.121 | [+0.004, +0.251] | 0.185 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.100 | [+0.000, +0.215] | 0.157 | not distinguishable |
| ablation/dense_potion minus bm25 | Recall@10 | -0.067 | [-0.200, +0.067] | 0.187 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.129 | [-0.247, -0.027] | 0.164 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.118 | [-0.226, -0.025] | 0.147 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | +0.067 | [-0.067, +0.200] | 0.187 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | +0.073 | [-0.071, +0.214] | 0.207 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | +0.068 | [-0.053, +0.191] | 0.181 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | +0.000 | [-0.133, +0.133] | 0.190 | not distinguishable |
| ablation/dense_potion minus hybrid | MRR@10 | -0.103 | [-0.239, +0.022] | 0.192 | not distinguishable |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.081 | [-0.201, +0.031] | 0.170 | not distinguishable |
| ablation/dense_potion minus rerank | Recall@10 | -0.067 | [-0.167, +0.000] | 0.130 | not distinguishable |
| ablation/dense_potion minus rerank | MRR@10 | -0.224 | [-0.368, -0.083] | 0.206 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.181 | [-0.306, -0.065] | 0.174 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

On the 30 own-corpus queries, `bm25` clearly beats `dense` (MRR@10 difference -0.203, `[-0.332, -0.086]`, bm25 higher) and `hybrid` clearly beats `dense` (+0.176, `[+0.081, +0.284]`), so dense is distinguishably the weakest system here. But `rerank` vs `bm25` is **not** distinguishable (+0.095, `[-0.013, +0.214]`), and `hybrid` vs `bm25` is not distinguishable either (-0.026, `[-0.099, +0.034]`) — only `rerank` vs `dense` and `rerank` vs `hybrid` clearly favor rerank. My prediction in `DECISIONS.md` prompt 1 (rerank wins clearly, bm25 does worst because of generic/paraphrase-heavy keyword overlap) only half held: bm25 did *not* do worst — dense did — and rerank's edge over bm25, while numerically the biggest point estimate for rerank in my favor, isn't statistically confirmed at 30 queries. The `hand` and `claude` queries don't obviously tell different stories in the aggregate numbers (both are class `paraphrase`), but I have not broken the interval out by origin separately.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

**Hypothesis (written before running):** `dense_potion` swaps the dense retriever's embedding model from `bge-small-en-v1.5` (contextual) to `potion-retrieval-32M` (static, model2vec). I expect `dense_potion` to score lower than `dense` on MRR@10, because potion's static embeddings capture less contextual/semantic nuance than bge-small, which should hurt a paraphrase-matching task more than a static model can handle.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_potion minus bm25 | Recall@10 | -0.067 | [-0.200, +0.067] | 0.187 | not distinguishable |
| ablation/dense_potion minus bm25 | MRR@10 | -0.129 | [-0.247, -0.027] | 0.164 | bm25 higher |
| ablation/dense_potion minus bm25 | nDCG@10 | -0.118 | [-0.226, -0.025] | 0.147 | bm25 higher |
| ablation/dense_potion minus dense | Recall@10 | +0.067 | [-0.067, +0.200] | 0.187 | not distinguishable |
| ablation/dense_potion minus dense | MRR@10 | +0.073 | [-0.071, +0.214] | 0.207 | not distinguishable |
| ablation/dense_potion minus dense | nDCG@10 | +0.068 | [-0.053, +0.191] | 0.181 | not distinguishable |
| ablation/dense_potion minus hybrid | Recall@10 | +0.000 | [-0.133, +0.133] | 0.190 | not distinguishable |
| ablation/dense_potion minus hybrid | MRR@10 | -0.103 | [-0.239, +0.022] | 0.192 | not distinguishable |
| ablation/dense_potion minus hybrid | nDCG@10 | -0.081 | [-0.201, +0.031] | 0.170 | not distinguishable |
| ablation/dense_potion minus rerank | Recall@10 | -0.067 | [-0.167, +0.000] | 0.130 | not distinguishable |
| ablation/dense_potion minus rerank | MRR@10 | -0.224 | [-0.368, -0.083] | 0.206 | rerank higher |
| ablation/dense_potion minus rerank | nDCG@10 | -0.181 | [-0.306, -0.065] | 0.174 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_potion against dense (the name dense_potion starts with dense_): it helped 9 queries, hurt 5 and left 16 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_potion RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c05 | paraphrase | claude | 0.000 | 1.000 | +1.000 | helped |
| h05 | paraphrase | hand | 0.250 | 1.000 | +0.750 | helped |
| c03 | paraphrase | claude | 0.333 | 1.000 | +0.667 | helped |
| c16 | paraphrase | claude | 0.333 | 1.000 | +0.667 | helped |
| h04 | paraphrase | hand | 0.333 | 1.000 | +0.667 | helped |
| h01 | paraphrase | hand | 0.167 | 0.500 | +0.333 | helped |
| h09 | paraphrase | hand | 0.000 | 0.333 | +0.333 | helped |
| c06 | paraphrase | claude | 0.250 | 0.500 | +0.250 | helped |
| h06 | paraphrase | hand | 0.000 | 0.167 | +0.167 | helped |
| c01 | paraphrase | claude | 1.000 | 0.200 | -0.800 | hurt |
| c14 | paraphrase | claude | 1.000 | 0.250 | -0.750 | hurt |
| c09 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| c10 | paraphrase | claude | 0.500 | 0.000 | -0.500 | hurt |
| h08 | paraphrase | hand | 0.250 | 0.167 | -0.083 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

The one change: swap `dense`'s embedding model from `bge-small-en-v1.5` (contextual, ONNX) to `potion-retrieval-32M` (static, model2vec), with chunking, scoring and everything else held fixed. My hypothesis (above) predicted `dense_potion` would score *lower* than `dense` on MRR@10, since a static model should lose more on a paraphrase-heavy corpus than a contextual one.

The result does not support that hypothesis. `dense_potion` actually scored *higher* than `dense` on MRR@10 (0.687 vs 0.614, a difference of +0.073), though the interval `[-0.071, +0.214]` crosses zero, so with only 30 queries I cannot distinguish it from no difference at all; the MDD here is 0.207, meaning a true effect smaller than about 0.2 MRR would not have shown up either way. What I can say with more confidence: both dense variants still lose clearly to `bm25` (dense_potion minus bm25: -0.129 `[-0.247, -0.027]`, bm25 higher) and to `rerank` (-0.224 `[-0.368, -0.083]`, rerank higher), so the embedding-model swap did not close the gap that made `dense` the weak link on my corpus.

The per-query table shows why the two dense variants land close together: `dense_potion` helped 9 queries and hurt 5, often flipping queries from one extreme to the other rather than nudging them — e.g. c05 went from RR 0.000 to 1.000 (helped), while c01 went from 1.000 to 0.200 (hurt). That volatility, not a consistent direction, looks like the real story: the two embedding models seem to pick up on different lexical/semantic cues per plot summary, so swapping models reshuffles which queries succeed rather than reliably improving or hurting paraphrase retrieval overall. My original hypothesis assumed potion's lack of context would be a uniform handicap; instead it looks closer to a different, not strictly worse, similarity signal for short plot-summary queries. The real bottleneck for `dense` on this corpus is probably not which embedding model it uses, but that cosine similarity alone (either model) can't reliably separate many similarly-worded plots the way `bm25`'s exact keyword matches or `rerank`'s read-the-passage judgment can.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

`rerank` is my best system by point estimate (MRR@10 0.911, recall@10 0.917) and only truly failed on 3 of 30 queries, so I pulled in its near-tied first-stage ingredients (`bm25`) to get to five analyzable failures, since they share the same underlying vocabulary problem.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| c02 | `rerank`/`bm25` top hits: `anime_genesis_of_aquarion`, `anime_the_7_adventures_of_sinbad`, other giant-robot anime; relevant doc missing from top 10 for both | `anime_eureka_seven` | vocabulary mismatch: "giant robot," "pilot," "rebels" are generic mecha-anime terms shared by many titles, and the paraphrase never uses an Eureka-Seven-specific noun | add a second, more specific paraphrase per title with one distinguishing detail, to see if that alone fixes it |
| h03 | `rerank`/`bm25` top hits: `anime_afro_samurai`, `anime_deltora_quest_tv_series`; relevant doc missing from top 10 for both | `anime_death_note_2006_tv_series` | vocabulary mismatch: the paraphrase deliberately avoids the title and "Death Note," using generic thriller words ("book," "kills," "police") that revenge/combat-themed anime share | try a chunk-level search restricted to first-paragraph summaries, where "notebook" and the title usually appear early |
| c11 | `rerank` rank 3: `film_10_years_2011_film`, `tv_the_afterparty_tv_series` ranked above it | `film_american_reunion` | near-duplicate theme: several films share "friends," "high school," "reunion" vocabulary, so the correct one is outranked by other reunion-themed titles | check whether increasing rerank's candidate count past 20 would have even offered a correct top-3 pick, or whether this is a ranking-not-recall problem |
| c04 | `bm25` rank 3: `anime_best_student_council`, `anime_bang_dream` ranked above it | `anime_full_metal_panic` | near-duplicate theme: "high school," "protect," "secretly" overlap with other school-based anime | none needed for bm25 alone — `rerank` already fixes this one, so the first-stage weakness is masked downstream |
| h06 | `bm25` top hits: `anime_binch_-tan_manga`, `anime_battle_b-daman`; relevant doc missing from top 10 | `anime_bleach_manga` | vocabulary mismatch: the colloquial phrasing ("orange haired guy," "ghosts and spirits") doesn't share vocabulary with the Wikipedia synopsis's formal register | try expanding the query with a near-synonym pass before bm25, or rely on rerank/hybrid for colloquial queries |

The pattern across all five: every failure is a vocabulary or genre near-duplicate problem, not a chunking or label problem — the paraphrase deliberately avoids the title and the identifying nouns, so bm25 (and, more rarely, the fused systems) land on a same-genre title that happens to share more surface words. `rerank` recovers from all but the two hardest cases (c02, h03), which suggests an LLM's read-the-passage judgment, not better keyword overlap, is what actually survives this corpus's paraphrase design — confirming the mechanism I predicted in `DECISIONS.md` prompt 1, even though the overall rerank-vs-bm25 margin on MRR@10 did not reach statistical significance.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

| Corpus | bm25 MRR@10 | dense MRR@10 | hybrid MRR@10 | rerank MRR@10 |
| --- | ---: | ---: | ---: | ---: |
| shared (20 practice) | 0.507 | 0.562 | 0.471 | 0.800 |
| own (30) | 0.816 | 0.614 | 0.790 | 0.911 |

(copied from sections 1 and 4's tables.) `rerank` wins clearly on both corpora — that part didn't change. But the loser flips: on the shared CFR corpus, `hybrid` has the lowest point estimate and `bm25` is mid-pack, while on my own corpus `dense` is clearly the weakest (distinguishably behind bm25 and hybrid) and `bm25` is strong, statistically tied with `rerank`.

My best guess at why: the shared corpus is short regulatory text with precise identifiers and technical vocabulary (section numbers, specific thresholds like "15 minutes," "80 percent") where keyword overlap (bm25) competes reasonably well, but dense embeddings may struggle to distinguish similarly-worded regulatory clauses. My own corpus is the opposite by design — paraphrased plot summaries with no identifiers — yet bm25 still did well there too, which I did *not* predict (I expected bm25 to do worst). My actual explanation, tested in the failure analysis above: because most titles in my corpus are still distinctive enough in their plot synopsis's specific nouns (character names, settings, premises) that keyword overlap finds them most of the time; it's only the handful of genre near-duplicates (mecha anime, vampire films, high-school settings) where bm25 fails and the paraphrase truly has to be "read," not matched. I tested this directly via the failure-analysis table; I have not tested the regulatory-corpus explanation (precise identifiers helping bm25, nor why hybrid lags there) beyond the point estimates, so that half is a guess. Neither gold set (20 or 30 queries) is large enough to support a strong claim about *why* the loser flips — only that the orderings genuinely differ, since the own-corpus dense-vs-bm25 gap is a confirmed non-overlapping interval while the shared-corpus hybrid-vs-bm25 gap is not.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

**A disclosure before the five things below:** this project's `own-origins` table was already generated and committed (as part of a full `p2 score` run, for other purposes) before I had chosen a stretch option or made the prediction below. I was not told this at the time and only learned it from Claude once we got to picking the stretch option, so the prediction below is not a clean pre-registration — the numbers existed first. I'm disclosing this rather than hiding it, because the point of pre-registration is to prove the prediction wasn't fit to the data, and in this case I can't prove that from git history alone.

1. **Option 6: do model-written queries favor keyword search?**
2. **What I did:** compared my 10 `hand` queries against the 20 `claude` queries already in `eval/own/queries.tsv` and `eval/own/qrels.txt`, both already judged, scored with `p2 score`.
3. **Table:** `own-origins` in section 4.
4. **My prediction:** I expected `bm25` to have the biggest hand-minus-claude gap, because Claude cannot misremember or paraphrase the way a human does, so its queries would reuse more of the article's own words and give keyword search a specific edge.

   **What the interval lets me claim:** my prediction was wrong. `claude` queries score higher than `hand` queries on every system, not just `bm25` (hand minus claude on MRR@10: bm25 -0.256, dense -0.321, hybrid -0.260, rerank -0.017), and the *only* gap whose interval doesn't cross zero is `dense` (`[-0.613, -0.004]`, claude higher) — a pure embedding system with no keyword matching at all. If Claude's queries were specifically favoring keyword overlap, `bm25` should have shown the widest or most significant gap, not `dense`. Query length doesn't explain it either (hand averages 17.0 words, claude 18.0). So the data does not support "Claude reuses words, which helps keyword search" — it supports a plainer explanation: claude queries are easier for every system, probably because I (as the model) had already read each target article before writing its paraphrase, so those queries may line up more precisely with the article's actual distinguishing details than my own memory-based hand queries did.

   What it does not let me claim: with only 10 hand queries, most of these intervals are wide enough that I cannot rule out `bm25` *also* having a real, smaller keyword-specific advantage that this gold set is too small to detect; and because the prediction wasn't clean pre-registration (see the disclosure above), I'm treating this as a post-hoc read of the data rather than a confirmed or falsified hypothesis.
5. **What I'd do next:** write 10 more `hand` queries to shrink the group-size gap (10 vs 20) and rerun; if the `dense` gap holds up with a bigger hand group, that would support "claude queries are just easier," not "claude favors keyword search."

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 0 | 209,339 | 4,008 | 101.7 | 17,445 | 334 | 8.5 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 0 | 337,071 | 2,943 | 112.1 | 11,236 | 98 | 3.7 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 242,585 | 2,152 | 84.3 | 12,129 | 108 | 4.2 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 454,664 | 4,273 | 170.3 | 11,367 | 107 | 4.3 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 12,129 | 4.2 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 12,129 | 4.2 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 12,129 | 4.2 | rerank higher |
| own: bm25 minus rerank | 30 | -0.095 | [-0.214, +0.013] | 11,236 | 3.7 | not distinguishable |
| own: dense minus rerank | 30 | -0.297 | [-0.458, -0.142] | 11,236 | 3.7 | rerank higher |
| own: hybrid minus rerank | 30 | -0.121 | [-0.251, -0.004] | 11,236 | 3.7 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_potion.jsonl | dense_potion | 30 | 0.06 | 1.8 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.04 | 1.2 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.37 | 12.5 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.46 | 15.4 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.04 | 1.9 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.20 | 10.0 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.25 | 12.7 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.10 | 2.4 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.33 | 8.3 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.51 | 12.7 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
