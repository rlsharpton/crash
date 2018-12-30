#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

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
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['add post', 'delete post', 'modify user']

    def list_privileges(self):
        print("The admin can {} do these things.".format(self.privileges))

joe = User_profile('Joe', 'Blow')
phil = User_profile('Phil', 'Jones')

joe.describe_user()

phil.describe_user()
robin = Admin('Robin', 'Sharpton')
robin.list_privileges()