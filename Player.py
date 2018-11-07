import pygame as pygame
from Constants import *

class Player(pygame.sprite.Sprite):

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
        self.state = STANDING
        self.facing = SOUTH
        self.timer = 0
        self.frame_duration = 50/1000

    def load_images(self):
        self.images.append(pygame.image.load(os.path.join(image_folder,"char01.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char02.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char03.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char04.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char05.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char06.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char07.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char08.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char09.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char10.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char11.png")).convert())
        self.images.append(pygame.image.load(os.path.join(image_folder,"char12.png")).convert())
        for image in self.images:
            image.set_colorkey(pygame.Color('#f6ffff'))
        self.image = self.images[self.animation_index]

    def animate(self, dt):
        if self.state == WALKING:
            self.timer += dt
            while self.timer >= self.frame_duration:
                self.timer -= self.frame_duration
                self.animation_index += 1
                south = self.animation_index % 3
                west = (self.animation_index % 3) + 3
                east = (self.animation_index % 3) + 6
                north = (self.animation_index % 3) + 9
                if self.facing == SOUTH:
                    index = south
                elif self.facing == WEST:
                    index = west
                elif self.facing == EAST:
                    index = east
                elif self.facing == NORTH:
                    index = north
                self.image = self.images[index]
        elif self.state == STANDING:
            if self.facing == SOUTH:
                self.image = self.images[1]
            elif self.facing == WEST:
                self.image = self.images[4]
            elif self.facing == EAST:
                self.image = self.images[7]
            elif self.facing == NORTH:
                self.image = self.images[10]

    def handle_event(self):
        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.vx = PLAYER_SPEED
        elif keys[pygame.K_UP]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.vy = PLAYER_SPEED

        #if self.vx != 0 and self.vy != 0:
        #    self.vx = 0.7101 * self.vx
        #    self.vy = 0.7101 * self.vy

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
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, new_y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def x_collision(self):
        new_x = self.x + self.vx * self.game.dt
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(new_x, self.y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def y_collision(self):
        new_y = self.y + self.vy * self.game.dt
        for sprite in self.game.all_sprites:
            if sprite in self.game.walls:
                if pygame.Rect(self.x, new_y, TILE, self.rect.height).colliderect(sprite):
                    return sprite

    def x_position_reset(self, sprite):
        if sprite:
            if self.vx > 0:
                self.x = sprite.x - TILE
                self.vx = 0
            elif self.vx < 0:
                self.x = sprite.x + TILE
                self.vx = 0
                
    def y_position_reset(self, sprite):
        if sprite:
            if self.vy > 0:
                self.y = sprite.y - self.rect.height
                self.vy = 0
            elif self.vy < 0:
                self.y = sprite.y + TILE
                self.vy =0

    def move(self): 
        self.x = self.x + self.vx * self.game.dt
        self.y = self.y + self.vy * self.game.dt
        if self.vx != 0 or self.vy !=0:
            self.state = WALKING
        else:
            self.state = STANDING
    
    def update(self):
        self.handle_event()
        self.update_facing()
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())
        self.move()
