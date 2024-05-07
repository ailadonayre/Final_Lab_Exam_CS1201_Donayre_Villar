choice = int(input("Enter your choice: "))

        while True:
            if choice == 1:
                CPU_points = 0
                self.points = 0

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