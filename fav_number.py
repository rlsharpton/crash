import json
# Program to prompt a user for thier favorite number then store this as json file
# When program runs again ask if the number is their favorite or prompt for new
# Functions get_stored_number get_new_number display_number

def get_stored_number():
    """Get stored fav number"""
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        new_num = input("Is " + number + " still your fav number?")
        if new_num == 'y':
            return number
        else:
            return get_new_number()



def get_new_number():
    """ Prompt for a new fav number"""
    number = input("What is your favorite number? ")
    filename = 'fav_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        return number




def display_number():
    """Shows the users fav number"""
    number = get_stored_number()
    if number:
        print("Your fav number is: " + number)
    else:
        number = get_new_number()
        print("Your fav number is: " + number)


display_number()