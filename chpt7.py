current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Enter a message to be displayed back: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

while True:
    pizza = []
    toppings = input("enter a topping")
    pizza