---
layout: post
title: "Large Graph Convolutional Network Training with GPU-Oriented Data Communication Architecture"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/2103.03330v1.pdf).

* zero-copy based, SM-initiated host-to-device copies of embeddings
* perform aligned reads and MPS (for resource provisioning) to maximize PCIe utilization

### Summary
- DMA-based host-to-device copies work only when the data is bulk. Embeddings in
  GNN's do not yield well to DMA-based copies. Thus, have SM's on GPU's issue
  host-to-device from zero-copy buffers
- even while doing zero-copy from the GPU's care needs to be taken in order to coalesce
  and also make sure that the number of PCIe requests are minimized. (Because each PCIe
  packet has 12-16B header overhead)
- need to also fully utilize the PCIe links by issuing as many such requests as
  possible. On PCIe3 number of such outstanding requests is 256 and 768 on PCIe4.
- So, to reduce the number of PCIe requests due to misaligned addresses, a circular
  shift is applied to all threads and warps.
- As expected, this circular shift is not necessary if the embedding size is less
  than the GPU cacheline size or it is already 128B aligned.
- We also need to make sure that the computation kernels are running alongside of
  this zero-copy kernel in order to maximize GPU utilization.
- But this is not guaranteed when there are blocking CUDA API calls like
  `cudaMalloc`, `cudaFree`, etc.
- So, the solution is to use MPS to provision the amount of SM's to be dedicated
  for the purpose of zero-copy. Thus, there'll be atleast 2 processes: one for
  zero-copy and the other for compute and CUDA IPC will be used to share the
  buffer addresses between these.
- The sample -> gather -> compute flow is pipelined (using ping-pong buffers) to
  maximize overlap of these phases.
- For multi-GPU training, this whole setup is duplicated across every GPU by just
  relying on DGL's data-parallel approach. The catch though is that unified memory
  in CUDA is not shareable across processes! So, they first create a host shared
  memory region and then call `cudaHostRegister` on this buffer inside each
  process for each of the GPU in the current node.
- They note that atleast on RTX-3090, SM split of 15:85 between zero-copy and the
  actual training kernels is good enough to saturate PCIe bandwidth.
- However they also note that a 10:90 split didn't show any noticeable change in
  the overall end-to-time minibatch time
