# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

The corpus I chose in stage 2 was one on wikipedia pages on movies, shows, or anime because certain keywords could describe many movies, but it rewards remembering the general summary of the media even if the exact words are off. I personally chose media because I enjoy watching shows in my free time and would like to see how good it is finding the right title. I predict that rerank will win because most of the descriptions will be paraphrase heavy and less on exact keywords. Which is why bm25 would do the worst because finding the exact keywords can be difficult and describe many generic movies with the same plots such as zombies or superheros.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

One design choice where I could've gone two ways was the embedding model for dense (bge-small-en-v1.5) vs potion-retrieval-32M. I measured both with dense(bge) scoring MRR@10 = 0.614 and dense portion scoring MRR@10 = 0.687. The difference was 0.073 and crosses zero but its not distinguishable with 30 queries. The difference is not provably better to choose the more expensive model bge but I would have to verify more to use potion which is cheaper/faster.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

A minor suggestion that Claude proposed that I had to overrule was a sequel show being recommended for the query that I had for the original show. This didn't go into qrels.txt but was spotted in the claude conversation. This could cause issues because someone that wanted to be introduced to a show for the first time would get the wrong summary of a continuation and although not a entirely wrong answer it is still wrong. 

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number that I do not trust is the rerank minus bm25 on the own corpus with a MRR@10 difference +0.095 crossing 0. Because while rerank technically beats bm25, the sample size is too small and the difference is not significant enough to prove my prediction in prompt 1 clearly. For me to trust it, I would need to run it over a larger sample size and make my conclusion then. 

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

One thing that is still not right is the findings with dense vs dense_potion because the gold set of 30 queries is too small to tell apart the ~0.2 MRR differences that it can detect (even though the actual gap was 0.073) between the two to make any clear statements. What I would do next would make more judged queries or a paired analysis isolating the paraphrase class only. To find this go to eval/own/queries.tsv and EVAL.md.
