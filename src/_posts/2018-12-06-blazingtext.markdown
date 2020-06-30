---
layout: post
title: "BlazingText"
tags: tech-notes paper-notes machine-learning word2vec
---

Summary of [this](https://dl.acm.org/citation.cfm?doid=3146347.3146354) paper on
BlazingText.

- parallelizing word2vec SGD on GPUs
- typical way of parallelizing SGD is through Hogwild approach
  - ignore conflicts that might arise between read/write of weights
  - since there are not many conflicts, convergence is not usually affected
- they too use Intel's minibatching technique + shared negative samples here
- they implement both the following kernels
  - one CTA per word
    - each thread maps to a vector dimension
    - peak parallel perf
    - but reduced accuracy due to increased probability of conflicts
  - one CTA per sentence
    - each thread maps to a vector dim
    - medium perf
    - due to reduced conflicts, gives better accuracy
    - more sentences worked upon at the same time increases chances of conflicts!
- distributed training
  - use data parallelism only
  - use ncclAllReduce
  - synchronize at the end of each epoch
  - they notice reduced accuracy with more GPUs added (specifically > 4)
