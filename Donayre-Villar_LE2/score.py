from dice_game import DiceGame

class Score:
    def __init__(self, score):
        self.score = score
    
    def get_score(self):
        print(f"Your current score is: {self.score}.")