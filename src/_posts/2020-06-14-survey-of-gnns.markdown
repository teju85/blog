---
layout: post
title: "A comprehensive survey on Graph Neural Networks"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main survey paper can be found [here](https://arxiv.org/pdf/1901.00596.pdf).
Divides GNNs into the following top-level four categories:
1. recurrent GNNs - iteratively exchange info with neighbors until some form of
   convergence is achieved. This idea is borrowed and improved by convGNNs.
2. convolutional GNNs - same as recGNNs, but here multiple such operations are
   stacked to extract high-level node representations based on neighbors that
   are further away.
3. graph autoencoders - unsupervised methods to represent graphs by latent
   vectors and then use a decoder phase to reconstruct the graph
4. spatio-temporal GNNs - combine convGNNs and then regular 1D-CNNs to capture
   both spatial and temporal info of the nodes, respectively

### Differences wrt regular DL
- data space is non-Euclidean
- graphs can be irregular
- number of neighbors vary, causing difficulty with regular convolutions
- instance (aka node) is not independent of the other

### Differences wrt network embedding
- NE involves other non-DL methods like factorization, random-walks
- GNNs provide and end-to-end solution for some of the graph-related tasks

### recGNNs
Perform message passing between nodes and their neighbors, until some form of
convergence is achieved.
$$h_v^{(t)} = \sum_{u \epsilon N(v)} f(X_v, x_{u,v}^e, x_u, h_u^{(t-1)})$$
* $$h_v$$ = hidden vector which is initialized to random value at time = 0
* $$f(.)$$ = a contraction mapping parametric function to ensure convergence
* $$X$$ = node feature matrix
* $$x$$ = edge feature matrix
* $$N(v)$$ = neighborhood of node $$v$$
* n = number of nodes
* m = number of edges

Gated GNNs - use GRU with fixed number of recurrence steps, instead of a
generic contraction mapping function. Then uses BPTT (backprop through time)
in order to learn parameters.
$$h_v^{(t)} = GRU(h_v^{(t-1)}, \sum_{u \epsilon N(v)} W h_u^{(t-1)}$$
* $$h_v^{(0)} = x_v$$

### convGNNs

#### spectral based
Based on graph signal processing and use normalized graph laplacian
$$L = I - D^{-0.5} A D^{-0.5}$$
* $$D$$ = diagonal matrix with $$D_{ii} = \sum_j A_{ij}$$

$$L$$ is real symmetric and positive semidefinite. So, it can be factored into
$$L = U \Lambda U^T$$
* $$U$$ = columwise eigenvectors ordered by eigenvalues
* $$\Lambda$$ = diagonal matrix of eigenvalues

Graph fourier transform on input $$x \epsilon R^n$$ is defined as $$y = U^T x$$
similarly vice-versa for graph inverse fourier transform.

Assuming a filter $$g \epsilon R^n$$, convolution operation will become
$$x*g = U (U^T x \odot U^T g) = U g_{\theta} U^T x$$ with $$g_{\theta} = U^T g$$
All spectral methods follow this, except for their choice of $$g_{\theta}$$.
Some methods are:
1. Spectral CNNs
2. Chebyshev spectral CNNs (ChebNet)
3. CayleyNet
4. [GCN]({{ site.baseurl }}{% post_url 2020-06-09-graph-convolutional-networks %})
   these are however a mix of spectral and spatial based by approximating
   ChebNet at first-order and simplifying learnable parameters.

#### spatial based
All these methods aggregate neighbor information in some form and propagate this
to the current node. Multiple such layers are stacked upon each other to
increase the neighborhood definition.

* Neural Network for Graphs: Somewhat resembles GCN.
  $$H^{(k)} = f(X W^{(k)} + \sum_{i=1}^{k - 1} A H^{(k-1)} \Theta^{(k)})$$
* Diffusion CNNs: $$H^{(k)} = f(W^{(k)} \odot P^k X)$$
* Diffusion Graph Convolution: $$H = \sum_{k=0}^K f(p^k X W^{(k)})$$
* Message Passing NN
* GraphSage: samples the neighbors in order to avoid needing full-batch
* fast-GCN: samples a fixed number of nodes instead of neighbors
* Graph Attention Network
  - $$h_v^{(k)} = \sigma(\sum_{u \epsilon N(v) \cup v} \alpha_{vu}^{(k)} W^{(k)} h_u^{(k-1)})$$
  - $$h_v^{(0)} = x_v$$
  - $$\alpha_{vu}^{(k)} = softmax(leakyReLU(a^T [W^{(k)}h_v^{(k-1)} || W^{(k)}h_u^{(k-1)}]))$$

#### spectral vs spatial
- spectral methods have theoretical framework
- spatial methods are computationally efficient and scalable
- spatial methods allow batching of nodes in a graph
- spectral methods only work with undirected graphs

#### graph pooling modules
coarsen the graph representation to reduce computationaly complexity for graph
classification and such other tasks next in the pipeline. Popular approach is to
use mean/max/sum based pooling functions:
$$h_G = poolFunction(h_1^{(K)}, h_2^{(K)}, ..., h_n^{(K)})$$

### Graph autoencoders

#### network embedding
Low dimensional representation of nodes which preserves the topological info.
* Graph AutoEncoder: uses GCN in encoder phase and decoder phase tries to
  reconstruct the adjacency matrix based on the generated embedding
* Variational GAE: Variational version of the above, using KL divergence as the
  metric

#### graph generation
Beneficial in solving molecular graph generation problem. There are methods
which try to generate graphs globally or sequentially.

### spatio-temporal GNNs
Capture both spatial and temporal dependencies together. eg: traffic speed
forecasting. Most simple way is to feed the output of convGNNs into recurrent
layer like RNNs/LSTMs.

### future directions
1. model depth - going infinite depth will pull all nodes into a single point!
   Does it make sense to increase depth?
2. scalability trade-off - use of clustering could destroy patterns, while
   sampling the neighbors may miss critical info at times. Need to find a good
   trade-off between scalability and info-loss
3. heterogeneous graphs support
4. dynamicity - STGNNs addresses some aspects of this.
