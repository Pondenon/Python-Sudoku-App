###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.variableStyleSheet import *
from Resources.pythonFiles.auxiliaryFunctions import *
from playGrid import playSudokuGrid
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
###############_______________LIBRARY_IMPORTS_______________###############___END



def addNewSudokuCode(root, startPage, previousPage, imageLogo, sudokuCode, language):
###############_______________GLOBAL_VARIABLES_______________###############___START
    difficultyVar = StringVar(root)
    difficultyVar.set(translatedText['difficultyVR'][language])
###############_______________GLOBAL_VARIABLES_______________###############___END



###############_______________WIDGET_ACTIONS_______________###############___START
    def confirmInfo():
        source = sourceEntry.get()
        difficulty = difficultyVar.get()
        if source != '' and source != translatedText['sourceET'][language] and difficulty != translatedText['difficultyVR'][language]:
            for value in levelTranslated.values():
                if value[language] == difficulty:
                    difficulty = value['English']
            addToFile('Resources/textFiles/sudokuCodes.txt', '\n' + source + ';' + difficulty + ';' + sudokuCode)
            clearWindow(root)
            playSudokuGrid(root, startPage, sudokuCode, language)

    def goToPreviousPage():
        clearWindow(root)
        previousPage(root, startPage, language)

    def on_difficulty_optionMenu(e):
        difficultyOptionMenu.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_difficulty_optionMenu(e):
        difficultyOptionMenu.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_source_entry(e):
        sourceEntry.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)
        if sourceEntry.get() == translatedText['sourceET'][language]:
            sourceEntry.delete(0, END)
    
    def off_source_entry(e):
        sourceEntry.config(bg=WHITE, fg=PRIMARYBLUE)
        if sourceEntry.get() == '':
            sourceEntry.insert(0, translatedText['sourceET'][language])

    def on_confirm_button(e):
        confirmButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_confirm_button(e):
        confirmButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_exit_button(e):
        exitButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_exit_button(e):
        exitButton.config(bg=WHITE, fg=PRIMARYBLUE)
###############_______________WIDGET_ACTIONS_______________###############___END



###############_______________WIDGET_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=665, y=275, anchor=CENTER)

    sourceEntry = Entry(root, font=enterNumbersFont, width=23)
    sourceEntry.config(bg=WHITE, fg=PRIMARYBLUE, highlightbackground=THEMEBLUE, highlightcolor=THEMEBLUE)
    #sourceEntry.insert(0, 'Origin of the Sudoku')
    sourceEntry.insert(0, translatedText['sourceET'][language])
    sourceEntry.bind('<FocusIn>', on_source_entry)
    sourceEntry.bind('<FocusOut>', off_source_entry)
    sourceEntry.place(x=275, y=200, anchor=CENTER)

    difficultyOptionMenu = OptionMenu(root, difficultyVar, *levelTranslated.keys())
    difficultyOptionMenu.config(font=enterNumbersFont, bg=WHITE, fg=PRIMARYBLUE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, highlightcolor=SECONDARYBLUE, width=22, height=1, highlightbackground=THEMEBLUE, borderwidth=0, highlightthickness=0)
    difficultyOptionMenu['menu'].config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE)
    difficultyOptionMenu.bind('<Enter>', on_difficulty_optionMenu)
    difficultyOptionMenu.bind('<Leave>', off_difficulty_optionMenu)
    difficultyOptionMenu.place(x=275, y=270, anchor=CENTER)

    confirmButton = Button(root, text=translatedText['confirmBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=450, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=confirmInfo)
    confirmButton.bind('<Enter>', on_confirm_button)
    confirmButton.bind('<Leave>', off_confirm_button)
    confirmButton.place(x=275, y=340, anchor=CENTER)

    exitButton = Button(root, text=translatedText['backBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=goToPreviousPage)
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=325, y=465, anchor=CENTER)
###############_______________WIDGET_DEFINING_______________###############___END