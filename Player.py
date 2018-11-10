import pygame as pygame
from Constants import *
from Entity import *

class Player(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def load_images(self):
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"char01.png")).convert())
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"char02.png")).convert())
        self.south_images.append(pygame.image.load(os.path.join(image_folder,"char03.png")).convert())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"char04.png")).convert())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"char05.png")).convert())
        self.west_images.append(pygame.image.load(os.path.join(image_folder,"char06.png")).convert())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"char07.png")).convert())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"char08.png")).convert())
        self.east_images.append(pygame.image.load(os.path.join(image_folder,"char09.png")).convert())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"char10.png")).convert())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"char11.png")).convert())
        self.north_images.append(pygame.image.load(os.path.join(image_folder,"char12.png")).convert())
        
        for image in self.south_images:
            image.set_colorkey(pygame.Color('#f6ffff'))
        for image in self.north_images:
            image.set_colorkey(pygame.Color('#f6ffff'))
        for image in self.east_images:
            image.set_colorkey(pygame.Color('#f6ffff'))
        for image in self.west_images:
            image.set_colorkey(pygame.Color('#f6ffff'))

        self.image = self.south_images[1]

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
