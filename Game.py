import pygame as pygame
import time
import sys
from Constants import *
from Player import *
from Camera import *
from Walls import *
from Map import *

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
        for j, row in enumerate(self.map.data):
            for i, column in enumerate(row):
                if self.map.data[j][i] == '1':
                    wall = Wall(self, i, j)
                    self.all_sprites.add(wall)
                    self.walls.add(wall)
                elif self.map.data[j][i] == 'p':
                    self.player = Player(self, i, j)
                    self.all_sprites.add(self.player)
                elif self.map.data[j][i] == 'M':
                    monster = Monster(self, i, j)
                    self.all_sprites.add(monster)
                    self.monsters.add(monster)
                    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.map = Map("map.txt")
        self.load_map()
        self.camera = Camera(self.map.width, self.map.height)

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
       
    def animate(self, dt):
        self.player.animate(dt)

    def draw_grid(self):
        for x in range(0, WIDTH, TILE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))
            
    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        for sprite in self.all_sprites:
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            elif keys[pygame.K_p]:
                if self.state == RUNNING:
                    self.state = PAUSED
                elif self.state == PAUSED:
                    self.state = RUNNING

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
        
