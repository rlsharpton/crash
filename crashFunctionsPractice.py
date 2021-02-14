from tucked_away import *

greet_user('Robin')
book = input("\nPlease tell me your favorite book: ")



fav_boook(book)



usrin_size = input("Please enter what size you want. ")
usrin_message = input("Please enter message for the shirt. ")

make_shirt(message=usrin_message)
make_shirt(size=usrin_size, message=usrin_message)
