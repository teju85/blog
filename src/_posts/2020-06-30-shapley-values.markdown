---
layout: post
title: "Shapley Values"
needmath: true
tags: tech-notes book-notes interpretable-machine-learning machine-learning
---

### Summary
The reference chapter can be found in [this](https://christophm.github.io/interpretable-ml-book/shapley.html)
book.

- Shapley Values (SV) explain prediction via considering each feature as a
  player and prediction as the payout and deals with how to fairly distribute
  the payout among the players
- has solid base in coalitional game theory
- gain (payout) here is the difference between actual prediction and average
- SV for an instance is the average marginal  contribution of a feature value
  across all possible coalitions (weighted average, to be precise)
- marginal contribution = difference between prediction with and without this
  feature value
- computing SV for linear models is very straightforward
- SV satisfy the following properties
  - Efficiency - feature contributions add upto difference between predicted and
    mean prediction
  - Symmetry - SV of 2 feature values should be the same if they contribute
    equally for all coalitions
  - Dummy - if a feature value does not contribute to the output, then its value
    should be 0
  - Additivity - for ensemble models, final SV can be computed by adding up the
    individual SV from each of the underlying models

#### Computating SV
$$\phi_j = \sum_{S \subset {x} - {x_j}} \frac{len(S)! (p - len(S) - 1)!}{p!} (val(S \bigcup {x_j}) - val(S))$$

$$val(S) = \int_{x \notin S} f(x_1, ..., x_p) - E[f(X)]$$

Where:
- $$\phi_j$$ - SV for j-th feature value
- $$p$$ - number of features
- $$f$$ - the model

#### Approximating SV via Monte-Carlo sampling
$$\phi'_j = \frac{1}{M} \sum_{m=1}^M f(x_{+j}^m) - f(x_{-j}^m)$$

Where:
- $$M$$ - number of samples
- $$f(x_{+j}^m)$$ - prediction where the feature values are first randomly
  permuted and then the first j feature values are kept from the input sample
  while the rest are randomly picked from another sample in the dataset.
- $$f(x_{-j}^m)$$ - same as above but with j-th feature value also chosen at
  random from another sample

#### Disadvantages
- suffers from inclusion of unrealistic feature values
- computationally super expensive
- explanation involves all the features, which can be difficult for humans to
  further interpret, as opposed to explainer models like LIME.
