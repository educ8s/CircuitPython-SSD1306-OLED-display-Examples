from adafruit_display_shapes.rect import Rect

class Paddle:
    def __init__(self, width, height, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.prev_y = y
        self.rect = Rect(self.x, self.y, self.width, self.height, fill=0xFFFFFF)
        self.SCREEN_HEIGHT = 64
    
    def update(self, ball):
        
        if self.y > self.SCREEN_HEIGHT - self.height:
            self.y = self.SCREEN_HEIGHT - self.height
        
        if self.y < 0:
            self.y = 0

        if self.y < ball.y:
            self.y += 1
        if self.y > ball.y:
            self.y -= 1
            
        self.rect.x = self.x
        self.rect.y = self.y