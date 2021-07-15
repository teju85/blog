---
layout: post
title: "Hash displace and compress"
tags: tech-notes paper-notes algorithms hash-tables
---

### Hash displace and compress
Main paper can be found [here](http://cmph.sourceforge.net/papers/esa09.pdf).

- CHD algorithm for generating perfect hash functions
- input is a set of 'n' keys, to be mapped to a space of 'm' numbers
- 2-level hashing approach
  - first hash puts all input keys into 'r' buckets
  - then there'll be multiple random hash functions
  - out of which, one will be allocated to a given bucket
- 2 parameters controlling the behavior
  - lambda - number of keys per bucket (r = ceil(n / lambda))
  - alpha - table load factor (m = ceil(n / alpha)
- in practice, heuristic hash functions proposed by Jenkins in
  "Algorithm Alley: Hash functions" Dr.Dobbs article is being used
- also supports k-perfect hash functions (but not my interest currently!)
