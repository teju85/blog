---
layout: post
title: "MLE and KLD from GAN's PoV"
needmath: true
tags: tech-notes math
---

### MLE and KLD
* Assume that $$P_r(x)$$ is the real distribution to be approximated
* MLE = $$max_\Theta \frac{1}{m} \Sigma_{i=1}^m log P_\Theta(x_i)$$
* in the limit $$m -> \infty$$, this is the same as minimizing KLD!

### Equations
* $$lt_{m -> \infty} max_\Theta \frac{1}{m} \Sigma_{i=1}^m log P_\Theta(x)$$
* $$max_\Theta (integral(P_r(x) log P_\Theta(x) dx))$$
* $$min_\Theta (-integral(P_r(x) log P_\Theta(x) dx))$$
* $$min_\Theta (integral(P_r(x) log P_r(x) dx) - integral(P_\Theta(x) log P_\Theta(x) dx))$$
* $$min_\Theta (integral(P_r(x) log \frac{P_r(x)}{P_\Theta(x)} dx))$$
* Which is the same as minimizing KLD!

### Issues with KLD
* KLD has numerical stability issues when $$P_r(x)$$ or $$P_\Theta(x)$$ is close
  to zero
* This is typically solved by adding noise to $$P_\Theta$$
* Sampling from $$P_\Theta$$ is computationally expensive

### Conclusion
* Thus, better to learn a function $$g_\Theta$$ which can transform a given
  transform a given distribution into $$P_\Theta$$ ie. $$P_\Theta ~= g_\Theta(z)$$
* This is the basis of GAN's :)
