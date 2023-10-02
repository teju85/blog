---
layout: post
title: "Installing 'numpy' on cygwin"
tags: tools
---
Recently, I wanted to use 'numpy' from the python environment inside my cygwin installation.
I had python version 3.8 and also had `python38-devel` and `libopenblas` installed already.
I even made sure that my cygwin version is >= 3.3. Even after this, my attempt at installing
numpy using `python3 -m pip install numpy` failed with the following error:

```
      Run-time dependency openblas found: NO (tried pkgconfig and cmake)
      Run-time dependency openblas found: NO (tried pkgconfig and cmake)

      ../../numpy/meson.build:207:4: ERROR: Problem encountered: No BLAS library detected! Install one, or use the `allow-noblas` build option (note, this may be up to 100x slower for some linear algebra operations).
```

In the end, I noticed that there's already a `python38-numpy` package in the cygwin repo.
I was able to install that package successfully and after that, I could use `numpy` from
my python3.8 REPL!
