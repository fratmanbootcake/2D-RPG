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
            self.width = 5
            self.height = TILE
        elif self.attacker.facing == EAST or self.attacker.facing == WEST:
            self.width = TILE
            self.height = 5

    def collision(self):
        hitbox_rect = pygame.Rect(self.x + self.vx * self.game.dt, self.y + self.vy * self.game.dt, self.width, self.height)
        for sprite in self.game.all_sprites:
            if sprite not in self.game.hitboxes and sprite != self.attacker:
                sprite_rect = pygame.Rect(sprite.x + sprite.vx * self.game.dt, sprite.y + sprite.vy * self.game.dt, sprite.rect.width, sprite.rect.height)
                if hitbox_rect.colliderect(sprite_rect):
                    sprite.kill()

    def move(self):
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

    def destruct(self):
        offset_position = self.game.camera.offset(self)
        if offset_position[0] < 0 or offset_position[0] > WIDTH:
            self.kill()
        elif offset_position[1] < 0 or offset_position[1] > HEIGHT:
            self.kill()

    def update(self):
        self.move()
        self.collision()
        if self.vy == 0 and self.vx == 0:
            self.timer += self.game.dt
            while self.timer > self.duration:
                self.timer -= self.duration
                self.kill()
        else:
            self.destruct()


    
        
