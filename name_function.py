#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def get_formatted_name(first, last, middle=""):
    '''Generate formatted name'''

    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()