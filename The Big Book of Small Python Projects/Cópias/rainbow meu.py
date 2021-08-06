"""Rainbow, by Al Sweigart al@inventwithpython.com
Shows a simple rainbow animation. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, bext, beginner, scrolling"""

import random, time, sys

try:
    import bext
except ImportError:
    print('Vá baixar o bext!')
    sys.exit()

indentacao = 0
aumentarIdentacao = True

try:
    while True:
        print(' ' * indentacao, end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('random')
        print('##')

        if aumentarIdentacao:
            indentacao += 1
            if indentacao == 60:
                aumentarIdentacao = False
        
        else:
            indentacao -= 1
            if indentacao == 0:
                aumentarIdentacao = True

        time.sleep(0.08)
except KeyboardInterrupt:
    sys.exit()