---
layout: post
title: "Power of GCNs"
tags: tech-notes graph gnn
---

### Power of GCNs
Summary of the content of the blog found [here](https://www.inference.vc/how-powerful-are-graph-convolutions-review-of-kipf-welling-2016-2/).

### Summary
- Author seems to claim that due to 1st order approximation of Chebyshev polynomials
  as the convolution filter, their expressive power might not be good
- that's because this approximation, when applied to the special case of regular
  graphs (2D images, eg), will lead to severely weak models
- But the [main authors of the GCN](https://tkipf.github.io/graph-convolutional-networks)
  paper also note that the Weisfeiler-Lehman algo also doesn't converge on
  regular graphs!
