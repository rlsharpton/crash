#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''
from random import randint

class Die():
    def __init__(self, sides = 6, rolls = 1):
        self.sides = sides
        self.rolls = rolls

    def roll_dice(self):
        total = 0
        for i in range(self.rolls):
            x = randint(1, self.sides)
            total += x
            print("you rolled a {} on a {} sided die.".format(x, self.sides))
        print("the total of your rolls were: {}".format(total))

num_sides = int(input("Enter number of sides: "))
num_rolls = int(input("Enter number of rolls: "))
my_dice = Die(num_sides, num_rolls)
my_dice.roll_dice()
