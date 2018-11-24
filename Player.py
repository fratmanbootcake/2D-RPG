"""
Player.py

This contains all of the player data and player methods.
"""

from Entity import *

class Player(Entity):

    def __init__(self, game, x, y):
        #initialize the parent class.
        super().__init__(game, x, y)

        #create an inventory sprite group and set a weight limit.
        self.inventory = pygame.sprite.Group()
        self.encumberance = 100

        #create an equipped sprite group and a slot of hand (weapon)
        #and body (armour).
        self.equipped = pygame.sprite.Group()
        self.hand = None
        self.body = None

        #define the starting level (1) and the experience
        #the first element is the current experience and the second is
        #the threshold for leveling up.
        self.level = 1
        self.exp = 0

    def load_images(self):
        #load and append the four images for the player and set the current
        #image as the first image in the list
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior01.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior02.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior03.png")).convert_alpha())
        self.images.append(pygame.image.load(os.path.join(image_folder,"warrior04.png")).convert_alpha())
        self.image = self.images[0]

    def handle_movement(self):
        #reset the movement
        self.vx = 0
        self.vy = 0

        #determine if a movement key (w,a,s,d) is being pressed and set the
        #player speed if one is currently pressed.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
        elif keys[pygame.K_w]:
            self.vy = -PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.vy = PLAYER_SPEED


    def move(self):
        #update the players position
        self.x = int(self.x + self.vx * self.game.dt)
        self.y = int(self.y + self.vy * self.game.dt)

    def level_up(self):
        #check if the player's experience exceeds the threshold for the next level
        if self.exp >= LEVELS[self.level]:
            self.exp -= LEVELS[self.level]
            self.level += 1
    
    def update(self):
        #set player's velocity and update the facing
        self.handle_movement()
        self.update_facing()
        
        #determine if the player collides with any sprite and if there is a
        #collision, reset the player's position
        if self.collisions():
            if self.x_collision():
                self.x_position_reset(self.x_collision())
            if self.y_collision():
                self.y_position_reset(self.y_collision())

        #move the player
        self.move()

        #update the player's health bar
        self.health_bar_update()

        #check if the player is ready to level up
        self.level_up()
