import random

numTentativas = 0

print('Qual o seu nome?')
name = input()

numeroMaquina = random.randint(1, 20)
print('Muito bem, ' + name + '. Você deve adinhar o número que eu escolhi de 1 a 20.')

for numTentativas in range(6):
    print('Qual o seu palpite?')
    tentativa = input()
    tentativa = int(tentativa)

    if tentativa < numeroMaquina:
        print('Seu palpite foi baixo.')

    if tentativa > numeroMaquina:
        print('Seu palpite foi alto.')
    
    if tentativa == numeroMaquina:
        break

if tentativa == numeroMaquina:
    print('Muito bem ' + name + '. Você acertou o meu número em ' + str(numTentativas+ 1) + ' tentativas.')

if tentativa != numeroMaquina:
    print('Infelizmente você não acertou!')