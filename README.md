### About

This is intended to be a precursor to the [JDC34](https://github.com/jdc-cunningham/jdc34-camera) and [JDC35](https://github.com/jdc-cunningham/jdc35-camera) cameras that I deveoped.

This uses:

- openbox
- pillow
- opencv
- python

To make a touch screen menu on a Raspberry Pi with an HDMI (or DSI) touch screen display.

See the YouTube video going over this code.

### Disclaimer

Note this was tested against Debian 13 Trixie on a Pi 4B with a 2.8" Waveshare HDMI touchscreen display

### Set display touch mode

There is a switch on the HDMI hat with two settings: I2C and USB, make sure it's set to I2C

### Run

#### Step 1 - install dependencies

The installation commands have been placed in the `install-deps.sh` bash script. Note that it requires sudo to run.

Make it executable: `$chmod +x install-deps.sh` then run as `./install-deps.sh`

#### Step 2 - try the openbox file

Make it executable `$chmod +x openbox`

Then run it `$sudo xinit ./openbox`

You should see your display change and show an image of Osaka from Azumanga Daioh

From there you can click through the basic menu example
