#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'honda' in cars:
    print("you like honda")
else:
    print("dont be a honda hater.")

age = int(input("enter your age: "))
if age < 4:
    price = 0
elif age < 18:
    price = 4
else:
    price = 10

print("your price is {}".format(str(price)))

alien_color = 'yellow'
if alien_color == 'green'



