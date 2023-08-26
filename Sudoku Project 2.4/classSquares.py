###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
###############_______________LIBRARY_IMPORTS_______________###############___END


###############_______________CLASS_SQUARES_______________###############___START
class Squares:
    def __init__(self, x, y):
        self.number = None #definitive number placed in square, None by default
        self.coordinates = (x, y)
        self.possibilities = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
        self.listOfPossibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.numbersTested = []
        self.defaultNumber = False

    def updateListPossibilities(self):
        self.listOfPossibilities = []
        for key in self.possibilities.keys():
            if self.possibilities[key] and key not in self.numbersTested:
                self.listOfPossibilities.append(key)

    def resetNumbersTested(self):
        self.numbersTested = []

    def insertNumber(self, number):
        self.number = number

    def removeNumber(self):
        self.number = None
        self.defaultNumber = False

    def __repr__(self):
        if self.number is None:
            return '   '#return ' ' + str(self.coordinates[0]) + '|' + str(self.coordinates[1]) + ' '
        else:
            return ' ' + str(self.number) + ' '
        
    def resetToDefault(self):
        self.number = None
        self.possibilities = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True}
        
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
    
    def allPossibleNumbers(self):
        numbers = []
        for key in self.possibilities.keys():
            if self.possibilities[key]:
                numbers.append(key)
        return numbers
###############_______________CLASS_SQUARES_______________###############___END