"""Collatz Sequence, by Al Sweigart al@inventwithpython.com
Generates numbers for the Collatz sequence, given a starting number.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, math"""

import sys, time

print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')
# Pedir e pegar o input do usuário.
print('Entre um número: (Maior que zero)')
numero = input('>  ')

# Se esse input não for número ou for diferente de zero, ativar o sys.exit()
if not numero.isdecimal() or numero == '0':
    sys.exit()

#Preciso que esse número em string, seja transformado em inteiro e passado para uma variável.
n = int(numero)
print(n, end=", ", flush=True) 
while n != 1:
    # Utilizando o condicional If, Else, preciso verificar se essa variável com o número, será odd ou even. E aplicar a fórmula para cada caso.
    #Dentro de cada condição anterior, vou mandar imprimir o resultado.
    if n % 2 == 0:
        n = n //2 
        print(n, end=", ", flush=True)
    else:
        n = n * 3 + 1
        print(n, end=", ", flush=True)
    time.sleep(0.1)

# Como pegar esses resultados e fazer com que apareça no começo da condição do while?
