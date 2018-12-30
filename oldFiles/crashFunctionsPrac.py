#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def city_country(usr_city, usr_country):
    city_country_pairs = {'city': usr_city, 'country': usr_country}
    print(city_country_pairs['country'] + ', ' + city_country_pairs['city'])


city_country('Austin', 'Texas')
city_country('Paris', 'France')
city_country('Oslo', 'Norway')

magician_list = ['houdini', 'copperfeild', 'robin']
def magic_folks(the_ones):
    """Function to take a list of name and display them."""
    for mago in the_ones:
        print(str(the_ones) + " is a magician.\n")

magic_folks(magician_list)




