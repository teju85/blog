---
layout: post
title: "Tree-LSTM's"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/1503.00075.pdf).

* Generalization of LSTMs to tree structured network topologies, with arbitrary
  branching factor
* demonstrate better results than "linear" LSTMs on SemEval and SSTB datasets

### Tree LSTMs
- "linear" LSTMs compute their current hidden state based on previous hidden
  state and current input
- tree LSTMs compute their current hidden state from current input and hidden
  states of children. There will be one forget gate for each child and only the
  leaf nodes get to take in the input vectors

#### Child tree LSTMs
- useful for unordered children
- eg: dependency trees
- $$C(j)$$ = children of j-th node
- $$\sigma$$ = sigmoid function
- $$x_j$$ inputs to the j-th node
- $$k \epsilon C(j)$$

$$h_j' = \sum_k h_k$$

$$i_j = \sigma(W^{(i)}x_j + U^{(i)}h_j' + b^{(i)})$$

$$f_{jk} = \sigma(W^{(f)}x_j + U^{(f)}h_k + b^{(f)})$$

$$o_j = \sigma(W^{(o)}x_j + U^{(o)}h_j' + b^{(o)})$$

$$u_j = tanh(W^{(u)}x_j + U^{(u)}h_j' + b^{(u)})$$

$$c_j = i_j \odot u_j + \sum_k f_{jk} c_k$$

$$h_j = o_j \odot tanh(c_j)$$

#### N-ary tree LSTMs
- useful when branching factor is atmost N
- has finer grained control over forget gates from each child node
- child nodes are expected to be ordered

$$i_j = \sigma(W^{(i)}x_j + \sum_{l=1}^N U_l^{(i)}h_{jl} + b^{(i)})$$

$$f_{jk} = \sigma(W^{(f)}x_j + \sum_{l=1}^N U_{kl}^{(f)}h_{jl} + b^{(i)})$$

$$o_j = \sigma(W^{(o)}x_j + \sum_{l=1}^N U_l^{(o)}h_{jl} + b^{(o)})$$

$$u_j = tanh(W^{(u)}x_j + \sum_{l=1}^N U_l^{(u)}h_{jl} + b^{(u)})$$

$$c_j = i_j \odot u_j + \sum_{l=1}^N f_{jl} \odot c_{jl}$$

$$h_j = o_j \odot tanh(c_j)$$
