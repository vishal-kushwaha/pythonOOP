class Restaurants(object):

    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def __str__(self):
        return '{0:<20} : {1} \n{2:<20} : {3}'.format('Restaurant Name', self.name, 'Cuisine_type', self.cuisine_type)

    def describe_restaurant(self):
        print self.name, 'is famous for its', self.cuisine_type, 'cuisines.'

    def open_restaurant(self):
        print '%s is now serving its %s food.' % (self.name, self.cuisine_type)

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served

Ginger = Restaurants('Lucky Ginger', 'Thai')

Ginger.describe_restaurant()
Ginger.open_restaurant()
