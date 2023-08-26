###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
###############_______________LIBRARY_IMPORTS_______________###############___END



###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.variableStyleSheet import *
###############_______________FILES_IMPORTS_______________###############___END



class EntryLabel:
    def __init__(self, root, text, font, bg, fg, activebackground, activeforeground, width, height):
        self.root = root
        self.font = font
        self.bg = bg
        self.fg = fg
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.width = width
        self.height = height
        self.text = text
        self.numbersEntered = []
        if text == '':
            self.widget = Entry(root, font=font, width=width)
            self.widget.config(bg=bg, fg=fg, highlightbackground=THEMEBLUE, highlightcolor=THEMEBLUE)
            self.widget.bind('<Return>', self.changeToLabel)
            self.widget.bind('<FocusIn>', self.focusInEntry)
            self.widget.bind('<FocusOut>', self.focusOutEntry)
            self.widget.bind('<KeyRelease>', self.changeToLabel)
            self.widget.bind('<Button-2>', self.changeToFrame)
            self.type = 'Entry'
        elif text in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.widget = Label(root, text=text, font=font, bg=bg, fg=fg, width=width)
            self.type = 'Label'

    def insert(self, text, fg):
        destroyWindow(self.widget)
        self.text = text
        self.widget = Label(self.root, text=text, font=self.font, bg=self.bg, fg=fg, width=self.width)
        self.type = 'Label'
        self.place(x=self.x, y=self.y)

    def focusInEntry(self, e):
        self.widget.config(bg=self.activebackground, fg=self.activeforeground)
    
    def focusOutEntry(self, e):
        self.widget.config(bg=self.bg, fg=self.fg)
        if self.widget.get() in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.changeToLabel(None)

    def changeToFrame(self, e):
        def markNumberDone(i):
            if possibleNumber[i]['bg'] == SECONDARYBLUE:
                possibleNumber[i].config(fg=PRIMARYBLUE, bg=WHITE)
                self.numbersEntered.append(i)
            else:
                possibleNumber[i].config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)
                self.numbersEntered.remove(i)

        destroyWindow(self.widget)
        self.widget = Frame(self.root, bg=WHITE, width=self.width*22, height=self.height*41)
        self.type = 'Frame'
        self.place(x=self.x, y=self.y)

        possibleNumber = []
        for i in range(9):
            if i in self.numbersEntered:
                bg, fg = WHITE, PRIMARYBLUE
            else:
                bg, fg = SECONDARYBLUE, BRIGHTBLUE
            bt = Button(self.widget, text=i+1, font=playNotesFont, fg=fg, bg=bg, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=WHITE, highlightbackground=WHITE, width=16, height=15, borderwidth=0, highlightthickness=0, borderless=0, command=lambda number=i: markNumberDone(number))
            bt.bind('<Button-2>', self.changeToEntry)
            if i < 3:
                bt.place(x=15*i-1, y=-1)
            elif i < 6:
                bt.place(x=15*(i-3)-1, y=13)
            else:
                bt.place(x=15*(i-6)-1, y=27)
            possibleNumber.append(bt)
        self.widget.bind('<Button-2>', self.changeToEntry)

    def changeToEntry(self, e):
        destroyWindow(self.widget)
        self.widget = Entry(self.root, font=self.font, width=self.width)
        self.widget.config(bg=self.bg, fg=self.fg, highlightbackground=THEMEBLUE, highlightcolor=THEMEBLUE)
        self.widget.bind('<Return>', self.changeToLabel)
        self.widget.bind('<FocusIn>', self.focusInEntry)
        self.widget.bind('<FocusOut>', self.focusOutEntry)
        self.widget.bind('<KeyRelease>', self.changeToLabel)
        self.widget.bind('<Button-2>', self.changeToFrame)
        self.type = 'Entry'
        self.place(x=self.x, y=self.y)
        self.widget.insert(0, self.text)
        self.text = ''

    def  changeToLabel(self, e):
        number = self.widget.get()
        if number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            destroyWindow(self.widget)
            self.text = number
            self.widget = Label(self.root, text=number, font=self.font, bg=self.bg, fg=self.fg, width=self.width)
            self.type = 'Label'
            self.place(x=self.x, y=self.y)
            self.widget.bind('<Button-1>', self.changeToEntry)

    def place(self, x, y):
        self.x = x
        self.y = y
        if self.type == 'Entry':
            self.widget.place(x=self.x-3, y=self.y-3)
        else:
            self.widget.place(x=self.x, y=self.y)


def createImage(fileName, width, height):
    image = Image.open(f'Resources/Images/{fileName}')
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image

def clearWindow(window):
    for widget in window.winfo_children():
        widget.destroy()

def destroyWindow(root):
    root.destroy()

def noDoubles(list):
    newList = []
    for elt in list:
        if elt in newList:
            return False
        else:
            newList.append(elt)
    return True

def convertCoordinatesToBox(i, j):
    if 0 < i < 4 and 0 < j < 4:
        return 1
    elif 0 < i < 4 and 3 < j < 7:
        return 2
    elif 0 < i < 4 and 6 < j < 10:
        return 3
    elif 3 < i < 7 and 0 < j < 4:
        return 4
    elif 3 < i < 7 and 3 < j < 7:
        return 5
    elif 3 < i < 7 and 6 < j < 10:
        return 6
    elif 6 < i < 10 and 0 < j < 4:
        return 7
    elif 6 < i < 10 and 3 < j < 7:
        return 8
    elif 6 < i < 10 and 6 < j < 10:
        return 9
    else:
        print(f'\n\n\nERROR - COORDINATES I = {i} AND J = {j} INCOMPATIBLE\n\n\n')
        return 0

def convertListToInt(list):
    #numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    intList = []
    for i in range(len(list)):
        if list[i].number is not None:
            intList.append(list[i].number)
    return intList

def convertToPlaceCoordinates(i, j, box):
    pad = 15
    y, x = 45*i+5, 48*j+5
    if box % 3 == 2:
        x += pad
    elif box % 3 == 0:
        x += pad * 2
    if 4 <= box <= 6:
        y += pad
    elif 7 <= box <= 9:
        y += pad * 2
    return y, x

def addToFile(filePath, line):
    file = open(filePath, 'a')
    file.write(line)
    file.close()

def nameDifficulty(code, level, language):
    file = open('Resources/textFiles/sudokuCodes.txt', 'r')
    list = file.readlines()
    file.close()
    for line in list:
        line = line.split(';')
        if line[2] == code:
            return levelTranslated[line[1]][language] + ' • ' + line[0]
    if level is not None:
        return levelTranslated[level][language] + ' • ' + translatedText['generatedSudoku'][language] + ' #' + str(numberOfGeneratedGrids+1)
    return ''

def numberOfGeneratedGrids():
    file = open('Resources/textFiles/sudokuCodes.txt', 'r')
    list = file.readlines()
    file.close()
    cpt = 0
    for line in list:
        line = line.split(';')
        if len(line[0]) > 16 and line[0][:18] == 'Generated Sudoku #':
            cpt += 1
    return cpt

def coordinatesInList(i, j, list):
    for elt in list:
        if elt[0] == i and elt[1] == j:
            return True
    return False