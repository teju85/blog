---
layout: post
title: "HashGraph - Scalable Hash Tables Using A Sparse Graph Data Structure"
tags: tech-notes paper-notes
---

### Introduction
Main paper can be found [here](https://arxiv.org/pdf/1907.02900.pdf).

- It is indifferent to the load factor.
- Deal with hash-collisions without open-addressing or chaining methods while
  having all their benefits
- New probing algorithm for query phase
- Currently only focuses on static data hash tables

### Summary
- goes through the data multiple times in order to figure out how to handle the
  collisions efficiently
- this shows a relationship between building hash tables and creating a sparse
  graph data structure. Like a bipartite graph, which can be represented using
  a CSR structure.
- Given an input we could use the hash function to get to know the hash value.
  Then use a CSR structure from the hash value to the inputs, in order to know
  the input for a given hash value.
- hashgraph v1 (same as how one would construct a CSR)
  - compute the hashes
  - compute the histogram of different values
  - compute the prefix sum of it to generate the offsets
  - write the inputs to the corresponding offset locations
- hashgraph v2
  - at first reorganize the hash values into multiple bins by doing a similar
    CSR construction, but at each bin level (instead of the hash value itself)
  - then go through this reorganized buffer in order to construct the final
    hashgraph using v1 algo
  - this helps take advantage of caches
  - memory footprint is double that of v1 algo
- probing
  - construct hashgraph for the query array
  - go through all the possible values and find intersection at each value in
    the CSR
