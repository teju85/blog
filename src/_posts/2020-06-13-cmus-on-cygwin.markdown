---
layout: post
title: "cmus installation and usage on cygwin"
tags: tools
---

### cmus
[cmus](https://cmus.github.io/) is a lightweight console player for unix-like
operating systems. Given here are the steps to build it on cygwin.

#### Steps
```
lynx -source rawgit.com/transcode-open/apt-cyg/master/apt-cyg > apt-cyg
install apt-cyg /bin
apt-cyg install ncurses ncursesw pkg-config
apt-cyg install libncursesw-devel libncurses-devel
apt-cyg install libopus-devel libwavpack-devel
apt-cyg install libtool flac-devel

cd ~
wget ftp://ftp.mars.org/pub/mpeg/libmad-0.15.1b.tar.gz
tar xf
cd libmad-0.15.1b
wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' -O config.guess
wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD' -O config.sub
sed -i '/-fforce-mem/d' configure
./configure
make
make install

cd ~
git clone https://github.com/cmus/cmus.git
cd cmus
./configure CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib
make
make install
```

#### Key controls
- v: stop playback
- b: next track
- z: previous track
- c: pause playback
- s: toggle shuffle (read about the m key below if you're going to use shuffle)
- m: toggles the "aaa mode."
- x: restart track
- i: jump view to the currently playing track (handy when in shuffle mode)
- o: toggle sorting
- /: searching cmus works as in many Unix programs.
  - Typing slash, a string, and enter will find the first instance of that
    string in your library.
  - Press n to go to the next string, N to go to the previous.
  - cmus's search isn't case sensitive and is quite smart; a search for damned
    insurrection will return Bulldozer's "Insurrection of the Living Damned"
    (rad tune).
- -: reduce the volume by 10%
- +: increase the volume by 10%
- :add path  - to add a playlist
