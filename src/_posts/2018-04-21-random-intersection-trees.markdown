---
layout: post
title: "Random Intersection Trees"
needmath: true
tags: tech-notes paper-notes
---

### Summary
Main paper can be found [here](http://jmlr.org/papers/v15/shah14a.html).

- Find higher-order interaction between feature variables efficiently
- Input: $$(Y_i, X_i) i \epsilon [1,N]$$
  - $$N$$ = number of points in the dataset
  - $$X_i$$ is a set of integers $$\epsilon [1,p]$$
  - $$p$$ = dataset dimensionality
- Output: a set of interactions which are statistically significant
- One efficient way to build them is to use
  - minwise hashing to estimate the probabilities
  - to use that, precompute a minwise hash matrix apriori
  - prune the tree at the beginning if the $$\theta_0$$ threshold has been
    crossed (for points belonging to class label 1)
