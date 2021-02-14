#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

class Car():
    '''A Simple attempt to model a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_level = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has {} miles on it.".format(str(self.odometer_reading)))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_tank(self, gas_added):
        self.gas_tank_level += gas_added

    def read_gas_tank(self):
        print("The car has {} gallons in it.".format(str(self.gas_tank_level)))

class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def fill_tank(self, gas_added):
        print("this car does not have a gas tank.")

    def describe_battery(self):
        '''
        Print a statement describing the battery
        :return:
        '''
        print("This car has a {} -kWh battery.".format(str(self.battery_size)))


monza = Car('Chevy', 'Monza', 1981)
monza.increment_odometer(500)
monza.fill_tank(10)
monza.read_gas_tank()
monza.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_tank(10)

