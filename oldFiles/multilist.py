#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

legit_toppings = ['onion', 'g pepper', 'cheese']
req_toppings = ['onion', 'fries', 'cheese']
pizza = []
for req_toppings in req_toppings:
    if req_toppings in legit_toppings:
        pizza.append(req_toppings)
        print(req_toppings + " good")
    else:
        print("not legit")

print("final pizza" + str(pizza))
