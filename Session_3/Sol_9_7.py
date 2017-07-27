from Classes.User import Users


class Admin(Users):
    def __init__(self, first_name, last_name, gender, *privileges):
        self.privileges = []
        for item in privileges:
            self.privileges.append(item)
        super(Admin, self).__init__(self, first_name, last_name, gender)

    def show_privileges(self):
        for item in self.privileges:
            print '* {:<20}'.format(item)

admin = Admin('Vishal', 'Kushwaha', 'Male', "can add post", "can delete post", "can ban user")
admin.show_privileges()
