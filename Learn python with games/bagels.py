import random

NUM_DIGTS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGTS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '. join(clues)

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. 
    if num == '':
        return False
    
    
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    
    return True


print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGTS))
print('The clues I give are...')
print('When I say:  That means:')
print('  Begels     None of this digits is correct.')
print('  Pico       One digit is correc but in the wrong position.')
print('  Fermi      One digit is correct and in the right position.')


while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it. ' % (MAX_GUESS))
    
    guessPrevius = []
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
            
        guess = ''
        while True: 
            print('Guess #%s' % (guessesTaken))
            print(guessPrevius)
            guess = input()
            
            if len(guess) != NUM_DIGTS:
                continue
            elif isOnlyDigits(guess) == False:
                continue
            elif guess not in guessPrevius:
                break 
            
        print(getClues(guess, secretNum))
        guessesTaken += 1
        guessPrevius.append(guess)

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
    