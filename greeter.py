def greet_user(message):
    """Display a simple greeting."""
    print(f"hello {message}")

message = input("please enter a name: ")
greet_user(message)

def fav_book(title):
    """Prints user's favorite book."""
    print(f"Your favorite book is {title}")

book = input("Please tell me your favorite book.")
fav_book(book)