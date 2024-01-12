#Wilfred Robert-Fajimi
#November 20
#csci 180
#hangman.py


#import graphics library
from graphics import *

#import random module
import random

#open and read from text file
MyWords = open('mywords.txt', 'r').read().splitlines()

#set first display screen
Button = Circle(Point(0.7, 2.0), 0.4)
Button.setOutline('green')
Button.setWidth(0.1)
Button.setFill('white')

Message = Text(Point(0.7, 2.0), 'PLAY')
Message.setSize(18)
Message.setFill('green')

#define function to draw first display screen
def Hangman():
    global win
    win = GraphWin('Hangman', 400,400)
    win.setBackground('grey')
    win.setCoords(0.0, 0.0, 4.0, 4.0) 
    
    Title = Text(Point(2.0, 3.8), 'Play the HANGMAN game')
    Title.setSize(20)
    Title.setStyle('bold')
    Title.setFace('courier')
    Title.draw(win)
    Line(Point(1.5, 3.6), Point(2.5, 3.6)).draw(win)
    Line(Point(2.5, 3.6), Point(2.5, 3.0)).draw(win)    
    Button.draw(win)
    Message.draw(win)
    
#define function to display win message  
def WinHangman():
    Win = Text(Point(2.5, 0.4), 'YOU WIN!').draw(win)
    Win.setFill('green')
    Back = Text(Point(2.5, 0.1), 'Press \'BACK\' to go back')
    Back.setSize(14)
    Back.draw(win)
    Win.setSize(34)
    Message.setText('Back')
      
def Hangman0():
    Hangman()
    WinHangman()
    win.getMouse()
    win.close()    
    
def Hangman1():
    Hangman()
    win.getMouse()
    win.close()

#define function to draw hangman for end of game    
def Hangman2():
    Hangman()
    Head = Circle(Point(2.5,2.5), 0.5).draw(win)
    UpperBody = Line(Point(2.5, 2.0), Point(2.5, 1.5)).draw(win)
    LowerBody = Line(Point(2.5, 1.5), Point(2.5, 1.0)).draw(win)
    LeftHand = Line(Point(2.5, 1.5), Point(1.5, 1.7)).draw(win)
    RightHand = Line(Point(2.5, 1.5), Point(3.5, 1.7)).draw(win)
    LeftLeg = Line(Point(2.5, 1.0), Point(1.5, 0.5)).draw(win)
    RightLeg = Line(Point(2.5, 1.0), Point(3.5, 0.5)).draw(win)
    
    GameOver = Text(Point(2.5, 0.4), 'GAME OVER!').draw(win)
    GameOver.setFace('courier')
    GameOver.setStyle('bold')
    PressQuit = Text(Point(2.5, 0.1), 'Press \'QUIT\' to quit').draw(win)
    PressQuit.setFace('courier')
    
    Button.setOutline('red')
    Button.setWidth(0.1)
    Message.setText('QUIT')
    Message.setFill('red')
    win.getMouse()
    win.close()

#define function to play game    
def PlayHangman():

    #choose random word from text file and define useful lists
    Word = random.choice(MyWords)
    Word = Word.lower()
    Wordlist = list(Word)
    Dashlist = ['_' *len(Word)]
    Wrong = 0
    Tried = []
    Dashlist = ['_' *len(Word)]

    #loop for gameplay
    for i in range (0,7):
        Dashstring = ''.join(Dashlist)
        print('\nWord:', Dashstring , '  Guesses:', i, 'Wrong:', Wrong, 'Tried:', ','.join(Tried))
        if Dashlist == Wordlist:
            break
        Choice = input('Enter a letter: ')
        Choice = Choice.lower()
        
        if Choice in Word and '_' in Dashstring:                               
            Dashlist = list(Dashstring)
            Tried.append(Choice)
            Position = Wordlist.index(Choice)
            for Position, n in enumerate(Wordlist):
                if n.lower() == Choice.lower():                    
                    Dashlist[Position] = Choice
    
        elif Choice in Word and '_' not in Dashstring:
            break     
        elif Choice not in Word and '_' in Dashstring:
            Tried.append(Choice)
            Wrong +=1
        elif Choice not in Word and '_' not in Dashstring:
            break

    if Choice not in Tried:
        Tried.append(Choice)
    else:
        pass
  
    print('\nWord:', ''.join(Dashlist), '  Guesses:', len(Tried), 'Wrong:', Wrong, 'Tried:', ','.join(Tried))        
    Correct = len(Tried) - Wrong
    if Correct == 1 :
        print('\nThe word was', Word, '\nYou won 1 of your guesses!')
    elif Correct > 1 :
        if '_' not in Dashstring or Correct == len(Word):
            
            #to display correct hangman for each case
            if Wrong == 1:
                Hangman()
                WinHangman()
                Head = Circle(Point(2.5,2.5), 0.5).draw(win)
                win.getMouse()
                win.close()
            elif Wrong == 2:
                Hangman()
                WinHangman()
                Head = Circle(Point(2.5,2.5), 0.5).draw(win)
                Upperbody = Line(Point(2.5, 2.0), Point(2.5, 1.5)).draw(win)
                win.getMouse()
                win.close()
            elif Wrong == 3:
                Hangman()
                WinHangman()
                Head = Circle(Point(2.5,2.5), 0.5).draw(win)
                Upperbody = Line(Point(2.5, 2.0), Point(2.5, 1.5)).draw(win)
                Lowerbody = Line(Point(2.5, 1.5), Point(2.5, 1.0)).draw(win)
                win.getMouse()
                win.close()
            elif Wrong == 4:
                Hangman()
                WinHangman()
                Head = Circle(Point(2.5,2.5), 0.5).draw(win)
                Upperbody = Line(Point(2.5, 2.0), Point(2.5, 1.5)).draw(win)
                Lowerbody = Line(Point(2.5, 1.5), Point(2.5, 1.0)).draw(win)
                Lefthand = Line(Point(2.5, 1.5), Point(1.5, 1.7)).draw(win)
                win.getMouse()
                win.close()
            elif Wrong == 0:
                Hangman0()
            else:
                pass
                
            print('\nBravo! You guessed all letters correctly in', len(Tried), 'guesses!')

        else:
            print('\nThe word was', Word, '\nYou got', Correct, ' of your guesses correctly!')
    elif Correct == 0:
        print('\nThe word was', Word, '\nSorry, you lost...')
    else:
        pass
        
   
    

        
#define main function    
def main():
    
    
    Hangman1()
    print('PLAY THE H A N G M A N GAME!')
    print('\nHello User! You will have 7 chances to guess correctly, as many letters from a random word as you can.\nLet\'s go!')
    PlayHangman()
    
    Answer = input('\nDo you want to play again?\nEnter y for Yes and n for No: ')
    Answer = Answer.lower()
    while Answer =='y':
        PlayHangman()
        
        Answer = input('\nDo you want to play again?\nEnter y for Yes and n for No: ')
    
    Hangman2()    
    
            



    
main()
