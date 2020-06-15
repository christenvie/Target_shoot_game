# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game
# 03/ 06 / 2020

# class to represent the settings of the game 

from game_stats import GameStats

class Settings:
    """A class to manage all the settings of the game"""

    def __init__(self):
        """Initialize the screen settings,  """
         #screen settings 
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (25, 0, 255)


        #Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 2
        
        # Rectangle settings
        self.rectangle_width = 200
        self.rectangle_height = 100
        self.rectangle_color = (188, 118, 118)
        self.rectangle_speed = 4.5

        # Chances settings
        self.number_of_chances = 3
        
        # How quickly the game speeds up 
        self.speedup_scale = 1.1

        # How quickly the score point values increase 
        self.score_scale = 1.5

        
        #Initilaize the dynamics settings of the game
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed= 2.5
        

        #rectangle movement direction 
        self.movement_direction = -1

        # Scoring
        self.rectangle_points = 50
        # initialise the timer
        self.timer = 15
    
    def increase_speed(self):
        """Increase speed settings an alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *=self.speedup_scale

        self.rectangle_points = int(self.rectangle_points * self.score_scale)