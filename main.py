# main.py
# Alon
# 1/1/2021
# gui section of war game

import tkinter # import tkinter module
from tkinter import messagebox # import message box
import GamePlay # import GamePlay file

class WarGUI:
    # represents the war GUI
    def __init__(self):
        self.play = GamePlay.WarGame() # initilize WarGame attribute (WarGame)
        self.initializeGetName() # get names from user
        self.initializeMain() # initialize the main window
    # end __init__() 

    def initializeGetName(self):
        # initilizes get name window
        # param: None
        # return: null
        self.getNameWindow = tkinter.Tk() # initilize window
        self.getNameWindow.title('Enter names') # no title
        self.getNameWindow.resizable(False, False) # make not resizable
        
        # initialize promot labels
        self.enterNameLabel1 = tkinter.Label(self.getNameWindow, text='Enter Player 1 name:')
        self.enterNameLabel2 = tkinter.Label(self.getNameWindow, text='Enter Player 2 name:')
        # initilize entries for names
        self.entryName1 = tkinter.Entry(self.getNameWindow, width=10)
        self.entryName2 = tkinter.Entry(self.getNameWindow, width=10)
        # initialize entry button
        self.enterButton = tkinter.Button(self.getNameWindow, text='Enter', command=self.enterNameClick)

        # set all widgets on grid
        self.enterNameLabel1.grid(row=1, column=1)
        self.entryName1.grid(row=1, column=2)
        self.enterNameLabel2.grid(row=2, column=1)
        self.entryName2.grid(row=2, column=2)
        self.enterButton.grid(row=3, column=2, sticky=tkinter.W+tkinter.E) # stretch widget west and east

        # enter main loop
        self.getNameWindow.mainloop()
        return
    # end InitializeGetName()
    
    def enterNameClick(self):
        # get names from entries
        # param: None
        # return null
        # get names from entries
        self.name1 = self.entryName1.get()
        self.name2 = self.entryName2.get()
        if self.name1 == ' '*len(self.name1) or self.name2 == ' '*len(self.name2): # checl names are not empty or whitespace
            messagebox.showinfo('Error', 'You must enter a name.') # display error message
        else:
            # strip leading or trailing whitespace and use only first 10 chars of names
            self.name1 = self.name1.strip()[:10]
            self.name2 = self.name2.strip()[:10]
            self.getNameWindow.destroy() # destroy the window
        return
    # end enterNameClick()

    def initializeMenu(self):
        # initilize the mainWindow menu
        self.mainMenu = tkinter.Menu(self.mainWindow) # create mainMenu
        self.menu = tkinter.Menu(self.mainMenu, tearoff = 0)
        self.menu.add_command(label='Instructions', command=self.displayInstructions) # create instructions command
        self.menu.add_command(label='Exit', command=self.mainWindow.destroy) # create exit command
        self.mainMenu.add_cascade(label='Menu', menu = self.menu)
        self.mainWindow.config(menu=self.mainMenu)
        return
    # initializeMenu

    def initializeFrames(self):
        # initialize all the frames 
        self.frame1 = tkinter.LabelFrame(self.mainWindow)
        self.frame2 = tkinter.LabelFrame(self.mainWindow)
        self.frame3 = tkinter.LabelFrame(self.mainWindow)
        self.frame4 = tkinter.LabelFrame(self.mainWindow)
        self.frame5 = tkinter.LabelFrame(self.mainWindow)
        self.frame6 = tkinter.LabelFrame(self.mainWindow)
        self.frame7 = tkinter.LabelFrame(self.mainWindow)
        return
    # end initializeFrames()

    def initializeLabels(self):
        # initialize all labels 
        # initialize name and score labels
        self.name1Lbl = tkinter.Label(self.frame1, text=f'{self.name1:^20}', font=('Arial Bold', 10))
        self.scoreLbl1 = tkinter.Label(self.frame1, text=len(self.play.deck1.cards), font=('Arial Bold', 10))
        self.name2Lbl = tkinter.Label(self.frame2, text=f'{self.name2:^20}', font=('Arial Bold', 10))
        self.scoreLbl2 = tkinter.Label(self.frame2, text=len(self.play.deck2.cards), font=('Arial Bold', 10))
        # pack labels to frames on top side
        self.name1Lbl.pack(side='top')
        self.scoreLbl1.pack(side='top')
        self.name2Lbl.pack(side='top')
        self.scoreLbl2.pack(side='top')
        # put frames in grid
        self.frame1.grid(row=2, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W) # stretch widget to all sides
        self.frame2.grid(row=3, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)  # stretch widget to all sides

        # initilize war label
        self.warLbl = tkinter.Label(self.frame3, text='Click NEXT to flip', font=('Arial Bold', 10))
        self.warLbl.pack() # pack label to frame
        self.frame3.grid(row=1, column=1, columnspan=2, sticky=tkinter.W+tkinter.E) # put frame in grid, stretch widget west and east

        self.winLbl = tkinter.Label(self.frame6, font=('Arial Bold', 10)) # initialize win label
        self.winLbl.pack() # pack label to frame
        self.frame6.grid(row=4, column=1, columnspan=2, sticky=tkinter.W+tkinter.E) # put frame in grid stretch widget west and east
        return
    # end initializeLabels

    def initializeCards(self):
        # initialize the card pictures
        self.blankCard = tkinter.PhotoImage(file='cards/blank.png') # create blank card picture
        # create labels with picture
        self.blankCardLbl1 = tkinter.Label(self.frame4, image=self.blankCard) 
        self.card1Lbl = tkinter.Label(self.frame4, image=self.blankCard)
        self.blankCardLbl2 = tkinter.Label(self.frame5, image=self.blankCard)
        self.card2Lbl = tkinter.Label(self.frame5, image=self.blankCard)
        # pack labels to frames on left
        self.blankCardLbl1.pack(side='left')
        self.card1Lbl.pack(side='left')
        self.blankCardLbl2.pack(side='left')
        self.card2Lbl.pack(side='left')
        # put frames in grid
        self.frame4.grid(row=2, column=2)
        self.frame5.grid(row=3, column=2)
        return 
    # end initializeCards()

    def initializeButton(self):
        # initialize next button
        self.nextBttn = tkinter.Button(self.frame7, text='NEXT', font=('Arial Bold', 10), command=self.next) # create button 
        self.nextBttn.pack() # pack button to frame
        self.frame7.grid(row=5, column=1, columnspan=2, sticky=tkinter.W+tkinter.E) # put frame in grid, stretch west and east
        return 
    # end initializeButton()

    def initializeMain(self):
        self.mainWindow = tkinter.Tk() # initialize main window
        self.mainWindow.resizable(False, False) # make window not resizble
        self.mainWindow.title('War') # set title to war

        self.initializeMenu() # initialize menu
        self.initializeFrames() # initialize frames
        self.initializeLabels() # initialize labels
        self.initializeCards() # initialize card pictures
        self.initializeButton() # initialize next button
          
        self.mainWindow.mainloop() # enter main loop
        return
    # end initializeMain()
        
    def displayInstructions(self):
        # display instructions
        # create messagebox with instructions
        messagebox.showinfo('Instruction', 'Each player gets 26 cards.\n\nClick NEXT to turn 2 cards from each player\'s deck.\n\nThe player that turned the higher valued card gets the 2 cards.\n\nIf cards are the same value, each player turns an additional\nthree cards face down and another face up.\n\nThe player with the higher value wins all the cards.')
        # return
    # end displayInstructions()
 
    def next(self):
        # update game and window when next is pressed
        self.play.nextRound() # play next round
        self.updateCards() # update cards pictures
        self.updateScore() # update scores
        self.updateWarLabel() # update war label
        self.updateWinLabel() # udpdate win label
        self.endGame() # end game when player wins
        return
    # end next()

    def updateCards(self):
        # update the pictures of the cards

        # set up new card1 picture
        card1 = tkinter.PhotoImage(file=f'cards/{self.play.card1.value}-{self.play.card1.suit}.png')
        self.card1Lbl.configure(image=card1)
        self.card1Lbl.photo = card1

        # set up new card2 picture
        card2 = tkinter.PhotoImage(file=f'cards/{self.play.card2.value}-{self.play.card2.suit}.png')
        self.card2Lbl.configure(image=card2)
        self.card2Lbl.photo = card2
        return
    # end updateCards()

    def updateScore(self):
        # update the score
        # configure the score labels with size of decks
        self.scoreLbl1.configure(text=len(self.play.deck1.cards))
        self.scoreLbl2.configure(text=len(self.play.deck2.cards))
        return
    # end updateScore()

    def updateWarLabel(self):
        # update the war label
        if self.play.card1.value > self.play.card2.value: # if player 1 won
            text = f'{self.play.card1.__str__()} is higher than {self.play.card2.__str__()}' # update text correctly
        # end if
        elif self.play.card2.value > self.play.card1.value: # if player 2 won
            text = f'{self.play.card2.__str__()} is higher than {self.play.card1.__str__()}' # update text correctly
        # end elif
        else:
            text = 'Tie'
        # end else
        self.warLbl.configure(text=f'{text:^30}') # configure label text 
        return
    # end updateWarLabel

    def updateWinLabel(self):
        # update the win label
        if self.play.card1.value > self.play.card2.value: # if player 1 won
            text = f'{self.name1} wins card' # update text correctly
        # end if
        elif self.play.card2.value > self.play.card1.value: # if player 2 won
            text = f'{self.name2} wins card' # update text correctly
        # end elif
        else:
            text = 'War!'
        # end else
        self.winLbl.configure(text=f'{text:^30}') # update label text
        return
    # end updateWinLabel()

    def endGame(self):
        # create endgame window when game ends
        if self.play.exit: # if exit is true: someone won
            self.nextBttn.destroy() # destroy the next button
            self.exitGame = tkinter.Tk() # create exitGame window
            self.exitGame.geometry('200x90')
            self.exitGame.resizable(False, False) # make window not resizble
            self.exitGame.title('Game Over') # set title to game over
            self.winnerLbl = tkinter.Label(self.exitGame, text=self.getWinner(), font=('Arial Bold', 10)) # set up label announcing the winner
            self.playAgainBttn = tkinter.Button(self.exitGame, text='Play Again', command=self.playAgain, font=('Arial Bold', 10)) # set up button to play again
            self.exitBttn = tkinter.Button(self.exitGame, text='Exit', command=self.exit, font=('Arial Bold', 10)) # set up button to exit game
            # pack all widgets
            self.winnerLbl.pack()
            self.playAgainBttn.pack()
            self.exitBttn.pack()
            self.exitGame.mainloop()
        # end if
        return
    # end endGame()
    
    def getWinner(self):
        # generate winner message
        # return: winner message (str)
        if not(self.play.deck1.hasCards()) and not(self.play.deck2.hasCards()): # if both decks are empty
            msg = 'Tie'
        elif not(self.play.deck1.hasCards()): # if deck1 is empty
            msg = f'{self.name2} won the game!'
        elif not(self.play.deck2.hasCards()): # if deck2 is empty
            msg = f'{self.name1} won the game!'
        # end if
        return msg
    # end getWinner

    def playAgain(self):
        # play again command
        self.exitGame.destroy() # destroy exit game window
        self.mainWindow.destroy() # destroy main window
        del self.play # delete instance of WarGame class
        self.__init__() # initialize warGUI object again
        return
    # end playAgain()
    
    def exit(self):
        # exit game command
        self.exitGame.destroy() # destroy exit game window
        self.mainWindow.destroy() # destroy mainWindow
        return
    # end exit()
        
game = WarGUI() # initialize WarGUI object