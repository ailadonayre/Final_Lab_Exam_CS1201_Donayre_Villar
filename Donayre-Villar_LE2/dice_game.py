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
        pass

    def play_game(self):
        print("1. Start Game")
        print("2. History")
        print("3. Log Out")

        CPU_points = 0
        self.points = 0

        while True:
            if choice == 1:
                choice = int(input("Enter 'y' to play: "))

                if user_choice.lower() == 'y':
                    user_choice = random.randint(1, 6)

                    CPU_choice == random.randint(1, 6)

                if CPU_choice < user_choice:
                    print("You win!")
                    self.points += 1
                elif CPU_choice > user_choice:
                    print("You lose!")
                    CPU_points += 1
                elif CPU_choice == user_choice:
                    print("It's a tie!")
                    continue

            if choice == 2:
                pass
            if choice == 3:
                pass
            else:
                print("Invalid input. Please try again.")
                continue
    def play(self):
        user_points = 0
        cpu_points = 0

        user_choice = random.randint(1, 6)
        cpu_choice = random.randint(1, 6)



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
                pass
            if choice == 3:
                exit()
            else:
                print("Invalid input. Please try again.")
                continue