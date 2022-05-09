---
layout: post
title: "cmdlogger in emacs"
tags: emacs-lisp
---

Happy New Year!

My previous blogs are still on [blogspot](http://ficklemind.blogspot.com/).

I wanted to log how much time I spend on pressing what keys while in an emacs session. There's [keyfreq](https://github.com/dacap/keyfreq) available on github, but I needed something that would just capture keystrokes (in the unix philosophy) and put them in a text format for a future analysis using any of the famous tools. Hence, I wrote [cmdlogger](https://github.com/teju85/cmdlogger) and open-sourced it on github.

### Install
Clone the repo. (hope to add this to MELPA soon)

```
$ git clone https://github.com/teju85/cmdlogger-el
```

### Usage
In your .emacs file:

```
(add-to-list 'load-path /path/to/cmdlogger-el)
(require 'cmdlogger)
(cmdlogger-mode)
```

### Disabling logging temporarily
Useful, especially, when you are trying to enter passwords and other sensitive info.

```
(cmdlogger-mode nil)
;; do your secret stuff
(cmdlogger-mode t)
```
