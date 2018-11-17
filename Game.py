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
from Hitbox import *
from Items import *



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
        self.map.add_tiles()
        self.map.add_sprites()                  
      
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.walls = []
        self.characters = pygame.sprite.Group()
        self.animations = pygame.sprite.Group()
        self.hitboxes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.tiles = []
        self.map = Map(self, "map.txt")
        self.load_map()
        self.camera = Camera(self.map.width, self.map.height)
        self.animator = Animation(self)
        self.Renderer = Renderer(self)

    def update(self):
        self.add_active_sprites()
        self.all_sprites.update()
        self.items.update()
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
            if self.state == MENU: # start menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.state = RUNNING
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()
            elif self.state == PAUSED: # paused
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = RUNNING
                    elif event.key == pygame.K_1:
                        pass
                    elif event.key == pygame.K_2:
                        pass
            elif self.state == RUNNING: # playing
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = PAUSED
                    elif event.key == pygame.K_i:
                        pass # show inventory
                    elif event.key == pygame.K_c:
                        pass # show character screen
                    elif event.key == pygame.K_SPACE:
                        self.player.attack(self.dt, 0, 0)
                    elif event.key == pygame.K_f:
                        self.player.attack(self.dt, 1, 1) # non-zero values used as placeholder until item types have been added
                    elif event.key == pygame.K_g:
                        self.player.pick_up_item()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.player.attack(self.dt, 0, 0)
            elif self.state == INVENTORY:
                pass
            elif self.state == CHARACTER_SCREEN:
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
            elif self.state == INVENTORY:
                pass
            elif self.state == CHARACTER_SCREEN:
                pass



game = Game()
game.game_loop()
        
