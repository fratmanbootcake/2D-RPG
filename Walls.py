import pygame as pygame
from Constants import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        self.x = x * TILE
        self.y = y * TILE
        self.rect = pygame.Rect(self.x, self.y, TILE, TILE)
