###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.auxiliaryFunctions import destroyWindow
from Resources.pythonFiles.variableStyleSheet import *
from playGrid import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
###############_______________LIBRARY_IMPORTS_______________###############___END



def chooseExistingGrid(root, startPage, previousPage, imageLogo, language):
###############_______________GLOBAL_VARIABLES_______________###############___START
    global firstClick
    firstClick = False

    global sourceVar
    sourceVar = StringVar(root)
    sourceVar.set(translatedText['sourceVR'][language])

    difficultyVar = StringVar(root)
    difficultyVar.set(translatedText['difficultyVR'][language])
###############_______________GLOBAL_VARIABLES_______________###############___END



###############_______________FILE_MANIPULATION_______________###############___START
    gridCodesFile = open('Resources/textFiles/sudokuCodes.txt', 'r')
    gridCodes = gridCodesFile.readlines()
    gridCodesFile.close()
    gridKeys = []
    for elt in gridCodes:
        gridKeys.append(elt.split(';'))
    levelDict = {}
    for elt in gridKeys:
        if elt[1] not in levelDict.keys():
            levelDict[elt[1]] = [elt[0]]
        else:
            levelDict[elt[1]].append(elt[0])
    level = []
    for keys in levelDict.keys():
        level.append(levelTranslated[keys][language])
###############_______________FILE_MANIPULATION_______________###############___END



###############_______________WIDGETS_ACTIONS_______________###############___START
    def changeGridSource(e):
    ###############_______________GLOBAL_VARIABLES_______________###############___START
        global firstClick
        global sourceOptionMenu
        global sourceVar
    ###############_______________GLOBAL_VARIABLES_______________###############___END



    ###############_______________WIDGETS_ACTIONS_______________###############___START
        def on_source_optionMenu(e):
            sourceOptionMenu.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

        def off_source_optionMenu(e):
            sourceOptionMenu.config(bg=WHITE, fg=PRIMARYBLUE)
    ###############_______________WIDGETS_ACTIONS_______________###############___END



    ###############_______________WIDGETS_ACTIONS_______________###############___START
        if firstClick:
            destroyWindow(sourceOptionMenu)
        difficulty = difficultyVar.get()
        for value in levelTranslated.values():
            if value[language] == difficulty:
                difficulty = value['English']
        firstClick = True
        sourceList = []
        for elt in gridKeys:
            if elt[1] == difficulty:
                sourceList.append(elt[0])
        
        sourceOptionMenu = OptionMenu(root, sourceVar, *sourceList)
        sourceOptionMenu.config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, highlightcolor=SECONDARYBLUE, width=22, height=1, highlightbackground=THEMEBLUE, borderwidth=0, highlightthickness=0)
        sourceOptionMenu['menu'].config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE)
        sourceOptionMenu.bind('<Enter>', on_source_optionMenu)
        sourceOptionMenu.bind('<Leave>', off_source_optionMenu)
        sourceOptionMenu.place(x=325, y=385, anchor=CENTER)
    ###############_______________WIDGETS_ACTIONS_______________###############___END



    def confirmGrid():
        if sourceVar.get() != translatedText['sourceVR'][language]:
            difficulty = difficultyVar.get()
            for value in levelTranslated.values():
                if value[language] == difficulty:
                    difficulty = value['English']
            for elt in gridKeys:
                if elt[1] == difficulty and elt[0] == sourceVar.get():
                    sudokuCode = elt[2]
            clearWindow(root)
            playSudokuGrid(root, startPage, sudokuCode, language)

    def goToPreviousPage():
        clearWindow(root)
        previousPage(root, startPage, language)
    
    def on_level_optionMenu(e):
        levelOptionMenu.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_level_optionMenu(e):
        levelOptionMenu.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_confirm_button(e):
        confirmButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_confirm_button(e): 
        confirmButton.config(bg=WHITE, fg=PRIMARYBLUE)

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

    levelOptionMenu = OptionMenu(root, difficultyVar, *level, command=changeGridSource)
    levelOptionMenu.config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, highlightcolor=SECONDARYBLUE, width=22, height=1, highlightbackground=THEMEBLUE, borderwidth=0, highlightthickness=0)
    levelOptionMenu['menu'].config(font=existingGridFont, bg=WHITE, fg=PRIMARYBLUE)
    levelOptionMenu.bind('<Enter>', on_level_optionMenu)
    levelOptionMenu.bind('<Leave>', off_level_optionMenu)
    levelOptionMenu.place(x=325, y=315, anchor=CENTER)

    confirmButton = Button(root, text=translatedText['confirmBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=confirmGrid)
    confirmButton.bind('<Enter>', on_confirm_button)
    confirmButton.bind('<Leave>', off_confirm_button)
    confirmButton.place(x=490, y=465, anchor=CENTER)

    exitButton = Button(root, text=translatedText['backBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=goToPreviousPage)
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=325, y=465, anchor=CENTER)
###############_______________WIDGETS_DEFINING_______________###############___END