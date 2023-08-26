###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
###############_______________LIBRARY_IMPORTS_______________###############___END



###############_______________FILES_IMPORTS_______________###############___START
from classSquares import Squares
from Resources.pythonFiles.auxiliaryFunctions import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________CLASS_GRID_______________###############___START
class Grid:
    def __init__(self):
        self.lists = [[Squares(i, j) for j in range(1, 10)] for i in range(1, 10)]



    def insertNumber(self, x, y, number):
        self.lists[x-1][y-1].insertNumber(number)



    def verifyCoordinates(self, characters):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if (len(characters) == 6 and characters[5] == '\n') or len(characters) == 5:
            if characters[1] == characters[3] == '/':
                if characters[0] in numbers and characters[2] in numbers and characters[4] in numbers:
                    return True
        return False
    
    def verifyCode(self, code):
        code = code.split(',')
        for coordinates in code:
            if not self.verifyCoordinates(coordinates):
                return False
        return True
    
    def verifyFullyCompleted(self):
        for i in range(9):
            for j in range(9):
                if self.lists[i][j].number is None:
                    return False
        return True

    def verifyResult(self):
        for i in range(1, 10):
            if not noDoubles(convertListToInt(self.line(i))) or not noDoubles(convertListToInt(self.column(i))) or not noDoubles(convertListToInt(self.box(i))):
                print('\n\nThe result is false.')
                return
        print('\n\nThe Sudoku is resolved !')



    def updatePossibleNumbers(self):
        if self.verifyFullyCompleted():
            self.verifyResult()
        else:
            for i in range(1, 10):
                for j in range(1, 10):
                    if self.lists[i-1][j-1].number is None:
                        line = convertListToInt(self.line(i))
                        column = convertListToInt(self.column(j))
                        box = convertListToInt(self.box(convertCoordinatesToBox(i, j)))
                        for number in range(1, 10):
                            if number in line or number in column or number in box:
                                self.lists[i-1][j-1].possibilities[number] = False
                

    def singleNumberPossible(self):
        numberPlaced = False
        for i in range(1, 10):
            for j in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    if self.lists[i-1][j-1].singlePossibilityExistant():
                        self.displayGrid()
                        numberPlaced = True
        if numberPlaced:
            self.solve()


    def singleOccurenceOfNumberInLine(self):
        numberPlaced = False
        for i in range(1, 10):
            numberOccurence = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for j in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    for key in self.lists[i-1][j-1].possibilities.keys():
                        if self.lists[i-1][j-1].possibilities[key]:
                            numberOccurence[key].append(i-1)
                            numberOccurence[key].append(j-1)
            for key in numberOccurence.keys():
                if len(numberOccurence[key]) == 2:
                    self.lists[numberOccurence[key][0]][numberOccurence[key][1]].number = key
                    self.displayGrid()
                    numberPlaced = True
        if numberPlaced:
            self.solve()

    def singleOccurenceOfNumberInColumn(self):
        numberPlaced = False
        for j in range(1, 10):
            numberOccurence = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for i in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    for key in self.lists[i-1][j-1].possibilities.keys():
                        if self.lists[i-1][j-1].possibilities[key]:
                            numberOccurence[key].append(i-1)
                            numberOccurence[key].append(j-1)
            for key in numberOccurence.keys():
                if len(numberOccurence[key]) == 2:
                    self.lists[numberOccurence[key][0]][numberOccurence[key][1]].number = key
                    self.displayGrid()
                    numberPlaced = True
        if numberPlaced:
            self.solve()

    def singleOccurenceOfNumberInBox(self):
        numberPlaced = False
        for i in range(1, 10):
            currentBox = self.box(i)
            numberOccurence = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for j in range(1, 10):
                if currentBox[j-1].number is None:
                    for key in currentBox[j-1].possibilities.keys():
                        if currentBox[j-1].possibilities[key]:
                            numberOccurence[key].append(j-1)
            for key in numberOccurence.keys():
                if len(numberOccurence[key]) == 1:
                    currentBox[numberOccurence[key][0]].number = key
                    self.displayGrid()
                    numberPlaced = True
        if numberPlaced:
            self.solve()



    def line(self, i):
        return self.lists[i-1]
    
    def column(self, j):
        column = []
        for i in range(9):
            column.append(self.lists[i][j-1])
        return column
    
    def box(self, i):
        slice1 = int(((i % 3) - 1) * 3 + (i+1)%3 * (i+2)%3 * 4.5)
        slice2 = int((i % 3) * 3 + (i+1)%3 * (i+2)%3 * 4.5)
        i = i-1
        while i % 3 != 0:
            i -= 1
        i += 1
        lines = [i, i+1, i+2]
        box = []
        for elt in lines:
            box += self.line(elt)[slice1:slice2]
        return box
    


    def prepareGrid(self, code):
        code = code.split(',')
        for coordinates in code:
            print(coordinates)
            self.insertNumber(int(coordinates[0]), int(coordinates[2]), int(coordinates[4]))

    def enterDefaultNumbers(self, gridCode):
        if self.verifyCode(gridCode):
            self.prepareGrid(gridCode)
            self.displayGrid()

    def solve(self):
        self.updatePossibleNumbers()
        self.singleNumberPossible()
        self.singleOccurenceOfNumberInLine()
        self.singleOccurenceOfNumberInColumn()
        self.singleOccurenceOfNumberInBox()

    def displayGrid(self):
        print('\n\n')
        for i in range(len(self.lists)):
            if (i) % 3 == 0:
                print('='*31)
            for j in range(len(self.lists[i])):
                if (j+1) % 3 == 0 and (j+1) != len(self.lists[i]):
                    print(self.lists[i][j], end='||')
                else:
                    print(self.lists[i][j], end='')
            print()
        print('='*31+'\n\n')
###############_______________CLASS_GRID_______________###############___END