---
layout: post
title: "Distilling NNs into soft decision trees"
needmath: true
tags: tech-notes paper-notes
---

### Summary
Main paper can be found [here](https://arxiv.org/abs/1711.09784).

- helps explain the outputs of a neural net
- hierarchical features, as seen in DNN's, are very difficult to explain
- but hierarchical decisions are easy to explain!
- hence this paper proposes to distill a DNN into a soft decision tree (SDT)
- each internal node in a SDT is a sigmoid logistic regression
  - represents probabliity of taking right child
- leaf nodes perform softmax classification
- this is trained using SGD end-to-end
- training data is obtained by running trained DNNs!
  - hence no dearth of labelled data
  - they found this to be better than directly training using the raw samples
- loss function is a cross-entropy weighted with path probability across all leaves
- for regularization
  - depth-wise decaying penalty
  - have inner nodes try to use both branches equally
  - moving window average of probabilities in each node

Update:
- there seems to be a [github repo](https://github.com/kimhc6028/soft-decision-tree)
  on this one using pytorch!
