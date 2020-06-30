---
layout: post
title: "What's wrong with convnets"
tags: tech-notes machine-learning
---

### Summary
A talk given by Dr. Geoffrey Hinton listing all the shortcomings in the current
convolutional networks and then alluding to his work on Capsule nets. Recording
can be found [here](http://techtv.mit.edu/collections/bcs/videos/30698-what-s-wrong-with-convolutional-nets)

- our neural nets have very few structure (unlike our brain!)
  - neurons, layers, the whole net - that's it
- we are also lacking entities in these nets
  - one way to define entities is through a group of neurons
    - aka capsule
    - aka mini-column
    - one entity per capsule
- capsule? - a group of neurons that represents:
  - probability of presence of a multi-dimensional entity it has been designed
    to search for
  - and that entity's instantiation params
    - these could be pose of the object - location, orientation, velocity,
      deformation, etc
- these capsules are then connected to form multiple layers
- coincidence filtering
  - a capsule receives a batch of multi-dim vec's from capsules beneath it
  - looks for tightly coupled clusters in that batch
  - if found this outputs
    - a high probability that an entity of "its" type exists in the batch
    - the center of gravity of the cluster
  - because, at higher dims coincidences very rarely happen by chance
- he believes in convolutions, but not pooling. He provides 4 arguments:
- Point1: doesn't model the psychology of shape perception
  - humans use rectangular coordinate frames to perceive shapes.
  - probably even have hierarchy of such frames used for final perception
  - This plays a vital role in our perception!
  - convnets have no notion of this
  - Hinton demonstrated this using a 2-sliced tetrahedron experiment!
  - another demonstration was the use of mental rotation
    - eg: tilted 'R' letter and deciding correct handedness
  - relation between object and viewer represented by bunch of active neurons
- Point2: doesn't solve the right problem
  - convnets aim for invariance
    - it's ok, as it is guided by label being invariant to viewpoint
    - however its better to aim for equivariance
    - changes in viewpoint lead to corresponding changes in neural activities
  - place-coded equivariance - PCE
    - different capsule represents this object while its translating
    - eg: convnets without pooling (wrt translated images)
  - rate-coded equivariance - RCE
    - for very slight translations, the same capsule represents it
    - but, its instantiation params change
  - lower level PCE is translated into higher level RCE
    - at lower capsules
      - most of it is PCE
      - only small changes cause RCE
    - at higher capsules
      - most of it is RCE
      - only very large changes cause PCE
- Point3: fails to take advantage of linear manifold (eg: computer graphics)
  - eg: comp-graphics
    - it already represents objects in the rectangular coordinate frame
    - that manifold of object representation is globally linear.
    - convnets don't exploit this property!
    - they collect and train on data of objects under different "properties"
    - thus need a lot of data to train such models
  - approach of figuring out the manifold through objects' pose, location,
    translation, deformation, etc is much better compared to convnets
  - this means we'll also need very less data to train our models
  - basically, we should design our nets to perform inverse graphics!
    - literally the inverse of the process what graphics pipelines do
    - this then exploits the underlying linear manifold
    - obviously, applies only to computer vision problems
  - this approach of coincidence filtering is more similar to hough transform
- Point4: a primitive way to do routing
  - convnets handle this through pooling by picking the most active neuron
    - certainly a primitive way of doing routing!
  - much better approach
    - route the info in images to the neurons that can best make sense of it!
    - route info dynamically based on agreement provided by upper capsules
    - upper capsules will request more input from the lower ones which vote
      for its cluster. They will request less, otherwise.
- proof of concept (on mnist dataset)
  - pixel intensities to primary capsules
    - i/p -> conv layer patch -> logistic layer -> capsules
    - this is done for each patch in the i/p image
    - all patches, however, share the same weights (similar to conv layer)
  - 2nd layer
    - poses of each capsule from each patch vote for poses of each o/p class
    - these layers are linear (see the globally linear manifold argument)
    - to take translation into account, the first 2 pose params will get added
      by x,y coordinates of the patch
    - no. of transformation matrices = #types x #classes
  - how to detect agreements?
    - use a mixture of gaussians and uniform distributions
    - use EM to estimate mean/var of these gaussians
      - typically converges in few iterations, it seems
    - find a score that is the difference of log-prob of all samples under
      condition from mixture and condition from only uniform
    - apply softmax on these to do final prediction
  - our brain doesn't do such clustering to find agreements!
- his prediction is that if we can use unsupervised learning to come up with
  primary capsules, then we will much less data
  - aka "derendering stage"
  - this has to be highly non-linear
  - one idea is to use the autoencoder approach
    - decoder tries to reconstruct the image based on each of the capsules
    - encoder then tries to learn how to map pixel intensities to capsules!
- the output these primary capsules is concatenated into a single vector
  - then 'N' number of factor analyzers will be applied on these
  - we'll get a mixture of factor analyzers
