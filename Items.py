import pygame as pygame
from Constants import *


class Item(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x * TILE
        self.y = y * TILE

    def update(self):
        if pygame.Rect(self.x, self.y, TILE, TILE).colliderect(pygame.Rect(self.game.player.x, self.game.player.y, TILE, TILE)):
            self.game.player.inventory.add(self)
            self.game.items.remove(self)

class Sword(Item):

    def __init__(self, game, x, y, filename):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()
        self.rect = self.image.get_rect()
        
        

    
    
