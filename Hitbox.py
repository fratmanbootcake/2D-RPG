import pygame as pygame
from Constants import *

class Hitbox(pygame.sprite.Sprite):

    def __init__(self, attacker, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.attacker = attacker
        self.get_orientation()
        self.get_position()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vx = PLAYER_SPEED
        self.vy = 0
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
        for sprite in self.game.all_sprites:
            if sprite not in self.game.hitboxes and sprite != self.attacker:
                print((sprite.x, sprite.rect.width, sprite.y, sprite.rect.width,
                      self.x, self.width, self.y, self.height))
                if pygame.Rect(sprite.x, sprite.y, sprite.rect.width, sprite.rect.height).colliderect(self.rect):
                    sprite.kill()

    def update(self):
        self.collision()
        self.timer += self.game.dt
        while self.timer > self.duration:
            self.timer -= self.duration
            self.kill()
        



    
        
