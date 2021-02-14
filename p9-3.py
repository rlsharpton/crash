class User_profile():
    '''A class that creates a basic user profile'''

    def __init__(self, first_name, last_name):
        '''Initialize first name and last name attributes'''
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This user is {}, {}".format(self.last_name, self.first_name))

    def greet_user(self):
        print("Hello {} {}".format(self.first_name, self.last_name))

class Admin(User_profile):
    def __init__(self):
        self.privileges = privileges

joe = User_profile('Joe', 'Blow')
phil = User_profile('Phil', 'Jones')

joe.describe_user()
phil.describe_user()