"""
Renderer.py

This handles all of the drawing to the screen. Each possible screen / menu
is handled separately within its own method. The helper method takes a string
and returns a pygame surface which can be passed to the Button class.

The Button class simply defines a surface at location x, y.
"""

import pygame as pygame
from Constants import *
from Textures import *
import os

class Renderer:

    def __init__(self, game):
        self.game = game
        self.menu_background = pygame.image.load(os.path.join(image_folder,"background01.png"))

    def draw_start_menu(self):
        BUTTON_1 = Button(TILE, TILE, self.write_text("1: NEW GAME"))
        BUTTON_2 = Button(TILE, 2*TILE, self.write_text("2: LOAD GAME"))
        BUTTON_3 = Button(TILE, 3*TILE, SWORD01)
        buttons = [BUTTON_1, BUTTON_2, BUTTON_3]
        self.game.screen.blit(self.menu_background, (0,0))
        for button_ in buttons:
            self.game.screen.blit(button_.surface, (button_.x, button_.y))
        pygame.display.flip()
    
    def draw_game(self):
        for element in self.game.tiles:
            self.game.screen.blit(element.image, self.game.camera.offset(element))

        for sprite in self.game.sprite_manager.active_sprites: 
            self.game.screen.blit(sprite.image, self.game.camera.offset(sprite))
            if sprite in self.game.characters:
                self.game.screen.blit(sprite.bar, self.game.camera.offset(sprite))
                self.game.screen.blit(sprite.health_bar, self.game.camera.offset(sprite))
        
        self.game.screen.blit(self.game.show_fps, (10, 10))
        pygame.display.flip()

    def draw_pause(self):
        PAUSED = self.write_text("PAUSED")        
        self.game.screen.blit(PAUSED, (int((self.game.width - PAUSED.get_size()[0])/2), int((self.game.height - PAUSED.get_size()[1])/2)))
        pygame.display.flip()
        
    def draw_inventory(self):         
        self.game.screen.blit(self.game.sprite_manager.background, (0,0))
        for item in self.game.sprite_manager.active_sprites:
            self.game.screen.blit(item.image, (item.x, item.y))           
        pygame.display.flip()

    def draw_character_screen(self):
        self.game.screen.blit(self.menu_background, (0,0))
        for item in self.game.sprite_manager.active_sprites:
            self.game.screen.blit(item.image, (item.x, item.y))           
        pygame.display.flip()

    def draw_character_creation(self):
        pass

    def write_text(self, string):
        #takes a string and turns it into a pygame surface
        return self.game.font.render(string, True, BLUE)

class Button:

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
        
