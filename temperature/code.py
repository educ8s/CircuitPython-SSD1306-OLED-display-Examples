# This script supports only the Raspberry Pi Pico board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# OLED DISPLAY: https://educ8s.tv/part/OLED096

import board, busio, displayio, os, terminalio, microcontroller, time
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

temperature = 0
displayio.release_displays()

sda, scl = board.GP0, board.GP1
 
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Load a font, we need it for the degrees symbol
font_file = "fonts/terminal.bdf"
font = bitmap_font.load_font(font_file)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(126, 62, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
splash.append(inner_sprite)

# Draw the temperature text label
temperature_label = label.Label(font, text="TEMPERATURE", color=0xFFFFFF)
temperature_label.anchor_point = (0.5, 0.0) # Change anchor point to center
temperature_label.anchored_position = (64, 5)
splash.append(temperature_label)

temperature_string = f"{temperature}°C"
# Draw the temperature value label
temperature_value_label = label.Label(font, text = temperature_string, color = 0xFFFFFF)
temperature_value_label.anchor_point = (0.5, 0.5) # Change anchor point to center
temperature_value_label.anchored_position = (64, 38)
temperature_value_label.scale = 3
splash.append(temperature_value_label)

while True:
    temperature =  round(microcontroller.cpu.temperature,1)
    temperature_string = f"{temperature}°C"
    temperature_value_label.text = temperature_string
    time.sleep(1)