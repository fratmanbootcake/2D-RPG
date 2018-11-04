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

    def collide_with_walls(self):
        for sprite in self.game.walls:
            if pygame.Rect(self.x + self.vx, self.y + self.vy, TILE, TILE).colliderect(sprite):
                return True

    def collide_with_item(self):
        pass
                
    def update(self):
        self.handle_event()
        if not self.collide_with_walls():
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            




