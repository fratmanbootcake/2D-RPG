"""
SpriteManager.py

This manages the currently active sprites and allows a single parameter to be
called for drawing the currently active sprites and also for detecting
collisions
"""

import pygame as pygame
from Map import *

class SpriteManager:

    def __init__(self, game):
        self.game = game
        self.width = WIDTH
        self.height = HEIGHT
        self.tile = TILE
        self.fps = FPS
        self.state = MENU
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(WHITE)
        self.active_sprites = pygame.sprite.Group()

    def add_sprites(self, group):
        self.active_sprites.empty()
        for sprite in group:
            self.active_sprites.add(sprite)

        
    
