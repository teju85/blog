---
layout: post
title: "Initial notes from my study on SAT solvers"
tags: tech-notes sat
---

Collection of random notes of mine while ramping up on the domain of SAT solvers.

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
* Max-SAT
  - Maximum satisfiability problem
  - return the maximum number of clauses that can be satisfied by the assignments
  - it is a generalization of the SAT problem
* Nice (4hrs!) talk on implementing a SAT solver from scratch
  - video: https://www.youtube.com/watch?v=II2RhzwYszQ
  - repo: https://github.com/arminbiere/satch (It is a from-scratch serial solver
    based on CDCL with restarting mechanism)
  - initial hour or so talks about the theory/background introducing popular
    solvers (eg: DPLL, CDCL)
  - Stopped at 1:05:15
* The Armin Biere's talk on SAT solving: https://www.youtube.com/watch?v=Emhg0uZnbNg
  - Knuth himself acknowledged SAT solving to be the "killer app"!
  - AIG - And-Inverter Gates. Logical gates built using only and and nor gates
  - IPASIR model showing different states of a SAT solver: (UNKNOWN, SAT,
    UNSAT, SOLVING), for interactive solving of formulae
  - In one of his videos, the CTO of Amazon spends 20mins talking about SMT solvers!
  - SMT solvers completely rely on CDCL technique
  - after constructing impllication graph, typically we would like to learn the
    clause out of its first UIP (Unique Implication Point) and then to recursive
    clause minimization
  - in his satch codebase this recursive clause minimization code when expressed in
    recursive fashion is running faster than the iterative version!
* Peek inside SAT solvers: https://www.youtube.com/watch?v=d76e4hV1iJY
  - introduction to the SAT problem and CNF notation
  - typical flow: high-level problem -> encode into SAT using a P-time algo -> use SAT solver
  - introduces the DFS based search space to solving this brute-force
  - but also notes that we are free to choose assignment as well as literal
    order in this DFS!
  - shows the benefit of simplifying the clause evaluation through unit propagation
  - thereby deriving DPLL (DFS + backtrack + unit-prop)
  - zChaff solver
    - VSIDS - ranking the literals based on their occurence count and then using
      this to assign values in order to reach solution faster
    - two watched literals - have an index of pair of literals to reach its
      clauses faster, especially to be notified when we get unit-prop
 - CDCL - GRASP solver
   - when conflicts arise, create an implication graph, separate the literals from
     the conflicts and then derive the clause that can help us not revisit this
     conflict during future traversals
   - then depending on the clauses we could also backjump multiple levels!
   - however one needs to consider the following while learning such clauses:
     - we simply can't keep learning all the clauses (space issues)
     - need to maintain these clauses in a clever manner
     - need to minimize these clauses using a technique called "resolution"
     - need to save the last assignment to variables called "phase saving"
 - restarts
   - we are not clearing the learned clauses, but only restarting the DFS
   - can help us get unstuck at times

### SAT Benchmarks
- Large SAT problems in CNF format: http://www.miroslav-velev.com/sat_benchmarks.html
- low-to-medium sized SAT problems in DIMACS CNF format: https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html

### GPU SAT solver implementations
- https://github.com/QuentinFiard/cuda-sat-solver - But doesn't seem to be calling any cuda kernels at all!?
- https://github.com/nicolasprevot/GpuShareSat
