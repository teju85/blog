---
layout: post
title: "Initial notes from my study on SAT solvers"
tags: tech-notes sat
---

### SAT solvers
* DNF - Disjunctive Normal Form. Eg: `(x AND y) OR (y AND z)`
* NNF - Negative Normal Form. All negations are only in front of variables
* CNF - Conjunctive Normal Form. Eg: `(x OR y) AND (y OR z)`
* CNF formula is a set of clauses (conjunctive) which each clause being a set of
  literals (disjunctive)
  - empty formula represents a true formula
  - empty clause represents a false clause
  - unit clause is a clause with just 1 literal
  - variable is referred by its id
  - positive id means the variable and negative means its negation
* SAT is NP-complete but in practice (aka real world problems) we can do much better
* Serial SAT algos
  - complete algos (aka systematic solvers)
    - Typically based on backtracking
    - eg: DPLL, GRASP
    - computationally expensive
    - will return all satisfying assignments if they exist
    - else will give proof for unsatisfiability
  - incomplete algos
    - eg: randomized algos, local search based, GSAT, WalkSAT
    - may or may not produce SAT/UNSAT
    - these local search strategies do often reach global minima!
* Parallel algos
  - partioning based
  - competition based
* DPLL
  - complete solver based on backtracking
  - most of the complete solvers are all mostly based on this algo
  - if it is a unit clause then assign it to true
  - repeat until no more unit clauses
  - if a conflict is found, backtrack and assign a different value to that literal
* GRASP
  - improvement over DPLL with learning clauses to reduce the amount of backtracking
  - uses CDCL - Conflict Driven Clause Learning
  - helps narrows search space with DPLL
* k-CNF = formulat with every clause having exactly 'k' literals
* 2-CNF formulae can be solved in poly-time, whereas 3-CNF is already NP-complete
* to reduce memory usage most solvers nowadays are iterative rather than recursive
* GSAT
  - randomized local search technique
  - selects assignments which most reduces the number of remaining clauses
  - can also move sideways (aka plateaus) which doesn't reduce this at all!
* WalkSAT
  - interleaves greedy moves of GSAT with random walks of a Metropolis search
* m = #of clauses, n = #of variables, for k-CNF problems, if clauses are generated
  randomly, then the hardness of these problems (aka number of DP calls) follows
  an easy-hard-easy pattern as a function of $$\frac{m}{n}$$. But when we don't
  consider fixed length clauses then there are no such clean indication of hardness!
* the above was the main reason which motivated local search methods for SAT solvers
* SP - Survey Propagation. Use of probabilistic reasoning for solving combinatorial
  search problems. But SP is currently limited only for random SAT instances!
