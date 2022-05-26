---
layout: post
title: "Accelerating weighted random sampling without replacement"
tags: tech-notes paper-notes
---

### Summary
Main paper can be found [here](https://www.ethz.ch/content/dam/ethz/special-interest/baug/ivt/ivt-dam/vpl/reports/1101-1200/ab1141.pdf).

- there are multiple approaches given here
- the simplest in terms of cuda is the one-pass sampling
  - generate exponentially distributed random numbers
  - scale them wrt the input weights of the data to be sampled
  - sort this scaled array
  - pick the items corresponding to the indices of the top-k items in this sorted array
- the issue is that this thing cannot be directly used for permuting arrays!
