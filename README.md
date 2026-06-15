# AI-Powered-Search
My reading notes following "AI-Powered Search" by Trey Grainger, Doug Turnbull, and Max Irwin

## Chapters

- [Chapter 1: Introducing AI-Powered Search](./chapter-01-introducing-ai-powered-search.md) - Foundation chapter covering what makes search hard, the landscape of modern search techniques (keyword, semantic, and learning-based), and a roadmap for building intelligent search systems that continuously improve relevance.

- [Chapter 2: Working with Natural Language](./chapter-02-working-with-natural-language.md) - Core NLP concepts for search including tokenization, stemming, lemmatization, stop words, synonyms, TF-IDF, and an introduction to word vectors and dense representations for turning raw text into searchable signals.

- [Chapter 3: Ranking and Content-Based Relevance](./chapter-03-ranking-content-based-relevance.md) - Classic ranking techniques including BM25, field-weight tuning, query-time vs. index-time boosting, and practical strategies for improving content-based relevance without machine learning.

- [Chapter 4: Crowdsourced Relevance](./chapter-04-crowdsourced-relevance.md) - Using explicit human signals — ratings, votes, editorial judgments — to drive relevance improvements, including how to collect, normalize, and apply crowdsourced feedback into ranking.

- [Chapter 5: Knowledge Graph Learning](./chapter-05-knowledge-graph-learning.md) - Building and leveraging knowledge graphs to encode entity relationships, power graph-based query expansion, and enrich search systems with structured domain knowledge beyond what's in the raw text corpus.

- [Chapter 6: Using Context to Learn Domain-Specific Language](./chapter-06-context-domain-specific-language.md) - Learning the vocabulary and semantics of a specific domain through co-occurrence statistics, word2vec, query-log analysis, and topic modeling to close the vocabulary gap between users and content.

- [Chapter 7: Interpreting Query Intent Through Semantic Search](./chapter-07-query-intent-semantic-search.md) - Mapping queries to user intent using classifiers, named entity recognition, and embedding-based matching, going beyond keyword lookup to understand what the user actually wants.

- [Chapter 8: Signals-Boosting Models](./chapter-08-signals-boosting-models.md) - Collecting and exploiting behavioral signals (clicks, purchases, dwell time) to build boosting models that reflect real-world user preferences and feed back into ranking in an automated, scalable way.

- [Chapter 9: Personalized Search](./chapter-09-personalized-search.md) - Tailoring results to individual users using their history, preferences, and session context, covering collaborative filtering, user embeddings, and the engineering trade-offs of personalization pipelines at scale.

- [Chapter 10: Learning to Rank for Generalizable Search Relevance](./chapter-10-learning-to-rank.md) - Applying machine learning to ranking with pointwise, pairwise, and listwise approaches, covering feature engineering, model evaluation metrics (NDCG, MRR), and building models that generalize across diverse query types.

- [Chapter 11: Automating Learning to Rank with Click Models](./chapter-11-automating-learning-to-rank.md) - Using implicit user feedback and click models (Position-Based, Cascade) to automatically generate labeled training data for learning-to-rank systems, reducing the dependency on expensive human annotation.

- [Chapter 12: Overcoming Ranking Bias Through Active Learning](./chapter-12-overcoming-ranking-bias.md) - Identifying and correcting position bias, selection bias, and other distortions in click data, and using active learning strategies to produce cleaner, more representative training sets for ranking models.

- [Chapter 13: Semantic Search with Dense Vectors](./chapter-13-semantic-search-dense-vectors.md) - Using Transformer models and LLM embeddings to represent queries and documents as dense vectors, covering approximate nearest-neighbor (ANN) search, scalar and binary quantization, and integrating vector search into production pipelines.

- [Chapter 14: Question Answering with a Fine-Tuned Large Language Model](./chapter-14-question-answering-llm.md) - Building retriever-reader QA pipelines, fine-tuning LLMs on domain-specific data using the SQuAD format, and combining neural question-answering systems with traditional search engines for an end-to-end solution.

- [Chapter 15: Foundation Models and Emerging Search Paradigms](./chapter-15-foundation-models.md) - Looking ahead at how large foundation models, retrieval-augmented generation (RAG), and neural-first architectures are reshaping search, and what the convergence of LLMs with classical IR means for the future of the field.


The book is available for purchase [here](https://www.oreilly.com/library/view/ai-powered-search/9781617296970/).