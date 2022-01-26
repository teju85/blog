---
layout: post
title: "In-memory interval join"
needmath: true
tags: tech-notes paper-notes
---

### Proposal
This is my summary of the in-memory interval join paper which can be found
[here](https://link.springer.com/content/pdf/10.1007/s00778-020-00639-0.pdf).

- improve perf of single threaded interval joins, without having to use any
  special data structures (unlike EBI method)
- parallelize this approach with the help of a novel domain-based data
  partitioning technique

#### Summary
- instead of going with the plane-sweep method based Endpoint Based Interval
  join (EBI) algorithm (which requires a special gapless hash map) for doing
  interval joins, they propose to use a forward-scan (FS) based approach.
- FS uses sweeps in the order of start points, whereas the above mentioned PS
  based method does sweeps on the sorted end points.
- Overall complexity is $$O(R + S + R \Join S)$$
  - $$R$$ = number of ranges in set R
  - $$S$$ = number of ranges in set S
  - $$R \Join S$$ = number of resulting ranges in the set after joining R and S
- EBI (Endpoint Based Interval join)
  - sort the ranges based on their values first and then by them being start or
    end values for the range
  - then perform a sweep based on the range value and continue to collect the
    intersecting ranges
  - along with lazy evaluation (collect multiple consecutive active ranges from
    one set and then do a single scan on the opposite set of active ranges) this
    approach also beats PS
- PS (Plane Sweep)
  - sort based on the start interval of R, S sets
  - sweep a line through every start point and collect all intersecting ranges
    from the other set
- Optimizations to FS
  - in the above complexity, the first two terms can't be reduced, however the
    third item can be
  - grouping
    - FS compares every interval from one set with every other in the active set
    - this optimization basically eliminates these comparisons as if the ranges
      are in the active set, they must anyways overlap
    - while implementing, just copying the groups into another buffer was faster
      due to less cache misses
  - bucket indexing
    - further reduces the comparisons by splitting the x-axis into equal sized
      buckets.
    - All bucket indices until the one containing the end range doesn't require
      any comparisons with the ranges from the other set that fall into these
      buckets
    - while implementing, bucket indices are not materialized
  - enhanced loop unrolling
    - unroll the inner scan loop and also do the range comparison only once per
      unrolled iteration. Only when the comparison fails, all the unrolled cases
      in the current iteration are compared.
    - this further reduces the comparisons required
  - decomposed data layout
    - store the structures in SoA format, thereby improving cache access patterns
- optFS
  - also propose a self-tuning version of the algo that initially samples the
    input data and then tries to estimate the cost of a forward scan.
  - if the FS covers only a few tens to a hundred ranges, then it is just enough
    to run unrolled FS, else it enables all 4 of the above optimizations
- parallelization
  - no-partioning
    - means data is not partitioned but stored in shared main memory and all the
      threads traverse the data in this memory region simultaneously
    - they design a master-slave approach for this
    - master thread advances the sweep line
    - for each "stoppage" of the sweep line, it assigns the next available thread
      for finding the joins
  - hash-based partitioning
    - partition each range (based on the hash value)
    - for all partition pairs between first and second sets perform the join
    - rule-of-thumb is to set $$k = \sqrt nc$$ where $$nc$$ is the number of
      cores on which to parallelize
  - domain-based partioning
    - each set is divided into 'k' non-overlapping regions
    - every range that is inside a region will be assigned that region, so there
      could be a range that belongs to multiple regions!
    - rule-of-thumb is to set $$k = nc$$ where $$nc$$ is the number of cores on
      which to parallelize
    - this requires quadratically fewer joins that hash-based partition method
    - we'll however need to de-duplicate the join results
    - they also propose various load balancing techniques
