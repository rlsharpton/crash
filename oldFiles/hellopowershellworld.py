#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

# -*- coding: iso-8859-1 -*-
import subprocess, sys

p = subprocess.Popen(["powershell.exe",
              ".\helloworld.ps1"],
              stdout=sys.stdout)
p.communicate()