---
layout: post
title: "GraphSAGE"
needmath: true
tags: tech-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/1706.02216.pdf).
SaGe = Sample and Aggregation functions

* Learns parametric functions in order to generate low dimensional embeddings of
  the nodes in the graph
* These functions can also be used to generate embeddings of unseen nodes too
* It can also optionally use node features as starting points for embeddings
* Configurable number of layers representing the number of hops for each node
* Custom loss function (based on negative-sampling) for unsupervised learning
* Also supports supervised learning
* Scales to large graphs through neighborhood sampling and minibatch techniques

### forward propagation algo
- $$h_v^0 = x_v$$
- for k = 1 to K
  - for v in minibatch
    - $$h_{N(v)}^k = aggregator_k(h_u^{k-1}, u \epsilon N(v))$$
    - $$h_v^k = \sigma(W^k concat(h_v^{k-1}, h_{N(v)}^k))$$
    - $$h_v^k = \frac{h_v^k}{L2norm(h_v^k)}$$
- $$z_v = h_v^K$$

Where:
- $$h^k$$ = hidden vectors at each layer for all vertices
- $$V$$ = nodes
- $$N(v)$$ = sampled neighborhood for each node
- $$K$$ = number of layers (hyperparameter)
- $$\sigma$$ = a non-linear activation function
- $$W^k$$ = learnable weights for each layer
- $$z$$ = output embedding

In paper the authors show the similarity of this algo with the popular
[Weisfeiler-Lehman](https://www.davidbieber.com/post/2019-05-10-weisfeiler-lehman-isomorphism-test/)
graph isomorphism test.

### neighborhood sampling
- performs uniform sampling
- different samples are drawn for each layer based on different sampling rates
  $$S_i$$, for each layer
- authors recommend to keep $$\Pi_i S_i \le 500$$
- sampling technique is pretty much the same as seen in
  [PinSage]({{ site.baseurl }}{% post_url 2020-06-10-pinsage %})
- They recommend $$K = 2, S_1 = 25, S_2 = 10$$

### learning
- via SGD + using Adam optimizer
- loss function for unsupervised mode is based on negative sampling and its
  equation is as follows: $$J(z_u) = -log(sigmoid(z_u^T z_v)) - Q E[log(sigmoid(z_u^T z_{v_n}))]$$
- $$Q$$ = number of negative samples
- $$v_n$$ = negative sample
- $$v$$ = node that is a neighbor of $$u$$

### aggregators
These must be permutation invariant. They test the following aggregators

#### mean aggregator
- $$h_v^k = \sigma(W^k Mean(h_u^{k-1} with u \epsilon N(v), h_v^{k-1}))$$
- note that this uses $$h_v^{k-1}$$ in the aggregation itself!
- thus this can be thought of as "skip connection" between layers

#### LSTM aggregator
- LSTM's are not permutation invariant
- So they make it to be invariant by randomly permuting the inputs
- this seems to show the best accuracy in their experimentation

#### pooling aggregator
- $$h_{N(v)}^k = max_{u \epsilon N(v)}(\sigma(W_{pool}^k h_u^k + b^k))$$
- aggregator can be either max or mean, both seem to provide similar accuracy
