#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

nouns = ['lizard', 'goat', 'mookie wilson']
verbs = ['ate', 'bleeted', 'lounged']
adverbs = ['lazily', 'vigorously', 'astoundingly']

for noun in nouns:
    print(noun)

def sentenator(n, v, a):
    print("A {n} {v} {a}".format(n, v, a))

#sentenator(nouns, verbs, adverbs)

squares =  [value ** 2 for value in range(1,11)]
#for value in range(1,11):
#    squares.append(value ** 2)

for square in squares:
    if ((square % 2) == 0):
        print("hit even a " + str(square))
    else:
        print(square)

print(sum(squares))

thirds = []
for value in range(1,11):
    third = value ** (1/3)
    thirds.append(third)

print(thirds)
