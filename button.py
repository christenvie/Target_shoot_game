# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game

import pygame.font 

class Button:
    """A class to manage the Button on the screen  """
    
    def __init__(self, tg_game, msg):
        """Initializes the button attributes """
        self.screen = tg_game.screen  
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width , self.height = 200 ,50
        self.button_color = ( 0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("DS-Digital", 48)

        # Build the button rectangle object and center it 
        self.button_rect = pygame.Rect(0,0, self.width,self.height)
        self.button_rect.center = self.screen_rect.center

        #preped the button message
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """ Display the message on the screen """
        self.msg_image = self.font.render(msg, True, self.text_color, 
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center 
    
    def draw_button(self):
        """Draw the button and its message """
        self.screen.fill(self.button_color,self.button_rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

        

        