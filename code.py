# SPDX-FileCopyrightText: 2020 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# SpaceX Launch Display, by Anne Barela November 2020
# MIT License - for Adafruit Industries LLC
# See https://github.com/r-spacex/SpaceX-API for API info

import time
import terminalio
from adafruit_magtag.magtag import MagTag

from walter import *
output = cow()
print(output)

magtag = MagTag()
#    url=DATA_SOURCE,
#    json_path=(NAME_LOCATION, DATE_LOCATION, DETAIL_LOCATION)
#)

magtag.add_text(
    text_font="/fonts/Major-Mono-Display-12.bdf",
    text_position=(30,90),
    text_scale=1,
    is_data=False,
    line_spacing=0.80,
)

magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(0,30),
    text_scale=2,
    is_data=True,
)

magtag.set_text(cow(),0)
magtag.set_text(walterize(),1)

import board
import neopixel

num_pixels = 4
pixels = magtag.peripherals.neopixels
pixels.brightness = 0.03

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

FLASH_DELAY_TIME = 0.5
UPDATE_DELAY_TIME = 300

def alternate(color_a, color_b):
    for i in range(num_pixels):
        pixels[i] = color_a if (i % 2 == 0) else color_b
    pixels.show()

while True:
    update_time = time.monotonic() + UPDATE_DELAY_TIME
    while (time.monotonic() < update_time):
        alternate(RED,GREEN)
        time.sleep(FLASH_DELAY_TIME)
        alternate(GREEN,RED)
        time.sleep(FLASH_DELAY_TIME)
    magtag.set_text(walterize(),1)
