#!/bin/bash

# OS update
sudo apt update
sudo apt upgrade

# deps for GUI
sudo apt install -y \
  build-essential \
  libcap-dev \
  openbox obconf \
  xinit \
  x11-xserver-utils \
  xterm \
  menu \
  xorg \
  unclutter \
  xinput \
  opencv-python
