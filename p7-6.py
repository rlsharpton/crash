prompt = "Please enter a topping"
topping = ''
counter = 0
while topping != 'quit':
    counter += 1
    if counter > 5:
        break
    else:
        topping = input(prompt)
        print("adding {} to the pizza".format(topping))
