"""
Game.py

This containts and updates the game data, handles events and runs the game loop.
"""

import time
import sys
from Camera import *
from Renderer import *
from Animation import *
from SpriteManager import *


class Game:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.tile = TILE
        self.fps = FPS
        self.state = MENU
        self.sprite_manager = SpriteManager(self)

    def create_window(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, TILE)
        
    def load_map(self):
        self.map = Map(self, "map.txt")
        self.map.add_tiles()
        self.map.add_sprites()
        self.sprite_manager.add_sprites(self.all_sprites)

    def load_helpers(self):
        self.camera = Camera(self.map.width, self.map.height)
        self.animator = Animation(self)
        self.Renderer = Renderer(self)

    def new_groups(self):
        self.walls = []
        self.tiles = []
        self.all_sprites = pygame.sprite.Group()
        self.characters = pygame.sprite.Group()
        self.animations = pygame.sprite.Group()
        self.hitboxes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
    def new_game(self):
        self.new_groups()
        self.load_map()
        self.load_helpers()

    def state_transition(self, next_state):
        # the idea here is to define a single group of sprite which updates based on the next state
        # this group is then used to draw in the Renderer class.
        # For example, when the state is RUNNING, the group has the player, the monsters, items etc
        # this group will be blitted onto the screen.
        # When the state transitions to INVENTORY, the group is emptied and populated with the items
        # in the players inventory
        self.state = next_state
        if next_state == INVENTORY:
            self.sprite_manager.add_sprites(self.player.inventory)
            self.order_player_inventory()
        elif next_state == CHARACTER_SCREEN:
            self.sprite_manager.add_sprites(self.player.equipped)
        elif next_state == RUNNING:
            self.sprite_manager.add_sprites(self.all_sprites)
        pass

    def update(self):
        self.sprite_manager.active_sprites.update()
        self.items.update()
        self.camera.update(self.player)

    def order_player_inventory(self):
        # need to make sure this properly wraps around the screen
        for i, item in enumerate(self.player.inventory):
            item.x = i * TILE
            item.y = 0

    def mouse_click_collision(self, position):
        pos_rect = pygame.Rect(position[0], position[1],1,1)
        for sprite in self.sprite_manager.active_sprites:
            sprite_rect = pygame.Rect(sprite.x, sprite.y, TILE, TILE)
            if pos_rect.colliderect(sprite_rect):
                return sprite

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.state == MENU: # start menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.state_transition(RUNNING)
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()
            elif self.state == PAUSED: # paused
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state_transition(RUNNING)
                    elif event.key == pygame.K_1:
                        pass
                    elif event.key == pygame.K_2:
                        pass
            elif self.state == RUNNING: # playing
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state_transition(PAUSED)
                    elif event.key == pygame.K_i:
                        self.state_transition(INVENTORY)
                    elif event.key == pygame.K_c:
                        self.state_transition(CHARACTER_SCREEN)
                    elif event.key == pygame.K_SPACE:
                        self.player.attack(self.dt, 0, 0)
                    elif event.key == pygame.K_f:
                        self.player.attack(self.dt, 1, 1) # non-zero values used as placeholder until item types have been added
                    elif event.key == pygame.K_g:
                        self.pick_up_item()
            elif self.state == INVENTORY: # inventory
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        self.state_transition(RUNNING)
                    if event.key == pygame.K_c:
                        self.state_transition(CHARACTER_SCREEN)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    item = self.mouse_click_collision(pygame.mouse.get_pos())
                    if item:
                        if event.button == LEFT:
                            self.equip_item(item)
                        elif event.button == RIGHT:
                            self.drop_item(item)
            elif self.state == CHARACTER_SCREEN: # character screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_c:
                        self.state_transition(RUNNING)
                    elif event.key == pygame.K_i:
                        self.state_transition(INVENTORY)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    item = self.mouse_click_collision(pygame.mouse.get_pos())
                    if item:
                        if event.button == LEFT:
                            self.unequip_item(item)
                        elif event.button == RIGHT:
                            self.drop_item(item)

    def equip_item(self, item):
        if isinstance(item, Weapon):
            item.x = 6*TILE
            item.y = 7*TILE
            if not self.player.hand:
                self.player.hand = item
                self.player.equipped.add(item)
                self.player.inventory.remove(item)
                self.sprite_manager.active_sprites.remove(item)
            else:
                self.player.inventory.remove(item)
                self.sprite_manager.active_sprites.remove(item)
                self.player.equipped.remove(self.player.hand)
                self.player.inventory.add(self.player.hand)
                self.sprite_manager.active_sprites.add(self.player.hand)
                self.player.equipped.add(item)
                self.player.hand = item
        elif isinstance(item, Armour):
            item.x = 7*TILE
            item.y = 7*TILE
            if not self.player.body:
                self.player.body = item
                self.player.equipped.add(item)
                self.player.inventory.remove(item)
                self.sprite_manager.active_sprites.remove(item)
            else:
                self.player.inventory.remove(item)
                self.sprite_manager.active_sprites.remove(item)
                self.player.equipped.remove(self.player.body)
                self.player.inventory.add(self.player.body)
                self.sprite_manager.active_sprites.add(self.player.body)
                self.player.equipped.add(item)
                self.player.body = item
        self.order_player_inventory()

    def unequip_item(self, item):
        self.player.equipped.remove(item)
        self.sprite_manager.active_sprites.remove(item)
        if isinstance(item, Weapon):
            self.player.inventory.add(item)
            self.player.hand = None
        elif isinstance(item, Armour):
            self.player.inventory.add(item)
            self.player.body = None
            
    def drop_item(self, item):
        item.x = self.player.x
        item.y = self.player.y
        if item in self.player.inventory:
            self.player.inventory.remove(item)
        elif item in self.player.equipped:
            self.player.equipped.remove(item)
        self.sprite_manager.active_sprites.remove(item)
        self.all_sprites.add(item)
        self.items.add(item)

    def pick_up_item(self):
        for item in self.items:
            if pygame.Rect(self.player.x, self.player.y, TILE, TILE).colliderect(pygame.Rect(item.x, item.y, TILE, TILE)):
                if not self.inventory_limit_reached(item):
                    self.player.inventory.add(item)
                    self.items.remove(item)
                    self.all_sprites.remove(item)
                    self.sprite_manager.active_sprites.remove(item)

    def inventory_limit_reached(self, item):
        weight = 0
        for item_ in self.player.inventory:
            weight += item_.weight
        weight += item.weight
        if weight <= self.player.encumberance:
            return False

    def game_loop(self):
        self.create_window()
        self.new_game()
        self.playing = True
        while self.playing:
            self.show_fps = self.font.render(str(int(self.clock.get_fps())), True, WHITE)
            self.clock.tick(self.fps)
            self.dt = self.clock.tick(self.fps) / 1000
            self.events()
            if self.state == MENU:
                self.Renderer.draw_start_menu()
            elif self.state == RUNNING:
                self.update()
                self.animator.animate(self.dt)
                self.Renderer.draw_game()
            elif self.state == PAUSED:
                self.Renderer.draw_pause()
            elif self.state == INVENTORY:
                self.Renderer.draw_inventory()
            elif self.state == CHARACTER_SCREEN:
                self.Renderer.draw_character_screen()



game = Game()
game.game_loop()
        
