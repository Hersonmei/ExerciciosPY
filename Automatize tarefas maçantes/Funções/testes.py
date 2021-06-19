
secretWord = 'ant'
correctLetters = 'at'
blanks = '_' * len(secretWord)

for i in range(len(secretWord)): # Raplace blanks with correctly guessed Letters.
    if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

for letter in blanks: # Show the secret word with spaces in between each letter.
    print(letter, end=' ')
print()