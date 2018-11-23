"""
Items.py

This contains the classes for items. The items are based on the pygame sprite
class and the various types of items are subclasses of an Item base class.

An item Factory allows for randomising the creation of items. The relevant
information is obtained from dictionaries in Constants.py.
"""

import pygame as pygame
import random
from Constants import *

class Item(pygame.sprite.Sprite):

    def __init__(self, x, y, filename, value, weight):
        pygame.sprite.Sprite.__init__(self)
        self.x = x * TILE
        self.y = y * TILE
        self.image = pygame.image.load(os.path.join(image_folder, filename)).convert_alpha()
        self.rect = self.image.get_rect()
        self.value = value
        self.weight = weight

    def use_item(self):
        pass

class Weapon(Item):

    def __init__(self, x, y, filename, quality, weight, damage, value, damage_type, hand, max_range):
        super().__init__(x, y, filename, value, weight)
        self.quality = quality
        self.damage = damage
        self.damage_type = damage_type
        self.hand = hand
        self.max_range = max_range

class Armour(Item):

    def __init__(self, x, y, filename, quality, weight, armour, value, resistance, body):
        super().__init__(x, y, filename, value, weight)
        self.quality = quality
        self.armour = armour
        self.resistance = resistance
        self.body = body
       

        
class Factory:

    def create_weapon(self, x, y):
        weapon = random.choice(list(WEAPONS))
        quality = random.randint(1,WEAPONS[weapon][QUALITY])
        weight = WEAPONS[weapon][WEIGHT]
        damage = WEAPONS[weapon][DAMAGE]
        damage_type = WEAPONS[weapon][DAMAGE_TYPE]
        value = WEAPONS[weapon][VALUE]
        hand = WEAPONS[weapon][HAND]
        max_range = WEAPONS[weapon][MAX_RANGE]
        filename = "{}{}".format(weapon,"01.png")
        return Weapon(x, y, filename, quality, weight, damage, value, damage_type, hand, max_range)

    def create_armour(self, x, y):
        armour = random.choice(list(ARMOURS))
        quality = random.randint(1,ARMOURS[armour][QUALITY])
        weight = ARMOURS[armour][WEIGHT]
        defence = ARMOURS[armour][ARMOUR]
        resistance = ARMOURS[armour][RESISTANCE]
        value = ARMOURS[armour][VALUE]
        body = ARMOURS[armour][BODY]
        filename = "{}{}".format(armour,"01.png")
        return Armour(x, y, filename, quality, weight, defence, value, resistance, body)

    def create_loot(self):
        pass


   
