---
layout: post
title: "GPU Multisplit"
tags: tech-notes paper-notes cuda algorithms
---

### GPU Multisplit
Main paper can be found [here](http://delivery.acm.org/10.1145/2860000/2851169/a12-ashkiani.pdf?ip=121.244.166.165&id=2851169&acc=ACTIVE%20SERVICE&key=D494438A622BF6CC%2ED494438A622BF6CC%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1561962172_44fee4c400764be9c464ccd99ad0ab9d)
and their reference implementation is [here](https://github.com/owensgroup/GpuMultisplit).

- efficiently bucketizing arrays based on keys
- only small number of buckets are considered here (2 - 64)
- for these cases, such an implementation will be much faster than full sort
- Idea is to split the algo into 3 phases
  - local - compute bucket histograms and their scans
  - global - compute global location of each element
  - local - compute local location of each element and perform scatter
- They also perform local multisplit to reduce memory divergence!
