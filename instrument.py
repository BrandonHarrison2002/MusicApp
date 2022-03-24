from time import sleep
from song import *

'''
A=57
ASHARP=58
B=59
C=60
CSHARP=61
D=62
DSHARP=63
E=64
F=65
FSHARP=66
G=67
GSHARP=68
'''

class instrument():
    def __init__(self, name="", midi=None):
        self.name=name
        self.song=midi

    def addsong(self, filename):
        self.song=song(filename)
        print(f"Added {filename[:-4]}")
        
    