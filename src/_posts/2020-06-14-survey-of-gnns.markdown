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

#### spectral vs spatial
- spectral methods have theoretical framework
- spatial methods are computationally efficient and scalable
- spatial methods allow batching of nodes in a graph
- spectral methods only work with undirected graphs

#### graph pooling modules

### Graph autoencoders

#### network embedding

#### graph generation

### spatio-temporal GNNs

### future directions
1. model depth - going infinite depth will pull all nodes into a single point!
   Does it make sense to increase depth?
2. scalability trade-off - use of clustering could destroy patterns, while
   sampling the neighbors may miss critical info at times. Need to find a good
   trade-off between scalability and info-loss
3. heterogeneous graphs support
4. dynamicity - STGNNs addresses some aspects of this.
