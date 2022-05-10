---
layout: post
title: "RAPIDS ML dev setup"
tags: cuda rapids cuml
---

### Introduction
This blog post is an attempt to simplify the process of setting up of an
environment for [cuML](https://github.com/rapidsai/cuml) development. If your
environment already has docker and you have access to building images and
running containers using them, then the Dockerfile shipped with cuML repo is the
easiest way to get started.

### Pre-reqs
1. Install the [cuda toolkit](https://developer.nvidia.com/cuda-downloads)
2. Download the bash script from the github gist [here](https://gist.github.com/teju85/51ff12886f5ae9967a4cab6fd0376953) and save it as `rapids-setup`.
3. ~10-15GB of free disk-space.

### Instructions
Run the bash script to install cuML and its dependencies. Recommended approach
is to use [anaconda](https://www.anaconda.com/). This script installs all the
needed dependencies in a stand-alone folder and thus does not need root access.
```
bash ./rapids-setup installCuml
```
At the end, it prints a couple of environment variables to be set in your bash
terminal. Execute them and you should now be ready to run tests and develop!
