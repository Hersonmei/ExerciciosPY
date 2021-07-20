"""Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, game"""

import random

def pegarPalpite():
    while True:
        resposta = input('> ')
        
        if resposta.isdecimal():
            return int(resposta)
        print('Você devee colocar um valor de 0 a 100.')

# Fazer uma função que vai pegar o número do jogador, revifircar se é decimal e retornar esse número.
# Essa função vai ter que ficar perguntando caso o jogador não tenha colocado um valor válido.

secretNumber = random.randint(1, 100)
print()
print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
print('Eu estou pensando em um número entre 0 e 100.')
# Apresentar o jogo...
# Print('Es tou pensando em um ...)

for i in range(10):
    
    print('Você tem {} chances sobrando. Dê seu palpite!'.format(10 - i))

    palpite = pegarPalpite()

    if palpite == secretNumber:
        break
    
    if palpite < secretNumber:
        print('Seu palpite é muito baixo, tente novamente!')
    if palpite > secretNumber:
        print('Seu palpite é muito alto, tente novamente!')



if palpite == secretNumber:
    print()
    print('Parabéns! Você acertou o número!')
else:
    print()
    print('Infelizmente você errou, o número correto era', secretNumber ,'.')