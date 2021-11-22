---
layout: post
title: "Google vs IBM: A Constraint Solving Challenge on the Job-Shop Scheduling Problem"
needmath: true
tags: tech-notes paper-notes sat
---

### Proposal
This is my summary of the paper that compares the quality and performance of
job-shop scheduling solvers by Google and IBM. The paper can be found
[here](https://arxiv.org/pdf/1909.08247).

- compare the quality of and time to (both single and quad core) solutions by
  the two famous solvers: Google OR-Tools and IBM CPO
- they compare these 2 against classic instances in the literature as well as
  a large scale benchmark with known optimal solutions
- CPO in general performs better on both these types of instances
- ORT performs better in the quad core setup
- CPO is much superior when it comes to large scale problems

#### Summary
- there are different types of scheduling problems: job-shop, flow-shop,
  open-shop etc
- job-shop is the most popular among them and it tries to minimize the makespan
  of the whole process.
- makespan = interval between the start of the earliest job and end of the
  latest job
- till now this has been posed as a constraint satisfaction problem
- recently it is being solved using LNS (Large Neighborhood Search) methods
- they chose CP-SAT from OR-Tools for solving job-shop problem and kept the
  default optimizer from CPO
- they only look at rectangular job-shop instances. Meaning:
  - every job has to go through all the machines
  - every job has number of ops equal to the number of machines
  - every machine will have assigned a number of ops equal to the number of jobs
- Both CPO and ORT use LNS as their technique
- CPO uses portfolio strategies along with ML to converge to the best
  neighborhoods but ORT uses the simple variable/constraint selection techniques
