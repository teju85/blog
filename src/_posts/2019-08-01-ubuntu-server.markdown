---
layout: post
title: "Installing Ubuntu 19.04 Server on desktop with Nvidia GPUs"
tags: linux
---

## Introduction
Notes based on my experience installing and setting up a desktop machine to run
Ubuntu 19.04 server.

## Installing Ubuntu
1. Download iso from [here](https://ubuntu.com/download/server)
2. Download unetbootin from [here](https://unetbootin.github.io/)
3. Have an empty ~4GB USB pen drive
4. Use unetbootin to flash the above iso into this usb drive
5. Boot via this usb drive on your desktop
6. In boot menu select 'Install Ubuntu ...'
7. Follow the instructions on screen
8. Don't forget to select "Install OpenSSH", if you want remote access
9. Select to upgrade and install ubuntu (optional)
10. Provide hostname, username and credentials
11. Wait until finished!

## Setting up
### Basics
My personal preference is to use python3. So, I just remove python2.7.
```bash
sudo apt remove python2.7 python python2.7-minimal
sudo apt purge python2.7 python python2.7-minimal
sudo apt autoremove
sudo ln -s /usr/bin/python3 /usr/bin/python
```
Some essentials:
```bash
sudo apt-get install curl g++ gcc git make tmux
```

### docker
Following steps will let you run docker commands without `sudo`:
```bash
curl -sSL https://get.docker.com/ | sudo sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

### nvidia driver
1. Make sure card is getting detected: `lspci | grep -i nv`.
2. Install kernel headers: `sudo apt-get install linux-headers-$(uname -r)`
3. Download toolkit installer: `wget https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.168_418.67_linux.run`
4. Install only the driver: `sudo sh cuda_10.1.168_418.67_linux.run --driver`
5. Disable nouveau driver: `sudo sh -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nouveau.conf && echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nouveau.conf && update-initramfs -u && reboot"`
6. `nvidia-smi` should now run successfully.

### nvidia-docker
```bash
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
# this is because 19.04 is not yet supported, at the time of this writing
# thus, force fallback on 18.04 version's release
# that seems to be working fine
#distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
distribution=18.04
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install nvidia-docker2
sudo pkill -SIGHUP dockerd
```
