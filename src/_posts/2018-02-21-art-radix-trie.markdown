---
layout: post
title: "ART radix trie"
tags: tech-notes paper-notes algorithms hash-tables
---

### ART radix trie
Main paper can be found [here](https://db.in.tum.de/~leis/papers/ART.pdf) and
its condensed version is in [this blog](https://www.the-paper-trail.org/post/art-paper-notes/).

- create a sort of 'union' struct with different nodes
- they support a different struct for upto 4, 16, 48, 256 children per nodes
  - Node4: one can do a brute search on its contents
  - Node16: sort its children and do binary search
  - Node48: store the children indexed with a 256 element array itself
  - Node256: the usual radix trie
- these data structures help improve L1 cache locality
- they have a paper on parallel ART: https://db.in.tum.de/~leis/papers/artsync.pdf
