###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from random import randint
###############_______________LIBRARY_IMPORTS_______________###############___END



###############_______________FILES_IMPORTS_______________###############___START
from classSquares import Squares
from Resources.pythonFiles.auxiliaryFunctions import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________CLASS_GRID_______________###############___START
class Grid:
    def __init__(self, display=False):
        self.lists = [[Squares(i, j) for j in range(1, 10)] for i in range(1, 10)]
        self.numberPlaced = 0
        self.display = display


    def createVerificationGrid(self):
        grid = Grid(False)
        for i in range(9):
            for j in range(9):
                grid.lists[i][j].number = self.lists[i][j].number
                grid.lists[i][j].coordinates = self.lists[i][j].coordinates
                grid.lists[i][j].possibilities = self.lists[i][j].possibilities
                grid.lists[i][j].listOfPossibilities = self.lists[i][j].listOfPossibilities
                grid.lists[i][j].numbersTested = self.lists[i][j].numbersTested
                grid.lists[i][j].defaultNumber = self.lists[i][j].defaultNumber
        return grid


    def enterDefaultNumbers(self, gridCode):
        if self.verifyCode(gridCode):
            self.prepareGrid(gridCode)
            if self.display:
                self.displayGrid()

    def convertIndexToCoordinates(self, index):
        x = index // 9
        y = index % 9
        return x, y

    def insertNumber(self, x, y, number):
        self.lists[x-1][y-1].insertNumber(number)
        self.lists[x-1][y-1].defaultNumber = True

    def prepareGrid(self, code):
        code = code.split(',')
        for coordinates in code:
            self.insertNumber(int(coordinates[0]), int(coordinates[2]), int(coordinates[4]))


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
                if self.display:
                    print('\n\nThe result is false.')
                return False
        if self.display:
            print('\n\nThe Sudoku is resolved !')
        return True


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
                            elif number not in line and number not in column and number not in box:
                                self.lists[i-1][j-1].possibilities[number] = True

    def updatePossibleNumberForSquare(self, i, j):
        line = convertListToInt(self.line(i))
        column = convertListToInt(self.column(j))
        box = convertListToInt(self.box(convertCoordinatesToBox(i, j)))
        for number in range(1, 10):
            if number in line or number in column or number in box:
                self.lists[i-1][j-1].possibilities[number] = False
            else:
                self.lists[i-1][j-1].possibilities[number] = True
        self.lists[i-1][j-1].updateListPossibilities()

    def updateContinuingNumber(self, index):
        #'''
        if index < 80:
            x, y = self.convertIndexToCoordinates(index+1)
            self.lists[x][y].resetNumbersTested()
            self.updatePossibleNumberForSquare(x+1, y+1)
        #'''


    def singleNumberPossible(self):
        numberPlaced = False
        for i in range(1, 10):
            for j in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    if self.lists[i-1][j-1].singlePossibilityExistant():
                        if self.display:
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
                    numberPlaced = True
                    if self.display:
                        self.displayGrid()
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
                    numberPlaced = True
                    if self.display:
                        self.displayGrid()
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
                    numberPlaced = True
                    if self.display:
                        self.displayGrid()
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



    def emptyGridSquares(self, difficulty):
        level = {'Very Easy':randint(45, 51), 'Easy':randint(39, 44), 'Medium':randint(34, 38), 'Hard':randint(29, 33), 'Very Hard':randint(24, 28), 'Impossible':randint(19, 23)}
        squareEmptied = []
        cpt = 0
        rest = 81-level[difficulty]
        if level[difficulty] >= 29:
            while rest > 0 and cpt < 81:
                grid = self.createVerificationGrid()
                i, j = randint(0, 8), randint(0, 8)
                while (i == 4 and j == 4) or coordinatesInList(i, j, squareEmptied):
                    i, j = randint(0, 8), randint(0, 8)
                x, y = 8 - i, 8 - j
                n1 = [i, j, self.lists[i][j].number]
                n2 = [x, y, self.lists[x][y].number]
                grid.lists[x][y].removeNumber()
                grid.lists[i][j].removeNumber()
                if self.display:
                    print('\n\n\nThe grid before vs after:\n', n1, n2)
                    grid.displayGrid()
                grid.solve()
                if self.display:
                    grid.displayGrid()
                if grid.verifyFullyCompleted() and grid.verifyResult():
                    self.lists[x][y].removeNumber()
                    self.lists[i][j].removeNumber()
                    squareEmptied.append(n1)
                    squareEmptied.append(n2)
                    rest -= 1
                else:
                    cpt += 1
        else:
            while rest > 0 and cpt < 81:
                grid = self.createVerificationGrid()
                i, j = randint(0, 8), randint(0, 8)
                while (i == 4 and j == 4) or coordinatesInList(i, j, squareEmptied):
                    i, j = randint(0, 8), randint(0, 8)
                n = [i, j, self.lists[i][j].number]
                grid.lists[i][j].removeNumber()
                if self.display:
                    print('\n\n\nThe grid before vs after:\n', n)
                    grid.displayGrid()
                grid.solve()
                if self.display:
                    grid.displayGrid()
                if grid.verifyFullyCompleted() and grid.verifyResult():
                    self.lists[i][j].removeNumber()
                    squareEmptied.append(n)
                    rest -= 1
                else:
                    cpt += 1
        if self.display:
            print('\n\n\nNumber of empty squares:\n', len(squareEmptied), cpt, '\n', squareEmptied)
            print('\nNumber of default values:', 81-level[difficulty], rest, level[difficulty], difficulty)
            self.displayGrid()

    def placeRandomDefaultNumbers(self):
        for i in range(6):
            i, j, number = randint(1, 5), randint(1, 7), randint(1, 9)
            line = convertListToInt(self.line(i))
            column = convertListToInt(self.column(j))
            box = convertListToInt(self.box(convertCoordinatesToBox(i, j)))
            while number in line or number in column or number in box:
                i, j, number = randint(1, 6), randint(1, 9), randint(1, 9)
                line = convertListToInt(self.line(i))
                column = convertListToInt(self.column(j))
                box = convertListToInt(self.box(convertCoordinatesToBox(i, j)))
            self.insertNumber(i, j, number)
        if self.display:
            print('\n\nRandom default numbers placed ont his grid:')
            self.displayGrid()

    def completeGrid(self, i=0, forward=True, arret=900, cpt=0):
        x, y = self.convertIndexToCoordinates(i)
        cpt += 1
        if i < 0 or i > 80 or arret <= 0 or cpt > 999:
            return
        else:
            if self.display:
                print('\n\n\n\nCase: x =', x+1, '; y =', y+1, '\nIndex:', i, '\nNombre de tours avant arret:', arret, '\nNombre de tours fait:', cpt, '\nNombre place sur la case avant changement:', self.lists[x][y].number)
            if self.lists[x][y].number is None:
                if self.display:
                    print('\nNo number placed before at coordinates', x+1, y+1, '\nPossibilities of other numbers:', self.lists[x][y].listOfPossibilities)
                if len(self.lists[x][y].listOfPossibilities) == 0:
                    if self.display:
                        print('\nNo possibilities of number, going back...')
                    self.lists[x][y].number = 'x'

                    self.lists[x][y].number = None
                    self.completeGrid(i-1, False, arret-1, cpt)
                else:
                    if self.display:
                        print('\nSome possible numbers, continuing with:', self.lists[x][y].listOfPossibilities[0])
                    self.lists[x][y].number = self.lists[x][y].listOfPossibilities[0]
                    self.lists[x][y].numbersTested.append(self.lists[x][y].listOfPossibilities[0])
                    self.lists[x][y].listOfPossibilities.pop(0)
                    self.updateContinuingNumber(i)
                    if self.display:
                        self.displayGrid()
                    self.completeGrid(i+1, True, arret-1, cpt)
            elif self.lists[x][y].number is not None and self.lists[x][y].defaultNumber is True:
                if self.display:
                    print('\nA default number was already placed here...')
                if forward:
                    if self.display:
                        print('Continuing forward...')
                    self.updateContinuingNumber(i)
                    if self.display:
                        self.displayGrid()
                    self.completeGrid(i+1, forward, arret-1, cpt)
                else:
                    if self.display:
                        print('Going back...')
                    if self.display:
                        self.displayGrid()
                    self.completeGrid(i-1, forward, arret-1, cpt)
            #'''
            else: #cas ou on a place un nombre mais il est faux
                if self.display:
                    print('\nA number was previously placed here at those coordinates:', x+1, y+1, '\nPossibilities of other numbers:', self.lists[x][y].listOfPossibilities)
                if len(self.lists[x][y].listOfPossibilities) == 0:
                    if self.display:
                        print('\nNo solutions remaining, going back one square...')
                    self.lists[x][y].number = 'x'
                    if self.display:
                        self.displayGrid()
                    self.lists[x][y].number = None
                    self.completeGrid(i-1, False, arret-1, cpt)
                else:
                    if self.display:
                        print('\nSome solutions remaining, testing:', self.lists[x][y].listOfPossibilities[0])
                    self.lists[x][y].number = self.lists[x][y].listOfPossibilities[0]
                    self.lists[x][y].numbersTested.append(self.lists[x][y].listOfPossibilities[0])
                    self.lists[x][y].listOfPossibilities.pop(0)
                    self.updateContinuingNumber(i)
                    if self.display:
                        self.displayGrid()
                    self.completeGrid(i+1, True, arret-1, cpt)
            #'''

    def generateGrid(self, difficulty):
        self.placeRandomDefaultNumbers()
        self.completeGrid()
        if self.display:
            self.displayGrid()
        if self.display:
            print('Fully Complete:', self.verifyFullyCompleted())
            print('Resolved:', self.verifyResult())
        if self.verifyFullyCompleted() and self.verifyResult():
            self.emptyGridSquares(difficulty)
            if self.display:
                print('\n\n\n\nThe sudoku is ready to be solved!')
            return True
        else:
            if self.display:
                print('\n\n\n\nAn unexpected error occured, please try again!')
            return False



    def extractGridCode(self):
        sudokuCode = ''
        for i in range(9):
            for j in range(9):
                if self.lists[i][j].number is not None:
                    sudokuCode += f',{i+1}/{j+1}/{self.lists[i][j].number}'
        if sudokuCode != '':
            return sudokuCode[1:]
        return sudokuCode

    def solve(self):
        self.updatePossibleNumbers()
        self.singleNumberPossible()
        self.singleOccurenceOfNumberInLine()
        self.singleOccurenceOfNumberInColumn()
        self.singleOccurenceOfNumberInBox()

    def displayGrid(self):
        print('\n')
        for i in range(len(self.lists)):
            if (i) % 3 == 0:
                print('='*31)
            for j in range(len(self.lists[i])):
                if (j+1) % 3 == 0 and (j+1) != len(self.lists[i]):
                    print(self.lists[i][j], end='||')
                else:
                    print(self.lists[i][j], end='')
            print()
        print('='*31+'\n')
###############_______________CLASS_GRID_______________###############___END