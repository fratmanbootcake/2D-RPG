from Constants import *

class Animation:

    def __init__(self, game):
        self.game = game

    def animate(self, entity, dt):
        if entity.state == WALKING:
            entity.timer += dt
            while entity.timer >= entity.frame_duration:
                entity.timer -= entity.frame_duration
                entity.animation_index += 1
                south = entity.animation_index % 3
                west = (entity.animation_index % 3) + 3
                east = (entity.animation_index % 3) + 6
                north = (entity.animation_index % 3) + 9
                if entity.facing == SOUTH:
                    index = south
                elif entity.facing == WEST:
                    index = west
                elif entity.facing == EAST:
                    index = east
                elif entity.facing == NORTH:
                    index = north
                entity.image = entity.images[index]
        elif entity.state == STANDING:
            if entity.facing == SOUTH:
                entity.image = entity.images[1]
            elif entity.facing == WEST:
                entity.image = entity.images[4]
            elif entity.facing == EAST:
                entity.image = entity.images[7]
            elif entity.facing == NORTH:
                entity.image = entity.images[10]
