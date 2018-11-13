from Constants import *
import pygame as pygame
from Textures import *

class Tiles(pygame.sprite.Rect):

    def __init__(self, game, x, y):
        self.game = game
        self.x = x * TILE
        self.y = y * TILE

class Grass(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = GRASS
        self.rect = self.image.get_rect()

class Tree(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = TREE
        self.rect = self.image.get_rect()

class Water(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WATER
        self.rect = self.image.get_rect()

class WaterLeft(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WATER_LEFT
        self.rect = self.image.get_rect()

class WaterBottomLeft(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WATER_BOTTOM_LEFT
        self.rect = self.image.get_rect()

class WaterBottom(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WATER_BOTTOM
        self.rect = self.image.get_rect()

class WaterTopRight2(Tiles):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WATER_TOP_RIGHT_2
        self.rect = self.image.get_rect()

class Roof1(Tiles):
    # a on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_1
        self.rect = self.image.get_rect()

class Roof2(Tiles):
    # d on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_2
        self.rect = self.image.get_rect()

class Roof3(Tiles):
    # b on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_3
        self.rect = self.image.get_rect()

class Roof4(Tiles):
    # c on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_4
        self.rect = self.image.get_rect()

class Roof5(Tiles):
    # f on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_5
        self.rect = self.image.get_rect()

class Roof6(Tiles):
    # i on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_6
        self.rect = self.image.get_rect()


class Roof7(Tiles):
    # l on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_7
        self.rect = self.image.get_rect()

class Roof8(Tiles):
    # e on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_8
        self.rect = self.image.get_rect()

class Roof9(Tiles):
    # g on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_9
        self.rect = self.image.get_rect()

class Roof10(Tiles):
    # j on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = ROOF_10
        self.rect = self.image.get_rect()

class Wall2(Tiles):
    # m on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WALL_2
        self.rect = self.image.get_rect()        


class Window1(Tiles):
    # n on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = WINDOW_1
        self.rect = self.image.get_rect()

class Door(Tiles):
    # D on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = DOOR
        self.rect = self.image.get_rect()

class Barrel(Tiles):
    # B on map
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.image = BARREL
        self.rect = self.image.get_rect()




        
