#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Test for name'''

    def test_first_last_name(self):
        '''Do names like Janis Joplin work?'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        '''Do names like Wolfgang Amadeus Mozart work?'''
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        