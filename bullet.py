# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage the bullets behavior """ 

    def __init__(self, tg_game):
        """Create the bulllet at the ship current position"""
        super().__init__()

        self.screen = tg_game.screen 
        self.settings = tg_game.settings
        self.color = self.settings.bullet_color 

        # create a bullet and set its position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height) 
        self.rect.midleft = tg_game.ship.ship_image_rect.midright

        # store the decimal value of the x position
        self.x = float(self.rect.x)

    def update(self):
        """Update thehorizontal position of the bullet """
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet on the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)

