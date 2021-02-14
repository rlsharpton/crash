pizzaToppings = ['pepperoni', 'sausage', 'ham']
for top in pizzaToppings:
    print(top + " is a topping for pizza")

for top in pizzaToppings:
    print("I love pizza with " + top)

print("I really love pizza")

print("this list of toppings have " + str(len(pizzaToppings)))

yourPizzaTops = pizzaToppings[:]
yourPizzaTops.append('onion')
print("Your pizza is: " + str(pizzaToppings))
print("My pizza is: " + str(yourPizzaTops))

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

squaresComprehension = [value ** 2 for value in range(1,11)]
print(squaresComprehension)

oneToTwenty = [value for value in range(1,21)]
print(oneToTwenty)

million = [value for value in range(1,1000001)]
print("The min value in million is: " + str(min(million)))
print("The max value in million is: " + str(max(million)))
print("The sum of the values in million is: " + str(sum(million)))

threes = [value for value in range(1,12,2)]
print(threes)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)
