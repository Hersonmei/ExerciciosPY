"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic"""

import math, shutil, sys, time

WIDTH, HEIGTH = shutil.get_terminal_size()

WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit!')
print()
print('Qual a menssagem você que mostrar? (Max', WIDTH //2, 'chars.)')
while True:
    message = 'Herson e Eleonora em 2021!'
    if 1 <= len(message) <= (WIDTH //2):
        break
    print('Menssage must be 1 to', WIDTH //2, 'characters long.')

step = 0.0
multiplier = (WIDTH - len(message)) / 2

try:
    while True:
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25 #(!) Try changing this to 0.1 or 0.5.
except KeyboardInterrupt:
    sys.exit()