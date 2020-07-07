class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        print("Good morning " + self.first_name + " " + self.last_name + ".")
    
    def increment_login_attempts(self, num):
        self.login_attempts += num
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def get_login_attemps(self):
        print(self.login_attempts)