---
layout: post
title: "Parallelizing word2vec in multi-core and many-core archs"
tags: tech-notes paper-notes machine-learning word2vec
---

Summary of [this](https://arxiv.org/pdf/1611.06172.pdf) paper on
parallelizing word2vec model training on Intel CPUs.

- convert level-1 blas to level-3 by using
  - shared negative samples
  - group multiple input contexts words for a given target word
- for scaling to multi-nodes
  - model update frequency is tied to word frequency
  - reduce starting learning rate as the number of nodes
  - m-weighted sampling updates
