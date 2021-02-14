import json


# Load the username, if it has been stored previously.
# Otherwise, prompt for th eusername and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we'll remember you next time " + username + "!")
else:
    print("welcome back " + username + "!")