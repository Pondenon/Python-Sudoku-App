###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.auxiliaryFunctions import *
from Resources.pythonFiles.variableStyleSheet import *
from selectPage import selectOriginSudoku
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
###############_______________LIBRARY_IMPORTS_______________###############___END



###############_______________WINDOW_DEFINING_______________###############___START
masterRoot = Tk()
masterRoot.title('Sudoku')
masterRoot.geometry('850x550')
masterRoot.resizable(False, False)
###############_______________WINDOW_DEFINING_______________###############___END



###############_______________VISUAL_CREATION_______________###############___START
logoImage = createImage('sudokuBanner.jpg', 977, 550)
###############_______________VISUAL_CREATION_______________###############___END



def launchSudokuApp(root, langue):
    ###############_______________GLOBAL_VARIABLES_______________###############___START
    global language
    language = langue
    ###############_______________GLOBAL_VARIABLES_______________###############___END



    ###############_______________WIDGET_ACTIONS_______________###############___START
    def changeLanguage():
        global language
        if language == 'English':
            language = 'Français'
        elif language == 'Français':
            language = 'Deutsch'
        elif language == 'Deutsch':
            language = 'Español'
        elif language == 'Español':
            language = 'English'
        changeWidgetTextLanguage()

    def changeWidgetTextLanguage():
        global language
        global translatedText
        languageButton.config(text=translatedText['languageBT'][language])
        startButton.config(text=translatedText['startBT'][language])
        exitButton.config(text=translatedText['exitBT'][language])

    def startGrid():
        clearWindow(root)
        selectOriginSudoku(root, launchSudokuApp, language)

    def on_start_button(e):
        startButton.config(bg=FADEDBLUE, fg=DARKBLUE)

    def off_start_button(e):
        startButton.config(bg=WHITE, fg=BRIGHTBLUE)

    def on_exit_button(e):
        exitButton.config(bg=FADEDRED, fg=DARKRED)

    def off_exit_button(e):
        exitButton.config(bg=WHITE, fg=BRIGHTRED)
    ###############_______________WIDGET_ACTIONS_______________###############___END



    ###############_______________WIDGETS_DEFINING_______________###############___START
    backgroundLabel = Label(root, image=logoImage)
    backgroundLabel.place(x=-60, y=0)

    languageButton = Button(root, text=translatedText['languageBT'][language], font=startLanguagePageFont, bg=BACKGROUNDBLUE, fg=WHITE, activeforeground=WHITE, activebackground=BACKGROUNDBLUE, highlightcolor=BACKGROUNDBLUE, highlightbackground=BACKGROUNDBLUE, width=40, height=30, borderwidth=0, highlightthickness=0, borderless=0, command=changeLanguage)
    languageButton.place(x=805, y=5)

    startButton = Button(root, text=translatedText['startBT'][language], font=startPageFont, bg=WHITE, fg=BRIGHTBLUE, activeforeground=DARKBLUE, activebackground=FADEDBLUE, highlightcolor=SECONDARYBLUE, highlightbackground=SECONDARYBLUE, width=430, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=startGrid)
    startButton.bind('<Enter>', on_start_button)
    startButton.bind('<Leave>', off_start_button)
    startButton.place(x=610, y=360, anchor=CENTER)

    exitButton = Button(root, text=translatedText['exitBT'][language], font=startPageFont, bg=WHITE, fg=BRIGHTRED, activeforeground=DARKRED, activebackground=FADEDRED, highlightcolor=SECONDARYBLUE, highlightbackground=SECONDARYBLUE, width=430, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=lambda *args: destroyWindow(masterRoot))
    exitButton.bind('<Enter>', on_exit_button)
    exitButton.bind('<Leave>', off_exit_button)
    exitButton.place(x=610, y=420, anchor=CENTER)
    ###############_______________WIDGETS_DEFINING_______________###############___END



launchSudokuApp(masterRoot, 'English')



###############_______________WINDOW_CLOSING_______________###############___START
masterRoot.mainloop()
###############_______________WINDOW_CLOSING_______________###############___END