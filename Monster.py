import pygame as pygame
from Constants import *
from Entity import *

class Monster(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def load_images(self):
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"ghost_fr1.png")).convert_alpha())
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"ghost_fr3.png")).convert_alpha())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"ghost_lf1.png")).convert_alpha())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"ghost_lf3.png")).convert_alpha())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"ghost_rt1.png")).convert_alpha())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"ghost_rt3.png")).convert_alpha())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"ghost_bk1.png")).convert_alpha())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"ghost_bk3.png")).convert_alpha())
        self.north_standing.append(pygame.image.load(os.path.join(image_folder,"ghost_bk2.png")).convert_alpha())
        self.south_standing.append(pygame.image.load(os.path.join(image_folder,"ghost_fr2.png")).convert_alpha())
        self.east_standing.append(pygame.image.load(os.path.join(image_folder,"ghost_rt2.png")).convert_alpha())
        self.south_standing.append(pygame.image.load(os.path.join(image_folder,"ghost_lf2.png")).convert_alpha())

        self.image = self.south_images[1]

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
        




