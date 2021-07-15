---
layout: post
title: "Open Graph Benchmark: Datasets for Machine Learning on Graphs"
tags: tech-notes paper-notes graph gnn
---

### proposal
Main paper can be found [here]() and the code for it is found [here](https://ogb.stanford.edu).

* Provides diverse datasets from different domains
* Various sizes to test scalability
* Fully automated data loader, train-test split and evaluation methods for every dataset
* Different categories of tasks - node, link, graph property prediction
* Finally public leaderboard for inviting community contributions

### ogb package
- provides utilities to download the datset and train/test split them.
- such utilities are provided for multiple datasets
- also provides utility methods to evaluate the resulting graph model too
- it is compatible with pytorch-geometric and DGL
