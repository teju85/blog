---
layout: post
title: "Can the brain do back-propagation"
tags: tech-notes machine-learning
---

### Summary
A Stanford Seminar given by Dr. Geoffrey Hinton. The recording of the talk can
be found [here](https://www.youtube.com/watch?v=VIRCybGgHts)
- neuro scientists think that its not possible because
  - there's no obvious supervision signal to brain
  - cortical neurons do not communicate real-valued activities (its just spikes)
  - the neuron will have to send 2 different signals, one during forward and another
    during backward pass
  - there's no symmetric reciprocal path between 2 neurons
- objection no.1: no supervision signal
  - we already have many generative models for this purpose
  - VAEs, GANs, etc...
- objection no.2: communication of real values
  - statisticians have told us to use more data than the number of parameters
  - but its always better to have bigger models than the data
    - or do NOT make your model small, so as to make data look big
    - because bigger models themselves are a great regularizers
  - dropout
    - nice way to share weights across model-ensembles!
    - thus a very good regularizer of your network
    - and during inference, it approximately evaluates the geometric mean across
      all of these models
  - so one could send spikes using a poisson process and its better than dropout
    since it makes use of all the synapses in our brain!?
- objection no.3: different signals in each pass
  - STDP - Spike Time Dependent Plasticity
    - we can use the spike rate to represent rate of change of its output
    - he showed how to use stacked AEs for this purpose
    - use temporal derivatives during a regression as gradients done during backprop
- objection no.4: no symmetric reciprocal path
  - researchers showed that backprop still works well even when using random
    top-down connections, the bottom-up connections would get adjusted accordingly!
  - but this approach is about 2 times slower than the normal backprop
