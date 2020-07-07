class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("Good morning " + self.first_name + " " + self.last_name + ".")

user_0 = User('aaa','bbb')
user_1 = User('ccc','ddd')

user_0.greet_user()
user_1.greet_user()