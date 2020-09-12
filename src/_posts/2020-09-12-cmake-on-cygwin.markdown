---
layout: post
title: "cmake on cygwin"
tags: tools
---

### correctly installing cmake on cygwin
I have had this issue when I install cmake on cygwin
```bash
$ apt-cyg install cmake
$ cmake --version
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
```

When I try to find where all cygwin is installed, here's the output:
```bash
$ which -a cmake
/bin/cmake
/usr/bin/cmake
```

When I now update my `PATH` environment variable to instead prioritize the
`/usr/bin` folder, by doing: `export PATH=/usr/bin:$PATH` at the end of my
`.bashrc` file, I'm now able to get cmake working.
```bash
$ which -a cmake
/usr/bin/cmake
/bin/cmake
$ cmake --version
cmake version 3.6.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

My guess is that when `cmake` gets resolved to `/bin` folder, it somehow gets
confused while finding cmake modules, leading to the above error.
