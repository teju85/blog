---
layout: post
title: "GraphCast: Learning skillful medium-range global weather forecasting"
needmath: true
tags: tech-notes paper-notes graph gnn
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/2212.12794.pdf).

* ML based weather simulator
* compares against HRES from ECMWF
* 10-day forecasts at 6-hour intervals, in under 60s on a TPUv4
* autoregressive model
* uses GNN as its underlying model (in an encode-process-decode config), with a
  form of multi-mesh-graph of the earth

### Summary

- ECMWF has 2 parts: data assimilation and forecasting (HRES and ENS). This
  paper focuses on using ML-based techniques for the latter part.
- HRES generates 0.1 degree resolution 10-day forecasts whereas this paper limits
  itself to 0.25 degrees.
- NWP (Numerical Weather Prediction) methods scale well with compute, whereas
  ML based methods scale well with increasing amount of data.
- Dataset is ERA5 from ECMWF
- looks at 37 different vertical pressure levels (instead of altitude)
- target variables
  - 5 surface variables
  - 6 atmospheric variables at 37 different vertical pressure levels
  - total of $$5 + (37 x 6) = 227$$ variables
- at any given point in time, these variables could change over the 1038240
  locations of the grid of the earth
  - $$(\frac{180}{0.25} + 1) (\frac{360}{0.25})$$
- thus, there are a total of $$1038240 x 227 = 235680480$$ inputs
- internally, however, these locations are represented with a multi-mesh structure
  which has homogeneous spatial resolution over the globe in the form of icosahedrons
  - this enables long-range interactions with just a few message-passing steps
  - in here, coarse mesh nodes are a subset of finer mesh nodes
- dataset split
  - training - 1979-2015
  - validation - 2016-2017
  - test - 2018
- weather prediction strategy
  - $$X'^{t+1} = GraphCast(X^t, X^{t-1})$$
  - for predicting multiple steps ahead in the future, this equation is iteratively
    applied in an autoregressive fashion
- encoder
  - maps the input data into the learned features on the multi-mesh
  - uses a GNN arch
  - assumes directed edges from the grid points to the multi-mesh nodes
- processor
  - 16-layer deep GNN to perform message passing on the multi-mesh
- decoder
  - reversal of encoder
  - only predicts the change in the next timestep (NOT the value itself)
- training
  - minizing objective function over 12 timesteps (= 3 days) against ERA5
  - gradient is computed by backprop through the entire autoregressive sequence
  - can potentially be retrained/finetuned regularly based on recent weather data
  - training took 3 weeks on 32x TPUv4, data parallel, gradient-checkpointing
    and using low-precision arithmetic
