---
layout: post
title: "Demystifying word2vec"
tags: tech-notes machine-learning word2vec
---

Summary of [this](http://www.deeplearningweekly.com/blog/demystifying-word2vec)
introductory blog post on word2vec.

- Latent Semantic Analysis
  - construct a matrix of wordOccurences-by-document
  - convert the frequency into tf-idf notation
    - term-frequency-inverse-document-frequency
    - this helps normalize the frequency values and prevent the stop words (a, an, the)
      in dominating the matrix
  - take SVD of this matrix and descending-order sort the singular values
  - the corresponding col-vectors in U matrix will represent the words grouped closer
    according to the frequency of their occurence (or topic)
  - this approach cannot predict subtle relationship with words
  - certainly cannot understand the relationship across sequence of words
- Word2vec
  - converts the words to vectors such that the words neighboring in context to the
    current word all appear close in the vector-domain (according to a certain norm)
  - skip-gram
    - predict a word given its surrounding context
    - pick a context of +/- 'c' words wrt a given word
    - maximize the log-probability of vector dot products (usually softmax is used)
    - this typically maintains distance between groups of words with similar meanings
      - eg: man->woman, king->queen, gentleman->lady, etc
    - this can also help predict similar words for a given word
  - continuous bag of words
    - given a word predict its surrounding context
