from dice_game import DiceGame

class User:
    def __init__(self, username, password, points):
        self.username = username
        self.password = password
        self.points = points
    
    def register(self, username, password, points):
        super().__init__(username, password, points)
        user_account = {}

        try:
            while True:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if len(password) < 4:
                    print('Password must have at least 4 characters')
                    continue
        except ValueError:
            print("[ValueError]. Invalid input. Please try again.")
        
        user_account[username] = {'password': password, 'points': points}
        
    def login(self):
        username = input('Enter Username: ')
        password = input('Enter password')

        if username in user_account and password == user_account[username]["password"]:
            print('Log in succefully')
            self.play_game()

