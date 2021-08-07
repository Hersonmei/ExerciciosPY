"""Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

while True:
    print(' Você quer saber como deixar um besta respondendo por horas? Y/N')

    resposta = input('> ')

    if resposta.lower == 'yes' or resposta.lower() == 'y':
        continue
    if resposta.lower() == 'no' or resposta.lower() == 'n':
        break
    print('"{}" Não é uma resposta válida!'.format(resposta))

print('Tenha um bom dia!')
