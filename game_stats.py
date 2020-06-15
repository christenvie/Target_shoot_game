#Author J'yrens Christenvie , Please acknowledge the author if you are using his code for your game


import json

class GameStats:
    """Track statistics """

    def __init__(self, tg_game):
        """Initialize the statistics """
        self.settings = tg_game.settings 
        self.reset_stats()

        # start the game in an active state
        self.game_active = False

        
        self.timer = self.settings.timer
        self.time = int(self.timer)

        self.load_high_score()
        

    def reset_stats(self):
        """Reset the number of chances """
        self.chances_left = self.settings.number_of_chances

        self.score = 0 
        self.level = 1
    
    def resets_timer(self):
        """Resets the timer to its orginal value """
        self.timer = self.settings.timer
    
    def load_high_score(self):
        """Load High score from a file and write it in a file """
        self.filename = 'high_score.json' 
        try :
            with open(self.filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
            with open(self.filename, 'w') as f:
                    json.dump(self.high_score, f)