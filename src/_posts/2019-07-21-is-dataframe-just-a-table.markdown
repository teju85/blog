---
layout: post
title: "Is dataframe just a table?"
tags: tech-notes paper-notes data-analytics
---

### Is Dataframe just a table?
Full article can be found [here](https://plateau-workshop.org/assets/papers-2019/10.pdf)

#### Proposal
The author tries to explain the reasons why the design of dataframes and tables
are different.

#### Details
- database folks think in terms of tables (aka relations)
- datascience folks think in terms of dataframes (read pandas)
- former uses lists, whereas the latter uses sets
  - author argues that this can have impact on how the implementations will differ
    between these cases use-cases!
  - because lists are dependent on the order whereas sets aren't
- matrices vs tables
  - matrices are good at aggregation kind of operations
  - however, by storing variables also as columns, such a "matrix" could be converted
    into a relation, thereby easing this process too!
- however, tables seem to outshine dataframes when it comes to joins
  - closest operation in dataframes is a merge
  - author argues that merge and concat ops in dataframes are not actually the same as
    as in join and union ops in tables and these dataframes ops are needlessly
    complicated!
- dataframes are procedural interfaces while relations offer more declarative style
- sql ops, for eg, only support first-order logic (looping across items is 2nd order)
- code reuse is better with dataframes than with tables
- debugging is also better with dataframes
- tables have query-optimizers which can lead to better optimized operations internally
  - in dataframes, users have to manually tune for perf
- dataframes offer many ways to solve one thing, which can be confusing to programmers
