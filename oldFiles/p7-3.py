#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''
car = input("please enter car: ")
print("let me find you a {}".format(car))

party_num = int(input("How many in your party? "))
if party_num > 8:
    print("you will need to wait.")
else:
    print("come this way.")

user_num = int(input("enter a number"))
if user_num % 10 == 0:
    print("your number is a multiple of ten.")
else:
    print("your number is {}".format(user_num))