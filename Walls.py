import pygame as pygame
from Constants import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE, TILE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x * TILE
        self.y = y * TILE
        self.rect.x = x * TILE
        self.rect.y = y * TILE
