import pygame as pygame
from Constants import *
from Entity import *

class Monster(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def load_images(self):
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_fr1.gif")).convert())
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_fr2.gif")).convert())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_lf1.gif")).convert())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_lf2.gif")).convert())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_rt1.gif")).convert())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_rt2.gif")).convert())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_bk1.gif")).convert())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"dvl1_bk2.gif")).convert())
        
        for image in self.south_images:
            image.set_colorkey(pygame.Color('#ffffff'))
        for image in self.north_images:
            image.set_colorkey(pygame.Color('#ffffff'))
        for image in self.east_images:
            image.set_colorkey(pygame.Color('#ffffff'))
        for image in self.west_images:
            image.set_colorkey(pygame.Color('#ffffff'))

        self.image = self.south_images[1]

    def try_move(self):
        self.vx = PLAYER_SPEED/2
        # until pathfinding is implemented (if required? maybe pokemon / FF style fights)

    def update(self):
        self.try_move()
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
        




