---
layout: post
title: "word2vec analysis"
tags: tech-notes machine-learning word2vec
---

Summary of [this](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
and [this](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)
tutorials on word2vec, as well as comments on the original C-implementation of
the word2vec model

### Summary
- learning task
  - input is a one-hot vector of the vocabulary
  - hidden layer dimension = 300 (based on google's popular word2vec on 1B dataset)
  - output is softmax with same dimension as input
    - predicts the input word's neighboring words
- after learning, just keep the weights leading to hidden layer!
- but training this would be computationally expensive
- it will also overfit on small datasets
- hence, the paper suggests
  - treating common word-pairs as single words
  - subsampling frequently occuring words during training
  - negative sampling to only update a few percentage of the weights during backprop
- subsampling is done based on the word frequency
- NS is also done based on the word frequency

### code annotations
#### word2phrase.c
- [code](https://github.com/chrisjmccormick/word2vec_commented/blob/master/word2phrase.c)
- params
  - threshold - ratio above which to consider phrasing 2 words
  - min_count - discard words appearing less than this number of times
- has a custom hash function to efficiently look up vocabulary
- if the vocab size >= 70% of hash table, prune out the vocab to reduce hash collisions
- finally writes out the "grouped" version of the input dataset

#### word2vec.c
- [code](https://github.com/chrisjmccormick/word2vec_commented/blob/master/word2vec.c)
- most of the basic primitives are shared with word2phrase.c
- main guy is TrainModelThread, which gets called by multiple posix threads from TrainModel
- learning rate will decay after every certain iterations
- subsampling of frequent words done through an empirical equation
  - we could potentially compute and cache it before the start of training loop
- for hierarchical softmax, it creates some sort of a binary tree?
