from Classes.Restaurant import Restaurants

Ginger = Restaurants('Lucky Ginger', 'Thai')
Om = Restaurants('Om Sweets', 'Indian')
Dominos = Restaurants('Dominos', 'Italian')


def main():
    Ginger.describe_restaurant()
    Ginger.open_restaurant()

    Om.describe_restaurant()
    Om.open_restaurant()

    Dominos.describe_restaurant()
    Dominos.open_restaurant()

if __name__ == '__main__':
    main()
