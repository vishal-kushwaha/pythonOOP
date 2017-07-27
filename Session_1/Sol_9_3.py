from Classes.User import Users

Vishal = Users('Vishal', 'Kushwaha', 'Male', 9654656057)
Mansi = Users('Mansi', 'Goyal', 'Female')
TestUser = Users('Test', 'User', 'Test')


def main():
    Vishal.describe_user()
    Vishal.greet_user()
    Mansi.describe_user()
    Mansi.greet_user()
    TestUser.describe_user()
    TestUser.greet_user()

if __name__ == '__main__':
    main()
