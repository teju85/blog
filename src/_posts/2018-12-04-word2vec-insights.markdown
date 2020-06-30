---
layout: post
title: "Insights on word2vec"
tags: tech-notes machine-learning word2vec
---

Summary of [this](http://mghassem.mit.edu/insights-word2vec/) blog post on word2vec.

- SGNS form of word2vec is the best performing method
- word2vec can be seen as a matrix factorization of PMI matrix
  - Pointwise Mutual Information
  - it basically performs a weighted factorization, so might as well be better than SVD
- CBOW good when having less data, SGNS good when having more data
  - CBOW smooths the learning function to regularize
  - but data is the ultimate regularizer!
