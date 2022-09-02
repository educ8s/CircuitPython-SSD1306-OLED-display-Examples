# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2
# OLED DISPLAY: https://educ8s.tv/part/OLED096

import board, busio, displayio, os, terminalio, time
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

FPS = 50
FPS_DELAY = 1 / FPS

displayio.release_displays()

board_type = os.uname().machine
print(f"Board: {board_type}")

if 'Pico' in board_type:
    sda, scl = board.GP0, board.GP1
    print("Supported.")
    
elif 'ESP32-S2' in board_type:
    sda, scl = board.IO40, board.IO41 # With the ESP32-S2 you can use any IO pins as I2C pins
    print("Supported.")
    
else:
    sda, scl = board.SDA, board.SCL
    print("This board is not directly supported. Change the pin definitions above.")
    
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Make a background color fill
color_bitmap = displayio.Bitmap(SCREEN_WIDTH, SCREEN_HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
splash.append(bg_sprite)

right_paddle = Paddle(3,20,SCREEN_WIDTH-3,int(SCREEN_HEIGHT/2 - 10))
splash.append(right_paddle.rect)

left_paddle = Paddle(3,20,0,int(SCREEN_HEIGHT/2 - 10))
splash.append(left_paddle.rect)

ball = Ball(3,10,5)
splash.append(ball.circle)

last_update_time = 0
now = 0
loops_since_update = 0

while True:
    # update time variable
    now = time.monotonic()

    # check if the delay time has passed since the last game update
    if last_update_time + FPS_DELAY <= now:
        
        # update objects
        ball.update(left_paddle, right_paddle )
        left_paddle.update(ball)
        right_paddle.update(ball)
        
        last_update_time = now
        loops_since_update = 0
    else:
        loops_since_update += 1