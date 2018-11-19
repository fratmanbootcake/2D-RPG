"""
Hitbox.py

This creates the Hitbox class. The class remembers who spawned it to allow
attacker stats to be used in the subsequent damage calls.

The update runs a collision detection, excluding the sprite that spawned it, and
when a collision occurs, the colliding sprites damage function is called.
"""

import pygame as pygame
from Camera import *
from Constants import *

class Hitbox(pygame.sprite.Sprite):

    def __init__(self, attacker, game, vx = 0, vy = 0):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.attacker = attacker
        self.get_orientation()
        self.get_position()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vx = vx
        self.vy = vy
        self.timer = 0
        self.duration = 50/1000
        self.range = 8*TILE

    def get_position(self):
        if self.attacker.facing == NORTH:
            self.x = self.attacker.x + int(self.attacker.rect.width / 2)
            self.y = self.attacker.y - self.height
        elif self.attacker.facing == SOUTH:
            self.x = self.attacker.x + int(self.attacker.rect.width / 2)
            self.y = self.attacker.y + self.attacker.rect.height
        elif self.attacker.facing == WEST:
            self.x = self.attacker.x - self.width
            self.y = self.attacker.y + int(self.attacker.rect.width / 2)
        elif self.attacker.facing == EAST:
            self.x = self.attacker.x + self.attacker.rect.width
            self.y = self.attacker.y + int(self.attacker.rect.height / 2)

    def get_orientation(self):
        if self.attacker.facing == NORTH or self.attacker.facing == SOUTH:
            self.width = 1
            self.height = int(3*TILE/4)
        elif self.attacker.facing == EAST or self.attacker.facing == WEST:
            self.width = int(3*TILE/4)
            self.height = 1

    def collision(self):
        hitbox_rect = pygame.Rect(self.x + self.vx * self.game.dt, self.y + self.vy * self.game.dt, self.width, self.height)
        for sprite in self.game.characters:
            if sprite != self.attacker:
                sprite_rect = pygame.Rect(sprite.x + int(TILE/4) + sprite.vx * self.game.dt, sprite.y + int(TILE/4) + sprite.vy * self.game.dt, sprite.rect.width, sprite.rect.height)
                if hitbox_rect.colliderect(sprite_rect):
                    self.kill()
                    return sprite

    def move(self):
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.range -= 0
        if self.vx != 0:
            self.range -= self.vx * self.game.dt
        elif self.vy != 0:
            self.range -= self.vy * self.game.dt

    def destruct(self):
        if self.range <= 0:
            self.vy = 0
            self.vx = 0

    def update(self):
        self.move()
        sprite = self.collision()
        if self.collision():
            if self.attacker.hit_connect(sprite):
                sprite.damage(self.attacker)
                sprite.rebound(self.attacker)
        if self.vy == 0 and self.vx == 0:
            self.timer += self.game.dt
            while self.timer > self.duration:
                self.timer -= self.duration
                self.kill()
        else:
            self.destruct()


    
        
