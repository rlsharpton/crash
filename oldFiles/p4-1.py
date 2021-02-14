pizzas = ['pepporoni', 'sausage', 'veggie']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("My favorite pizzas are: {}".format(pizza))

print("that's a lot of pizza")

pizzas.append("super veg")
friend_pizza = pizzas[:]
print(friend_pizza)
pizzas.append('stromboli')
friend_pizza.append('hawaiian')
print("now my pizzzas are: {}".format(pizzas))
print("friend pizzas are: {}".format(friend_pizza))