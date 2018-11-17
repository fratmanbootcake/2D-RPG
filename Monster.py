import pygame as pygame
from Constants import *
from Entity import *
from Textures import *


class Monster(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def load_images(self):
        self.images = SKELETON

        self.image = self.images[0]

    def try_move(self):
        pass
        #self.vx = PLAYER_SPEED/2
        # until pathfinding is implemented

    def update(self):
        self.try_move()
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
        if not self.is_alive():
            self.kill()
            return
        self.health_bar_update()
        
        




