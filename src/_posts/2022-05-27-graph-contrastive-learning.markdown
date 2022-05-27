---
layout: post
title: "Graph Contrastive Learning with Augmentations"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/2010.13902.pdf).

* propose a graph contrastive learning (GraphCL) framework for learning
  unsupervised representations of graph data
* to incorporate priors they propose using various augmentation schemes
* this approach additionally helps boosting robustness against adversarial
  attacks

### Summary
- All the code is open-sourced [here](https://github.com/Shen-Lab/GraphCL).
- Authors stress the importance of pre-training methods for GNNs too

#### augmentation
- mostly focuses on graph-level augmentations
- augmentation methods
  - node dropping - randomly discard certain nodes and their connections
  - edge perturbation - randomly adding/dropping certain ratio of edges
  - attribute masking - randomly mask certain attributes of the vertices
  - subgraph - by doing random walk on the original graph
- default augmentation ratio is 0.2

#### graph contrastive learning
- Flowchart
  - take the input graph
  - perform augmentations as described above to generate different graphs
  - pass these graphs through a GNN model to generate graph level embedding
  - pass this embedding further through a projection head (in this case the
    authors used 2-layer MLP)
  - apply a contrastive loss function (eg: normalized temperature-scaled cross
    entropy loss) to maximize similarity between positive pairs and minimize
    similarity between negative pairs
- $$sim(z_i, z_j) = \frac{z_i^T . z_j}{||z_i|| ||z_j||}$$
  - $$z_*$$ = output of projection head for a given graph
  - $$i, j$$ = augmented graph pairs
- $$l_n = -log\frac{exp(sim(z_{n,i}, z_{n,j}) / \tau)}{\Sigma_{n' != n}exp(sim(z_{n',i}, z_{n',j}) / \tau)}$$
  - $$l_n$$ = loss for the $$n$$th graph
  - $$n \epsilon [0, N)$$
  - $$N$$ = number of graphs
  - $$\tau$$ = temperature parameter
