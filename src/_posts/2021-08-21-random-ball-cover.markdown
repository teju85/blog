---
layout: post
title: "Accelerating Nearest Neighbor Search on Manycore Systems"
needmath: true
tags: tech-notes math
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/1103.2635.pdf).

* An indexing technique for NN queries
* It scales sublinearly ($$O(\sqrt n)$$) on the dataset size
* It generalizes to all distance metrics
* Depends only on the intrinsic dimensionality of the dataset
* Easy to parallelize on multi/many core systems

### Summary
- techniques like LSH do scale sublinearly wrt dataset sizes. However, they are
  hard to tune, approximate and work on omly certain metrics
- brute force NN search is easy to parallelize but does more work
- $$\rho$$ is the distance metric
- Data structure introduced is called Random Ball Cover (RBC):
  - randomly pick $$n_r$$ representatives from the dataset
  - for each rep, it "owns" a set of points in the dataset $$L_r$$. They
    typically are the closest points to this rep.
  - for each rep, also store the max distance from it to the points in its
    cover, $$\psi_r$$
- there are 2 search algos based on RBC: exact and one-shot. And for both these
  algos, building RBC boils down to calling brute-force NN search.
- one-shot
  - $$L_r$$ contains a suitably sized $$s$$ NNs of that rep from the dataset
  - when given a query, it is first brute-forced through all the representative
    points to find the nearest rep
  - then again brute-forced through its $$L_r$$ for the NNs
  - it can be proved that it's complexity is $$O(\sqrt n)$$
  - it sometimes can give approximate results, but can be very fast in practice
- exact
  - $$L_r$$ contains all points in the dataset for which this rep is the closest
  - this relies on triangle inequality in order to guarantee exact results
  - the closest point to $$q$$ called $$r_q$$ is found from the set of reps
  - let $$\gamma = \rho(q, r_q)$$. This is an upper bound on q's NNs.
  - all reps with $$\rho(r, q) > \gamma + \psi_r$$ are discarded
  - all reps with $$\rho(r, q) > 3 \rho(r_q, q)$$ are also discarded
  - after this, do a brute force on all the points belonging to the remaining reps
  - it can be proved that it's complexity is $$O(\sqrt n)$$
- for parallelization strategy, they simply come up with an effective way to
  parallelize brute force search, which is very similar to a gemm implementation
