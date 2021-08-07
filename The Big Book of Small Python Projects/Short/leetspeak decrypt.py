# Essa foi o programa com as alterações que fiz para desencriptar as mensagens criadas pelo programa anterior.

import random

try:
    import pyperclip # pyperclip copies text to the clipboard
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com
Enter your leet message:''')
    english = input('> ')
    leetspeek = englishToLeetspeak(english)
    print(leetspeek)


    try:
        # Trying to use pyperclip will raise a NameError exception if it wasn't imported:
        pyperclip.copy(leetspeek)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass # Do nothing if pyperclip wasn't installed.


def englishToLeetspeak(message):
    """Convert the English string in message and return leetspeak."""
    # Make sure all the keys in 'charMapping' are lowercase.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    
    for chave, valores in charMapping.items():
        for x in valores:
            if x in message:
                message = message.replace(x, chave)
    
    return message

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
    