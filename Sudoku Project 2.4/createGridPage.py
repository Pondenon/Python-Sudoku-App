###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.variableStyleSheet import *
from Resources.pythonFiles.auxiliaryFunctions import *
from playGrid import playSudokuGrid
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
from classGrid import Grid
###############_______________LIBRARY_IMPORTS_______________###############___END



def createUserSudoku(root, startPage, previousPage, language):
###############_______________GLOBAL_VARIABLES_______________###############___START
    difficultyVar = StringVar(root)
    difficultyVar.set(translatedText['diffVR'][language])
    level = []
    for keys in levelTranslated.keys():
        level.append(levelTranslated[keys][language])
###############_______________GLOBAL_VARIABLES_______________###############___END



###############_______________WIDGETS_ACTIONS_______________###############___START
    def finishedNumberPlacement():
        sudokuCode = ''
        #sudokuCode = '1/2/7,1/3/1,1/4/9,1/7/5,2/3/5,2/4/7,2/5/4,2/9/3,3/1/4,3/6/5,3/8/9,3/9/2,4/3/7,4/4/5,4/6/1,4/8/8,4/9/9,5/2/3,5/8/6,6/1/1,6/2/2,6/4/6,6/6/7,6/7/4,7/1/8,7/2/6,7/4/2,7/9/1,8/1/7,8/5/6,8/6/8,8/7/9,9/3/2,9/6/3,9/7/6,9/8/5'
        for i in range(9):
            for j in range(9):
                if listEntryLabel[i][j].text in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    sudokuCode +=  ',' + str(i+1) + '/' + str(j+1) + '/' + str(listEntryLabel[i][j].text)
        if sudokuCode != '' and sudokuCode[0] == ',':
            sudokuCode = sudokuCode[1:]
        print(sudokuCode)
        if len(sudokuCode) > 0:
            newSudoku = Grid()
            newSudoku.enterDefaultNumbers(sudokuCode)
            newSudoku.solve()
            if newSudoku.verifyFullyCompleted():
                difficulty = difficultyVar.get()
                if sourceEntry.get() != '' and sourceEntry.get() != translatedText['srcET'][language] and difficultyVar.get() != translatedText['diffVR'][language]:
                    for value in levelTranslated.values():
                        if value[language] == difficulty:
                            difficulty = value['English']
                    addToFile('Resources/textFiles/sudokuCodes.txt', '\n' + sourceEntry.get() + ';' + difficulty + ';' + sudokuCode)
                    clearWindow(root)
                    playSudokuGrid(root, startPage, sudokuCode, language)
                else:
                    errorButton = Button(root, text=translatedText['missingInfo'][language], font=missingInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=300, height=30, borderwidth=0, highlightthickness=0, borderless=0)
                    errorButton.place(x=682, y=358, anchor=CENTER)
                    errorButton.after(5000, lambda *args: destroyWindow(errorButton))
            else:
                errorButton = Button(root, text=translatedText['incompleteSudoku'][language], font=missingInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=300, height=30, borderwidth=0, highlightthickness=0, borderless=0)
                errorButton.place(x=682, y=358, anchor=CENTER)
                errorButton.after(5000, lambda *args: destroyWindow(errorButton))
        else:
            errorButton = Button(root, text=translatedText['incompleteSudoku'][language], font=missingInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=300, height=30, borderwidth=0, highlightthickness=0, borderless=0)
            errorButton.place(x=682, y=358, anchor=CENTER)
            errorButton.after(5000, lambda *args: destroyWindow(errorButton))

    def goToPreviousPage():
        clearWindow(root)
        previousPage(root, startPage, language)

    def on_finished_button(e):
        finishedButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_finished_button(e):
        finishedButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_level_optionMenu(e):
        levelOptionMenu.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_level_optionMenu(e):
        levelOptionMenu.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_source_entry(e):
        sourceEntry.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)
        if sourceEntry.get() == translatedText['srcET'][language]:
            sourceEntry.delete(0, END)
    
    def off_source_entry(e):
        sourceEntry.config(bg=WHITE, fg=PRIMARYBLUE)
        if sourceEntry.get() == '':
            sourceEntry.insert(0, translatedText['srcET'][language])

    def on_exit_button(e):
        exitButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_exit_button(e): 
        exitButton.config(bg=WHITE, fg=PRIMARYBLUE)
###############_______________WIDGETS_ACTIONS_______________###############___END



###############_______________WIDGETS_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    global imageLogo
    imageLogo = createImage('sudokuLogo.png', 200, 222)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=682, y=0, anchor=N)

    global listEntryLabel
    listEntryLabel = []
    for i in range(1, 10):
        newLine = []
        for j in range(1, 10):
            bt = EntryLabel(root, text='', font=enterNumbersFont, fg=PRIMARYBLUE, bg=WHITE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, width=2, height=1)
            coorx, coory = convertToPlaceCoordinates(i, j, convertCoordinatesToBox(i, j))
            bt.place(x=coory, y=coorx)
            newLine.append(bt)
        listEntryLabel.append(newLine)

    sourceEntry = Entry(root, font=enterNumbersFont, width=16)
    sourceEntry.config(bg=WHITE, fg=PRIMARYBLUE, highlightbackground=THEMEBLUE, highlightcolor=THEMEBLUE)
    sourceEntry.insert(0, translatedText['srcET'][language])
    sourceEntry.bind('<FocusIn>', on_source_entry)
    sourceEntry.bind('<FocusOut>', off_source_entry)
    sourceEntry.place(x=682, y=238, anchor=CENTER)

    levelOptionMenu = OptionMenu(root, difficultyVar, *level)
    levelOptionMenu.config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, highlightcolor=SECONDARYBLUE, width=12, height=1, highlightbackground=THEMEBLUE, borderwidth=0, highlightthickness=0)
    levelOptionMenu['menu'].config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE)
    levelOptionMenu.bind('<Enter>', on_level_optionMenu)
    levelOptionMenu.bind('<Leave>', off_level_optionMenu)
    levelOptionMenu.place(x=682, y=308, anchor=CENTER)

    finishedButton = Button(root, text=translatedText['saveBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=300, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=finishedNumberPlacement)
    finishedButton.bind('<Enter>', on_finished_button)
    finishedButton.bind('<Leave>', off_finished_button)
    finishedButton.place(x=682, y=408, anchor=CENTER)

    exitButton = Button(root, text=translatedText['backBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=goToPreviousPage)
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=682, y=465, anchor=CENTER)
###############_______________WIDGETS_DEFINING_______________###############___END