"""
Monster.py

This contains a skeleton daughter class of Entity.
"""


import pygame as pygame
from random import choice
from Constants import *
from Entity import *
from Textures import *
from Helper import *


class Monster(Entity):

    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.exp = 200
        self.path = []
        self.state = IDLE
        self.range = 10
        self.path_timer = 1/2
        self.path_refresh = 1/2
        self.next_node = None
        self.path = []
        self.moving = False
        self.walk_timer = 1/2
        self.walk_refresh = 1/2

    def load_images(self):
        self.images = SKELETON
        self.image = self.images[0]

    def state_update(self):
        if (self.game.camera.offset(self)[0] < 0 and self.game.camera.offset(self)[0] > WIDTH and
            self.game.camera.offset(self)[1] < 0 and self.game.camera.offset(self)[1] > HEIGHT):
                self.state = SLEEP
        elif (self.game.player.x > self.x - self.range*TILE and self.game.player.x < self.x + self.range*TILE and
            self.game.player.y > self.y - self.range*TILE and self.game.player.y < self.y + self.range*TILE):
            self.state = HUNTING
        else:
            self.state = IDLE
    
    def random_walk(self):
        self.vx = choice([PLAYER_SPEED*1.5, 0, -PLAYER_SPEED*1.5])
        self.vy = choice([PLAYER_SPEED*1.5, 0, -PLAYER_SPEED*1.5])

    def random_walk_timer(self):
        self.walk_timer += self.game.dt
        if self.walk_timer >= self.walk_refresh:
            self.walk_timer -= self.walk_refresh
            return True

    def check_path_timer(self):
        self.path_timer += self.game.dt
        if self.path_timer >= self.path_refresh:
            self.path_timer -= self.path_refresh
            return True
        
    def get_path(self):
        #data = self.game.map.get_chunk(self)
        self.moving = False
        start = (int(number_round(self.x,TILE)/TILE),int(number_round(self.y,TILE)/TILE))
        end = (int(number_round(self.game.player.x,TILE)/TILE),int(number_round(self.game.player.y,TILE)/TILE))
        
        self.path = self.game.map.astar_path(self.game.map.data,start,end)

    def move_to_node(self):
        if not self.moving:
            self.next_node = self.path.pop(0)
            self.moving = True
            
        if self.moving:    
            if self.next_node[0]*TILE + TILE/4 < self.x:
                self.vx = -PLAYER_SPEED*1.5
            elif self.next_node[0]*TILE - TILE/4 > self.x:
                self.vx = PLAYER_SPEED*1.5

         
            if self.next_node[1]*TILE + TILE/4 < self.y:
                self.vy = -PLAYER_SPEED*1.5
            elif self.next_node[1]*TILE - TILE/4 > self.y:
                self.vy = PLAYER_SPEED*1.5

            if self.vy != 0 and self.vy != 0:
                self.vx *= 0.7
                self.vy *= 0.7
            
            if (self.next_node[1]*TILE - TILE/4 < self.y < self.next_node[1]*TILE + TILE/4 and
                  self.next_node[0]*TILE - TILE/4 < self.x < self.next_node[0]*TILE + TILE/4):
                self.vx = 0
                self.vy = 0
                self.moving = False

    def move(self):
        #if state is IDLE, do random walk
        #else check path time, and if true, get the path and then get the next node
        #check whether the path has items left and whether the monster is not moving.
        #If true, get the next node and set moving to True, otherwise pass. Finally, move to the next node
        if self.state == IDLE:
            if self.random_walk_timer():
                self.random_walk()
        elif self.state == SLEEP:
            self.vx = self.vy = 0
        elif self.state == HUNTING:
            if self.check_path_timer():
                self.get_path()
            if self.path:
                self.move_to_node()
            else:
                self.state = IDLE

    def attack(self):
        if pygame.Rect(self.x, self.y, TILE, TILE).colliderect(self.game.player.x, self.game.player.y,TILE,TILE):
            self.game.player.damage(4)
            self.game.player.rebound(self.facing)

    def on_death(self):
        pass

    def update(self):
        self.state_update()
        self.move()
        
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.x += self.vx*self.game.dt
        self.y += self.vy*self.game.dt
        self.attack()

        if not self.is_alive():
            self.kill()
            return
        self.health_bar_update()
        
        




