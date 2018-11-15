from os import path
from Constants import *
from Tiles import *

class Map:

    def __init__(self, filename):

        self.data = []
        with open(filename, "rt") as f:
            for row in f:
                self.data.append(row.strip())
        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILE
        self.height = self.tile_height * TILE

    def add_tiles(self, game):
        #loads map tiles
        for j, row in enumerate(game.map.data):
            for i, column in enumerate(row):
                game.tiles.append(Grass(game, i, j))
                if game.map.data[j][i] == '1':
                    game.tiles.append(Water(game, i, j))
                elif game.map.data[j][i] == '2':
                    game.tiles.append(WaterBottom(game, i, j))
                elif game.map.data[j][i] == '3':
                    game.tiles.append(WaterTopRight2(game, i, j))
                elif game.map.data[j][i] == '4':
                    game.tiles.append(WaterLeft(game, i, j))
                elif game.map.data[j][i] == '5':
                    game.tiles.append(WaterBottomLeft(game, i, j))
                elif (game.map.data[j][i] == 'T' or
                      game.map.data[j][i] == 't'):
                    game.tiles.append(Tree(game, i, j))
                elif game.map.data[j][i] == 'a':
                    game.tiles.append(Roof1(game, i, j))
                elif game.map.data[j][i] == 'd':
                    game.tiles.append(Roof2(game, i, j))
                elif game.map.data[j][i] == 'b':
                    game.tiles.append(Roof3(game, i, j))
                elif game.map.data[j][i] == 'c':
                    game.tiles.append(Roof4(game, i, j))
                elif game.map.data[j][i] == 'f':
                    game.tiles.append(Roof5(game, i, j))
                elif game.map.data[j][i] == 'g':
                    game.tiles.append(Roof6(game, i, j))
                elif game.map.data[j][i] == 'j':
                    game.tiles.append(Roof7(game, i, j))
                elif game.map.data[j][i] == 'e':
                    game.tiles.append(Roof8(game, i, j))
                elif game.map.data[j][i] == 'i':
                    game.tiles.append(Roof9(game, i, j))
                elif game.map.data[j][i] == 'l':
                    game.tiles.append(Roof10(game, i, j))
                elif game.map.data[j][i] == 'm':
                    game.tiles.append(Wall2(game, i, j))
                elif game.map.data[j][i] == 'n':
                    game.tiles.append(Window1(game, i, j))
                elif game.map.data[j][i] == 'B':
                    game.tiles.append(Barrel(game, i, j))
                elif game.map.data[j][i] == 'D':
                    game.tiles.append(Door(game, i, j))








