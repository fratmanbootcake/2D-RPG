"""
Button.py

This creates a surface at location x, y.
"""

from Constants import *
import pygame as pygame

class Button:

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface

