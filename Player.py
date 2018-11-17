import pygame as pygame
from Constants import *
from Entity import *
from Hitbox import *

class Player(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.inventory = pygame.sprite.Group()
        self.encumberance = 100

    def load_images(self):
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior01.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior02.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior03.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior04.png")).convert_alpha())
        self.image = self.images[0]

    def handle_movement(self):
        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
        elif keys[pygame.K_w]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.vy = PLAYER_SPEED

    def move(self): 
        self.x = int(self.x + self.vx * self.game.dt)
        self.y = int(self.y + self.vy * self.game.dt)

    def level_up(self):
        pass

    def pick_up_item(self):
        for item in self.game.items:
            if pygame.Rect(self.x, self.y, TILE, TILE).colliderect(pygame.Rect(item.x, item.y, TILE, TILE)):
                if not self.inventory_limit_reached(item):
                    self.inventory.add(item)
                    self.game.items.remove(item)

    def inventory_limit_reached(self, item):
        weight = 0
        for item_ in self.inventory:
            weight += item_.weight
        weight += item.weight
        if weight <= self.encumberance:
            return False
    
    def update(self):
        self.handle_movement()
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
        self.health_bar_update()
