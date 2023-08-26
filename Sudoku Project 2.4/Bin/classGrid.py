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
        self.noChange = 0

    def insertNumber(self, x, y, number):
        self.lists[x-1][y-1].insertNumber(number)

    def prepareGrid(self, command):
        command = command.split(',')
        for elt in command:
            if not verifyInput(elt):
                print(elt)
                self.prepareGrid()
        for elt in command:
            self.insertNumber(int(elt[0]), int(elt[2]), int(elt[4]))

    def play(self):
        while True:
            command = input('Enter the information concerning the square you wish to modify: ')
            while not verifyInput(command):
                command = input('Re-enter the information concerning the square you wish to modify: ')
            self.insertNumber(int(command[0]), int(command[2]), int(command[4]))
            self.display()

    def solve(self):
        self.updatePossibilities()
        self.shrinkPossibilities()

    def verifyFullyCompleted(self):
        for i in range(9):
            for j in range(9):
                if self.lists[i][j].number is None:
                    return False
        return True

    def updatePossibilities(self):
        if self.verifyFullyCompleted():
            self.verifyResult()
        else:
            self.noChange += 1
            for i in range(1, 10):
                for j in range(1, 10):
                    if self.lists[i-1][j-1].number is None:
                        line = convertListToInt(self.line(i))
                        column = convertListToInt(self.column(j))
                        box = convertListToInt(self.box(convertCoordinatesToBox(i, j)))
                        print(line, '\n', column, '\n', box)
                        for number in range(1, 10):
                            print(number, number in line,  number in column, number in box)
                            if number in line or number in column or number in box:
                                self.lists[i-1][j-1].possibilities[number] = False
                            elif number not in line and number not in column and number not in box:
                                self.lists[i-1][j-1].possibilities[number] = True
                        print(self.lists[i-1][j-1].possibilities, i-1, j-1)
                        if self.lists[i-1][j-1].verifySinglePossibility():
                            self.noChange = 0
                            self.display()
                            print(1)
                            self.solve()
                
    def shrinkPossibilities(self):
        self.noChange += 1
        #for all lines
        for i in range(1, 10):
            dico = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for j in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    for key in self.lists[i-1][j-1].possibilities.keys():
                        if self.lists[i-1][j-1].possibilities[key]:
                            dico[key].append((i, j))
            for key in dico.keys():
                if len(dico[key]) == 1:
                    self.lists[dico[key][0][0]-1][dico[key][0][1]-1].number = key
                    self.nochange = 0
                    self.display()
                    print(3)
                    self.updatePossibilities()
            #change line
        #for all columns
        for j in range(1, 10):
            dico = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for i in range(1, 10):
                if self.lists[i-1][j-1].number is None:
                    for key in self.lists[i-1][j-1].possibilities.keys():
                        if self.lists[i-1][j-1].possibilities[key]:
                            dico[key].append((i, j))
            for key in dico.keys():
                if len(dico[key]) == 1:
                    self.lists[dico[key][0][0]-1][dico[key][0][1]-1].number = key
                    self.nochange = 0
                    self.display()
                    print(4)
                    self.updatePossibilities()
            #change column
        # for all boxes
        for i in range(1, 10):
            box = self.box(i)
            dico = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
            for j in range(len(box)):
                if box[j].number is None:
                    for key in box[j].possibilities.keys():
                        if box[j].possibilities[key]:
                            dico[key].append(j)
            for key in dico.keys():
                if len(dico[key]) == 1:
                    box[dico[key][0]].number = key
                    self.nochange = 0
                    self.display()
                    print(5)
                    self.updatePossibilities()

    def start(self, command):
        self.prepareGrid(command)
        self.display()
        
    def start1(self):
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
    
    def box1(self, i):
        if i == 1:
            return self.line(1)[:3] + self.line(2)[:3] + self.line(3)[:3]
        elif i == 2:
            return self.line(1)[3:6] + self.line(2)[3:6] + self.line(3)[3:6]
        elif i == 3:
            return self.line(1)[6:] + self.line(2)[6:] + self.line(3)[6:]
        
        elif i == 4:
            return self.line(4)[:3] + self.line(5)[:3] + self.line(6)[:3]
        elif i == 5:
            return self.line(4)[3:6] + self.line(5)[3:6] + self.line(6)[3:6]
        elif i == 6:
            return self.line(4)[6:] + self.line(5)[6:] + self.line(6)[6:]
        
        elif i == 7:
            return self.line(7)[:3] + self.line(8)[:3] + self.line(9)[:3]
        elif i == 8:
            return self.line(7)[3:6] + self.line(8)[3:6] + self.line(9)[3:6]
        elif i == 9:
            return self.line(7)[6:] + self.line(8)[6:] + self.line(9)[6:]

    def display(self):
        for i in range(len(self.lists)):
            if (i) % 3 == 0:
                print('='*31)
            for j in range(len(self.lists[i])):
                if (j+1) % 3 == 0 and (j+1) != len(self.lists[i]):
                    print(self.lists[i][j], end='||')
                else:
                    print(self.lists[i][j], end='')
            print()
        print('='*31)

    def verifyResult(self):
        for i in range(1, 10):
            if not noDoubles(convertListToInt(self.line(i))) or not noDoubles(convertListToInt(self.column(i))) or not noDoubles(convertListToInt(self.box(i))):
                print('\n\nThe result is false.')
                return
        print('\n\nThe Sudoku is resolved !')
###############_______________CLASS_GRID_______________###############___END


s = Grid()
s.start('1/4/6,1/6/3,1/7/9,2/5/2,2/6/1,2/7/8,3/1/3,3/2/1,3/6/9,4/1/1,4/2/5,4/3/6,4/9/2,5/2/9,5/8/7,6/1/4,6/7/5,6/8/6,6/9/9,7/4/5,7/8/2,7/9/4,8/3/5,8/4/3,8/5/4,9/3/4,9/4/2,9/6/6')
s.start1()