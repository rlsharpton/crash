#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

friend = {'f_name': 'Randal',
          'l_name': 'Ferguson',
          'age': 47,
          'city': 'clyde',}
print(friend)

glossary = {'key': 'The first value in a key value pair when using dictonaries',
            'value': 'The second value in a key value pair when using dictonaries',
            'keyword': 'These are words with established meanings and can not be used otherwise',
            'list': 'These are collections of data that are mutable',
            'tuple': 'Similar to lists except immutable uses () instead of []', }
for key, value in glossary.items():
    print("\nthe key is: " + key)
    print("the value is: " + value)

rivers = {
    'nile': {
        'name': 'The Nile River',
        'country': ['Egypt', 'Somolia', 'Ethiopia'],
        'length': 'longest',
    },
    'amazon': {
        'name': 'The Amazon River',
        'country': ['Brazil', 'Peru', 'Equador'],
        'length': 'second',
    },
    'mississippi': {
    'name': 'The Mighty Mississippi',
    'country': 'USA',
    'length': 'third',
    },
}

print(rivers)

people = [{'fred':'birch tech support','friend': True, 'gender': 'male',},
          {'Ian': 'my youngest son', 'friend': True, 'gender': 'male',},
          {'Belal':'demon from wheel of time','friend': False, 'gender': 'none',}]

for k in people:
    print("\nThe key is: " + str(k))

print("If I only want the friend slice: " + str(people[1:2]))
    #print("The value is: " + v)

#people[0:1],['fred'] = 'Joe'

#print(people)




