---
layout: post
title: "LLVM/Clang inside Docker"
tags: compiler
---

### Introduction
The [instructions](https://clang.llvm.org/get_started.html) on building LLVM/Clang
from source are pretty accurate. That and the fact that it's dependencies are very
minimal, building it from source is a cake-walk!

### Setting up llvm inside docker
As part of my work, I needed the clang tools for code analysis. I nowadays prefer
working inside docker. So, as a first shot, here's how I set up my initial
Dockerfile.

```
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        git \
        make \
        python \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists*

RUN mkdir -p /opt/compiler && \
    cd /opt/compiler && \
    git clone "http://llvm.org/git/llvm" && \
    cd llvm/tools && \
    git clone "http://llvm.org/git/clang" && \
    cd clang/tools && \
    git clone "http://llvm.org/git/clang-tools-extra" extra && \
    mkdir -p /opt/compiler/build && \
    cd /opt/compiler/build && \
    cmake -G "Unix Makefiles" ../llvm && \
    make -j8 && \
    make install && \
    cd / && \
    rm -rf /opt/compiler

ENV PATH=/usr/local/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

Interestingly, this ended up generating a really huge docker image!
```
$ docker images | head -n2
REPOSITORY              TAG                  IMAGE ID            CREATED             SIZE
llvm                    latest-9.2           ba5b2786b5e5        About an hour ago   47.1GB
```

### Solution (LLVM_TARGETS_TO_BUILD)
Main reason for this is clang ends up generating cross-compilation for multiple
targets. (Refer to LLVM_ALL_TARGETS variable inside llvm/CMakeLists.txt) Thus, I
had to update the cmake command to only build for my targets of interest.

```
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        git \
        make \
        python \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists*

RUN mkdir -p /opt/compiler && \
    cd /opt/compiler && \
    git clone "http://llvm.org/git/llvm" && \
    cd llvm/tools && \
    git clone "http://llvm.org/git/clang" && \
    cd clang/tools && \
    git clone "http://llvm.org/git/clang-tools-extra" extra && \
    mkdir -p /opt/compiler/build && \
    cd /opt/compiler/build && \
    cmake -G "Unix Makefiles" \
        -DLLVM_TARGETS_TO_BUILD="X86;NVPTX" \
        -DCMAKE_BUILD_TYPE=Release \
        ../llvm && \
    make -j8 && \
    make install && \
    cd / && \
    rm -rf /opt/compiler

ENV PATH=/usr/local/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

This puts me in a more reasonable docker image size. :)
```
$ docker images | head -n2
REPOSITORY              TAG                  IMAGE ID            CREATED             SIZE
llvm                    latest-9.2           57ee054cbfe8        18 seconds ago      3.62GB
```

Hope this is useful to others.
