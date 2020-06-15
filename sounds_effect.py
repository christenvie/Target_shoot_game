# Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game
# People acknowledged for the sounds :
# Users Grunz , Bertrof , Davidbain , Jagadamba from freesound.org 

import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/NFF-laser-gun-02.wav')
level_increase_sound = pygame.mixer.Sound('sounds/109662__grunz__success.wav')
miss_sound = pygame.mixer.Sound('sounds/351563__bertrof__game-sound-incorrect-with-delay.wav')
end_of_game_sound = pygame.mixer.Sound('sounds/135831__davidbain__end-game-fail.wav')
clock_ticking_sound = pygame.mixer.Sound('sounds/254315__jagadamba__clock-tick.wav')
