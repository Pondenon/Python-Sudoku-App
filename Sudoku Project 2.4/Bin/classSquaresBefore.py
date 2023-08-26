###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
###############_______________LIBRARY_IMPORTS_______________###############___END


###############_______________CLASS_SQUARES_______________###############___START
class Squares:
    def __init__(self, x, y):
        self.number = None
        self.coordinates = (x, y)
        self.possibilities = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}

    def insertNumber(self, number):
        self.number = number

    def __repr__(self):
        if self.number is None:
            return '   '
        else:
            return ' ' + str(self.number) + ' '

    def singlePossibilityExistant(self):
        cpt = 0
        n = None
        for number in range(1, 10):
            if self.possibilities[number]:
                cpt += 1
                n = number
        if cpt == 1:
            self.number = n
            return True
        return False
###############_______________CLASS_SQUARES_______________###############___END