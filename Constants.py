"""
Constants.py

This contains all of the constants that are used in the game. It also defines
the relevant stats for each item.
"""

import os

#define the game screen constants
WIDTH = 320
HEIGHT = 240
TILE = 16
GRID_WIDTH = WIDTH / TILE
GRID_HEIGHT = HEIGHT / TILE
FPS = 30

#define the game states
RUNNING = 'RUNNING'
PAUSED = 'PAUSED'
MENU = 'MENU'
INVENTORY = 'INVENTORY'
CHARACTER_SCREEN = 'CHARACTER_SCREEN'

#define the player attributes
STRENGTH = 'strength'
VITALITY = 'vitality'
AGILITY = 'agility'

#define the experience curve
def experience_thresholds():
    exp = []
    for i in range(21):
        if i < 11:
            exp.append(int(round(2*(2.5**i),-2)/4) + i*250)
        elif i < 21:
            exp.append(int(round(2*(1.7**(i+8)),-2)/4))
        else:
            exp.append(int(round(1.05*(2**(i+2)),-2)/4))
    return exp


LEVELS = experience_thresholds()

#define the pygame mouse click values for left and right mouse buttons
LEFT = 1
RIGHT = 3

#define the weapons
SWORD = 'sword'
AXE = 'axe'
BATTLEAXE = 'battleaxe'
LONGBOW = 'longbow'

#define the armours
LEATHER = 'leather'
CHAINMAIL = 'chainmail'
PLATE = 'plate'

#define the item parameters
QUALITY = 'quality'
WEIGHT = 'weight'
DAMAGE = 'damage'
VALUE = 'value'
DAMAGE_TYPE = 'damage type'
MAX_RANGE = 'max range'
RESISTANCE = 'resistance'
ARMOUR = 'armour'
SLASHING = 'slashing'
CRUSHING = 'crushing'
PIERCING = 'piercing'

#define the handedness 
HAND = 'hand'
LEFT_HAND = 'left hand'
RIGHT_HAND = 'right hand'

#define the body part
BODY = 'body'
HEAD = 'head'
TORSO = 'torso'

#define the concrete parameter values for the various weapons
WEAPONS = {SWORD:{QUALITY:2,
                 WEIGHT:5,
                 DAMAGE_TYPE:SLASHING,
                 HAND:RIGHT_HAND,
                 MAX_RANGE:0,
                 DAMAGE:8,
                 VALUE:20},
           AXE:{QUALITY:2,
               WEIGHT:3,
               DAMAGE_TYPE:SLASHING,
               HAND:RIGHT_HAND,
               MAX_RANGE:0,
               DAMAGE:6,
               VALUE:10},
           BATTLEAXE:{QUALITY:1,
               WEIGHT:10,
               DAMAGE_TYPE:SLASHING,
               HAND:RIGHT_HAND,
               MAX_RANGE:0,
               DAMAGE:10,
               VALUE:15},
           LONGBOW:{QUALITY:2,
               WEIGHT:5,
               DAMAGE_TYPE:PIERCING,
               HAND:LEFT_HAND,
               MAX_RANGE:12*TILE,
               DAMAGE:8,
               VALUE:10}
    }

#define the concrete parameter values for the various armours
ARMOURS = {LEATHER:{QUALITY:2,
                 WEIGHT:25,
                 ARMOUR:3,
                 RESISTANCE:SLASHING,
                 BODY:TORSO,
                 VALUE:15},
           CHAINMAIL:{QUALITY:2,
               WEIGHT:3,
               RESISTANCE:SLASHING,
               BODY:TORSO,
               ARMOUR:6,
               VALUE:100},
           PLATE:{QUALITY:1,
               WEIGHT:10,
               RESISTANCE:SLASHING,
               BODY:TORSO,
               ARMOUR:10,
               VALUE:1500}
    }

#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#define folder paths
game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")

#define player-related constants and states
PLAYER_SPEED = 120
WALKING = 'WALKING'
STANDING = 'STANDING'
ATTACKING = 'ATTACKING'

#define monster states
IDLE = 'IDLE'
HUNTING = 'HUNTING'
SLEEP = 'SLEEP'

#define the directions/facing
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'
NORTH_EAST = 'NORTH EAST'
NORTH_WEST = 'NORTH WEST'
SOUTH_EAST = 'SOUTH_EAST'
SOUTH_WEST = 'SOUTH_WEST'










        
