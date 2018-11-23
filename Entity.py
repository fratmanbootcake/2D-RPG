"""
Entity.py

This contains the base class for players, monsters and npcs. It contains the
images, position, velocities, facing and various timers. Also included are
collision methods, position reset methods, an attack method, a method to check
whether it's alive, a health bar update method, a rebound method and a take
damage method. The update method is left blank as it is overwritten in the
daughter classes.
"""

from Constants import *
from Hitbox import *
import pygame as pygame
from random import randint

class Entity(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.animation_index = 0
        self.load_images()
        self.rect = self.image.get_rect()
        self.x = x * TILE
        self.y = y * TILE
        self.vx = 0
        self.vy = 0
        self.facing = SOUTH
        self.horizontal_facing = EAST
        self.timer = 0
        self.frame_duration = 200/1000
        self.attack_timer = 0
        self.attack_duration = 50/1000
        self.hp = 20
        self.max_hp = self.hp
        self.armour = 10
        self.strength = 2
        self.vitality = VITALITY
        self.agilty = AGILITY

    def health_bar_update(self):
        self.bar = pygame.Surface((TILE, 2))
        self.bar.fill(BLACK)
        self.health_bar = pygame.Surface((int(self.hp / self.max_hp * TILE), 2))
        self.health_bar.fill(RED)

    def update_facing(self):
        if self.vx > 0 and self.vy == 0:
            self.facing = EAST
        elif self.vx < 0 and self.vy == 0:
            self.facing = WEST
        elif self.vx == 0 and self.vy > 0:
            self.facing = SOUTH
        elif self.vx == 0 and self.vy < 0:
            self.facing = NORTH

        if self.facing == EAST or self.facing == WEST:
            self.horizontal_facing = self.facing

    def collisions(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(new_x, new_y, TILE, TILE).colliderect(wall.rect):
                return wall

    def sprite_collision(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.characters:
            if sprite != self:
                if pygame.Rect(sprite.x, sprite.y, TILE, TILE).colliderect(pygame.Rect(new_x, new_y, TILE, TILE)):
                     return sprite

    def x_collision(self):
        new_x = self.x + self.vx * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(new_x, self.y, TILE, TILE).colliderect(wall.rect):
                return wall           

    def y_collision(self):
        new_y = self.y + self.vy * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(self.x, new_y, TILE, TILE).colliderect(wall.rect):
                    return wall            

    def x_position_reset(self, wall):
        if wall:
            if self.vx > 0:
                self.x = wall.x - self.rect.width
                self.vx = 0
            elif self.vx < 0:
                self.x = wall.x + wall.rect.width
                self.vx = 0
                
    def y_position_reset(self, wall):
        if wall:
            if self.vy > 0:
                self.y = wall.rect.y - self.rect.height
                self.vy = 0
            elif self.vy < 0:
                self.y = wall.rect.y + wall.rect.height
                self.vy =0

    def move(self): 
        self.x = self.x + self.vx * self.game.dt
        self.y = self.y + self.vy * self.game.dt

    def damage(self, damage):
        self.hp -= damage        

    def attack(self, dt):
        # determine the kind of weapon the entity has equipped, then determine the hitbox velocity based on that
        if not self.hand or self.hand.max_range == 0:
            vx, vy = 0, 0
        else:
            if self.facing == NORTH:
                vx, vy = 0, -2*PLAYER_SPEED
            elif self.facing == SOUTH:
                vx, vy = 0, 2*PLAYER_SPEED
            elif self.facing == EAST:
                vx, vy = 2*PLAYER_SPEED, 0
            elif self.facing == WEST:
                vx, vy = -2*PLAYER_SPEED, 0
                
        self.attack_timer += dt
        while self.attack_timer >= self.attack_duration:
            self.attack_timer -= self.attack_duration
            Hitbox(self, self.game, vx, vy)

    def rebound(self, attacker_facing):
        #determine the direction the sprite will be rebounded and determine
        #the new x,y coordinates
        if attacker_facing == NORTH:
            new_y = self.y - TILE
            new_x = self.x
        elif attacker_facing == SOUTH:
            new_y = self.y + TILE
            new_x = self.x
        elif attacker_facing == WEST:
            new_x = self.x - TILE
            new_y = self.y
        elif attacker_facing == EAST:
            new_x = self.x + TILE
            new_y = self.y

        #check for potential collisions and if one is encountered, reset the 
        for wall in self.game.walls:
            if pygame.Rect(new_x, new_y, TILE, TILE).colliderect(wall.rect):
                if attacker_facing == NORTH:
                    new_y = wall.y + TILE
                elif attacker_facing == SOUTH:
                    new_y = wall.y - TILE
                elif attacker_facing == WEST:
                    new_x = wall.x + TILE
                elif attacker_facing == EAST:
                    new_x = wall.x - TILE
                
        self.x = new_x
        self.y = new_y
                    
        

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def update(self):
        pass




    
