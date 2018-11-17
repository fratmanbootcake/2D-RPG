import pygame as pygame
import random
from Constants import *

class Item(pygame.sprite.Sprite):

    def __init__(self, x, y, filename, cost, weight):
        pygame.sprite.Sprite.__init__(self)
        self.x = x * TILE
        self.y = y * TILE
        self.image = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()
        self.rect = self.image.get_rect()
        self.cost = cost
        self.weight = weight

    def use_item(self):
        pass

class Weapon(Item):

    def __init__(self, x, y, filename, quality, weight, damage, cost, damage_type):
        super().__init__(x, y, filename, cost, weight)
        self.quality = quality
        self.damage = damage
        self.damage_type = damage_type

class Armour(Item):

    def __init__(self, x, y, filename, quality, weight, armour, cost, resistance):
        super().__init__(x, y, filename, cost, weight)
        self.quality = quality
        self.armour = armour
        self.resistance = resistance
       


        
class Factory:

    def create_weapon(self, x, y):
        weapon = random.choice(list(WEAPONS))
        quality = random.randint(1,WEAPONS[weapon][QUALITY])
        weight = WEAPONS[weapon][WEIGHT]
        damage = WEAPONS[weapon][DAMAGE]
        damage_type = WEAPONS[weapon][DAMAGE_TYPE]
        cost = WEAPONS[weapon][COST]
        filename = "{}{}".format(weapon,"01.png")
        return Weapon(x, y, filename, quality, weight, damage, cost, damage_type)

    def create_armour(self):
        armour = random.choice(list(ARMOUR))
        quality = random.randint(1,ARMOUR[armour][QUALITY])
        weight = ARMOUR[armour][WEIGHT]
        armour = ARMOUR[armour][DAMAGE]
        resistance = ARMOUR[armour][RESISTANCE]
        cost = ARMOUR[armour][COST]
        filename = "{}{}".format(weapon,"01.png")
        return Armour(x, y, filename, quality, weight, armour, cost, resistance)

    def create_loot(self):
        pass

   
