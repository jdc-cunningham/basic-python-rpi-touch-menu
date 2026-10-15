#!/bin/bash

# OS update
sudo apt update
sudo apt upgrade

# set and activate venv
python -m venv .touch-menu
source .touch-menu/activate
python install -r requirements.txt

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
  python3-opencv
