---
layout: post
title: "CUDA distutils"
tags: cuda
---

### Introduction
After reading McGibbon's [npcuda-example](https://github.com/rmcgibbo/npcuda-example),
I set out on an attempt at creating extension modules by creating a separate
nvcc cuda compiler to the distutils process.

Obviously, most of the idea is inspired from npcuda-example. But instead of
doing runtime hot-patches to the compiler object, this goes via the OO way, in
the hope of keeping things cleaner.

### Example Usage
Taking the setup.py of npcuda-example/cython/setup.py as an example, here's
what it would take to add support for building extension modules having CUDA
kernels.
{% highlight python %}
import os
from setuptools import setup
from distutils.extension import Extension
import cudistutils as cud
import numpy as np
env = cud.CudaEnv()
ext = Extension("gpuadder",
                sources=["src/manager.cu", "wrapper.pyx"],
                library_dirs=[env.lib64],
                libraries=env.base_cuda_libs,
                language="c++",
                runtime_library_dirs=[env.lib64],
                extra_compile_args={"gcc"  : [],
                                    "nvcc" : env.default_nvcc_opts()},
                include_dirs = [np.get_include(), env.include, "src"])
setup(name="gpuadder",
      author="Robert McGibbon",
      version="0.1",
      ext_modules = [ext],
      cmdclass={"build_ext": cud.cuda_build_ext},
      zip_safe=False)
{% endhighlight python %}
As can be seen, most of your setup.py remains similar to writing C/C++ extension
modules. Only change comes with passing 'extra_compile_args', which is needed
since the underlying compiler class switches between C/C++ compiler and cuda
compiler based on the input source file extension.

The project is hosted [here](https://github.com/teju85/cudistutils).
Hopefully will spend some time to get it accessible via 'pip install'.
