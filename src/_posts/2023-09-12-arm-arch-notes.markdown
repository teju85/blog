---
layout: post
title: "ARM Architecture notes"
tags: architecture arm
---


## Introduction
Collection of some ARM architecture related information which could come in handy.
This is mostly going to be a live-document. As and when I continue to find new
information, I'll be updating this page (mostly for my perusal in the future).

## Random tidbits
- NVIDIA Grace GPU is Neoverse V2 based (code named Demeter). Implements ARMv9.0-A ISA.
- AWS Gravitron3 is Neoverse V1 based (code named Zeus). Implements ARMv8.4-A and ARMv8.6-A ISA's.
- Ampere Altra is Neoverse N1 based.
- Neoverse V3 is code named Poseidon
- Neoverse V2 is based off of Cortex X3.

## Nomenclature
- *Neoverse* - 64b ARM processor cores
- *Neoverse V series* - for HPC
- *Neoverse N series* - for datacenter
- *Neoverse E series* - for edge computing
- *BTB* - Branch Target Buffer
- *Rename* - ??
- *IQ* - Issue Queue
- *SX* - ??
- *MX* - ??
- *VX* - ??
- *SB* - Store Buffer
- *SA* - Set Associative
- *TQ* - Transaction Queue (to queue L2$ misses)
- *SLC* - System Level Cache

## Architecture
### Neoverse V2 Core arch
- frontend
  - eight-wide OOO core
  - much deeper branch predictor, hiding L1-I$ miss latency (ideal for super branchy codes)
  - BTB capacity of 12K entries. It is 2-level.
  - 2 predicted branches per cycle
  - L1-I$ - 64kB 4-way SA
  - Frontend does 8uops and 6insts per cycle
- decode
  - Decoder width is 6 insts (in order to match that of Frontend's output). Generates 8-wide uops as output
- backend
  - few of the reg-reg and imm mov ops execute with zero latency
  - more instruction fusion (CMP + CSEL/CSET)
  - Vector and FP instructions go to the VX schedulers (dual-ported)
- load/store
  - 2 load/store pipes and 1 load pipe (=> 3 mem ops per cycle)
  - 48 entry TLB
- Memory subsystem
  - 2MB L2$ (8-way SA), 4 independent banks
  - 64B read or write per 2 cycles per bank to L1$ (10 cycles load to use latency)
  - L2$ also caches L1-I$ (i.e. instruction coherency)
  - L2$ to next level cache is via AMBA CHI with 32B uni-directional bandwidth
- A V2 core consists of ALUs, L1$ and L2$. They are connected with each other using CMN-700 mesh interconnect
- maximum possible mesh size is 12x12 (most likely to hit reticle limit)
- CMN-700 also maintains coherency via snoop filters

## References
1. https://en.wikipedia.org/wiki/ARM_Neoverse
2. https://chipsandcheese.com/2023/09/11/hot-chips-2023-arms-neoverse-v2/
