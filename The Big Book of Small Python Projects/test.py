import math, time, random

guess = input('>  ')

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
secretLetter = (random.choice(ALFABETO))
numeroGuess = ''
numeroSecret = ''

for i, x in enumerate(ALFABETO):
        if guess == x:
            numeroGuess += str(i)
        
        if secretLetter == x:
            numeroSecret += str(i)

if (int(numeroSecret) - int(numeroGuess)) >= 5:
    print('Frio')
else:
    print('Quente!')






print(secretLetter)
print(numeroGuess)
print(numeroSecret)
