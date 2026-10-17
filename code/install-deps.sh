#!/bin/bash

# OS update
sudo apt update
sudo apt upgrade

# set and activate venv
python -m venv .touch-menu
source .touch-menu/bin/activate
python -m pip install -r requirements.txt

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
  xinput
