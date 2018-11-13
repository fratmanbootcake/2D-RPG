from Constants import *
import pygame as pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, game, x, y, text):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.text = text

