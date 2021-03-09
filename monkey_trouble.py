def monkey_trouble(smile_one, smile_two):
    """ function to see if we have Monkey trouble. 
    We have trouble if both Monkeys are smiling or none."""
    if (smile_one):  # and smile_two True or !smile_one and !smile_two):
        return ("Monkey Trouble")
    else:
        return ("Smooth Sailing")


smile_one = input("enter True or False: ")

if isinstance(smile_one, int):
    print("good Boolean")
else: 
    print("Not Boolean")


print(f"You entered: {smile_one}.")
smile_two = input("enter True or False: ")

if (smile_one and smile_two):
    print("Both true")
else:
    print("something else")
#print(monkey_trouble(smile_one, smile_two))