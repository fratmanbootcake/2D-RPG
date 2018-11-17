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
