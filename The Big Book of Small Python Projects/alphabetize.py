import random, time, slow

# Set up the constants:
# (!) Try change these constants:

QUESTION_SIZE = 5 # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30 # The quis last 30 seconds.

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALFABET = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

def main():
    # Fancy animation for the title:
    slowPrint(ALPHABET, 0.02) # (!) Try changing 0.02 to 0.0 or 1.0.
    slowPrint('     Alphabetize Quiz', 0.02)
    slowPrint(REVERSE_ALFABET, 0.02)
    time.sleep(0.5)
