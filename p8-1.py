#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue

    print(current_number)