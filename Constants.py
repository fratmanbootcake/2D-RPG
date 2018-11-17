import os

WIDTH = 320
HEIGHT = 240
TILE = 16
GRID_WIDTH = WIDTH / TILE
GRID_HEIGHT = HEIGHT / TILE
FPS = 30
RUNNING = 'RUNNING'
PAUSED = 'PAUSED'
MENU = 'MENU'
INVENTORY = 'INVENTORY'
CHARACTER_SCREEN = 'CHARACTER_SCREEN' 
LEFT = 1
RIGHT = 3

SWORD = 'sword'
AXE = 'axe'
BATTLEAXE = 'battleaxe'

LEATHER = 'leather'
CHAINMAIL = 'chainmail'
PLATE = 'plate'

QUALITY = 'quality'
WEIGHT = 'weight'
DAMAGE = 'damage'
COST = 'cost'
DAMAGE_TYPE = 'damage type'
RESISTANCE = 'resistance'
ARMOUR = 'armour'
SLASHING = 'slashing'
CRUSHING = 'crushing'
PIERCING = 'piercing'


WEAPONS = {SWORD:{QUALITY:2,
                 WEIGHT:5,
                 DAMAGE_TYPE:SLASHING,
                 DAMAGE:8,
                 COST:20},
           AXE:{QUALITY:2,
               WEIGHT:3,
               DAMAGE_TYPE:SLASHING,
               DAMAGE:6,
               COST:10},
           BATTLEAXE:{QUALITY:1,
               WEIGHT:10,
               DAMAGE_TYPE:SLASHING,
               DAMAGE:10,
               COST:15}
    }

ARMOUR = {LEATHER:{QUALITY:2,
                 WEIGHT:25,
                 RESISTANCE:SLASHING,
                 ARMOUR:3,
                 COST:15},
           CHAINMAIL:{QUALITY:2,
               WEIGHT:3,
               RESISTANCE:SLASHING,
               ARMOUR:6,
               COST:100},
           PLATE:{QUALITY:1,
               WEIGHT:10,
               RESISTANCE:SLASHING,
               ARMOUR:10,
               COST:1500}
    }

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")

PLAYER_SPEED = 160
WALKING = 'WALKING'
STANDING = 'STANDING'
ATTACKING = 'ATTACKING'

NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'
NORTH_EAST = 'NORTH EAST'
NORTH_WEST = 'NORTH WEST'
SOUTH_EAST = 'SOUTH_EAST'
SOUTH_WEST = 'SOUTH_WEST'

