###############_______________FILES_IMPORTS_______________###############___START
from selectPage import selectOriginSudoku
from Resources.pythonFiles.variableStyleSheet import *
from Resources.pythonFiles.auxiliaryFunctions import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
###############_______________LIBRARY_IMPORTS_______________###############___END



def listUserChoice(root):
###############_______________WIDGET_ACTIONS_______________###############___START
    def playGrid():
        selectOriginRoot = Toplevel()
        selectOriginRoot.title('Sudoku - Origin Grid')
        selectOriginRoot.geometry('850x550')
        selectOriginRoot.resizable(False, False)
        selectOriginSudoku(selectOriginRoot, imageLogo)
        destroyWindow(root)
        selectOriginRoot.mainloop()

    def resolveGrid():
        resolveGridRoot = Toplevel()
        resolveGridRoot.title('Sudoku - Resolve')
        resolveGridRoot.geometry('850x550')
        resolveGridRoot.resizable(False, False)
        #resolveUserSudoku(resolveGridRoot)
        destroyWindow(root)
        resolveGridRoot.mainloop()

    def on_grid_button(e):
        playGridButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)
        explanationLabel.config(text='INFORMATION\n\nAsk the computer to generate an\nentire sudoku for you! Or play the\nmany sudoku already installed.\n\nIf you find yourself stuck, you can      \nalways count on the computer to\ngive you hints or resolve the\nsudoku!\n\n\n\n\n', justify=LEFT)

    def off_grid_button(e):
        playGridButton.config(bg=WHITE, fg=PRIMARYBLUE)
        explanationLabel.config(text='')

    def on_resolve_button(e):
        resolveButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)
        explanationLabel.config(text='INFORMATION\n\nHaving a problem with a sudoku\nyou are doing ? Curious about wether\nor not the sudoku you created works ?\n\nType it in the game and let\nthe computer tell you!\n\n\n\n\n\n\n')

    def off_resolve_button(e):
        resolveButton.config(bg=WHITE, fg=PRIMARYBLUE)
        explanationLabel.config(text='')

    def on_exit_button(e):
        exitButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_exit_button(e):
        exitButton.config(bg=WHITE, fg=PRIMARYBLUE)
###############_______________WIDGET_ACTIONS_______________###############___END



###############_______________VISUAL_CREATION_______________###############___START
    global imageLogo
    imageLogo = createImage('sudokuLogo.png', 243, 270) #429, 477
###############_______________VISUAL_CREATION_______________###############___END



###############_______________WIDGETS_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=425, y=0, anchor=N)

    explanationLabel = Label(root, text='', font=choicePageInfoFont, bg=THEMEBLUE, fg=PRIMARYBLUE, width=30, height=15)
    explanationLabel.place(x=540, y=290)

    playGridButton = Button(root, text='Play A Grid', font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=380, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=playGrid)
    playGridButton.bind('<Enter>', on_grid_button)
    playGridButton.bind('<Leave>', off_grid_button)
    playGridButton.place(x=325, y=315, anchor=CENTER)

    resolveButton = Button(root, text='Resolve Grid', font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=380, height=50, borderwidth=0, highlightthickness=0, borderless=0)
    resolveButton.bind('<Enter>', on_resolve_button)
    resolveButton.bind('<Leave>', off_resolve_button)
    resolveButton.place(x=325, y=385, anchor=CENTER)

    exitButton = Button(root, text='Back', font=choicePageBackFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=THEMEBLUE, width=140, height=40, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: destroyWindow(root))
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=325, y=465, anchor=CENTER)
###############_______________WIDGETS_DEFINING_______________###############___END