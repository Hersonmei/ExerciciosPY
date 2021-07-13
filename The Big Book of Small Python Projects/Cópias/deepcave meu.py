"""Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, scrolling, artistic"""

import random, sys, time

#Definir Constantes  do tempo e do WIDTh
WIDTH = 70
TIME_DESCIDA = 0.05
# Esperar 1 seg para começar, dentro do try e o excep CTRL-C.
try:
    time.sleep(1)
except KeyboardInterrupt:
    sys.exit()

#definir o gap e o left para começar.
tamEsquerdo = 20
tamGap = 10

while True:
    #colocar o cálculo do direito = WIDTH - gap - left
    tamDireito = WIDTH - tamEsquerdo - tamGap
    #print('#' * left + ' ' * gap + '#' * direito)
    print('#' * tamEsquerdo + ' ' * tamGap + '#' * tamDireito)

    #usar o time aqui dentro, para colocar a velocidade de impressão das linhas.
    time.sleep(TIME_DESCIDA)
    #Fazer o random.randit e atribuir para uma variável.
    n = random.randint(1, 6)
    #If == 1 and ....:
    if n == 1 and tamEsquerdo > 1:
        tamEsquerdo = tamEsquerdo + 1
    elif n == 2 and tamEsquerdo + tamGap < WIDTH - 1:
        tamEsquerdo = tamEsquerdo - 1
    #else: pass
    else:
        pass

