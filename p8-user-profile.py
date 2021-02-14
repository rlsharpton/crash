#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def build_profile(first, last, **user_info):
    '''Build a dictonary containing everything we know about a user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

def car_builder(make, model, **packages):
    car_profile = {}
    car_profile['make'] = make
    car_profile['model'] = model
    for key, value in packages.items():
        car_profile[key] = value
    return car_profile

car_profile = car_builder('toyota', 'prius', gas_converter = 'ethanol', battery_size = 'extra_large')
car_profile = car_builder('honda', 'accord', gas_converter = 'unleaded', battery_size = 'none')
print(car_profile)