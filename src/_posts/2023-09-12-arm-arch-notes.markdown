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
- Aarch64 (64b arch version) of ARM cpu's were introduced in Armv8-A.
  - Execution state - 64b GPR's, 64b PC, SP (for each implemented exception level), ELR
- NVIDIA Grace GPU is Neoverse V2 based (code named Demeter). Implements ARMv9.0-A ISA.
- AWS Gravitron3 is Neoverse V1 based (code named Zeus). Implements ARMv8.4-A and ARMv8.6-A ISA's.
- Ampere Altra is Neoverse N1 based.
- Neoverse V3 is code named Poseidon
- Neoverse V2 is based off of Cortex X3.
- V series typically are in the 80-350W TDP range.
- Armv9.0A extends the architecture from Armv8.0-A till Armv8.6-A.

## Nomenclature
- *Neoverse* - 64b ARM processor cores
  - *V series* - HPC
  - *N series* - datacenter
  - *E series* - edge computing
- *AMBA* - Advanced Microcontroller Bus Architecture. Family of protocols for SoC interconnect.
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
- *SP* - Stack Pointer
- *ELR* - Exception Link Register
- *PC* - Program Counter
- *GPR* - General Purpose Register
- *Neon* - SIMD processing using dedicated SIMD and floating-point register banks. 128b, 64b,
  32b, 16b, 8b register accesses are possible.
- *PSR* - Program Status Register. Holds PSTATE info
- *PSTATE* - Abstraction of the process state
- *SPSR* - Saved PSR. Copy of current PSR of the cores saved by HW during an exception
- *MPKI* - Misses Per Kilo Instructions
- *PTW* - Page Table Walker
- *Core* - that which contains ALU, FP, L1, L2 units
- *Uncore* - rest of the units L3, memory controller, PCIe root complex, etc
- Profiles
  - A-Profile - Application - for HPC segment
  - R-Profile - Real-Time - for workloads with realtime requirements
  - M-Profile - Microcontroller - for power-efficient devices
- *BSA* - Base System Architecture - HW system arch that system SW can rely on.
  IOW, things that an OS needs like interrupt controllers, timers, etc.
- *SVE* - Scalable Vector Instructions, for SIMD execution.

## Architecture (Neoverse V2)
### Overview
- aarch64 execution state across all EL0-EL3
- supports BF16/INT8 formats as well
- instruction execution pipeline overview
  - instruction fetch
  - decode into macro-ops (MOP)
  - register renaming and dispatch
  - MOPs split into upto 2 micro-ops (uOP)
  - uOPs wait for their operands
  - finally, OOO issue to one of 17 issue pipelines 
  - each issue pipeline can take one uOP per cycle

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
3. https://developer.arm.com/documentation/105565/latest/
4. https://developer.arm.com/documentation/PJDOC-466751330-593177/latest/
