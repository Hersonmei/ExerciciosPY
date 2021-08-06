"""Rainbow, by Al Sweigart al@inventwithpython.com
Shows a simple rainbow animation. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, bext, beginner, scrolling"""

import random
import sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0
indentIncreasing = True 

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('random')
        print('##', end='')
        bext.fg('random')
        print('##')

        if indentIncreasing:
            indent = indent + 1
            if indent == 60:
                indentIncreasing = False
        
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

        time.sleep(0.08)

except KeyboardInterrupt:
    sys.exit()