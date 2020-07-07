from user import User

class Admin(User):

    def __init__(self, first_name = '', last_name = ''):
        super().__init__(first_name, last_name)
        self.privileages = []
    
    def increase_privileages(self, *privileage):
        self.privileages = privileage[:]
    
    def show_privileages(self):
        print(self.privileages)

admin = Admin()
privileages = ['can add post', 'can delete post', 'can ban user']
admin.increase_privileages(privileages)

admin.show_privileages()
