#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

# declare the lists of the words
nouns = ['Larry Lizard', 'Mookie Wilson', 'Freddy Fly']
adjectives = ['lazily', 'vigorously', 'chaoticly']
verbs = ['sang', 'danced', 'cried']

# function to do the sentence building
def sentenator (a, b, c):
    sentance = ('The ',a, ' ',b, ' ',c)
    return sentance

# function call
one =input('Please enter first number 1 -3: ')
two =input('Please enter second number 1 -3: ')
three =input('Please enter third and final number 1 -3: ')
print(sentenator(nouns[int(one)],adjectives[int(two)],verbs[int(three)]))

print("now for something completely different!")
new_noun = input("Enter a new noun: ")
new_adjective = input("Enter a new adjective: ")
new_verb = input("Enter a new verb: ")

nouns.insert(0, new_noun)
adjectives.insert(0, new_adjective)
verbs.insert(0, new_verb)

print(nouns)


