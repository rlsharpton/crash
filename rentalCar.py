userChoice = input("What model of rental would you like? We have these available: ")
modelsAvail = {'honda': {'accord': 3}, 'civic', 'fit', 'odyesse']},
{'toyota': ['camry', 'corolla', 'prius']},
{'hyundai': ['accent', 'tiberon']},
{'kia': ['soul', 'optima', 'rio']},
{'ford': ['mustang', 'taurus', 'impala']},
{'chevy': ['corvette', 'something']},
}

if userChoice in modelsAvail:
    print("Success, we have a" + userChoice)
else:
    print("Sorry we do not have that car")