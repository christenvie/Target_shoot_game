# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game

import pygame

class Ship:
    """A class to manage a ship behavior """

    def __init__(self,tg_game):
        """Initialize the ship and set its starting position """
        # Take the screen settings and its rectangle 
        self.settings = tg_game.settings
        self.screen = tg_game.screen 
        self.screen_rect = self.screen.get_rect()

        # loading the ship and getting its rectangle 
        self.ship_image = pygame.image.load("images/ship2.bmp") 
        self.ship_image_rect = self.ship_image.get_rect()

        # start each new ship at the left side of the screen
        self.ship_image_rect.bottom = self.screen_rect.bottom

        #store decimal position of the ship y value
        self.y = float(self.ship_image_rect.y)

        #flag movement 
        self.moving_up = False
        self.moving_down =False  

    def update(self):
        """Update the ship position based on the movement's flag """
        if self.moving_up and self.ship_image_rect.top >= 0:
            self.y  -=self.settings.ship_speed
        if self.moving_down and self.ship_image_rect.bottom <= self.screen_rect.bottom :
            self.y  +=self.settings.ship_speed

        self.ship_image_rect.y = self.y 

    
    def blitme(self):
        """Draw the ship at its current location """
        self.screen.blit(self.ship_image,self.ship_image_rect)
    
    def center_ship(self):
        """center the ship """
        self.ship_image_rect.midleft = self.screen_rect.midleft 
        self.y = float(self.ship_image_rect.y)

    

    

        

        