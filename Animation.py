from Constants import *

class Animation:

    def __init__(self, game):
        self.game = game

    def animate_sprite(self, entity, dt):
        if entity.state == WALKING:
            entity.timer += dt
            while entity.timer >= entity.frame_duration:
                entity.timer -= entity.frame_duration
                entity.animation_index += 1
                if entity.facing == SOUTH:
                    entity.image = entity.south_images[entity.animation_index % len(entity.south_images)]
                elif entity.facing == WEST:
                    entity.image = entity.west_images[entity.animation_index % len(entity.west_images)]
                elif entity.facing == EAST:
                    entity.image = entity.east_images[entity.animation_index % len(entity.east_images)]
                elif entity.facing == NORTH:
                    entity.image = entity.north_images[entity.animation_index % len(entity.north_images)]
        elif entity.state == STANDING:
            if entity.facing == SOUTH:
                entity.image = entity.south_standing[0]
            elif entity.facing == WEST:
                entity.image = entity.west_standing[0]
            elif entity.facing == EAST:
                entity.image = entity.east_standing[0]
            elif entity.facing == NORTH:
                entity.image = entity.north_standing[0]
