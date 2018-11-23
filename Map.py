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
from random import choice
from operator import attrgetter


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

    def astar_path(self, data, start, target):
        """this determines the shortest path between two points using the
            A* algorithm."""
        #create starting node
        start_node = Node(start,None)
        start_node.g, start_node.h, start_node.f = 0,0,0

        #creating ending node
        target_node = Node(target,None)
        target_node.g, target_node.h, target_node.f = 0,0,0

        #initialize the open and closed lists
        open_list = []
        closed_list = []

        #add the starting node to the open list
        open_list.append(start_node)

        #begin loop which ends after the target has been found or no path exists
        while len(open_list)>0:
            
            #prioritise the open list by lowest f value and
            #make the lowest the current node. Add the current node to the
            #closed list and remove it from the open list
            open_list.sort(key=attrgetter('f'))
            current_node = open_list[0]
            open_list.remove(current_node)
            closed_list.append(current_node)
            
            #check to see if the target is the current node and if it is, step backwards
            #though the parents adding them to the path list. Once done, reverse it so
            #it reads from start to end
            if current_node.position == target_node.position:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]

            #generate the children of the current node
            children = []
            for new_position in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:

                #get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                #check if the node position is within the map limits and ignore if it is not
                if node_position[0] > (len(data[0])-1) or node_position[0] < 0 or node_position[1] > (len(data)-1) or node_position[1] < 0:
                    continue

                #check if the node is walkable and ignore if it is not
                if data[node_position[0]][node_position[1]] != '.':
                    continue

                #create new node at node_position and give it the current node as its
                #parent. Append it to the children list
                new_node = Node(node_position, current_node)

                #calculate the new nodes's g, h and f values. h value is the city block method
                if new_position in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_node.g = current_node.g + 10
                else:
                    new_node.g = current_node.g + 14

                new_node.h = (10*(new_node.position[0] - target[0])**2)+(10*(new_node.position[1] - target[1])**2)
                new_node.f = new_node.g+new_node.h

                
                children.append(new_node)

            #for each child, check if it is on the closed list and ignore if it is
            for child in children:

                for closed_node in closed_list:
                    if child.position == closed_node.position:
                        continue

                #check whether the child equals a node in the open list and compare g values with
                #the version in the open list. if the g value is higher than the g value for the version
                #in the open list, ignore the child.
                for open_node in open_list:
                    if child.position == open_node.position and child.g > open_node.g:
                        continue

                #if the code reaches here, the child can be added  to the open listt because it either
                #is not in the open list at all or a better path to this node was found
                #open_list.append(child)
                open_list.append(child)



class Node:

    def __init__(self, position, parent = None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0


