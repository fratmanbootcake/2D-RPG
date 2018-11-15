import pygame as pygame
from Constants import *
from Button import *
import os

class Renderer:

    def __init__(self, game):
        self.game = game
        self.menu_background = pygame.image.load(os.path.join(image_folder,"background01.png"))
    
    def draw_game(self):
        for element in self.game.tiles:
            self.game.screen.blit(element.image, self.game.camera.offset(element))
        for sprite in self.game.active_sprites:
            self.game.screen.blit(sprite.image, self.game.camera.offset(sprite))
        self.game.screen.blit(self.game.show_fps, (10, 10))
        pygame.display.flip()

    def draw_pause(self):
        PAUSED = self.write_text("PAUSED")        
        self.game.screen.blit(PAUSED, (int((self.game.width - PAUSED.get_size()[0])/2), int((self.game.height - PAUSED.get_size()[1])/2)))
        pygame.display.flip()

    def draw_start_menu(self):
        BUTTON_1 = Button(self.game, TILE, TILE, self.write_text("1: NEW GAME"))
        BUTTON_2 = Button(self.game, TILE, 2*TILE, self.write_text("2: LOAD GAME"))
        BUTTON_3 = Button(self.game, TILE, 3*TILE, self.write_text("3: QUIT"))
        buttons = [BUTTON_1, BUTTON_2, BUTTON_3]
        self.game.screen.blit(self.menu_background, (0,0))
        for button_ in buttons:
            self.game.screen.blit(button_.text, (button_.x, button_.y))
        pygame.display.flip()
        
    def draw_inventory(self):
        pass

    def draw_character_menu(self):
        pass

    def draw_battle(self):
        pass

    def write_text(self, string):
        #takes a string and turns it into a pygame surface
        return self.game.font.render(string, True, BLUE)
        
