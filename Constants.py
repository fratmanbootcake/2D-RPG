import os

WIDTH = 640
HEIGHT = 640
TILE = 32
GRID_WIDTH = WIDTH / TILE
GRID_HEIGHT = HEIGHT / TILE
FPS = 30
RUNNING = 'RUNNING'
PAUSED = 'PAUSED'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")

PLAYER_SPEED = 360
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

