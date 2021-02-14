fav_language = {}

def get_name():
    name = input("enter your name: ")
    return name

def fav_lang():
    lang = input("enter your fav language: ")
    return lang

def build_dict():
    fav_language['name'] = get_name()
    fav_language['fav_lang'] = fav_lang()

x = 0
while x != 'q':
    x = input(" do you want to enter more?")
    build_dict()


for k in fav_language.keys():
    print("The participants are: {}".format(k))

for v in set(fav_language.values()):
    print("the languages are: {}".format(v))

print(fav_language)