'''  favorite_languages = {
       'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
       ➊ for name, language in favorite_languages.items():
       ➋     print(name.title() + "'s favorite language is "
        +           language.title() + ".")
        '''
potential_pollees = ['sarah', 'phil', 'george', 'greg', 'jason']
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

for pollee in potential_pollees:
    if pollee in favorite_languages.keys():
        print("Hey thanks {} for taking the poll".format(pollee))
    else:
        print("{} please take the poll".format(pollee))
