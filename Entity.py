from Constants import *
import pygame as pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.north_images = []
        self.south_images = []
        self.east_images = []
        self.west_images = []
        self.attacking_images = []
        self.animation_index = 0
        self.load_images()
        self.rect = self.image.get_rect()
        self.x = x * TILE
        self.y = y * TILE
        self.vx = 0
        self.vy = 0
        self.state = STANDING
        self.facing = SOUTH
        self.timer = 0
        self.frame_duration = 50/1000

    def update_facing(self):
        if self.vx > 0 and self.vy == 0:
            self.facing = EAST
        elif self.vx < 0 and self.vy == 0:
            self.facing = WEST
        elif self.vx == 0 and self.vy > 0:
            self.facing = SOUTH
        elif self.vx == 0 and self.vy < 0:
            self.facing = NORTH
        elif self.vx > 0 and self.vy > 0:
            self.facing = SOUTH_EAST
        elif self.vx < 0 and self.vy > 0:
            self.facing = SOUTH_WEST
        elif self.vx > 0 and self.vy < 0:
            self.facing = NORTH_EAST
        elif self.vx < 0 and self.vy < 0:
            self.facing = NORTH_WEST

    def collisions(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.active_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, new_y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def x_collision(self):
        new_x = self.x + self.vx * self.game.dt
        for sprite in self.game.active_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, self.y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def y_collision(self):
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.active_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(self.x, new_y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def x_position_reset(self, sprite):
        if sprite:
            if self.vx > 0:
                self.x = sprite.x - self.rect.width
                self.vx = 0
            elif self.vx < 0:
                self.x = sprite.x + sprite.rect.width
                self.vx = 0
                
    def y_position_reset(self, sprite):
        if sprite:
            if self.vy > 0:
                self.y = sprite.rect.y - self.rect.height
                self.vy = 0
            elif self.vy < 0:
                self.y = sprite.rect.y + sprite.rect.height
                self.vy =0

    def move(self): 
        self.x = self.x + self.vx * self.game.dt
        self.y = self.y + self.vy * self.game.dt
        if self.vx != 0 or self.vy !=0:
            self.state = WALKING
        else:
            self.state = STANDING

    def update(self):
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
