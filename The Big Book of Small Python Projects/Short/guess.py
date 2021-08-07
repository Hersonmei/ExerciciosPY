"""Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, game"""

import random

def askForGuess():
    while True:
        guess = input(secretLetter) # Enter the guess.

        if guess.isalpha():
            return guess.upper()  # Convert string guess to an integer.
        print('Please enter a number between A-Z.')
    


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
secretLetter = random.choice(ALFABETO) # Select a random number.

print('I am thinking of a letter between A-Z.')


for i in range(10): # Give the player 10 guesses.
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretLetter:
        break   # Break out of the for loop if the guess is correct.
    
    numeroGuess = ''
    numeroSecret = ''
    for i, x in enumerate(ALFABETO):
        if guess == x:
            numeroGuess += str(i)
        
        if secretLetter == x:
            numeroSecret += str(i)
        
    if (int(numeroSecret) - int(numeroGuess)) >= 3:
        print('Frio')
    else:
        print('Quente!')

# Reveal the results:
if guess == secretLetter:
    print('Yay! You guesses my LETTER!')
else:
    print('Game over. The number I was thinkinf of was', secretLetter)


