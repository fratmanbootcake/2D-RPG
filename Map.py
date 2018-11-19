"""
Map.py

This contains the Map class. This loads a map via reading in a text file and
assigning the relevant tiles to the Game class's tiles. It also adds the
sprites into the appropiate group from Game class. It also appends the walls
into the Game class's wall list.
"""

from os import path
from Constants import *
from Tiles import *
from Walls import *
from Player import *
from Monster import *
from Items import *


class Map:

    def __init__(self, game, filename):
        self.game = game
        self.data = []
        with open(filename, "rt") as f:
            for row in f:
                self.data.append(row.strip())
        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILE
        self.height = self.tile_height * TILE

    def add_tiles(self):
        #loads map tiles
        for j, row in enumerate(self.data):
            for i, column in enumerate(row):
                self.game.tiles.append(Grass(self.game, i, j))
                if self.data[j][i] == '1':
                    self.game.tiles.append(Water(self.game, i, j))
                elif self.data[j][i] == '2':
                    self.game.tiles.append(WaterBottom(self.game, i, j))
                elif self.data[j][i] == '3':
                    self.game.tiles.append(WaterTopRight2(self.game, i, j))
                elif self.data[j][i] == '4':
                    self.game.tiles.append(WaterLeft(self.game, i, j))
                elif self.data[j][i] == '5':
                    self.game.tiles.append(WaterBottomLeft(self.game, i, j))
                elif (self.data[j][i] == 'T' or
                      self.data[j][i] == 't'):
                    self.game.tiles.append(Tree(self.game, i, j))
                elif self.data[j][i] == 'a':
                    self.game.tiles.append(Roof1(self.game, i, j))
                elif self.data[j][i] == 'd':
                    self.game.tiles.append(Roof2(self.game, i, j))
                elif self.data[j][i] == 'b':
                    self.game.tiles.append(Roof3(self.game, i, j))
                elif self.data[j][i] == 'c':
                    self.game.tiles.append(Roof4(self.game, i, j))
                elif self.data[j][i] == 'f':
                    self.game.tiles.append(Roof5(self.game, i, j))
                elif self.data[j][i] == 'g':
                    self.game.tiles.append(Roof6(self.game, i, j))
                elif self.data[j][i] == 'j':
                    self.game.tiles.append(Roof7(self.game, i, j))
                elif self.data[j][i] == 'e':
                    self.game.tiles.append(Roof8(self.game, i, j))
                elif self.data[j][i] == 'i':
                    self.game.tiles.append(Roof9(self.game, i, j))
                elif self.data[j][i] == 'l':
                    self.game.tiles.append(Roof10(self.game, i, j))
                elif self.data[j][i] == 'm':
                    self.game.tiles.append(Wall2(self.game, i, j))
                elif self.data[j][i] == 'n':
                    self.game.tiles.append(Window1(self.game, i, j))
                elif self.data[j][i] == 'B':
                    self.game.tiles.append(Barrel(self.game, i, j))
                elif self.data[j][i] == 'D':
                    self.game.tiles.append(Door(self.game, i, j))

    def add_sprites(self):
        #loads sprites and walls
        for j, row in enumerate(self.data):
            for i, column in enumerate(row):
                if self.data[j][i] in ['2','4','5','t','a','b','c','n','m','l','e','j','g','B','D']:
                    wall = Wall(self.game, i, j)
                    self.game.walls.append(wall)
                elif self.data[j][i] == 'p':
                    self.game.player = Player(self.game, i, j)
                    self.game.all_sprites.add(self.game.player)
                    self.game.animations.add(self.game.player)
                    self.game.characters.add(self.game.player)
                elif self.data[j][i] == 'M':
                    monster = Monster(self.game, i, j)
                    self.game.all_sprites.add(monster)
                    self.game.characters.add(monster)
                    self.game.animations.add(monster)
                elif self.data[j][i] == 'S':
                    item = Factory().create_weapon(i,j)
                    self.game.items.add(item)
                    self.game.all_sprites.add(item)
                elif self.data[j][i] == 'A':
                    item = Factory().create_armour(i,j)
                    self.game.items.add(item)
                    self.game.all_sprites.add(item)






