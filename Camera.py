import pygame as pygame
from Constants import *

class Camera:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

    def offset(self, sprite):
        offset_x = sprite.x - self.camera.x 
        offset_y = sprite.y - self.camera.y
        return (offset_x, offset_y)

    def update(self, target):
        # fixes sprite in centre of map        
        x = target.x - int(WIDTH / 2) 
        y = target.y - int(HEIGHT / 2)

        x = max(0,x)
        y = max(0,y)

        x = min(x, self.width - WIDTH)
        y = min(y, self.height - HEIGHT) 

        self.camera = pygame.Rect(x, y, WIDTH, HEIGHT)
