#wordal game. to play the game, you must also download the 5LetterWords.txt file from LINK .
from tkinter import *
root = Tk()
import random
try : 
    Fopen = open('5LetterWords.txt') 
except :
    print('5LetterWords.txt could not be found. Please ensure that you have downloaded and properly names the file from github, and that it is placed in the same folder as wordal.py')
    quit()

#Import the list of words to Python.
WordBase = list()
for word in Fopen :
    word1 = word.upper()
    wordA = word1.split()
    WordBase = WordBase + wordA

#Playing the game function
def BackgroundSetup():
    global GuessCount
    #Choosing a random word. 
    ChosenNumber = random.randint(0,2497)
    ChosenWord = WordBase[ChosenNumber]

    #Guess Box
    GuessPrompt = Label(root, text = "Enter a Guess:")
    GuessPrompt.grid(row = 3, column = 1)
    GuessSpace = Entry(root, width = 20, borderwidth = 5)
    GuessSpace.grid(row = 3, column = 2)
    GuessInitiate = Button(root, text = 'Confirm Guess', borderwidth = 3, fg = 'blue', command = PlayWordal)
    GuessInitiate.grid(row = 3, column = 3,)

    #Reset Guesses
    GuessCount = 6

    #Import 5x5 Grid
    for r in range(5):
       for c in range(5):
          Button(root, text = '?', borderwidth = 3, height = 4, width = 16,).grid(row = r+6,column = c)
   
#Guesses.
def PlayWordal() :
    global GuessCount
    while GuessCount > 0:
        PlayerGuess = input('Enter a Guess. NEED TO MAKE PROPER INPUT')
        if len(PlayerGuess) != 5 :
            print('Please enter a 5 letter word.')
            continue
        GuessCount = GuessCount-1
        if GuessCount == 0 :
            break
    
#Importing GUI
root.title("Wordal")
greeting = Label(text = "Welcome to Wordal")
greeting.grid(row = 1, column = 1)
ButtonGuess = Button(root, text = 'Start/Reset', borderwidth = 3, height = 2, width = 10, command = BackgroundSetup)
ButtonGuess.grid(row = 1, column = 3)

root.mainloop()




