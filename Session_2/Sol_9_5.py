# from Classes.User import Users
from Session_1.Sol_9_3 import Vishal


def print_login(self):
    return 'Login attempts: {:>2}\n'.format(self.login_attempts)

# Vishal = Users('Vishal', 'Kushwaha', 'Male', 9654656057)


def main():
    for i in range(5):
        Vishal.increment_login_attempts()
    print print_login(Vishal)

    Vishal.reset_login_attempts()
    print print_login(Vishal)

if __name__ == '__main__':
    main()
