""" Author: Robin Sharpton Version: 0.1
Simple program to simulate a bouncers job."""
def bouncer(client_name, client_age):
    if client_name in blacklist:
        print(f"{client_name} you can't come in")
        return 0
    else:
        print("Let's check your age.")

    if (client_age < 0):
        print("not born yet, go away")
    elif (client_age < 21):
        print("Can't come in.")
    else:
        print("Come on in.")
    
client_name = input("Please enter your name: ")
client_age = input("Please enter your age: ")
try:
    client_age = int(client_age)
except ValueError:
    print("you did not enter a number")

blacklist = ['Bob', 'Joe', 'Susan']
bouncer(client_name, client_age)