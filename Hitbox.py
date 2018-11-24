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
from random import randint

class Hitbox(pygame.sprite.Sprite):

    def __init__(self, attacker, game, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.game.hitboxes.add(self)
        self.game.sprite_manager.active_sprites.add(self)
        self.attacker = attacker
        self.attacker_facing = self.attacker.facing
        self.get_orientation()
        self.get_position()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vx = vx
        self.vy = vy
        self.timer = 0
        self.duration = 50/1000
        self.set_range()

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

    def collides_with_walls(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(new_x, new_y, TILE, TILE).colliderect(pygame.Rect(wall.rect.centerx, wall.rect.centery,2,2)):
                self.kill()

    def set_range(self):
        if self.vx > 0 or self.vy > 0:
            self.range = self.attacker.hand.max_range
        else:
            self.range = 0

    def move(self):
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        if self.vx != 0:
            self.range -= self.vx * self.game.dt
        elif self.vy != 0:
            self.range -= self.vy * self.game.dt

    def stop(self):
        if self.range <= 0:
            self.vy = 0
            self.vx = 0

    def get_damage(self):
        if not self.attacker.hand:
            return randint(1,2) + self.attacker.strength
        else:
            return randint(1,self.attacker.hand.damage) + self.attacker.strength

    def hit_connect(self, sprite):
        if randint(1,20) + self.attacker.strength > sprite.armour:
            return True

    def update(self):
        self.move()
        self.collides_with_walls()
        sprite = self.collision()
        if self.collision():
            if self.hit_connect(sprite):
                sprite.rebound(self.attacker_facing)
                sprite.damage(self.get_damage())
                if not sprite.is_alive() and self.attacker == self.game.player:
                    self.game.player.exp += sprite.exp
        if self.vy == 0 and self.vx == 0:
            self.timer += self.game.dt
            while self.timer > self.duration:
                self.timer -= self.duration
                self.kill()
        else:
            self.stop()


    
        
