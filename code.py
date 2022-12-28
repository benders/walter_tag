# SPDX-FileCopyrightText: 2020 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# SpaceX Launch Display, by Anne Barela November 2020
# MIT License - for Adafruit Industries LLC
# See https://github.com/r-spacex/SpaceX-API for API info

import terminalio
from adafruit_magtag.magtag import MagTag
import alarm
import board
import digitalio
import neopixel
import time

from walter import *

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


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK= (0, 0, 0)
WALTER_COLOR = (32, 240, 141)

UPDATE_DELAY_TIME = 15

def alternate(color_a, color_b):
    for i in range(num_pixels):
        pixels[i] = color_a if (i % 2 == 0) else color_b
    pixels.show()

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def color_show(color_a, color_b):
    FLASH_DELAY_TIME = 0.1
    magtag.peripherals.neopixel_disable = False
    color_chase(BLUE, FLASH_DELAY_TIME)
    color_chase(CYAN, FLASH_DELAY_TIME)
    color_chase(BLACK, FLASH_DELAY_TIME)
    magtag.peripherals.neopixel_disable = True

def set_mood(adjective = "cool", eyes = "oo", color_a = RED, color_b = GREEN):
    magtag.set_text(cow(eyes),0)
    magtag.set_text(walterize(adjective),1)
    color_show(color_a, color_b)

def snooze():
    # Create a an alarm that will trigger 10 seconds from now.
    time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + UPDATE_DELAY_TIME)

    # Do a light sleep until the alarm wakes us.
    alarm.light_sleep_until_alarms(time_alarm)

num_pixels = 4
pixels = magtag.peripherals.neopixels
pixels.brightness = 0.03

while True:
    set_mood("tired","--",BLUE,CYAN)
    snooze()
