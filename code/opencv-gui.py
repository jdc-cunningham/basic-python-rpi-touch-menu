#!/usr/bin/env -S python

import cv2
import numpy as np

# setup GUI window
img = np.zeros((480, 640, 3), dtype=np.uint8) # black bg
window_name = "OpenCV GUI"
window_width = 640
window_height = 480
img_path = "/home/pi/basic-python-rpi-touch-menu/code/osaka.png"
boot_scene = cv2.imread(img_path)

# setup menu assets
proceed_btn_img = "/home/pi/basic-python-rpi-touch-menu/code/proceed-button.png"
orange_tile_img = "/home/pi/basic-python-rpi-touch-menu/code/orange-tile.png"
red_tile_img = "/home/pi/basic-python-rpi-touch-menu/code/red-tile.png"
new_pg_img = "/home/pi/basic-python-rpi-touch-menu/code/new-page.png"
proceed_btn = cv2.imread(proceed_btn_img)
orange_tile = cv2.imread(orange_tile_img)
red_tile = cv2.imread(red_tile_img)
new_pg = cv2.imread(new_pg_img)

# place proceed button over boot scene
fg_height, fg_width, _ = proceed_btn.shape
x_offset = 195
y_offset = 300
boot_scene[y_offset:y_offset+fg_height, x_offset:x_offset+fg_width] = proceed_btn

# setup new page interactive tile
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(new_pg, 'Tap tiles', (220, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

def add_tile(color, is_left):
  tile = orange_tile if color == "orange" else red_tile
  y_offset = 100

  if is_left:
    x_offset = 30
  else:
    x_offset = 310

  fg_height, fg_width, _ = tile.shape
  new_pg[y_offset:y_offset+fg_height, x_offset:x_offset+fg_width] = tile

add_tile("orange", True)
add_tile("orange", False)

# menu logic
on_next_page = False

def next_page():
  global on_next_page # usually want to avoid this pattern
  on_next_page = True

# mouse callback
def on_mouse(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    # wait for proceed click, these are the x, y offsets of the button
    if not on_next_page:
      if x > 195 and x < 445:
        if y > 300 and y < 380:
          next_page()
    else:
      # reset tiles
      add_tile("orange", True)
      add_tile("orange", False)

      # left tile
      if x > 30 and x < 280:
        if y > 100 and y < 260:
          add_tile("red", True)

      if x > 310 and x < 560:
        if y > 100 and y < 260:
          add_tile("red", False)

# setup the window
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) # hide GUI window border and menu buttons
cv2.setMouseCallback(window_name, on_mouse)
cv2.imshow(window_name, boot_scene)

# render menu
while True:
  try:
    if on_next_page:
      cv2.imshow(window_name, new_pg)
    else:
      cv2.imshow(window_name, boot_scene)

    cv2.waitKey(17)
  except KeyboardInterrupt:
    break

cv2.destroyAllWindows()
