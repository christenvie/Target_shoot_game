# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game
# People acknowledged for the sounds :
# Users Grunz , Bertrof , Davidbain , Jagadamba from freesound.org 

import sys
import json
import pygame

from time import sleep


from settings import Settings 
from button import Button 
from pause import Pause
from ship import Ship  
from rectangle import Rectangle
from bullet import Bullet
from game_stats import GameStats
from scoreboard import Scoreboard
import sounds_effect as se 

class TargetPractice:
    """A class to manage all the assets and the game behavior """

    def __init__(self):
        """Initialize the game and create game ressources """
        pygame.init()

        self.settings = Settings()
        self.screen  = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("J'y-rens Target Shoot 1.0")

        #Set the clock and time click
        self.clock = pygame.time.Clock()
        self.dt = 0

        # create an instance of the game stats class
        self.stats = GameStats(self)

        #Create an instance of the scoreboard class
        self.sb = Scoreboard(self)

        # Create an instance of the class ship
        self.ship = Ship(self)

        #create a list of bullets that hit the rectangle 
        self.bullets_hit_rectangle = []

        # create an instance of the class rectangle
        self.rectangle  = Rectangle(self)

        # create an instance of the group bullets
        self.bullets = pygame.sprite.Group()

        # create an instance of the button
        self.play_button= Button(self,"Play")
        
        # create an instance of the pause Button
        self.pause_button = Pause(self,"Pause")

    def run_game(self):
        """Start the main loop of the game """ 
        
        while True : 
            # watch for keyboard events
            self._check_events()
            
            if self.stats.game_active:
                # start the  timer on the screen
                self.start_timer()
                
                #update the ship position
                self.ship.update()

                # update the position of the bullet
                self._update_bullets()

                #update the rectangle
                self._update_rectangle()
             
            # Update aliens
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # store the highest score before quiting
                self.write_high_score_to_folder()
                sys.exit()   
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_pause_button(mouse_pos)
    
    def _check_pause_button(self, mouse_pos):
        """Lock the game when the player cliks the pause  button """
        button_clicked = self.pause_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.stats.game_active:
            # pause the game .
            self.stats.game_active = False       
                
    def _check_play_button(self, mouse_pos):
        """Check the play button """
        button_clicked = self.play_button.button_rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # starts the game when the player clicks play and the game is inactive
            if self.stats.chances_left == 0 and self.sb.time == 0 or self.stats.score == 0:
                # Restart the game when the time is 0 seconds 
                # and all the chances are gone 
                self._start_game()

            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_timer()
            self.sb.prep_chances_left()
            
    def start_timer(self):
        """Start the timer when the game starts """
        self.stats.timer -= self.dt
        
        if self.stats.timer <= 0 :
            sleep(1)
            self.stats.resets_timer()
        
        self.sb.prep_timer()
        self.dt = self.clock.tick(200) / 1000  # / 1000 to convert to seconds.
              
    def _start_game(self):
        """Start the game """   
        # set the game to active state 
        self.stats.game_active = True

        # reset the stats 
        self.stats.reset_stats()

        # set the timer back to zero
        self.stats.resets_timer()

        # Empty the bullets 
        self.bullets.empty()

        # center the ship and the rectangle
        self.rectangle.center_rectangle()
        self.ship.center_ship()
    
    def _check_keydown_events(self,event):
        """Respond to keydown events """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q: 
            self.write_high_score_to_folder()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_p or pygame.K_KP_ENTER:
            if not self.stats.game_active:
                self._start_game()
    
    def write_high_score_to_folder(self):
        """write High score to folder"""
        with open(self.stats.filename, 'w') as f:
                    json.dump(self.stats.high_score, f)
    
    def _fire_bullets(self):
        """Draws bullet on the screen """
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            se.bullet_sound.play()

    def _update_bullets(self):
        """Update the position of the bullets """
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)

        # check bullets and rectangle collisions and update bullets
        self._check_bullet_rectangle_collision()
                
    def _check_bullet_rectangle_collision(self):
        """Respond to bullets and rectangle collision """
        
        bullet = pygame.sprite.spritecollideany( self.rectangle ,self.bullets)
        if  bullet and self.stats.timer > 0:
            
            self.bullets_hit_rectangle.append(bullet)
            self.stats.score += self.settings.rectangle_points
            self.sb.prep_score()
            self.sb.check_high_score()
            
            # detect that the rectangle has been hit
            # and start a new level
            self._rectangle_hit()
            self.start_new_level()

        elif self.sb.time == 0 and not self.bullets_hit_rectangle :
            self._rectangle_not_hit() 
    
    def start_new_level(self):
        """Start a new level if the rectangle has been hit """
        self.settings.increase_speed()
        self.sb.prep_level()
        
    def _check_keyup_events(self,event):
        """Respond to keyup events """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _change_movement_direction(self):
        """change the movememnt direction of the rectangle """
        self.settings.movement_direction *= -1

    def _check_rectangle_edges(self):
        """check rectangle edges and change the movement direction """
        if self.rectangle.check_edges():
            self._change_movement_direction()
            
    def _update_rectangle(self):
        """Update rectangle position before"""
        
        self._check_rectangle_edges()
        self.rectangle.update()
                    
    def _rectangle_not_hit(self):
        """Respond when the rectangle has not been hit and the timer has reached 0 """
        if self.stats.chances_left > 0:
            
            #Decrement the number of chances
            self.stats.chances_left -=1
            
            self.sb.prep_chances_left()

            se.miss_sound.play()

            self.bullets.empty()

            # Center the rectangle
            self.rectangle.center_rectangle()

            # resets timer to its initial value
            self.stats.resets_timer()

            sleep(0.5)
        else:
            self.end_of_game()
                    
    def _rectangle_hit(self):
        """Respond when the rectangle is hit """
        if self.stats.chances_left >= 0:

            # Empty the bullets_hit_rectangle list 
            self.bullets_hit_rectangle = []

            #Increment the level and empty the bullets 
            
            self.stats.level +=1
            se.level_increase_sound.play()
            self.bullets.empty()

            # resets the bullets to its orginal 15 seconds
            self.stats.resets_timer()

            # center the rectangle
            self.rectangle.center_rectangle()

            sleep(1)
        else:
            self.end_of_game()
            
    def end_of_game(self):
        """Play end of game sound """
        sleep(2)
        se.end_of_game_sound.play()
        self.stats.game_active = False

    def _update_screen(self):
        """Update the screen anytime an item position is modified on the screen """
        self.screen.fill(self.settings.bg_color)

        #Draw the ship of the screen
        self.ship.blitme()

        #Draw the rectangle to the screen
        self.rectangle.draw_rectangle()

        # Draw bullets on the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Draw the score button
        self.sb.show_score()

        #Draw the play button if the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()
        else:
            self.pause_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    tg = TargetPractice()
    tg.run_game()