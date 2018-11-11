import pygame as pygame
import time
import sys
from Constants import *
from Player import *
from Camera import *
from Walls import *
from Map import *
from Animation import *
from Monster import *
from Tiles import *

class Game:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.tile = TILE
        self.fps = FPS
        self.grid_height = self.height / self.tile
        self.grid_width = self.width / self.tile
        self.state = RUNNING

    def create_window(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def load_map(self):
        #loads map tiles
        for j, row in enumerate(self.map.data):
            for i, column in enumerate(row):
                if self.map.data[j][i] == '1':
                    self.tiles.append(Water(self, i, j))
                elif self.map.data[j][i] == '2':
                    self.tiles.append(WaterBottom(self, i, j))
                elif self.map.data[j][i] == '3':
                    self.tiles.append(WaterTopRight2(self, i, j))
                elif self.map.data[j][i] == '4':
                    self.tiles.append(WaterLeft(self, i, j))
                elif self.map.data[j][i] == '5':
                    self.tiles.append(WaterBottomLeft(self, i, j))
                elif self.map.data[j][i] == 'T' or self.map.data[j][i] == 't' :
                    self.tiles.append(Tree(self, i, j))
                else:
                    self.tiles.append(Grass(self, i, j))

        #loads sprites and hitboxes            
        for j, row in enumerate(self.map.data):
            for i, column in enumerate(row):
                if self.map.data[j][i] == '2' or self.map.data[j][i] == '4' or self.map.data[j][i] == '5' or self.map.data[j][i] == 't':
                    wall = Wall(self, i, j)
                    self.all_sprites.add(wall)
                    self.walls.add(wall)
                elif self.map.data[j][i] == 'p':
                    self.player = Player(self, i, j)
                    self.all_sprites.add(self.player)
                    self.animations.add(self.player)
                elif self.map.data[j][i] == 'M':
                    monster = Monster(self, i, j)
                    self.all_sprites.add(monster)
                    self.monsters.add(monster)
                    self.animations.add(monster)
                    self.walls.add(monster)
                                    
                    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.animations = pygame.sprite.Group()
        self.tiles = []
        self.map = Map("map.txt")
        self.load_map()
        self.camera = Camera(self.map.width, self.map.height)
        self.animator = Animation(self)

    def update(self):
        self.add_active_sprites()
        self.all_sprites.update()
        self.camera.update(self.player)
       
    def animate(self, dt):
        for sprite in self.active_sprites:
            for sprite in self.animations:
                self.animator.animate_sprite(sprite, dt)

    def add_active_sprites(self):
        self.active_sprites.empty()
        for sprite in self.all_sprites:
            sprite_offset = self.camera.offset(sprite)
            if sprite_offset[0] >= 0 or sprite_offset[0] <= self.width:
                if sprite_offset[1] >= 0 or sprite_offset[1] <= self.height:
                    self.active_sprites.add(sprite)

    def draw_grid(self):
        for x in range(0, WIDTH, TILE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))
            
    def draw(self):
        for element in self.tiles:
            self.screen.blit(element.image, self.camera.offset(element))
        for sprite in self.active_sprites:
            self.screen.blit(sprite.image, self.camera.offset(sprite))
        pygame.display.flip()

    def draw_pause(self):
        self.screen.fill(WHITE)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if self.state == RUNNING:
                        self.state = PAUSED
                    elif self.state == PAUSED:
                        self.state = RUNNING
                elif event.key == pygame.K_i:
                    pass # show inventory
                elif event.key == pygame.K_c:
                    pass # show character info
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                pass

    def game_loop(self):
        self.create_window()
        self.new()
        self.playing = True
        self.paused = False
        while self.playing:
            self.clock.tick(self.fps)
            self.dt = self.clock.tick(self.fps) / 1000
            self.events()
            if self.state == RUNNING:
                self.update()
                self.animate(self.dt)
                self.draw()
            elif self.state == PAUSED:
                self.draw_pause()



game = Game()
game.game_loop()
        
