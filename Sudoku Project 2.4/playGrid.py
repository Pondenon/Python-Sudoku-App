###############_______________FILES_IMPORTS_______________###############___START
from Resources.pythonFiles.auxiliaryFunctions import *
from Resources.pythonFiles.variableStyleSheet import *
###############_______________FILES_IMPORTS_______________###############___END



###############_______________LIBRARY_IMPORTS_______________###############___START
from tkinter import *
from tkmacosx import *
from classGrid import Grid
###############_______________LIBRARY_IMPORTS_______________###############___END



def playSudokuGrid(root, startPage, sudokuCode, language, level=None):
###############_______________GLOBAL_VARIABLES_______________###############___START
    solvedSudoku = Grid()
    solvedSudoku.enterDefaultNumbers(sudokuCode)

    global imageLogo
    imageLogo = createImage('sudokuLogo.png', 200, 222)

    global logoImage
    logoImage = createImage('sudokuLogo.png', 346, 385)

    global startTime
    startTime = 0

    global sudokuRunning
    sudokuRunning = True

    global sudokuUnFinished
    sudokuUnFinished = True

    nameAndLevel = nameDifficulty(sudokuCode, level, language)
###############_______________GLOBAL_VARIABLES_______________###############___END



###############_______________WIDGET_ACTIONS_______________###############___START
    def markNumberDone(i):
        if finishNumberButton[i-1]['bg'] == SECONDARYBLUE:
            finishNumberButton[i-1].config(fg=PRIMARYBLUE, bg=THEMEBLUE)
        else:
            finishNumberButton[i-1].config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def verifySudoku():
        global sudokuUnFinished
        for lines in listEntryLabel:
            for elt in lines:
                if elt.type == 'Entry':
                    sudokuResultButton.config(text=resultButton['incomplete'][language])
                    return
        for i in range(9):
            for j in range(9):
                if str(listEntryLabel[i][j].text) != str(solvedSudoku.lists[i][j].number):
                    sudokuResultButton.config(text=resultButton['false'][language])
                    return
        sudokuUnFinished = False
        sudokuResultButton.config(text=resultButton['solved'][language])
    
    def convertTimeToAnalogue(seconds):
        hours = seconds // 3660
        seconds -= hours * 3660
        minutes = seconds // 60
        seconds -= minutes * 60
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        if seconds < 10:
            seconds = '0' + str(seconds)
        return str(hours) + ':' + str(minutes) + ':' + str(seconds)

    def clock():
        global startTime
        global sudokuRunning
        global sudokuUnFinished
        if sudokuRunning and sudokuUnFinished:
            startTime += 1
            timer = convertTimeToAnalogue(startTime)
            timerLabel.config(text=timer)
        timerLabel.after(1000, clock)

    def hideSudoku():
        global sudokuRunning
        global hideFrame
        global resumeButton
        global sudokuUnFinished
        if sudokuRunning and sudokuUnFinished:
            def on_resume_button(e):
                resumeButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

            def off_resume_button(e):
                resumeButton.config(bg=WHITE, fg=PRIMARYBLUE)

            hideFrame = Frame(root, bg=THEMEBLUE, width=470, height=470)
            hideFrame.place(x=50, y=50)
            logoLabel = Label(hideFrame, image=logoImage, bg=THEMEBLUE)
            logoLabel.place(x=235, y=192, anchor=CENTER)
            resumeButton = Button(root, text=translatedText['resumeBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=380, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=hideSudoku)
            resumeButton.bind('<Enter>', on_resume_button)
            resumeButton.bind('<Leave>', off_resume_button)
            resumeButton.place(x=285, y=458, anchor=CENTER)
            sudokuRunning = False
        elif sudokuUnFinished:
            destroyWindow(hideFrame)
            destroyWindow(resumeButton)
            sudokuRunning = True

    def giveHintUser():
        number = int(hintButton['text'][2])
        if number > 0 and sudokuUnFinished and sudokuRunning:
            number -= 1
            hintButton.config(text='?•'+str(number))
            sudokuResultButton.config(text=resultButton[str(number)+'hint'][language])
            for i in range(9):
                for j in range(9):
                    if str(listEntryLabel[i][j].text) != str(solvedSudoku.lists[i][j].number):
                        listEntryLabel[i][j].insert(solvedSudoku.lists[i][j].number, THEMEBLUE)
                        return
                    
    def solveGrid():
        global sudokuUnFinished
        if sudokuUnFinished:
            for i in range(9):
                for j in range(9):
                    if str(listEntryLabel[i][j].text) != str(solvedSudoku.lists[i][j].number):
                        listEntryLabel[i][j].insert(solvedSudoku.lists[i][j].number, PRIMARYRED)
            sudokuResultButton.config(text=resultButton['solved'][language])
            sudokuUnFinished = False

    def goToPreviousPage():
        clearWindow(root)
        startPage(root, language)

    def on_pause_button(e):
        pauseResumeButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_pause_button(e):
        pauseResumeButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_hint_button(e):
        hintButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_hint_button(e):
        hintButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_solve_button(e):
        solveButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_solve_button(e):
        solveButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_finished_button(e):
        finishedButton.config(bg=SECONDARYBLUE, fg=BRIGHTBLUE)

    def off_finished_button(e):
        finishedButton.config(bg=WHITE, fg=PRIMARYBLUE)

    def on_abandon_button(e):
        abandonButton.config(bg=SECONDARYRED, fg=BRIGHTRED)

    def off_abandon_button(e):
        abandonButton.config(bg=WHITE, fg=PRIMARYRED)
###############_______________WIDGET_ACTIONS_______________###############___END



###############_______________WIDGET_DEFINING_______________###############___START
    backgroundLabel = Label(root, width=850, height=550, bg=THEMEBLUE)
    backgroundLabel.place(x=0, y=0)

    logoLabel = Label(root, image=imageLogo, bg=THEMEBLUE)
    logoLabel.place(x=682, y=0, anchor=N)

    global listEntryLabel
    listEntryLabel = []
    for i in range(1, 10):
        newLine = []
        for j in range(1, 10):
            if solvedSudoku.lists[i-1][j-1].number is None:
                text, fg = '', PRIMARYBLUE
            else:
                text, fg = solvedSudoku.lists[i-1][j-1].number, DEFAULTBLUE 
            bt = EntryLabel(root, text=text, font=enterNumbersFont, fg=fg, bg=WHITE, activebackground=SECONDARYBLUE, activeforeground=BRIGHTBLUE, width=2, height=1)
            coorx, coory = convertToPlaceCoordinates(i, j, convertCoordinatesToBox(i, j))
            #if text == '':
                #coorx, coory = coorx-3, coory-3
            bt.place(x=coory, y=coorx)
            newLine.append(bt)
        listEntryLabel.append(newLine)
    solvedSudoku.solve()

    finishNumberButton = []
    for i in range(1, 10):
        bt = Button(root, text=i, font=choicePageInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=30, height=30, borderwidth=0, highlightthickness=0, borderless=0, command= lambda number=i: markNumberDone(number))
        if i < 4:
            bt.place(x=50*i+9, y=485)
        elif i < 7:
            bt.place(x=50*i+16, y=485)
        else:
            bt.place(x=50*i+26, y=485)
        finishNumberButton.append(bt)

    sudokuNameDifficulty = Label(root, text=nameAndLevel, font=playInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE)
    sudokuNameDifficulty.place(x=682, y=228, anchor=CENTER)

    sudokuResultButton = Button(root, text='', font=choicePageInfoFont, fg=PRIMARYBLUE, bg=THEMEBLUE, activebackground=THEMEBLUE, activeforeground=PRIMARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=300, height=30, borderwidth=0, highlightthickness=0, borderless=0)
    sudokuResultButton.place(x=682, y=258, anchor=CENTER)

    timerLabel = Button(root, text='00:00:00', font=startPageFont, bg=THEMEBLUE, fg=PRIMARYBLUE, activeforeground=PRIMARYBLUE, activebackground=THEMEBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=180, height=50, borderwidth=0, highlightthickness=0, borderless=0)
    timerLabel.place(x=622, y=318, anchor=CENTER)
    timerLabel.after(1000, clock)

    pauseResumeButton = Button(root, text='⏵/⏸', font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=100, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=hideSudoku)
    pauseResumeButton.bind('<Enter>', on_pause_button)
    pauseResumeButton.bind('<Leave>', off_pause_button)
    pauseResumeButton.place(x=782, y=318, anchor=CENTER)

    hintButton = Button(root, text='?•3', font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=80, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=giveHintUser)
    hintButton.bind('<Enter>', on_hint_button)
    hintButton.bind('<Leave>', off_hint_button)
    hintButton.place(x=572, y=388, anchor=CENTER) 

    solveButton = Button(root, text=translatedText['solveBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=200, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=solveGrid)
    solveButton.bind('<Enter>', on_solve_button)
    solveButton.bind('<Leave>', off_solve_button)
    solveButton.place(x=732, y=388, anchor=CENTER)

    finishedButton = Button(root, text=translatedText['verifyBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYBLUE, activeforeground=BRIGHTBLUE, activebackground=SECONDARYBLUE, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=140, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=verifySudoku)
    finishedButton.bind('<Enter>', on_finished_button)
    finishedButton.bind('<Leave>', off_finished_button)
    finishedButton.place(x=602, y=458, anchor=CENTER)

    abandonButton = Button(root, text=translatedText['abandonBT'][language], font=startPageFont, bg=WHITE, fg=PRIMARYRED, activeforeground=BRIGHTRED, activebackground=SECONDARYRED, highlightcolor=THEMEBLUE, highlightbackground=THEMEBLUE, width=140, height=50, borderwidth=0, highlightthickness=0, borderless=0, command=goToPreviousPage)
    abandonButton.bind('<Enter>', on_abandon_button)
    abandonButton.bind('<Leave>', off_abandon_button)
    abandonButton.place(x=762, y=458, anchor=CENTER)
###############_______________WIDGET_DEFINING_______________###############___END