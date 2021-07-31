"""Numeral System Counters, by Al Sweigart al@inventwithpython.com
Shows equivalent numbers in decimal, hexadecimal, and binary.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, math"""

print('''Numeral System Counters, by Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
''')

while True:
    response = input('Enter the starting number (e.g. 0) > 0: ')
    if response == '':
        response = 0
        break
    if response.isdecimal():
        break
    print('Entre um número igual ou maior que zero!')
começo = int(response)

while True:
    response = input('Enter how many numbers to display (e.g. 1000) > 20: ')
    if response == '':
        response = 0
        break
    if response.isdecimal():
        break
    print('Coloque um valor váliso seu lezado! =D')
tamanho = int(response)

for numero in range(começo, começo + tamanho):
    binario = bin(numero)[2:]
    hexa = hex(numero)[2:].upper()
    print('DEC: {} HEX: {} BIN: {}'.format(numero, hexa, binario))