#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
#Greets the player
colors = ['red','orange','yellow','green','blue','violet','purple']
#these are the colors that could be chosen
play_again = ''
#play_again response will determine what comes next
best_count = sys.maxsize            # the biggest number
#The less tries the player took to achieve the correct answer

while (play_again != 'n' and play_again != 'no'):
    #If they wish to play again this will play on loop and if not then it will end the game.
    match_color = random.choice(colors)
    #the color is chosen at random from one of the colors listed on line 9
    count = 0
    #count starts at 0
    color = ''
    #color chosen from line 9
    while (color != match_color):
        #while they are playing this is what will play on repeat
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #while playing this is the question the player will be trying to answer
        color = color.lower().strip()
        #prevents capitalizations or lower cased letters or spaces to interfere with correct results
        count += 1
        #counts how many guesses the player had to do in order to get the correct answer
        if (color == match_color):
            #if they guess the correct color
            print('Correct!')
            #The game will tell them correct!
        else:
            #If anything but the correct color is guessed
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            #the game will tell them to try again and how many times they have already guessed
    
    print('\nYou guessed it in {} tries!'.format(count))
    #The game will tell them how many tries it took them to get the correct answer.

    if (count < best_count):
        #If it is the lowest number of guesses it took them to get the correct answer
        print('This was your best guess so far!')
        #tells the player this was their best guess
        best_count = count
        #best count refers to least number of guesses it took to get the correct answer

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
    #asks the player if they want to play again, without capitalization or lower cased letters or spaces before or after being an issue

print('Thanks for playing!')
#ends game if they say no to playing again.