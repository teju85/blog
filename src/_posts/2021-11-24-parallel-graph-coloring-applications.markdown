---
layout: post
title: "Parallel Graph Coloring with Applications to the Incomplete-LU Factorization on the GPU"
needmath: true
tags: tech-notes paper-notes
---

### Proposal
This is my summary of the paper that gives a parallel graph coloring approach
and discusses its application to incomplete LU factorization. The paper can be
found [here](https://research.nvidia.com/sites/default/files/pubs/2015-05_Parallel-Graph-Coloring/nvr-2015-001.pdf).

Note that I mostly read this paper for the discussions related only to the
parallelization of graph coloring problem. Thus, my notes below only reflect
this! If you need to know more the applications, please refer to the main paper
itself.

#### Summary
- a simple sequential approach to graph coloring is the standard BFS approach.
  This is simple to implement but might not be optimal.
- However a different approach to parallelize this is to instead focus on the
  maximal independent set construction.
- Luby's parallel algo for independent set construction is as follows:
```
Generate a random number for each vertex: r(v)
for all vertices in parallel:
  if r(v) > r(w) for all its neighboring nodes w:
    Add vertex v into the independent set S
```
- Jones and Plassman extended this to (called JPL):
```
W = V   # start with full set of vertices in the graph
for k in 1, 2, ... until W becomes empty:
  S = find independent set based on Luby's algo above
  assign color k to all vertices in S
  remove vertices in S from W
```
- Cohen and Castonguay updated this by proposing different heuristic for
  ordering the vertices (called CC): (implemented in csrcolor of cusparse)
  - use a hash function to compute on-the-fly instead of random numbers
  - associate multiple hash values to each node thereby generating different
    independent sets at once
- we could also stop after certain iterations and color the remaining uncolored
  nodes with the next highest unchosen color or color them all sequentially with
  different colors
- CC can be 2-3x faster than JPL, but can use 2-3x more colors!
