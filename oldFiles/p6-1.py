alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'yellow', 'points':10}
print(alien_0)
print(alien_0['color'])
newPoints = alien_0['points']
print("you earned {} points.".format(newPoints))
def totalPoints():
    d = {'key1': 1, 'key2': 14, 'key3': 47}
    sum1 = alien_0['points'] + alien_1['points']
    print(sum1)

totalPoints()
glossary = {'abstraction':'removing a layer of complexity to focus on a smaller piece of the whole',
            'recursion':'to fold or loop back over oneself',
            'conditional':'based on something else'}

print(glossary.values())

