###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.auxiliaryFunctions import *
from Resources.pythonFiles.variableStyleSheet import *
from playGrid import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
from classGrid import Grid
###############_______________LIBRARY_IMPORTS_______________###############___END



def generateUserGrid(root, startPage, previousPage, imageLogo, language):
###############_______________WIDGETS_ACTIONS_______________###############___START
    def generateUserGridDifficulty(difficulty):
        newSudoku = Grid(False)
        if newSudoku.generateGrid(difficulty):
            sudokuCode = newSudoku.extractGridCode()
            addToFile('Resources/textFiles/sudokuCodes.txt', '\n' + 'Generated Sudoku #' + str(numberOfGeneratedGrids()+1) + ';' + difficulty + ';' + sudokuCode)
            clearWindow(root)
            playSudokuGrid(root, startPage, sudokuCode, language, difficulty)
        else:
            errorButton = Button(root, text=translatedText['unexpectedError'][language], font=choicePageInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=400, height=30, borderwidth=0, highlightthickness=0, borderless=0)
            errorButton.place(x=620, y=465, anchor=CENTER)
            errorButton.after(5000, lambda *args: destroyWindow(errorButton))

    def goToPreviousPage():
        clearWindow(root)
        previousPage(root, startPage, language)

    def on_veryEasy_button(e):
        veryEasyButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_veryEasy_button(e):
        veryEasyButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_easy_button(e):
        easyButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_easy_button(e):
        easyButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_medium_button(e):
        mediumButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_medium_button(e):
        mediumButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_hard_button(e):
        hardButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_hard_button(e):
        hardButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_veryHard_button(e):
        veryHardButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_veryHard_button(e):
        veryHardButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_impossible_button(e):
        impossibleButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_impossible_button(e):
        impossibleButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_exit_button(e):
        exitButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_exit_button(e): 
        exitButton.config(bg=WHITE, fg=PRIMARYBLUE)
###############_______________WIDGETS_ACTIONS_______________###############___END



###############_______________WIDGETS_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=425, y=0, anchor=N)

    veryEasyButton = Button(root, text=levelTranslated['Very Easy'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Very Easy'))
    veryEasyButton.bind('<Enter>', on_veryEasy_button)
    veryEasyButton.bind('<Leave>', off_veryEasy_button)
    veryEasyButton.place(x=165, y=300, anchor=CENTER)

    easyButton = Button(root, text=levelTranslated['Easy'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Easy'))
    easyButton.bind('<Enter>', on_easy_button)
    easyButton.bind('<Leave>', off_easy_button)
    easyButton.place(x=425, y=300, anchor=CENTER)

    mediumButton = Button(root, text=levelTranslated['Medium'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Medium'))
    mediumButton.bind('<Enter>', on_medium_button)
    mediumButton.bind('<Leave>', off_medium_button)
    mediumButton.place(x=685, y=300, anchor=CENTER)

    hardButton = Button(root, text=levelTranslated['Hard'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Hard'))
    hardButton.bind('<Enter>', on_hard_button)
    hardButton.bind('<Leave>', off_hard_button)
    hardButton.place(x=165, y=370, anchor=CENTER)

    veryHardButton = Button(root, text=levelTranslated['Very Hard'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Very Hard'))
    veryHardButton.bind('<Enter>', on_veryHard_button)
    veryHardButton.bind('<Leave>', off_veryHard_button)
    veryHardButton.place(x=425, y=370, anchor=CENTER)

    impossibleButton = Button(root, text=levelTranslated['Impossible'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=250, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: generateUserGridDifficulty('Impossible'))
    impossibleButton.bind('<Enter>', on_impossible_button)
    impossibleButton.bind('<Leave>', off_impossible_button)
    impossibleButton.place(x=685, y=370, anchor=CENTER)

    exitButton = Button(root, text=translatedText['backBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=goToPreviousPage)
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=325, y=465, anchor=CENTER)
###############_______________WIDGETS_DEFINING_______________###############___END