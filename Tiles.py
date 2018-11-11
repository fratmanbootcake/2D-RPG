from Constants import *
import pygame as pygame

class Tiles(pygame.sprite.Rect):

    def __init__(self, game, x, y):
        self.game = game
        self.x = x * TILE
        self.y = y * TILE

class Grass(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "grass.png"))
        self.rect = self.image.get_rect()


class Tree(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "tree01.png"))
        self.rect = self.image.get_rect()

class Water(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "water.png"))
        self.rect = self.image.get_rect()

class WaterLeft(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "water_l.png"))
        self.rect = self.image.get_rect()

class WaterBottomLeft(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "water_bl.png"))
        self.rect = self.image.get_rect()

class WaterBottom(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "water_b.png"))
        self.rect = self.image.get_rect()

class WaterTopRight2(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = pygame.image.load(os.path.join(image_folder, "water_tr2.png"))
        self.rect = self.image.get_rect()











        
