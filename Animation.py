"""
Animation.py

This handles the animation of sprites by implementing a simple timer.
Once the timer reaches the threshhold frame duration, the sprite's animation
index is progressed by +1. Once the final image is reached, the modulo operator
ensures the images loop back to the beginning.
"""

from Constants import *

class Animation:

    def __init__(self, game):
        self.game = game

    def animate_sprite(self, entity, dt):
        entity.timer += dt
        while entity.timer >= entity.frame_duration:
            entity.timer -= entity.frame_duration
            entity.animation_index += 1
            if entity.horizontal_facing == EAST:
                entity.image = entity.images[2 + entity.animation_index % 2]
            elif entity.horizontal_facing == WEST:
                entity.image = entity.images[entity.animation_index % 2]

    def animate(self, dt):
        for sprite in self.game.all_sprites:
            for sprite in self.game.animations:
                self.animate_sprite(sprite, dt)
