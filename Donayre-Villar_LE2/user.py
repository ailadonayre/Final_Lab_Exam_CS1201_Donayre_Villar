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
        except ValueError:
            print("[ValueError]. Invalid input. Please try again.")
        
        user_account[username] = {'password': password, 'points': points}
        
    def login(self):