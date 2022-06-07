---
layout: post
title: "Fine-grained and Accurate Source Code Differencing"
needmath: true
tags: tech-notes paper-notes
---

### Proposal
Main paper can be found [here](https://dl.acm.org/doi/pdf/10.1145/2642937.2642982).

* an efficient AST diff algorithm
* not interested in the shorted edit scripts, but the edit script that closely
  mimics the developer's intent
* also includes move actions (eg: when doing source code refactor)

### Summary
- All the code is open-sourced [here](https://github.com/GumTreeDiff/gumtree).
- AST differencing - computing a sequence of edit actions to transform one AST
  into another (similar to edit distance on strings). This sequence is called
  edit script
- following operations are considered in an edit script
  - $$update(t, v)$$ = replace old value of node $$t$$ with value $$v$$
  - $$add(t, t_p, i, l, v)$$ = adds a new node $$t$$ with label $$l$$ and value
    $$v$$. It will be added as the $$i$$th child of parent node $$t_p$$, if this
    is not specified, then it will be added as the new root node
  - $$delete(t)$$ = delete the node $$t$$
  - $$move(t, t_p, i)$$ = move node $$t$$ as the $$i$$th child of parent node
    $$t_p$$. This moves the whole subtree
- If move operation is included, finding the shortest sequence of edits will be
  a NP-hard problem
- typical solutions involve 2 step process
  - finding the mapping between nodes of the 2 ASTs
  - use this mapping to compute the sequence of edits
- this paper only focuses on the first step. For second step the authors refer
  us to [this work](http://ilpubs.stanford.edu:8090/115/1/1995-46.pdf)
- This is further split into 2 sub-steps
  - greedy top-down algo to find isomorphism in the sub trees - anchor mappings
  - bottom-up algo where 2 nodes match if their descendants include a large
    number of anchor mappings - container mapping. When 2 nodes match, apply an
    optimal algo to search for additional mappings (recovery mapping) among their
    descendants
- height of a node is 1 if it is a leaf node, else maximum height of all its
  children plus 1.
- top-down phase
  - uses data structure called height-indexed priority list. It is a sequence of
    nodes with decreasing height. Following are the ops supported
    - push - pushes a node onto the list
    - peekMax - returns the greatest height of the list
    - pop - returns and removes all nodes with height peekMax
    - open - pushes all children of a given node into the list
  - dice function - ratio of common descendants between 2 nodes
    - $$dice(t_1, t_2, M) = \frac{2 |t_1 \epsilon s(t_1)|}{|s(t_1)| + |s(t_2)|}$$
    - $$M$$ = mapping
    - $$s(t_*)$$ = set of descendants of $$t_*$$
- bottom-up phase
  - takes the output of the top-down phase as input
  - maps the remaining unmapped nodes from top-down phase
- the perf bottleneck of this approach is the parsing time to generate the ASTs
  - thus a "simple" difference tool like `diff` can be a lot faster than this!
  - however, such tools are limited to only line-level granularity
