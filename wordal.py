#wordal game. to play the game, you must also download the 5LetterWords.txt file from https://github.com/spruce04/Wordal-Game/blob/main/5LetterWords.txt
#Place the txt file in the same location as this script and ensure it is properly named. 
from tkinter import *
import tkinter.font as font
root = Tk()
import random
try : 
    Fopen = open('5LetterWords.txt') 
except :
    print('5LetterWords.txt could not be found. Please ensure that you have downloaded and properly names the file from github, and that it is placed in the same folder as wordal.py')
    quit()

#Setup Font
myFont = font.Font(size=60)

#Comparing Player Choice and Randomly Chosen Word
def ComparePC() :
    global PlayerGuess 
    global ChosenWord
    global PGLetter1
    global PGLetter2
    global PGLetter3
    global PGLetter4
    global PGLetter5
    global CWLetter1
    global CWLetter2
    global CWLetter3
    global CWLetter4
    global CWLetter5
    global LetterColour1
    global LetterColour2
    global LetterColour3 
    global LetterColour4 
    global LetterColour5
    #Extract the positions and letters of PlayerGuess
    PGLetter1 = PlayerGuess[0]
    PGLetter2 = PlayerGuess[1]
    PGLetter3 = PlayerGuess[2]
    PGLetter4 = PlayerGuess[3]
    PGLetter5 = PlayerGuess[4]
    #Extract the positions and letters of ChosenWord
    CWLetter1 = ChosenWord[0]
    CWLetter2 = ChosenWord[1]
    CWLetter3 = ChosenWord[2]
    CWLetter4 = ChosenWord[3]
    CWLetter5 = ChosenWord[4]

#Determine if they are equal
def DetermineColour() :
    global LetterColour1
    global LetterColour2
    global LetterColour3
    global LetterColour4
    global LetterColour5
#First Letter
    FindFirstLetterA = ChosenWord.find(PGLetter1)
    FindFirstLetterB = ChosenWord.find(CWLetter1)
    if FindFirstLetterA == -1 :
        LetterColour1 = 'black'
        ChosenWord1 = list(ChosenWord)
        ChosenWord1[FindFirstLetterA] = '.'
        ChosenWord1A = ''.join(ChosenWord1)
    elif FindFirstLetterA == FindFirstLetterB :
         LetterColour1 = 'green'
         #Accounting for Duplicates
         ChosenWord1 = list(ChosenWord)
         ChosenWord1[FindFirstLetterA] = '.'
         ChosenWord1A = ''.join(ChosenWord1)
         WinCheck()
         
    else :
        LetterColour1 = 'orange'
        ChosenWord1 = list(ChosenWord)
        ChosenWord1[FindFirstLetterA] = '.'
        ChosenWord1A = ''.join(ChosenWord1)
        
    #Second Letter
    FindSecondLetterA = ChosenWord1A.find(PGLetter2)
    FindSecondLetterB = ChosenWord1A.find(CWLetter2)
    if FindSecondLetterA == -1  :
        LetterColour2 = 'black'
        ChosenWord2 = list(ChosenWord1A)
        ChosenWord2[FindSecondLetterA] = '.'
        ChosenWord2A = ''.join(ChosenWord2)
    elif FindSecondLetterA == FindSecondLetterB :
         LetterColour2 = 'green'
         ChosenWord2 = list(ChosenWord1A)
         ChosenWord2[FindSecondLetterA] = '.'
         ChosenWord2A = ''.join(ChosenWord2)
         WinCheck()
    else :
        LetterColour2 = 'orange'
        ChosenWord2 = list(ChosenWord1A)
        ChosenWord2[FindSecondLetterA] = '.'
        ChosenWord2A = ''.join(ChosenWord2)
    #Third Letter
    FindThirdLetterA = ChosenWord2A.find(PGLetter3)
    FindThirdLetterB = ChosenWord2A.find(CWLetter3)
    if FindThirdLetterA == -1  :
        LetterColour3 = 'black'
        ChosenWord3 = list(ChosenWord2A)
        ChosenWord3[FindThirdLetterA] = '.'
        ChosenWord3A = ''.join(ChosenWord3)
    elif FindThirdLetterA == FindThirdLetterB :
         LetterColour3 = 'green'
         ChosenWord3 = list(ChosenWord2A)
         ChosenWord3[FindThirdLetterA] = '.'
         ChosenWord3A = ''.join(ChosenWord3)
         WinCheck()
    else :
        LetterColour3 = 'orange'
        ChosenWord3 = list(ChosenWord2A)
        ChosenWord3[FindThirdLetterA] = '.'
        ChosenWord3A = ''.join(ChosenWord3)
    #Fourth Letter
    FindFourthLetterA = ChosenWord3A.find(PGLetter4)
    FindFourthLetterB = ChosenWord3A.find(CWLetter4)
    if FindFourthLetterA == -1  :
        LetterColour4 = 'black'
        ChosenWord4 = list(ChosenWord3A)
        ChosenWord4[FindFourthLetterA] = '.'
        ChosenWord4A = ''.join(ChosenWord4)
    elif FindFourthLetterA == FindFourthLetterB :
         LetterColour4 = 'green'
         ChosenWord4 = list(ChosenWord3A)
         ChosenWord4[FindFourthLetterA] = '.'
         ChosenWord4A = ''.join(ChosenWord4)
         WinCheck()
    else :
        LetterColour4 = 'orange'
        ChosenWord4 = list(ChosenWord3A)
        ChosenWord4[FindFourthLetterA] = '.'
        ChosenWord4A = ''.join(ChosenWord4)
    #Fifth Letter
    FindFifthLetterA = ChosenWord4A.find(PGLetter5)
    FindFifthLetterB = ChosenWord4A.find(CWLetter5)
    if FindFifthLetterA == -1 :
        LetterColour5 = 'black'
    elif FindFifthLetterA == FindFifthLetterB :
        LetterColour5 = 'green'    
        WinCheck()
    else :
        LetterColour5 = 'orange'
    
#Check for wether the player has won
def WinCheck() :
    global LetterColour1
    global LetterColour2
    global LetterColour3
    global LetterColour4
    global LetterColour5
    global GuessCount
    global Victory
    if LetterColour1 == 'green' and LetterColour2 == 'green' and LetterColour3 == 'green' and LetterColour4 == 'green' and LetterColour5 == 'green' :
        Victory.grid(row = 13, column = 3)
    
#Import the list of words to Python.
WordBase = list()
for word in Fopen :
    word1 = word.upper()
    wordA = word1.split()
    WordBase = WordBase + wordA
GuessCount = 6

#Some setup (The programn doesn't work without it.)
PlayerGuess = '?????'
ChosenNumber = random.randint(0,2481)
ChosenWord = str(WordBase[ChosenNumber])
LetterColour1 = 'black'
LetterColour2 = 'black'
LetterColour3 = 'black'
LetterColour4 = 'black'
LetterColour5 = 'black'
ComparePC()

#Import 5x5 Grid
#Import First Row
def changeFIRSTrow () :
    global TextONEone
    global TextONEtwo
    global TextONEthree
    global TextONEfour 
    global TextONEfive
    TextONEone = '' + PGLetter1
    LetterONEone = Button(root, text = TextONEone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 7, column = 1)
    TextONEtwo = '' + PGLetter2
    LetterONEtwo = Button(root, text = TextONEtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 7, column = 2)
    TextONEthree = '' + PGLetter3
    LetterONEthree = Button(root, text = TextONEthree, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour3).grid(row = 7, column = 3)
    TextONEfour = '' + PGLetter4
    LetterONEfour = Button(root, text = TextONEfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 7, column = 4)
    TextONEfive = '' + PGLetter5
    LetterONEfive = Button(root, text = TextONEfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 7, column = 5)
#Import Second Row
def changeSECONDrow () :
    global TextTWOone
    global TextTWOtwo
    global TextTWOthree
    global TextTWOfour 
    global TextTWOfive
    TextTWOone = '' + PGLetter1
    LetterTWOone = Button(root, text = TextTWOone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 8, column = 1)
    TextTWOtwo = '' + PGLetter2
    LetterTWOone = Button(root, text = TextTWOtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 8, column = 2)
    TextTWOthree = '' + PGLetter3
    LetterTWOthree = Button(root, text = TextTWOthree, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour3).grid(row = 8, column = 3)
    TextTWOfour = '' + PGLetter4
    LetterTWOfour = Button(root, text = TextTWOfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 8, column = 4)
    TextTWOfive = '' + PGLetter5
    LetterTWOfive = Button(root, text = TextTWOfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 8, column = 5)
#Import Third Row
def changeTHIRDrow () :
    global TextTHREEone
    global TextTHREEtwo
    global TextTHREEthree
    global TextTHREEfour 
    global TextTHREEfive
    TextTHREEone = '' + PGLetter1
    LetterTHREEone = Button(root, text = TextTHREEone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 9, column = 1)
    TextTHREEtwo = '' + PGLetter2
    LetterTHREEone = Button(root, text = TextTHREEtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 9, column = 2)
    TextTHREEthree = '' + PGLetter3
    LetterTHREEthree = Button(root, text = TextTHREEthree, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour3).grid(row = 9, column = 3)
    TextTHREEfour = '' + PGLetter4
    LetterTHREEfour = Button(root, text = TextTHREEfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 9, column = 4)
    TextTHREEfive = '' + PGLetter5
    LetterTHREEfive = Button(root, text = TextTHREEfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 9, column = 5)
#Import Fourth Row
def changeFOURTHrow () :
    global TextFOURone
    global TextFOURtwo
    global TextFOURthree
    global TextFOURfour 
    global TextFOURfive
    TextFOURone = '' + PGLetter1
    LetterFOURone = Button(root, text = TextFOURone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 10, column = 1)
    TextFOURtwo = '' + PGLetter2
    LetterFOURone = Button(root, text = TextFOURtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 10, column = 2)
    TextFOURthree = '' + PGLetter3
    LetterFOURthree = Button(root, text = TextFOURthree, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour3).grid(row = 10, column = 3)
    TextFOURfour = '' + PGLetter4
    LetterFOURfour = Button(root, text = TextFOURfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 10, column = 4)
    TextFOURfive = '' + PGLetter5
    LetterFOURfive = Button(root, text = TextFOURfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 10, column = 5)
#Import Fifth Row
def changeFIFTHrow () :
    global TextFIVEone
    global TextFIVEtwo
    global TextFIVEthree
    global TextFIVEfour 
    global TextFIVEfive
    TextFIVEone = '' + PGLetter1
    LetterFIVEone = Button(root, text = TextFIVEone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 11, column = 1)
    TextFIVEtwo = '' + PGLetter2
    LetterFIVEone = Button(root, text = TextFIVEtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 11, column = 2)
    TextFIVEthree = '' + PGLetter3
    LetterFIVEthree = Button(root, text = TextFIVEthree, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour3).grid(row = 11, column = 3)
    TextFIVEfour = '' + PGLetter4
    LetterFIVEfour = Button(root, text = TextFIVEfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 11, column = 4)
    TextFIVEfive = '' + PGLetter5
    LetterFIVEfive = Button(root, text = TextFIVEfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 11, column = 5)
#Import Sixth  Row
def changeSIXTHrow () :
    global TextSIXone
    global TextSIXtwo
    global TextSIXthree
    global TextSIXfour 
    global TextSIXfive
    TextSIXone = '' + PGLetter1
    LetterSIXone = Button(root, text = TextSIXone, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour1).grid(row = 12, column = 1)
    TextSIXtwo = '' + PGLetter2
    LetterSIXone = Button(root, text = TextSIXtwo, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour2).grid(row = 12, column = 2)
    TextSIXthree = '' + PGLetter3
    LetterSIXthree = Button(root, text = TextSIXthree, borderwidth = 5, height = 6, width = 16, fg = 'white',  bg = LetterColour3).grid(row = 12, column = 3)
    TextSIXfour = '' + PGLetter4
    LetterSIXfour = Button(root, text = TextSIXfour, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour4).grid(row = 12, column = 4)
    TextSIXfive = '' + PGLetter5
    LetterSIXfive = Button(root, text = TextSIXfive, borderwidth = 5, height = 6, width = 16, fg = 'white', bg = LetterColour5).grid(row = 12, column = 5)

#Resetting the game function
def BackgroundSetup():
    global GuessCount
    global ChosenWord
    global PGLetter1
    global PGLetter2
    global PGLetter3
    global PGLetter4
    global PGLetter5
    global CWLetter1
    global CWLetter2
    global CWLetter3
    global CWLetter4
    global CWLetter5
    global LetterColour1
    global LetterColour2 
    global LetterColour3 
    global LetterColour4 
    global LetterColour5
    global Victory
    #Choosing a random word. 
    ChosenNumber = random.randint(0,2497)
    ChosenWord = WordBase[ChosenNumber] 
    #Reset grid Colours
    LetterColour1 = 'black'
    LetterColour2 = 'black'
    LetterColour3 = 'black'
    LetterColour4 = 'black'
    LetterColour5 = 'black'
    
    #Reset Guesses
    GuessCount = 6
    Invalid_Guess.grid_remove()
    Victory.grid_remove()
    PGLetter1 = ''
    PGLetter2 = ''
    PGLetter3 = ''
    PGLetter4 = ''
    PGLetter5 = ''
    CWLetter1 = ''
    CWLetter2 = ''
    CWLetter3 = ''
    CWLetter4 = ''
    CWLetter5 = ''
    changeFIRSTrow()
    changeSECONDrow()
    changeTHIRDrow()
    changeFOURTHrow()
    changeFIFTHrow()
    changeSIXTHrow()

#Guesses
def PlayWordal() :
    global GuessCount
    global PlayerGuess
    global PGLetter1
    global PGLetter2
    global PGLetter3
    global PGLetter4
    global PGLetter5
    global CWLetter1
    global CWLetter2
    global CWLetter3
    global CWLetter4
    global CWLetter5
    global TextONEone
    global TextONEtwo
    global TextONEthree
    global TextONEfour
    global TextONEfive
    global LetterColour1
    global LetterColour2 
    global LetterColour3 
    global LetterColour4 
    global LetterColour5
    GuessCount = GuessCount-1
    PlayerGuess = GuessSpace.get().upper() 
    if len(PlayerGuess) != 5 :
        Invalid_Guess.grid(row = 3, column = 4)
        GuessCount = GuessCount + 1
    else :
        ComparePC()
        if GuessCount == 5 :
            DetermineColour()
            changeFIRSTrow()
            print(ChosenWord)
        elif GuessCount == 4 :
            DetermineColour()
            changeSECONDrow()
            print(ChosenWord)
        elif GuessCount == 3 :
            DetermineColour()
            changeTHIRDrow()
            print(ChosenWord)
        elif GuessCount == 2 :
            DetermineColour()
            changeFOURTHrow()
            print(ChosenWord)
        elif GuessCount == 1 :
            DetermineColour()
            changeFIFTHrow()
        elif GuessCount == 0 :
            DetermineColour()
            changeSIXTHrow()
            
#Importing GUI
root.title("Wordal")
Invalid_Guess = Label(root, text = "Enter a 5 Letter Word.", fg = 'red')
Invalid_Guess.grid(row = 3, column = 4)
Victory = Label(root, text = 'Victory!')
BackgroundSetup()
greeting = Label(text = "Welcome to Wordal.")
greeting.grid(row = 1, column = 1)
ButtonGuess = Button(root, text = 'Reset', borderwidth = 3, height = 2, width = 10, command = BackgroundSetup)
ButtonGuess.grid(row = 1, column = 3)
CreditDue = Label(root, text = "Made by Sam Flax")
CreditDue.grid(row = 1, column = 5)

#Guess Box
GuessPrompt = Label(root, text = "Enter a Guess:").grid(row = 3, column = 1)
GuessSpace = Entry(root, width = 20, borderwidth = 5)
GuessSpace.grid(row = 3, column = 2)
GuessInitiate = Button(root, text = 'Confirm Guess', borderwidth = 3, fg = 'blue', command = PlayWordal)
GuessInitiate.grid(row = 3, column = 3,)

root.mainloop()
