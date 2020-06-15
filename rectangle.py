
# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game

import pygame   

class Rectangle:
    """A class to manage the rectangle that appears on the screen """

    def __init__(self,tg_game):
        """Initialize the rectangle attributes. """
        super().__init__()
        # Take the screen settings and its rectangle 
        self.settings = tg_game.settings
        self.screen = tg_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.rectangle_color

        # create a rectangle and set its position
        self.rect = pygame.Rect(0,0 ,self.settings.rectangle_width, 
            self.settings.rectangle_height)
        self.rect.right = self.screen_rect.right

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if an alien is at the edge of the screen """
        if self.rect.bottom  >= self.screen_rect.bottom or self.rect.top <= 0:
            return True
    
    def update(self):
        """Move the rectangle up and down """
        self.y +=(self.settings.rectangle_speed * self.settings.movement_direction)

        self.rect.y = self.y

    def draw_rectangle(self):
        """draw the rectangle on the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)

    def center_rectangle(self):
        """center the ship at the right side of the screen """
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)




