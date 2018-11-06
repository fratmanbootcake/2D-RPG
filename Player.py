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
        elif keys[pygame.K_UP]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.vy = PLAYER_SPEED        

    def collides(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.all_sprites:
            if pygame.Rect(new_x, new_y, TILE, TILE).colliderect(sprite):
                    return sprite
            
    def position_update(self, sprite, rebound):
        if self.vx > 0:
            self.x = sprite.x - rebound
            self.vx = 0
        elif self.vx < 0:
            self.x = sprite.x + rebound
            self.vx = 0
        if self.vy > 0:
            self.y = sprite.y - rebound
            self.vy = 0
        elif self.vy < 0:
            self.y = sprite.y + rebound
            self.vy = 0
     
    def update(self):
        self.handle_event()
        if self.collides():
            sprite = self.collides()
            if sprite in self.game.walls:
                self.position_update(sprite, TILE)
            elif sprite in self.game.monsters:
                self.position_update(sprite, 2*TILE)
            #elif sprite in self.game.items:
                # some update for collecting items
        else:
            self.x = self.x + self.vx * self.game.dt
            self.y = self.y + self.vy * self.game.dt
            




