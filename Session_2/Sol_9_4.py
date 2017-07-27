# from Classes.Restaurant import Restaurants
from Session_1.Sol_9_2 import Ginger


def customers_served(self):
    return '{} has served {} customers.\n'.format(self.name, self.number_served)

# Ginger = Restaurants('Lucky Ginger', 'Thai')


def main():
    print customers_served(Ginger)

    Ginger.number_served = 523
    print customers_served(Ginger)

    Ginger.set_number_served(834)
    print customers_served(Ginger)

    Ginger.increment_number_served(150)
    print customers_served(Ginger)

if __name__ == '__main__':
    main()
