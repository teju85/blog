---
layout: post
title: "Graph Convolutional Networks"
needmath: true
tags: tech-notes graph gnn
---

### Graph Convolutional Networks
Summary of the content of the blog found [here](https://tkipf.github.io/graph-convolutional-networks).

### Summary
- Inputs:
  - N = number of nodes
  - D = dimensionality of input feature vector for each node
  - A = adjacency matrix
  - L = number of layers
  - $$L_i$$ = output features at each layer
  - $$f_i$$ = output activation at each layer
  - X = feature matrix [dim = N x D]
  - F = output feature vector dimension
- Weights
  - $$W_i$$ = weight matrix at each layer [dim = $$L_{i-1}$$ x $$L_i$$], with $$L_0$$ = D
- Outputs:
  - Z = transformed feature vector for each node [dim = N x F]
- L layers means that this network does "convolution" with neighbor nodes upto L hops from a given node
- A' = A + I, in order introduce self-loops
- D = diagonal matrix of node degrees (very useful in normalizing the adjacency matrix)
- each layer's operation = $$f_i(D^{-0.5} A' D^{-0.5} X_i W_i)$$
- author's show forward prop on this network is generalized, differentiable version of Weisfeiler-Lehman algo!
- code is on [github](https://github.com/tkipf/gcn). Uses TF
