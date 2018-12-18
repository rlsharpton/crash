pets = ['dog', 'cat', 'fish', 'bird', 'cat']
print(pets)
pets.remove('cat')
#while 'cat' in pets:
#    pets.remove('cat')

print(pets)

def describe_pets(pet_name, animal_type='dog'):
    '''describes the pet type and name'''
    print("I have a {} who's name is {}".format(animal_type, pet_name.title()))
    return

describe_pets('willy', 'peacock')

def t_shirt(size='medium', message='Have A Nice Day'):
    '''accepts a t-shirt size and message'''
    print("You ordered a {} t-shirt and it will say: \n\
    {}".format(size, message))

t_shirt('small', 'Little Bits')

def build_person(f_name, l_name, m_name=''):
    '''takes names and returns a dictonary'''
    if m_name:
        person = {'f_name': f_name, 'l_name':l_name, 'm_name':m_name}
    else:
        person = {'f_name': f_name, 'l_name':l_name}
    return person

print(build_person('jimi', 'hendrix'))