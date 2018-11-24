"""
Helper.py

A series a utility functions such as rounding numbers to the nearest integer or
simulating a dice roll.
"""

from math import floor
from random import randint

def number_round(number, base):
	r = number/base - floor(number/base)
	if r < 0.5:
		return base*int(floor(number/base))
	else:
		return base*int(floor(number/base)+1)

def die_roll(sides):
    return randint(1,sides)
