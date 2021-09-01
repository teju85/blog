---
layout: post
title: "Incomplete Algorithms for SAT solving"
needmath: true
tags: tech-notes sat
---

### Summary
This is my summary of the 6th Chapter of the Handbook of Satisfiability by
Dr. Armin Biere et.al This book can be found [here](https://www.iospress.com/catalog/books/handbook-of-satisfiability).
This chapter provides a very concise view of some of the popular incomplete
algorithms designed for solving SAT instances.

- incomplete methods don't provide guarantee of both satisfying assignments or
  unsatisfiability
- mostly they are biased towards satisfying side (aka one-sided error)
- generally based on Stochastic Local Search (SLS)
- GSAT and WalkSAT pioneered these group of methods
- SAT formula $$F$$ with $$n$$ variables and $$m$$ clauses $$C_1, C_2, ..., C_m$$
  can be seen as a manifold in the space of $${0, 1}^n x {0, 1, ..., m}$$
  - $${0, 1}^n$$ = the truth assignment space
  - $${0, 1, ..., m}$$ = number of unsatisfied clauses in $$F$$
- thus, this becomes a global minimization problem in the manifold, which obviously
  can have local minima!
- this is a useful representation because we can use to solve max-SAT instances
  too (but with two-sided error)

#### GSAT
```
for i = 1 : max_tries:
  sigma = random truth assignment for F
  for j = 1 : max_flips:
    if sigma satisfies F return sigma
    v = variable whose flipping results in greatest decrease in the number of unsatisfied clauses
    flip v in sigma
return FAIL
```
- typically the manifold has a lot of plateaus
- this means GSAT spends a lot of time in traversing these plateaus before
  jumping to another one

#### WalkSAT
```
for i = 1 : max_tries:
  sigma = random truth assignment for F
  for j = 1 : max_flips:
    if sigma satisfied F return sigma
    C = a random unsatisfied clause from F
    if for a variable x in C which has break-count = 0"
      v = x  // freebie move
    else:
      if biased coin toss with probability p:
        v = a random variable in C  // random walk move
      else:
        v = variable in C with smallest break-count  // greedy move
    flip v in sigma
return FAIL
```
- introduces noise (aka uphill moves) to avoid the "plateau issue" of GSAT
- interleaves GSAT moves with random walks of a Metropolis search
- focuses the search space by always selecting the variables to flip from one of
  the unsatisfied clauses only
- break-count = number of satisfied clauses being unsatisfied due to the flip

#### Others
- UnitWalk = unit propagation + WalkSAT
- TSAT = tabu list + GSAT
- clause-re-weighting techniques
  - assign positive weights to each unsatisfied clauses
  - attempt to minimize the sum of these weights
  - re-weigh the remaining unsatisifed clauses and repeat
- DLM - Discrete Lagrangian Methods
  - generalized version of clause re-weighting methods, but with theory from
    Lagrangian multipliers
  - Assume $$x$$ to be an assigment of $$F$$
  - then a SAT problem can be represented as the following minimization problem
  - $$minimize N(x) = \Sigma_{i=1}^m U_i(x) subject to U_i(x) = 0$$
  - $$U_i(x)$$ is 0 if $$C_i$$ is satisifed by $$x$$, else 1
  - now rewrite this using Lagrangian multipliers by doing as below
  - $$L_d(x, \lambda) = N(x) + \Sigma_{i=1}^m \lambda_i U_i(x)$$
  - then use difference gradient methods to optimize this equation
- Survey Propagation (SP)
  - performs iterative local message updates on the marginal probabilities of
    the set of satisfying assignments
  - assigns the values to variables with extreme probabilities
  - simplifies the formula based on this assignment and repeats
  - this is based on methods derived from statistical physics
  - works well on random SAT instances, though not yet on real world problems
  - they are recently found to be similar to belief propagation methods
  - first example of using probabilistic reasoning to solve a combinatorial
    optimization problem!
  - Note: This seems to be similar to message passing neural nets!?
