"""
Textures.py

This file loads all of the images required in the game.
"""

import pygame as pygame
from Constants import *

#TEXTURES#

GRASS = pygame.image.load(os.path.join(image_folder, "grass.png"))
TREE = pygame.image.load(os.path.join(image_folder, "tree01.png"))
WATER = pygame.image.load(os.path.join(image_folder, "water.png"))
WATER_LEFT = pygame.image.load(os.path.join(image_folder, "water_l.png"))
WATER_BOTTOM_LEFT = pygame.image.load(os.path.join(image_folder, "water_bl.png"))
WATER_BOTTOM = pygame.image.load(os.path.join(image_folder, "water_b.png"))
WATER_TOP_RIGHT_2 = pygame.image.load(os.path.join(image_folder, "water_tr2.png"))
ROOF_1 = pygame.image.load(os.path.join(image_folder, "roof_01.png"))
ROOF_2 = pygame.image.load(os.path.join(image_folder, "roof_02.png"))
ROOF_3 = pygame.image.load(os.path.join(image_folder, "roof_03.png"))
ROOF_4 = pygame.image.load(os.path.join(image_folder, "roof_04.png"))
ROOF_5 = pygame.image.load(os.path.join(image_folder, "roof_05.png"))
ROOF_6 = pygame.image.load(os.path.join(image_folder, "roof_06.png"))
ROOF_7 = pygame.image.load(os.path.join(image_folder, "roof_07.png"))
ROOF_8 = pygame.image.load(os.path.join(image_folder, "roof_08.png"))
ROOF_9 = pygame.image.load(os.path.join(image_folder, "roof_09.png"))
ROOF_10 = pygame.image.load(os.path.join(image_folder, "roof_10.png"))
WALL_2 = pygame.image.load(os.path.join(image_folder, "wall_02.png"))
WINDOW_1 = pygame.image.load(os.path.join(image_folder, "window_01.png"))
BARREL = pygame.image.load(os.path.join(image_folder, "barrel.png"))

#MONSTERS#

DEMON = []
DEMON01 = DEMON.append(pygame.image.load(os.path.join(image_folder, "demon01.png")))
DEMON02 = DEMON.append(pygame.image.load(os.path.join(image_folder, "demon02.png")))
DEMON03 = DEMON.append(pygame.image.load(os.path.join(image_folder, "demon03.png")))
DEMON04 = DEMON.append(pygame.image.load(os.path.join(image_folder, "demon04.png")))

SKELETON = []
SKELETON01 = SKELETON.append(pygame.image.load(os.path.join(image_folder, "skeleton01.png")))
SKELETON02 = SKELETON.append(pygame.image.load(os.path.join(image_folder, "skeleton02.png")))
SKELETON03 = SKELETON.append(pygame.image.load(os.path.join(image_folder, "skeleton03.png")))
SKELETON04 = SKELETON.append(pygame.image.load(os.path.join(image_folder, "skeleton04.png")))

SHADOW = []
SHADOW01 = SHADOW.append(pygame.image.load(os.path.join(image_folder, "shadow01.png")))
SHADOW02 = SHADOW.append(pygame.image.load(os.path.join(image_folder, "shadow02.png")))
SHADOW03 = SHADOW.append(pygame.image.load(os.path.join(image_folder, "shadow03.png")))
SHADOW04 = SHADOW.append(pygame.image.load(os.path.join(image_folder, "shadow04.png")))

#ITEMS#

SWORD01 = pygame.image.load(os.path.join(image_folder, "sword01.png"))
AXE01 = pygame.image.load(os.path.join(image_folder, "axe01.png"))
BATTLEAXE01 = pygame.image.load(os.path.join(image_folder, "battleaxe01.png"))











