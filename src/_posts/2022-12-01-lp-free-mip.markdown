---
layout: post
title: "Feasibility Jump: an LP-free Lagrangian MIP heuristic"
needmath: true
tags: tech-notes paper-notes optimization
---

### Proposal
Main paper can be found [here](https://luteberget.github.io/preprints/feasibilityjump-2022-11-07.pdf).

* LP-free primal heuristic for MIP solver
* [Implemented a C++ plugin](https://github.com/sintef/feasibilityjump) for the FICO Xpress solver

### Summary

#### The problem and its notation
- MIP (Mixed Integer Programming) is an optimization problem of the form
  - minimize $$\Sigma_{j \epsilon N} c_j x_j$$
  - subject to
    - $$\Sigma_{j \epsilon N} a_{ij} x_j \le b_i \qquad (i \epsilon M)$$
    - $$l_j \le x_j \le u_j \qquad (j \epsilon N)$$
    - $$x_j \epsilon Z \qquad (j \epsilon I)$$
- where
  - $$N$$ = number of variables
  - $$M$$ = number of constraints
  - $$Z$$ = set of integers
  - $$I$$ = set of variables that can only take integer values

#### Algorithm
- Lagrangian relaxation
  - Relax all the constraints (except the variable bounds and integrality constraints)
  - Penalize the relaxed ones, when they violate the constraints, in the objective function
- IOW
  - minimize $$O^q(x) + F^w(x)$$
  - subject to
    - $$l_j \le x_j \le u_j \qquad (j \epsilon N)$$
    - $$x_j \epsilon Z \qquad (j \epsilon I)$$
  - where
    - $$O^q(x) = q \Sigma_{j \epsilon N} c_j x_j$$ = original objective weighted by $$q$$
    - $$F^w(x) = \Sigma_{i \epsilon M} w_i f_i(x)$$ = total infeasibility penalty
    - $$w_i$$ = weight for each constraint
    - $$f_i(x) = max(0, \Sigma_{j \epsilon N} a_{ij} x_j - b_i)$$
    - using 'max' function means we are interested in the solutions that live on
      the edge rather than interior of the feasibility region.
- this doesn't minimize the langrangian function directly, but instead looks for
  a local minimum in the feasible neighborhoods where only variable is varied.

#### jump value
- current assignment assumed to be $$x = \overline{x}$$ and only one variable $$x_j$$
  is allowed to change with the rest of them fixed.
- However, we expect the resultant value of $$x_j$$ to not be $$\overline{x_j}$$
- Let's say $$r_{ij} = \frac{b_i - \Sigma_{k \ne j} a_{ik} \overline{x_k}}{a_{ij}}$$
- Thus, if $$x_j$$ is integer variable, we have
  - $$t_{ij}(\overline{x_{k \ne j}}) = \lfloor r_{ij} \rfloor \qquad if \qquad a_{ij} > 0$$
  - $$t_{ij}(\overline{x_{k \ne j}}) = \lceil r_{ij} \rceil \qquad if \qquad a_{ij} < 0$$
- else, if $$x_j$$ is fractional, we have: $$t_{ij}(\overline{x_{k \ne j}}) = r_{ij}$$
- We'll get a piecewise linear convex function:
  - $$g_{ij}(t|\overline{x_{k \ne j}}) = max(0, w_i(t - t_{ij}(\overline{x_{k \ne j}}))) \qquad if \qquad a_{ij} > 0$$
  - $$g_{ij}(t|\overline{x_{k \ne j}}) = max(0, -w_i(t - t_{ij}(\overline{x_{k \ne j}}))) \qquad if \qquad a_{ij} < 0$$
- constraint violation penalty then is: $$G_j(t|\overline{x_{k \ne j}}) = \Sigma_{i \epsilon M} g_{ij}(t|\overline{x_{k \ne j}}) \qquad a_{ij} \ne 0$$
- jump for this variable would then become
  - $$J_j(\overline{x_{k \ne j}}) = argmin_{t \epsilon [l_j, u_j] - \overline{x_j}} G_j(t|\overline{x_{k \ne j}})$$
  - this means, it can only be one of: $$J_j(\overline{x_{k \ne j}}) = \text{\textbraceleft} l_j, u_j, t_{ij}(\overline{x_{k \ne j}}) \text{\textbraceright}$$
