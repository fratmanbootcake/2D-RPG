import pygame as pygame
from Constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE, TILE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x * TILE
        self.y = y * TILE
        self.vx = 0
        self.vy = 0

    def handle_event(self):
        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.vx = PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.vy = PLAYER_SPEED

        if self.vx != 0 and self.vy != 0:
            self.vx = 0.7101 * self.vx
            self.vy = 0.7101 * self.vy   

    def collisions(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, new_y, TILE, TILE).colliderect(sprite):
                    return sprite

    def x_collision(self):
        new_x = self.x + self.vx * self.game.dt
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, self.y, TILE, TILE).colliderect(sprite):
                    return sprite

    def y_collision(self):
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(self.x, new_y, TILE, TILE).colliderect(sprite):
                    return sprite

    def x_position_reset(self, sprite):
        if sprite:
            if self.vx > 0:
                self.x = sprite.x - TILE
                self.vx = 0
            elif self.vx < 0:
                self.x = sprite.x + TILE
                self.vx = 0
                
    def y_position_reset(self, sprite):
        if sprite:
            if self.vy > 0:
                self.y = sprite.y - TILE
                self.vy = 0
            elif self.vy < 0:
                self.y = sprite.y + TILE
                self.vy =0

    def move(self): 
        self.x = self.x + self.vx * self.game.dt
        self.y = self.y + self.vy * self.game.dt
    
    def update(self):
        self.handle_event()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
            




