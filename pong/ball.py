from adafruit_display_shapes.circle import Circle
import time

class Ball:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        self.speed_x = 1
        self.speed_y = 1
        
        # Create a circle object for the screen
        self.circle = Circle(self.x, self.y, self.size, fill=0xFFFFFF)
        self.SCREEN_HEIGHT = 64
        self.SCREEN_WIDTH = 128
    
    def update(self, left_paddle, right_paddle):
        
         if self.x <= left_paddle.x - self.size:
            self.speed_x *= -1

         if self.x + self.size + right_paddle.width == right_paddle.x:
            self.speed_x *= -1
        
         if self.x >= self.SCREEN_WIDTH-self.size*2 or self.x <= self.size:
            self.speed_x *= -1
            
         if self.y >= self.SCREEN_HEIGHT-self.size*2 or self.y <= self.size:
            self.speed_y *= -1
            
         self.x += self.speed_x
         self.y += self.speed_y
        
         self.circle.x = self.x
         self.circle.y = self.y