favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print(" Hi " + name.title()+
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("The languages mentioned")
for language in set(favorite_languages.values()):
    print(language.title())
