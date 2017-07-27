from Classes.Restaurant import Restaurants


class IceCreamStand(Restaurants):
    def __init__(self, name, cuisine_type, *flavors):
        self.flavors = []
        for item in flavors:
            self.flavors.append(item)
        super(IceCreamStand, self).__init__(self, name, cuisine_type)
        # Restaurants.__init__(self, name, cuisine_type)

    def print_flavors(self):
        for idx, item in enumerate(self.flavors):
            print '{:<2} : {:>15}'.format(idx+1, item)

IceCream = IceCreamStand('Ice cream parlor', 'Ice-cream', 'Vanilla', 'Chocolate', 'American nuts', 'Butterscotch')

IceCream.print_flavors()
