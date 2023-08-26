###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.variableStyleSheet import *
from Resources.pythonFiles.auxiliaryFunctions import *
from importPage import addNewSudokuCode
from createGridPage import createUserSudoku
from choiceExistingGridPage import chooseExistingGrid
from generatePage import generateUserGrid
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
from tkinter.filedialog import askopenfilename
from classGrid import Grid
###############_______________LIBRARY_IMPORTS_______________###############___END



def selectOriginSudoku(root, startPage, language):
###############_______________VISUAL_CREATION_______________###############___START
    global imageLogo
    imageLogo = createImage('sudokuLogo.png', 243, 270)
###############_______________VISUAL_CREATION_______________###############___END



###############_______________WIDGETS_ACTIONS_______________###############___START
    def playExistingGrid():
        clearWindow(root)
        chooseExistingGrid(root, startPage, selectOriginSudoku, imageLogo, language)
    
    def generateGrid():
        clearWindow(root)
        generateUserGrid(root, startPage, selectOriginSudoku, imageLogo, language)

    def createGrid():
        clearWindow(root)
        createUserSudoku(root, startPage, selectOriginSudoku, language)

    def importGrid():
        filePath = askopenfilename(initialdir='C:/', title=translatedText['importLB'][language], filetypes=(("Text File", ".txt"), ("All Files", "*.*")))
        with open(filePath, 'r+') as askedFile:
            fileContents = askedFile.read()
        sudokuTest = Grid()
        sudokuTest.enterDefaultNumbers(fileContents)
        sudokuTest.solve()
        if not sudokuTest.verifyFullyCompleted():
            errorButton = Button(root, text=translatedText['importErrorLB'][language], font=choicePageInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=340, height=30, borderwidth=0, highlightthickness=0, borderless=0)
            errorButton.place(x=325, y=415, anchor=CENTER)
        else:
            clearWindow(root)
            addNewSudokuCode(root, startPage, selectOriginSudoku, imageLogo, fileContents, language)

    def goToHomePage():
        clearWindow(root)
        startPage(root, language)

    def on_explore_button(e):
        exploreGridButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_explore_button(e):
        exploreGridButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_generate_button(e):
        generateGridButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_generate_button(e):
        generateGridButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_create_button(e):
        createGridButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_create_button(e):
        createGridButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_import_button(e):
        importGridButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_import_button(e):
        importGridButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_exit_button(e):
        exitButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_exit_button(e): 
        exitButton.config(bg=WHITE, fg=PRIMARYBLUE)
###############_______________WIDGETS_ACTIONS_______________###############___END



###############_______________WIDGETS_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=665, y=250, anchor=CENTER)

    exploreGridButton = Button(root, text=translatedText['exploreBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=420, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=playExistingGrid)
    exploreGridButton.bind('<Enter>', on_explore_button)
    exploreGridButton.bind('<Leave>', off_explore_button)
    exploreGridButton.place(x=325, y=160, anchor=CENTER)

    generateGridButton = Button(root, text=translatedText['generateBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=420, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=generateGrid)
    generateGridButton.bind('<Enter>', on_generate_button)
    generateGridButton.bind('<Leave>', off_generate_button)
    generateGridButton.place(x=325, y=230, anchor=CENTER)

    createGridButton = Button(root, text=translatedText['createBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=420, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=createGrid)
    createGridButton.bind('<Enter>', on_create_button)
    createGridButton.bind('<Leave>', off_create_button)
    createGridButton.place(x=325, y=300, anchor=CENTER)

    importGridButton = Button(root, text=translatedText['importBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=420, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=importGrid)
    importGridButton.bind('<Enter>', on_import_button)
    importGridButton.bind('<Leave>', off_import_button)
    importGridButton.place(x=325, y=370, anchor=CENTER)

    exitButton = Button(root, text=translatedText['backBT'][language], font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=goToHomePage)
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=325, y=465, anchor=CENTER)
###############_______________WIDGETS_DEFINING_______________###############___END