from Constants import *
from Hitbox import *
import pygame as pygame
from random import randint

class Entity(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.north_images = []
        self.south_images = []
        self.east_images = []
        self.west_images = []
        self.north_standing = []
        self.south_standing = []
        self.east_standing = []
        self.west_standing = []
        self.attacking_images = []
        self.animation_index = 0
        self.load_images()
        self.rect = self.image.get_rect()
        self.x = x * TILE
        self.y = y * TILE
        self.vx = 0
        self.vy = 0
        self.state = STANDING
        self.facing = SOUTH
        self.timer = 0
        self.frame_duration = 50/1000
        self.attack_timer = 0
        self.attack_duration = 50/1000
        self.hp = 20
        self.armour = 10
        self.strength = 2

    def update_facing(self):
        if self.vx > 0 and self.vy == 0:
            self.facing = EAST
        elif self.vx < 0 and self.vy == 0:
            self.facing = WEST
        elif self.vx == 0 and self.vy > 0:
            self.facing = SOUTH
        elif self.vx == 0 and self.vy < 0:
            self.facing = NORTH
        elif self.vx > 0 and self.vy > 0:
            self.facing = SOUTH_EAST
        elif self.vx < 0 and self.vy > 0:
            self.facing = SOUTH_WEST
        elif self.vx > 0 and self.vy < 0:
            self.facing = NORTH_EAST
        elif self.vx < 0 and self.vy < 0:
            self.facing = NORTH_WEST

    def collisions(self):
        new_x = self.x + self.vx * self.game.dt
        new_y = self.y + self.vy * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(new_x, new_y, TILE, self.rect.height).colliderect(wall.rect):
                return wall            

    def x_collision(self):
        new_x = self.x + self.vx * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(new_x, self.y, TILE, self.rect.height).colliderect(wall.rect):
                return wall           

    def y_collision(self):
        new_y = self.y + self.vy * self.game.dt
        for wall in self.game.walls:
            if pygame.Rect(self.x, new_y, TILE, self.rect.height).colliderect(wall.rect):
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
        if self.vx != 0 or self.vy !=0:
            self.state = WALKING
        else:
            self.state = STANDING

    def damage(self, attacker):
        self.hp -= randint(1, 8) + attacker.strength        

    def attack(self, dt, vx, vy):
        if vx != 0 or vy != 0:
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
            hit = Hitbox(self, self.game, vx, vy)
            self.game.hitboxes.add(hit)
            self.game.all_sprites.add(hit)

    def hit_connect(self, sprite):
        if randint(1,20) + self.strength > sprite.armour:
            return True

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def update(self):
        pass
