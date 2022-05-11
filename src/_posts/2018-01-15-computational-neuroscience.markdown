---
layout: post
title: "Computational Neuroscience Coursera notes"
needmath: true
tags: course-notes
---

My notes while taking the Computational Neuroscience course.


## Week1 - Models
- description models of the brain (DM)
- mechanistic models of brain cells and networks (MM)
- interpretive (or normative) models of brain (IM)

### what is computational neuroscience?
- to explain in computational terms how brains generate behaviors
- it provides tools and methods for characterizing what nervous systems do,
  determining how they function, and understanding why operate in particular ways
  - DM's explain the 'what' part
  - MM's explain the 'how' part
  - IM's explain the 'why' part

### receptive fields (RFs)
- specific properties of a sensory stimulus that generate a strong response from the cell
- can describe all 3 types of models to these

### DM of RFs
- center-surround RFs in the retina
  - on-center off-surround RF (center = a small patch of retina associated with the cell)
  - off-center on-surround RF
- RFs can be thought of as filters giving peak response to certain types of inputs!
- primary visual cortex = V1
- cortical RFs - ex: oriented RFs
  - these oriented RFs are obtained from center-surround RFs
  - can be explained using MM

### MM of RFs
- visual processing circuitry
  - retina -> LGN -> V1
  - LGN RF = center-surround
  - V1 RF = oriented RF
  - LGN = Lateral Geniculate Nucleus
  - a number of LGN cells give input to a V1 cell
- to get oriented RFs from center-surround, LGN cells are displaced along the preferred orientation of V1!
- but this doesn't take into account recurrent connection from other V1 cells

### IM of RFs
- efficient coding hypothesis (EC)
  - goal is to represent images as faithfully and efficiently as possible using neurons with $$RF_i$$
  - I = image, I' = reconstructed image, $$r_i$$ = neural responses
  - I' = $$\sum_i (RF_i * r_i)$$
  - what are the $$RF_i$$ that minimize $$\|I-I'\|^2$$ and are as independent as possible?
- start out with random $$RF_i$$ and run your EC algo on natural image patches
  - sparse coding
  - PCA (ICA - Independent Component Analysis)
  - predictive coding
- conclusion: brain may be trying to find faithful & efficient representations of an animal's natural environment

### Neurobiology 101
- Neuron = the brain cell (about 25um) - made up of cell-body, axon and dendrites
- neuron doctrine
  - neuron is the fundamental structural & functional unit of brain
  - they are discrete cells & not continuous with others
  - information flows from dendrites to the axon via the cell-body
- idealized neuron
  - inputs through dendrites (Axons from other cells)
  - cell-body (with a nucleus) at the center of dendrites
  - from cell-body axons connect to presynaptic terminals (outputs)
  - axons are covered by myelin
  - at places where there is no myelin = node of ranvier
- input to neuron from other axons = EPSP = Excitatory Post-Synaptic Potential
- if these inputs from other neurons exceed the threshold level, the current neuron fires an output spike
  - output spike = action potential

#### what is a neuron?
- leaky bag of charged liquid!
  - bag because contents of neuron are enclosed within a cell membrane
  - cell membrane is a lipid bilayer
    - bilayer is impermeable to charged ion species such as Na+, Cl-, K+
    - ionic channels embedded in membrane allow ions in and out

#### electrical properties of neuron
- each neuron maintains a potential difference across its membrane
- inside is about -70mV relative to outside
- this is the resting potential of neuron
- this is because of higher concentration of certain ions in the outside compared to inside
- more Na+, Cl- on outside
- more K+, organic ions [A-] inside
- an ionic pump maintains this potential by actively maintaining this concentration difference

#### ionic channels
- these are made of proteins
- and only allow certain ions to pass through them
- these channels are gated
  - voltage-gated = probability of opening depends on membrane voltage
  - chemically-gated = binding to a chemical causes channel to open (ex: synapses)
  - mechanically-gated = sensitive to pressure/stretch

#### neuronal signalling
- these gated channels allow neuronal signalling
- synapse = junctions between neurons
- inputs from other neurons
  -> synapses opening
  -> change in local membrane potential
  -> opening/closing of voltage-gated channels in dendrites/body/axon
  -> causes depolarization/hyperpolarization
  -> strong polarization results in a spike (action potential)
- depolarization = excess +ve voltage
- hyperpolarization = excess -ve voltage
- action potential flow
  - start  -> Na+ channel open -> more Na+ open    -> Na+ close -> K+ open -> K+ close -> end
  - rest. pote. -> +ve V raise -> more +ve V raise -> peak      -> V drop  -> V drop   -> resting potential
- this spike is then propagated through the axon
- myelin due to oligodendrocytes (glial cells) wrap axons
  - enable fast long range spike communication!
  - these are non-conductors of electricity
  - spike hops from one node of ranvier to the next (saltatory conduction)
  - this 'active wiring' allows lossless signal propagation!

#### synapses
- junction/connection bet. 2 neurons. 2 types:
  - electrical - uses gap junctions
    - these are fast and are used for synchronizing the firing of neurons
  - chemical - uses neurotransmitters
    - one can control the effect of spike from adjacent neuron by reducing the number of receptors in the current neuron
    - these are used in memory and learning
- excitatory synapse - increase postsynaptic membrane potential
  - input spike
    -> neurotransmitter release
    -> binds to ion channel receptors
    -> ion channels open
    -> Na+ influx
    -> depolarization due to excitatory postsynaptic potential (EPSP)
- inhibitory synapse - decrease postsynaptic membrane potential
  - input spike
    -> neurotransmitter release
    -> binds to ion channel receptors
    -> ion channels open
    -> K+ leaves cell
    -> hyperpolarization due to inhibitory postsynaptic potential (IPSP)
- synapse doctrine = synapses are the basis for memory and learning
- synapse learning happens through a mechanism called synaptic plasticity (SP)
  - hebbian plasticity
    - if neuron A repeatedly takes part in firing neuron B, then their synapse should be strengthened
    - neurons that fire together, wire together
    - proof: Long Term Potentiation: LTP
    - experimentally observed increase in synaptic strength that lasts for hours/days
    - Long Term Depression: LTD
    - experimentally observed decrease in synaptic strength that lasts for hours/days
  - SP depends on relative timing of input & output spikes!
    - i/p spike before o/p spike => LTP
    - i/p spike after o/p spike => LTD

#### nervous system (NS)
- nerves = bundle of axons
- Peripheral NS - PNS
  - somatic - nerves connecting to voluntary skeletal muscles and sensory receptors
    - afferent nerve fibers - incoming - axons that carry info away from PNS to CNS
    - efferent nerve fibers - outgoing - axons that carry info from CNS to PNS
  - autonomic - nerves connecting heart, blood vessels, glands, etc.
- Central NS - CNS
  - consists of spinal cord + brain
  - spinal cord
    - local feedback loops control reflexes (reflex arcs)
    - descending motor control signals from brain activate spinal motor neurons
    - ascending sensory axons convey sensory info from muscles/skin back to brain
  - brain
    - hindbrain
      - medulla oblangata - controls breathing, muscle tone, blood pressure
      - pons - connected to cerebellum, sleep and arousal
      - cerebellum - coordination & timing of voluntary movements, sense of equilibrium, language, attention etc.
    - midbrain - eye movements, visual and auditory reflexes
    - reticular formation - modulates muscle reflexes, breathing & pain perception. Regulates sleep, wakefulness & arousal
    - thalamus - relay station for all sensory info (except smell). regulates sleep and wakefulness
    - hypothalamus - regulates basic needs: fighting, flighting, feeding & mating
    - Cerebrum - perception, motor control, memory, emotion, learning
      - cerebral cortex - convoluted surface of cerebrum. layered sheet of neurons
        - large number of neurons + synapses
        - huge amount of connections!
        - 6 layers of neurons
        - relatively uniform in structure across the brain
      - basal ganglia
      - hippocampus
      - amygdala

## Week2 - Neural Code
### recording from the brain
- fMRI - function Magnetic Resonance Imaging
- EEG - Electro EncephaloGraphy
- Electrode Arrays - invasive, but can read from individual neurons
- calcium imaging
- patch electrodes - to look inside the cells
- people also generate raster plots to look at neural activity

### encoding - how does a stimulus cause a pattern of responses
- building quasi mechanistic models of our neural systems
- $$P(response\|stimulus)$$ = encoding
- typically neural response = avg. firing rate or prob. of generating a spike

### decoding - what do these responses tell about the stimulus
- how to reconstruct what the brain is doing
- helps in neuro-prosthetics
- $$P(stimulus\|response)$$ = decoding

### tuning curves
- example: gaussian tuning curve
- neural firing frequency over the orientation of the bar

### brain seems to construct complex features from a set of lower level features
- this forms basis of deep learning models!
- however, in brain, these lower level neurons also get feedback from higher ones!

### construction of response models
- $$P(response\|stimulus)$$ = encoding
- r(t) = firing rate and its dependency on stimulus
- response = spike produced by a single neuron
- linear temporal filter: $$r(t) = \sum_k s_{t-k}*f_k$$
  - similar to FIR filter in DSP!
  - or a convolution filter
- leaky avarage (or integrator) - moving window average with weights decreasing exponentially on the past samples
- linear spatial filter: $$r(x,y) = \sum_{x',y'} s_{x-x',y-y'}*f_{x',y'}$$
- similar logic applies to spatio-temporal filtering too
  - like a 3D convolution
- another approach could be to apply a non-linear function on the convolved output
  - $$r(t) = g(\sum_k s_{t-k}*f_k)$$
  - g = non-linear function, eg: sigmoid

### learning model from data
#### feature selection
- sample (N times) the stimulus in a window to get N-dimensional vector
- collect only those samples whose right-end-window generates a spike
- take average of all such samples = spike-triggered average (STA)
  - it will be a vector in the N-dim space
  - this can also be applied to images
- now to apply linear filtering using STA
  - make this STA vector as the 'f' and apply convolution with the input!
  - equivalent to vector dot product or projection

#### determining the nonlinear function
- this nonlinear function (or input/output function) is basically P(spike|stimulus)
- can be found from data using Baye's rule
- to extend this to multiple features, think of creating a multi-feature probability distribution

### Kullback-Leibler divergence
- D_KL(P(s),Q(s)) = \Sigma_s P(s) * log_2(P(s)/Q(s))
- measure of difference between 2 probability distributions
- choose filter in order to maximize D_KL between spike-conditional and prior distributions
- similar to maximizing mutual info between them!

### neuron spike rate modelling
- can use binomial distribution
- in the limit of number of bins to inf, this distribution becomes poisson!
- assuming each firing is independent of another, time interval between 2 adjacent spikes becomes exp. distribution
- for higher rates, poisson looks more gaussian
- fano factor = variance / mean
- Generalized Linear Model
  - input -> stimulus filter, post-spike filter
    -> non-linearity
    -> stochastic spike generator
    -> post-spike filter

## Week3
### decoding
- how well can we learn the stimulus given its neural responses
- example: determining a threshold for classifying positive and negative samples, given their distribution
  - basically putting a threshold on the likelihood ratio
  - P(r|-) / P(r|+)  > thresh
- Neyman-Pearson lemma
  - likelihood ratio test is the most efficient statistic in that it has the most power for a given size
- assuming we don't have to decide immediately to the stimulus
  - keep accumulating the log of the likelihood ratio over time
  - define 2 threshold bars, one for positive and another for negative class
  - whenever the cumulative sum of this ratio reaches one of these bars, stop accumulating
  - declare the output as that class
- we should also be taking into account the role of priors for each of these classes!
  - makes sense for cases where these classes are not equally distributed
- should also be adding the cost of false-negatives and false-positives!

### population coding and bayesian estimation
- population codes = decoding from many neurons
- cricket neurons are sensitive to wind
  - $$\frac{f(s)}{r_{max}} = cos(s - s_a)$$
  - $$s_a$$ = preferred angle for the neuron where the firing rate is maximum
  - $$r_{max}$$ = max firing rate, used to normalize the output
  - can also be written as dot product of vectors:
    - $$\frac{f(s)}{r_{max}} = v . c_a$$
    - $$c_a$$ = preffered direction of wind for the neuron's maximum firing rate
  - summing up across all neurons gives rise to population vector
- however, population vector is neither general nor optimal!?
- Baye's law
  - $$p(s\|r) = p(r\|s) * \frac{p(s)}{p(r)}$$
  - $$p(r\|s)$$ = likelihood function, conditional distribution
  - $$p(s)$$ = prior distribution
  - $$p(r)$$ = marginal distribution
  - $$p(s\|r)$$ = aposteriori distribution
- assume gaussian distribution for stimulus and poisson for response
- also assume firing rate of each neuron is independent of another
- with this, one can generate likelihood distribution for response given stimulus
  - solve this to get maximum log likelihood
- with this, one can also generate aposteriori distribution for stimulus given response
  - solve this to get maximum log aposteriori
- but these approaches do not take into account the correlations in the population

### stimulus reconstruction: (reading minds)
- to create an estimator: s_bayes
- use least squared error wrt s_bayes and s (true stimulus)

### Guest Lecture Fred Reike
- extracting sparse signals from noise
- appears similar to logistic classifier!
- Priors matter while trying to extract sparse signals from noise!
- basically try to put the threshold based on aposteriori probability

## Week4
### information and entropy
- probability of seeing an event = P(1) = p, thus P(0) = 1 - p
  - information(P(1)) = $$-log_2(p)$$
  - information(P(0)) = $$-log_2(1-p)$$
- Entropy = avg. information = $$-\Sigma_i(p_i * log_2(p_i))$$
  - units are bits
- mutual information
  - amount of entropy that is used in coding the stimulus
  - MI(S,R) = TotalEntropy - AvgNoiseEntropy
  - $$MI(S,R) = -\Sigma_r(p(r) * log_2(p(r))) + \Sigma_s(p(s) * \Sigma_r(p(r\|s) * log_2(p(r\|s))))$$
- Quantifying how independent R and S are:
  - $$I(S,R) = D_{KL}(P(S,R), P(S)P(R))$$
  - using this, one can derive with the MI equation above!
  - MI is symmetric between S and R!

### calculating info in spike trains
- information in spike patterns
  - each time, if there's spike assign a binary 1, else 0
  - create binary words ($$w_i$$) of fixed bits out of this resulting bit-vector
  - compute $$p(w_i)$$, then use entropy equation on it
  - calculate the diff between total variability driven by stimuli and that due to noise, averaged over stimuli
- information in single spike
  - repeat similar such analysis but with words of one bit!
### information and coding efficiency
- natural stimuli:
  - typically have huge dynamic range
  - follows power-law scaling
  - have structure at many scales
- to have maximum output entropy, a good encoder should match its o/p's to the distribution of its i/p's
  - this also optimizes mutual info between i/p and o/p
  - and as one changes the characteristics of i/p, changes can occur in the i/p -> o/p function and in the encoded feature!
- redundancy reduction
  - $$entropy(R_1,R_2) <= entropy(R_1) + entropy(R_2)$$
  - $$R_1$$ and $$R_2$$ are responses of 2 neurons
  - in order to be efficient in terms of entropy and coding, neurons must be independent
- But neurons are observed to be redundant
  - error correction
  - robust coding
  - helps in discrimination

## Week5
### modeling neurons
- membrane can be thought of as a capacitor and resistor in parallel
  - thus, using kirchoff's law:
  - $$C \frac{dV}{dt} = -\frac{V}{R} + I_{ext}$$
- but membrane also has potential due to ionic equilibrium (called nernst potential)
  - $$E = k_B * \frac{T}{z * q} * ln(\frac{inside}{outside})$$
    - $$k_B$$ = boltzmann constant
    - inside, outside = ionic concentration
    - $$T$$ = temperature
    - $$z$$ = number of charges in the ion
    - $$q$$ = ionic charge
  - thus, part of voltage drop across resistor will be due to this potential
  - $$C \frac{dV}{dt} = -\frac{V - V_rest}{R} + I_{ext}$$
  - solution to this is the classic exponential decay RC circuit!
- conductance = $$resistance^{-1}$$
- different ion channels have associated conductances
  - given conductance tends to move the membrane potential toward the equilibrium potential for that ion

### spikes (what makes a neuron compute)
- excitability arises from ion channel nonlinearity
- the conductances of these channels depend on the voltage difference!
- hodgkin huxley equation describes the movement of Na/K ions through the membrane

### simplified model neurons
- motor neurons typically fire in regular intervals
- integrate-and-fire neuron model
  - pretty close to real neuronal spikes
  - $$V_0$$ = stability potential
  - $$V_{reset}$$ = reset potential immediately after the spike
  - $$V_{th}$$ = threshold potential after which spike occurs
  - $$V_{max}$$ = max spike potential
- to make the above model fire intrinsically
  - add a non-linearity after the linear region
    - quadratic or exponential
    - remaining else same as before
- another model is theta neuron
  - to model periodically firing neurons
- for 2-dimensional models, using nullclines, one can determine the stable point

### forest of dendrites
- neurons have complicated spatial structures
- voltage decays with distance in passive membranes
- this is modelled use cable theory (or cable equation)
- rall model for passive dendrites

### Guest Lecture Eric Shea Brown
- correlations and synchrony in neural populations
- tuning curve = plot of firing rate against the stimulus
- pairwise correlation
  - count number of spikes in a moving window for 2 neurons
  - $$\rho = \frac{cov(n_1,n_2)}{\sqrt{var(n_1)*var(n_2)}}$$
- correlation can degrade the signal encoding
  - it becomes hard to distinguish between the responses for different stimuli
  - since there will be more overlap of responses
- more number of neurons we have, the better the SNR is (mean:std ratio)
  - if they are all statistically independent, the SNR just keeps growing
  - however, if there's some correlation between them, the SNR saturates after certain number of neurons!
  - more the correlation, the lesser the value at which SNR saturates
- but in other cases of negative correlation, it can enhance the signal encoding too!
- thus, information increases in heterogeneous populations
- information decreases in homogeneous populations

## Week6
### modeling synapses and network of connected neurons
- chemical synapses are the most common ones found in the brain
- modeling a synapse is through an RC circuit
- modeling synapse inputs to a post-synaptic neuron is again through another channel of conductance
  - this synaptic conductance however changes based on the spikes ariving in the pre-synaptic neuron
- simple model of 2 neurons connected to each other
  - both are excitatory = alternate firing
  - both are inhibitory = synchrony!

### network models
- modelling based on spiking neurons
  - computationally expensive
  - can model synchrony between neurons
- modelling based on firing rate
  - more efficient representation and modelling large networks
  - no spike timing issues
- spiking neuron model = linear filter model on the firing rate model!
  - we can do so only when the neurons are not correlated to each other
  - spike train \rho_b(t) can be replaced with firing rate u_b(t)
- total synaptic current to the neuron input is summation of weighted inputs from all its synapses
- firing rate based model
  - output firing rate changes like this
    - $$\tau_r \frac{dv}{dt} = -v + F(I_s(t))$$
  - input synaptic current changes like this
    - $$\tau_s \frac{dI_s}{dt} = -I_s + w.u$$
  - the steady state function is the same as used in ANNs!
  - recurrent networks
    - $$\tau \frac{dv}{dt} = -v + F(Wu + Mv)$$
    - M = weight matrix for recurrent connections
    - W = weight matrix for feedforward connections

### recurrent networks
- linear recurrent network with symmetric M
  - will give orthogonal eigen vectors
  - thus we can write output to be linear combination of these eigen vectors
  - $$v(t) = \Sigma_i c_i(t)e_i$$
  - then we can solve for each of these $$c_i$$ to finally solve for v(t)
  - the eigen values determine the network stability
  - it can amplify its inputs!
  - it can also manifest memory!
- non-linear recurrent networks with symmetric M
  - these can also amplify its inputs!
  - even if eigen value is greater than 1, it can be stable, due to rectifier non-linearity!
    - this would have caused instability in case of linear recurrent networks
  - can also perform 'selective attention'!
    - performs 'winner-takes-all' input selection
  - can perform gain modulation
  - can also maintain memory
- non-linear recurrent networks with non-symmetric M

## Week7
### synaptic plasticity and learning
- long term potentiation (LTP)
  - one type of plasticity
  - experimentally observed increase in synaptic strength that lasts for hours or days
- long term depression (LTD)
  - experimentally observed decrease in synaptic strength that lasts for hours or days
- Hebbian learning rule
  - if neuron A repeatedly takes part in firing neuron B, then synapse from A to B is strengthened
- formalizing Hebbian learning rule will give us the standard gradient descent equation!
- Hebb's rule increases only LTP, but not LTD
  - covariance rule helps solve this
- however, for both hebb and covariance rules, the length of weight vector grows unbounded over time!
- Oja's rule for hebbian learning - stable and converges to a value
- for solving hebbian equation using covariance rule, we can use eigen vectors!
  - this means, that brain is basically performing Principal Component Analysis!!! (PCA)

### Unsupervised learning
- competitive learning
  - given a new input, pick the most active neuron (winner takes all)
  - update weight vector for that neuron
- Self Organizing Maps (Kohonen Maps)
  - given a new input, pick the winning neuron
  - update weights for it and its neighbors
  - eg: orientation preference map in the primary visual cortex
- goal of unsupervised learning
  - learn a generative model for the data being observed
  - ie. mimic the data generation proces
  - it involves 2 steps:
    1. learning the posterior probability for the new input
    2. using this probablity to learn the parameters
- EM algo for unsupervised learning
  - involves 2 steps: E-step and M-step
  - which pretty much matches the above 2 steps mentioned!
  - competitive learning is online, whereas EM requires all the data points to be available!

### Sparse coding and predictive coding
- how to learn good representation for images?
- eigenvectors?
  - eg: eigenfaces!
  - eigenvector representation is good for compression, but not so good if you want to
    extract the local components of an image!
- linear model of natural images?
  - in this case, we need to learn the basis vector for all the components and their weights
  - for this we can learn a generative model for the input image
  - assume parse distribution for the weights
  - will get an equation that is close to the cost function with regularization error!
  - when you try to maximize the value for 'v', you get recurrent network!
  - when you try to maximize the value for 'G', you get hebbian rule!

## Week8
### supervised learning
- simplest model is of perceptron
  - they can perform linear classification
  - based on the output error, weights are updated accordingly
  - but perceptrons cannot learn any function
    - example: XOR function!
  - they can only classify linearly separable data
- can use multilayer perceptron to classify linearly inseparable data
- for continuous valued output, use sigmoid function in place of step function
- learning multilayered sigmoid networks
  - use gradient descent to learn the weight matrices
  - perform the same + backpropagation learning rule to learn the weights in lower layers

### reinforcement learning: predicting rewards
- selecting an action that maximizes the total expected future reward
- predicting delayed rewards
  - predict rewards delivered some time after the stimulus is presented
  - use a tapped delay line and weighted summation of past inputs
  - the approach is very similar to creating a discrete linear filter!
  - to learn weights, minimize the predicted reward error
  - however, we have future rewards that are not yet available!
- Temporal Difference (TD) learning
  - idea is to rewrite the error function to get rid of future terms
  - minimize this using gradient descent

### reinforcement learning: selecting action
- learning a state-to-action mapping (aka policy)
- actor-critic learning
  - actor = selects action and maintains policy
  - critic = maintains the value of each state
- learning process
  1. critic learning (policy evaluation): using TD rule
  2. actor learning (policy improvement): select an action at a given state using softmax function
  3. Repeat 1 and 2
