---
layout: post
title: "An optimization model for a real-time flight scheduling problem"
needmath: true
tags: tech-notes paper-notes optimization
---

### Proposal
Main paper can be found [here](https://www.researchgate.net/profile/Jacques-Desrosiers/publication/222682436_An_optimization_model_for_a_real-time_flight_scheduling_problem/links/5a1190ec458515cc5aa93d1b/An-optimization-model-for-a-real-time-flight-scheduling-problem.pdf?origin=publication_detail).

* Focuses on DAYOPS (Day of Operations Scheduling) problem in real-time under
  minor perturbations from the original plan.
* Both activity start and duration times are considered as variables
* Authors show that the dual of the resulting model is a network problem and
  thus has a linear complexity of time to solution

### Summary
- DAYOPS involves determining real-time changes to flight schedules when
  perturbations occur to minimize customer inconvenience and airline costs
- planning process of large airlines involves the following 4 phases:
  - flight scheduling
  - fleet assignment
  - aircraft routing
  - crew scheduling
- these phases are done offline with lots of data and time at hand. But for DAYOPS
  scenario both are scarce
- they show that while the primal equation with constraints scales polynomially in
  runtime wrt the model size, the dual form only scales linearly. Thereby making
  the latter a suitable candidate for realtime requirements
- Authors use CPLEX linear optimizer to solve the resulting system of constrainted
  equations
