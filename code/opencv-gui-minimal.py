#!/usr/bin/env -S python

# this minimal code sample will display Osaka when running successfully

import cv2
import numpy as np

# setup GUI window
img = np.zeros((480, 640, 3), dtype=np.uint8) # black bg
window_name = "OpenCV GUI"
window_width = 640
window_height = 480
img_path = "/home/pi/basic-python-rpi-touch-menu/code/osaka.png"
boot_scene = cv2.imread(img_path)

# mouse callback
def on_mouse(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    print("lb")

# setup the window
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback(window_name, on_mouse)
cv2.imshow(window_name, boot_scene)

# render menu
while True:
  try:
    cv2.imshow(window_name, boot_scene)
    cv2.waitKey(17)
  except KeyboardInterrupt:
    break

cv2.destroyAllWindows()
