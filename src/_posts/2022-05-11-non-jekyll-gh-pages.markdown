---
layout: post
title: "Creating non-jekyll gh-pages on github"
tags: programming
---

### Introduction
This blog walks through my experience with setting up a non-jekyll, python based
static webpage generator and hosting those pages via [Github Pages](https://pages.github.com/).

### Why?
- I couldn't get the latest kramdown + katex combination to work at all
- For fun and to learn at the same time!

### pykyll!
This is my python based (almost) jekyll compliant static page generator. The
whole project is basically just a [single python file](https://github.com/teju85/blog/blob/gh-pages/gen/pykyll.py).
Ofcourse, it depends on the awesome [mistletoe](https://github.com/miyuchina/mistletoe)
project for markdown to html converter. So, technically this is not a single
file based python project :)

It follows a config based approach for generating the html pages out of the
markdown files. My config file is [here](https://github.com/teju85/blog/blob/gh-pages/config.json).

All of these are simplified with a top-level `Makefile` in the github repo.
* In order to build the html files: `make generate`
* In order to start a http server to serve these files (mainly to be used during
  development): `make serve`. (For now, as a workaround, you'll need to create a
  symlink to the current directory with the same name as that of 'base_url' as
  in the config file) You'll also need to install the "flask" python module in
  order to run the server.

### Finally...
As mentioned in [this](https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/)
post, you'll also need to drop a file named ".nojekyll" in order to prevent the
"github-pages" bot from trying to build your files using jekyll.
