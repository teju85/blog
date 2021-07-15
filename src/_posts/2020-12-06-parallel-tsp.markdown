---
layout: post
title: "Parallel GPU version of TSP"
needmath: true
tags: tech-notes paper-notes graph cuda tsp
---

### Proposal
Main paper can be found [here](https://userweb.cs.txstate.edu/~burtscher/papers/pdpta11b.pdf).

* An optimized GPU version of TSP solver using Iterative Hill Climbing (IHC)
  technique
* Paper limits itself to 100-cities with 100,000 random restarts.
* However, the techniques suggested here can be generalized

### Summary
- each thread works on one of the climbers.
  - continues to perform the 4851 2-opt moves in each IHC step, until convergence
  - FYI, $$4851 = \frac{(100 - 1) * (100 - 2)}{2}$$
- after convergence of each climber, a global atomicCAS is performed in order to
  update the best solution found so far
- they only compute the incremental TSP cost instead of computing the full path
  cost inside IHC step and only compute the global path cost after convergence
- all threads continue to fetch their next climber from a global queue until it
  is exhausted
- distance matrix is assumed to be pre-computed (for edge weights)
