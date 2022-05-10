---
layout: post
title: "Building 'mu' on cygwin"
tags: tools
---
Recently, I wanted to play with the popular 'mu' tool for indexing my mails. Started with Matthias' [mu-on-cygwin](https://frosch03.de/blog/2016/05/mu4e-within-cygwin.html) blog. Interestingly, even after following the steps he mentions there, I was welcomed with the below error!

```
  CXX      utils.lo
utils.cc: In function ‘std::string Mux::format(const char*, ...)’:
utils.cc:187:44: error: ‘vasprintf’ was not declared in this scope
   const auto res = vasprintf (&s, frm, args);
                                            ^
utils.cc: In function ‘std::string Mux::date_to_time_t_string(const string&, bool)’:
utils.cc:313:52: error: ‘strptime’ was not declared in this scope
  if (!strptime (date.c_str(), "%Y%m%d%H%M%S", &tbuf) &&
                                                    ^
make[3]: *** [Makefile:749: utils.lo] Error 1
```

I had to do the following hack in order to get this working on my cygwin-env. (assuming you're already inside 'mu')

```
$ cd lib/parser
$ sed -e 's/^#define GNU_SOURCE/#define _GNU_SOURCE/' utils.cc  > tmp
$ mv tmp utils.cc 
```

After this, the compilation and installation happened without any errors. Hope this helps others, in case they get stuck with the same error.
