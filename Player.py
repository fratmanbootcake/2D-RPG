import pygame as pygame
from Constants import *
from Entity import *

class Player(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def load_images(self):
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"male_char_fr1.png")).convert_alpha())
        self.south_standing.append(pygame.image.load(os.path.join(image_folder,"male_char_fr2.png")).convert_alpha())
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"male_char_fr3.png")).convert_alpha())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"male_char_lf1.png")).convert_alpha())
        self.west_standing.append(pygame.image.load(os.path.join(image_folder,"male_char_lf2.png")).convert_alpha())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"male_char_lf3.png")).convert_alpha())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"male_char_rt1.png")).convert_alpha())
        self.east_standing.append(pygame.image.load(os.path.join(image_folder,"male_char_rt2.png")).convert_alpha())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"male_char_rt3.png")).convert_alpha())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"male_char_bk1.png")).convert_alpha())
        self.north_standing.append(pygame.image.load(os.path.join(image_folder,"male_char_bk2.png")).convert_alpha())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"male_char_bk3.png")).convert_alpha())

        self.image = self.south_standing[0]

    def handle_event(self):

        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.vx = PLAYER_SPEED
        elif keys[pygame.K_UP]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.vy = PLAYER_SPEED

    def move(self): 
        self.x = self.x + self.vx * self.game.dt
        self.y = self.y + self.vy * self.game.dt
        if self.vx != 0 or self.vy !=0:
            self.state = WALKING
        else:
            self.state = STANDING

    
    def update(self):
        self.handle_event()
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
