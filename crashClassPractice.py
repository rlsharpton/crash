class Restaurant():
    """A simple class to describe a restaurant"""

    def __init__(self, name, type):
        """Initialize name and type of food"""
        self.name = name
        self.type = type
        self.customers_served = 0

    def describe(self):
        """Print info about restaurant"""
        print(self.name.title() + " is a fine " + self.type + " restaurant.")

    def restaurant_state(self):
        """Prints if the restaurant is open or closed"""
        meat = input("Does this restaurant serve meat? ")
        if meat == 'yes':
            print("the restaurant is closed")
        else:
            print("The restaurant is open")

    def number_served(self):
        """Records number of customers served"""
        print("The number of customers served is: " + str(self.customers_served))

    def set_number_served(self, number):
        """Allows you to set the number of customers served."""
        self.customers_served = number


my_restaurant = Restaurant('Conans', 'pizza')

my_restaurant.describe()
my_restaurant.restaurant_state()
my_restaurant.number_served()
my_restaurant.set_number_served(15)
my_restaurant.number_served()

