from user import *
from user_manager import *
from score import *
from datetime import datetime
import random
import os

class DiceGame:
    def load_scores():
        pass
    
    def save_scores():
        score_folder = os.path.join(score_folder, "w")
        with open("score_folder", "w"):
            if not os.path.exists:
                pass

    def play_game(self):
        print("1. Start Game")
        print("2. History")
        print("3. Log Out")

        CPU_points = 0
        user_points = 0
        CPU_choice = 0
        user_choice = 0

        while True:
            if choice == 1:
                choice = int(input("Enter 'y' to play and 'n' to Exit: "))

                if choice.lower() == 'y':
                    user_choice = random.randint(1, 6)
                    CPU_choice == random.randint(1, 6)

                if CPU_choice < user_choice:
                    print("You win!")
                    user_points += 1
                elif CPU_choice > user_choice:
                    print("You lose!")
                    CPU_points += 1
                elif CPU_choice == user_choice:
                    print("It's a tie!")
                    continue
                else:
                    choice.lower() == 'n'
                    if user_points > CPU_points:
                        print(f'You won with your points: {user_points} and CPU points: {CPU_points}')
                        self.points += 1
                        self.score += 1
                    else:
                        print(f'You lost with your points: {user_points} and CPU points: {CPU_points}')

            if choice == 2:
                pass
            if choice == 3:
                pass
            else:
                print("Invalid input. Please try again.")
                continue

    def show_top_scores():
        pass

    def log_out():
        exit()

    def menu():
        print("Welcome to Dice Roll Game!\n")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        while True:
            if choice == 1:
                self.register()
            if choice == 2:
                self.login()
            if choice == 3:
                exit()
            else:
                print("Invalid input. Please try again.")
                continue

game = DiceGame()
game.menu()