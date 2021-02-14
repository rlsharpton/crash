import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

letters = ['a', 'b', 'c', 'd']

filename = 'letters.json'
with open(filename, 'w') as f_obj:
    json.dump(letters, f_obj)

