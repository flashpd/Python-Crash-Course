class Privileges():
    def __init__(self, *privilege):
        self.privileges = privilege[:]

    def show_privileages(self):
        print(self.privileages)


class Admin(Privileges):

    def __init__(self, *privilege):
        super().__init__(*privilege)
        self.privileages = privilege[:]

privileages = ['can add post', 'can delete post', 'can ban user']
admin = Admin(privileages)
admin.show_privileages()
