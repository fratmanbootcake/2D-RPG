import time
import sys
from Player import *
from Map import *
from Monster import *
from Tiles import *
from Camera import *
from Walls import *
from Renderer import *
from Animation import *



class Game:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.tile = TILE
        self.fps = FPS
        self.state = MENU

    def create_window(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, TILE)

    def load_map(self):
        self.map.add_tiles(self)

        #loads sprites and hitboxes            
        for j, row in enumerate(self.map.data):
            for i, column in enumerate(row):
                if self.map.data[j][i] in ['2','4','5','t','a','b','c','n','m','l','e','j','g','B','D']:
                    wall = Wall(self, i, j)
                    self.walls.append(wall)
                elif self.map.data[j][i] == 'p':
                    self.player = Player(self, i, j)
                    self.all_sprites.add(self.player)
                    self.animations.add(self.player)
                elif self.map.data[j][i] == 'M':
                    monster = Monster(self, i, j)
                    self.all_sprites.add(monster)
                    self.monsters.add(monster)
                    self.animations.add(monster)
                    self.walls.append(monster)
      
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.walls = []
        self.monsters = pygame.sprite.Group()
        self.animations = pygame.sprite.Group()
        self.tiles = []
        self.map = Map("map.txt")
        self.load_map()
        self.camera = Camera(self.map.width, self.map.height)
        self.animator = Animation(self)
        self.Renderer = Renderer(self)

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

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.state == MENU:
                    if event.key == pygame.K_1:
                        self.state = RUNNING
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()
                elif self.state == PAUSED:
                    if event.key == pygame.K_p:
                        self.state = RUNNING
                elif self.state == RUNNING:
                    if event.key == pygame.K_p:
                        self.state = PAUSED
                elif self.state == BATTLE:
                    pass

    def game_loop(self):
        self.create_window()
        self.new()
        self.playing = True
        self.paused = False
        while self.playing:
            self.show_fps = self.font.render(str(int(self.clock.get_fps())), True, WHITE)
            self.clock.tick(self.fps)
            self.dt = self.clock.tick(self.fps) / 1000
            self.events()
            if self.state == MENU:
                self.Renderer.draw_start_menu()
            elif self.state == RUNNING:
                self.update()
                self.animate(self.dt)
                self.Renderer.draw_game()
            elif self.state == PAUSED:
                self.Renderer.draw_pause()
            elif self.state == BATTLE:
                pass



game = Game()
game.game_loop()
        
