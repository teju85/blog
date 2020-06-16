---
layout: post
title: "Single-pass Parallel Prefix Scan with Decoupled Look-back"
tags: tech-notes paper-notes cuda algorithms
---

### Single-pass Parallel Prefix Scan with Decoupled Look-back
Main paper can be found [here](https://research.nvidia.com/sites/default/files/pubs/2016-03_Single-pass-Parallel-Prefix/nvr-2016-002.pdf).

- requires only ~2n memory accesses
- achieves SOL on memory BW
- launch as many CTAs on the chip as the occupancy limits
- spread the work on these CTAs so as to cover the whole input array
- have each block compute upsweep phase of the prefix scan
- store the aggregate as well as inclusive prefix sum of these aggregates from preceding CTAs
- use a 3-valued ternary flag to indicate invalid/aggregate-done/prefix-done
- use this flag from preceding CTAs to compute the prefix-sum for this CTA to finish the task
