"""Prime Numbers, by Al Sweigart al@inventwithpython.com
Calculates prime numbers, which are numbers that are only evenly
divisible by one and themselves. They are used in a variety of practical
applications.
More info at: https://en.wikipedia.org/wiki/Prime_number
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, math, scrolling"""

import math, sys

def main():
    print('Prime Numbers, by Al Sweigart al@inventwithpython.com')
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('applications, but cannot be predicted. They must be')
    print('calculated one at a time.')
    print()
    

    #Primeiro criar um While para perguntar e receber o input, feito isso, verificar se é decimal..
    #Se for, pegar e transformar em interiro e atribuir para variável num. Faz o break.
    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
        resposta = '0'
        if resposta.isdecimal():
            num = int(resposta)
            break
    
    #Sigo para o segundo while dentro do main(), devo pegar e chamar outra função com o valor do while anterior.
    while True:
        if isPrimo(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1
    # Dependendo do retorno, se for True, vou ativar o print do número, com espaço/vírgua e o flush.
    #Abaixo disso, aumento o número em +1:

def isPrimo(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True
    #A segunção função vai avaliar se é primo. Vai ser uma sequência. Se for menor que 2, já retorna false, se for igual a 2 retorna true:
    # Seguida de outra condição. Vou realizar um for i in range(2, int(math.sqrt(num) + 1)):
    #Verifico se esse numero divido por i, vai restar zero, se for, vai retornar false!

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()