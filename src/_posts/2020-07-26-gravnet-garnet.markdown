---
layout: post
title: "Learning representations of irregular particle-detector geometry with distance-weighted graph networks"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/1902.07987.pdf).

* Usage of GNN's for irregular-geometry detectors for particle reconstruction
* propose 2 new distance-weighted GNN layers: GRAVNET, GARNET
* open-source their work based on TF [here](https://github.com/jkiesele/caloGraphNN)
* proposed computations assume no structure-dependent info from the input data
  and thus this could be generalizable for other tasks such as tracking, jet
  identification, etc

### gravnet and garnet layers
- input: $$X$$ of dimension $$B . V . F_{in}$$
  - $$B$$ = number of elements in the batch
  - $$V$$ = number of detector hits per element
  - $$F_{in}$$ = input feature dimension per hit
- perform linear transformation with bias
  - dimension of a vector in $$Y$$ is $$S + F_{lr}$$
  - $$S$$ = learned spatial representation of input vector
  - $$F_{lr}$$ = learned attributes for the nodes in the resulting graph
- graph construction: (done for each element)
  - gravnet - a kNN graph is constructed for each element in the batch, based on
    the pairwise euclidean distances between all hits in that element.
  - garnet - each of the $$S$$ values is considered as a distance from that hit
    to an aggregator
  - the distance between jth vertex and kth vertex in such a graph is called as
    $$d_{jk}$$
- gravent and garnet layer computations
  - scale the features based on a potential function $$V_p$$
    - $$f_{jk}^i = f_j^i V_p(d_{jk})$$
    - gravnet: $$V_p(x) = e^{-x^2}$$
    - garnet: $$V_p(x) = e^{-abs(x)}$$
  - aggregation of scaled features
    - $$f_k^i = agg_j(f_{jk}^i)$$
    - tried both max and mean
    - aggregation function which was most effective for their use-case was mean
  - transformation: (output dimension = $$F_{out}$$
    - in case of garnet, each of these $$f_k^i$$ aggregator features will again
      be weighted using similar equation in order to project them back to the
      original vertices.
    - concatenate the input $$F_{in}$$ features with this $$f_k^i$$ feature
    - perform linear transformation with bias, followed by tanh activation
- a custom loss function is defined based on the domain knowledge

### models
- both a local and global exchange of message across sensors is proposed
- gravnet model
  - has 4 blocks
    - concat mean of vertex features and vertex features
    - 3 dense layers with tanh activation (dim = 64)
    - one gravnet layer
    - final dense layer with dim = 128 and relu activation
  - gravnet layer
    - 'k' value for kNN-graph is set to 40
    - S = 4
    - $$F_{lr}$$ = 22
    - $$F_{out}$$ = 48
  - output of each block before the final dense layer is concatenated and then
    passed to the final dense layer
- garnet model
  - has 4 blocks
    - concat mean of vertex features and vertex features
    - one dense layer with tanh activation (dim = 32)
    - 11 garnet layers!
    - final dense layer with dim = 48 and relu activation
  - garnet layer
    - S = 4
    - $$F_{lr}$$ = 20
    - $$F_{out}$$ = 32
  - output of each block before the final dense layer is concatenated and then
    passed to the final dense layer
- batch norm is applied to the input and output of all blocks
- for all these models, at the end, the following 2 layers are applied
  - a dense layer with dim = 3 and relu activation
  - another dense layer with dim = 2 and softmax activation
- trained using Adam optimizer
