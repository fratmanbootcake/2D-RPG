from os import path
from Constants import *

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
