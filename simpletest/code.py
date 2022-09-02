# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2
# OLED DISPLAY: https://educ8s.tv/part/OLED096

import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()

board_type = os.uname().machine
print(f"Board: {board_type}")

if 'Pico' in board_type:
    sda, scl = board.GP0, board.GP1
    print("Supported.")
    
elif 'ESP32-S2' in board_type:
    scl, sda = board.IO41, board.IO40 # With the ESP32-S2 you can use any IO pins as I2C pins
    print("Supported.")
    
else:
    print("This board is not directly supported. Change the pin definitions above.")
    
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 54, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=28)
splash.append(text_area)

while True:
    pass