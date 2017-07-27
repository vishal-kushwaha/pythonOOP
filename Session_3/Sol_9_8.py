from Classes.User import Users


class Privileges(object):
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for item in self.privileges:
            print '* {:<20} {:<5}'.format(item, 'test')


class Admin(Users):
    def __init__(self, first_name, last_name, gender, privilege):
        self.privileges = privilege

        super(Admin, self).__init__(self, first_name, last_name, gender)

privilege = Privileges()

admin = Admin('Vishal', 'Kushwaha', 'Male', privilege)
admin.privileges.show_privileges()
