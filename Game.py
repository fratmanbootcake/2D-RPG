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
        #define the screen related constants and set-up the sprite manager
        self.width = WIDTH
        self.height = HEIGHT
        self.tile = TILE
        self.fps = FPS
        self.state = MENU
        self.sprite_manager = SpriteManager(self)

    def create_window(self):
        #initialize the pygame window
        pygame.init()
        pygame.mixer.init()

        #create the screen and clock
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        #define a font
        self.font = pygame.font.Font(None, TILE)
        
    def load_map(self):
        #load the map, add tiles and sprite
        self.map = Map(self, "map.txt")
        self.map.add_tiles()
        self.map.add_sprites()

        #set the current sprite manager's sprites
        self.sprite_manager.add_sprites(self.all_sprites)

    def load_helpers(self):
        #load the camera, animator and renderer classes
        self.camera = Camera(self.map.width, self.map.height)
        self.animator = Animation(self)
        self.Renderer = Renderer(self)

    def new_groups(self):
        #define new groups
        self.walls = []
        self.tiles = []
        self.all_sprites = pygame.sprite.Group()
        self.characters = pygame.sprite.Group()
        self.animations = pygame.sprite.Group()
        self.hitboxes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
    def new_game(self):
        #create a new game
        self.new_groups()
        self.load_map()
        self.load_helpers()

    def state_transition(self, next_state):
        # transition to the next state and update the sprite manager's currently active sprites based on
        # the new game state
        self.state = next_state
        if next_state == INVENTORY:
            self.sprite_manager.add_sprites(self.player.inventory)
            self.order_player_inventory()
        elif next_state == CHARACTER_SCREEN:
            self.sprite_manager.add_sprites(self.player.equipped)
        elif next_state == RUNNING:
            self.sprite_manager.add_sprites(self.all_sprites)

    def update(self):
        #update the sprites and the camera view
        self.sprite_manager.active_sprites.update()
        self.items.update()
        self.camera.update(self.player)

    def order_player_inventory(self):
        #order the player's items in the inventory.
        #need to make sure this properly wraps around the screen once the width of the screen is exceeded.
        for i, item in enumerate(self.player.inventory):
            item.x = i * TILE
            item.y = 0

    def mouse_click_collision(self, position):
        #create a single pixel rectangle located at the position and check whether it collides with
        #and of the sprites in the sprite_manager's active sprites. If there is a collision, the sprite
        #is returned.
        #//NOTE// I couldn't seem to get built-in sprite.collidepoint method to work so I opted to create
        #a single pixel rectangle and this seems to do the job.
        pos_rect = pygame.Rect(position[0], position[1],1,1)
        for sprite in self.sprite_manager.active_sprites:
            sprite_rect = pygame.Rect(sprite.x, sprite.y, TILE, TILE)
            if pos_rect.colliderect(sprite_rect):
                return sprite

    def events(self):
        #get the event based on user input. The game's state is updated by calling the state_transition method.
        #the if/elif block is broken down by the state and the relevant method is called after user input.
        #I'm not happy with this as it's getting longer and longer so refactoring is on the to-do list.
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
                    elif event.key == pygame.K_r:
                        self.state_transition(INVENTORY)
                    elif event.key == pygame.K_c:
                        self.state_transition(CHARACTER_SCREEN)
                    elif event.key == pygame.K_SPACE:
                        self.player.attack(self.dt)
                    elif event.key == pygame.K_e:
                        self.pick_up_item()
            elif self.state == INVENTORY: # inventory
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_r:
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
        #determine if the item is a weapon or a piece of armour. Update the item's (x,y) position based on
        #where the character screen will show the body and weapon slots. The player's hand/body is checked to
        #determine whether an item is being held/worn. If not, the item is added to the relevant slot and to
        #the equipped group. It is then removed from the player's inventory and the sprite manager's active
        #sprite group. If an item is currently being held/worn, the new item is removed from the inventory and
        #sprite manager's active sprites. The held/worn item is then removed from the equipped group and added
        #to the inventory and sprite manager's active sprites. The new item is then added the equipped group
        # and finally the player's hand/body item is set as the item. 
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
        #removes the item from the equipped group and the sprite manager's active sprites
        self.player.equipped.remove(item)
        self.sprite_manager.active_sprites.remove(item)

        #check if the item is either a Weapon or a piece of Armour. The item is added to the inventory and
        #the relevant slot (hand/body) is set to None.
        if isinstance(item, Weapon):
            self.player.inventory.add(item)
            self.player.hand = None
        elif isinstance(item, Armour):
            self.player.inventory.add(item)
            self.player.body = None
            
    def drop_item(self, item):
        #sets the item's x,y coordinates as the same as the player's.
        item.x = self.player.x
        item.y = self.player.y

        #goes through the items in the player's inventory and the player's equipped items and removes from the
        #relevant group and also removes from the sprite manager's active sprites.
        if item in self.player.inventory:
            self.player.inventory.remove(item)
        elif item in self.player.equipped:
            self.player.equipped.remove(item)
        self.sprite_manager.active_sprites.remove(item)

        #adds the item to the game's all_sprites and the game's items groups.
        self.all_sprites.add(item)
        self.items.add(item)

    def pick_up_item(self):
        #cycles through the items and determines whether there is a collision between the player and the item's
        #rectangle. If there is, the item is added to the player's inventory and removed from the game's items,
        #all_sprites and the sprite manager's active sprites.
        for item in self.items:
            if pygame.Rect(self.player.x, self.player.y, TILE, TILE).colliderect(pygame.Rect(item.x, item.y, TILE, TILE)):
                if not self.inventory_limit_reached(item):
                    self.player.inventory.add(item)
                    self.items.remove(item)
                    self.all_sprites.remove(item)
                    self.sprite_manager.active_sprites.remove(item)

    def inventory_limit_reached(self, item):
        #creates the local weight variable and determines the weight of the items in the player's inventory
        #and equipped groups. It then addes the new item's weight and checks if the sum is less than or equal
        #to the player's encumberance limit.
        weight = 0
        for item_ in self.player.inventory:
            weight += item_.weight
        for item_ in self.player.equipped:
            weight += item_.weight
        weight += item.weight
        if weight <= self.player.encumberance:
            return False

    def game_loop(self):
        #create a game window, initialize a new game and set the playing parameter to true.
        self.create_window()
        self.new_game()
        self.playing = True

        #enter the game loop
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
        
