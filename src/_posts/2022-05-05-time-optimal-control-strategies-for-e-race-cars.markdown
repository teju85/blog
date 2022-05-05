---
layout: post
title: "Time-optimal Control Strategies for Electric Race Cars with Different Transmission Technologies"
needmath: true
tags: tech-notes paper-notes optimization
---

### Proposal
Main paper can be found [here](https://arxiv.org/pdf/2005.07592v1.pdf).

* a convex model of battery and transmission system for electric race cars
* support for modelling single gear ratio (SR) and CVT types of transmissions
* a computationally efficient optimization framework for energy management

### Summary
- authors model the vehicle dynamics, transmission, electric motor and battery
  pack via classical mechanics and control systems
- the optimization problem is posed as minimizing the laptime, iteratively
- optimization solver used is ECOS. They run this iterative optimizer 3 times in
  order to achieve robustness.
- (ECOS is a second order cone programming solver)
- discretization along the track is done with a $$\Delta s$$ of 10m.
- on a mid-range Intel CPU, they achieve an overall runtime of 1min
