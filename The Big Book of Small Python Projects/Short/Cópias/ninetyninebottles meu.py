"""Ninety-Nine Bottles of Milk on the Wall
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, scrolling"""

import sys, time

print('Ninety-Nine Bottles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

PAUSE = 0
bottles = 99

try:
    while bottles > 1:
        time.sleep(PAUSE)
        print('{} bottles of milk on the wall,'.format(bottles))
        time.sleep(PAUSE)
        print('{} bottles of milk,'.format(bottles))
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1
        print('{} bottles of milk on the wall,'.format(bottles))
        print()

    print('1 bottles of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottles of milk,')
    time.sleep(PAUSE)
    print('Take one down, pass it around,')
    time.sleep(PAUSE)
    print('0 bottles of milk on the wall,')


except KeyboardInterrupt:
    sys.exit()


'''
99 bottles of milk on the wall,
99 bottles of milk,
Take one down, pass it around,
98 bottles of milk on the wall!
98 bottles of milk on the wall,
98 bottles of milk,
Take one down, pass it around,
97 bottles of milk on the wall!'''