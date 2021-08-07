"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic"""

import time, shutil, sys, math

WIDTH, WEIGTH = shutil.get_terminal_size()

WIDTH -= 1
print("""Sine Message, by Al Sweigart al@inventwithpython.com
(Press Ctrl-C to quit.)""")
print()
print('Qual menssagem você quer mostrar? Precisa ser menor que', WIDTH //2, 'caracteres.')

while True:
    menssagem = 'Herson e Elo'     #input('Qual menssagem você quer mostrar? Precisa ser menor que', WIDTH //2, 'caracteres.')
    if 1 < len(menssagem) < WIDTH //2:
        break
    print('Sua menssagem deve ter de 1 a ', WIDTH//2, 'caracteres.')

tep = 0.0
multiple = (WIDTH - len(menssagem)) // 2


while True:
    dado = math.sin(tep)
    padding = ' ' * int((dado + 1) * multiple)
    print(padding + menssagem)
    tep += 0.25
    time.sleep(0.1)

