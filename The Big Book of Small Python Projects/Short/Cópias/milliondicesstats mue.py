"""Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
A simulation of one million dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math, simulation"""
import random, time

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
Enter how many six-sided dice you want to roll:''')
numeroDados = int('3')  #Colocar um input aqui!!

#Criar um dicionário com a soma dos valores de acordo com as possibilidades de soma dos dados.
dicioSoma = {}
for i in range(numeroDados, (numeroDados * 6) + 1):
    dicioSoma[i] = 0

# Fazer a for com 1000000, com um if prmieiro, usando aquelas paradas do time.time() com 1 seg, e depois aquele que tem um total, para cada soma, acrescentar 1 no dicionário da soma correspondente.
print('Simulating 1,000,000 rolls of {} dice...'.format(numeroDados))
timeAtual = time.time()
for i in range(1000000):
    
    if time.time() > timeAtual + 1:
        print('{}% done.'.format(round(i / 10000, 1)))
        timeAtual = time.time()

    soma = 0
    for j in range(numeroDados):
        soma = soma + random.randint(1, 6)
    dicioSoma[soma] = dicioSoma[soma] + 1

# Por ultimo, tenho que a fazer a impressão, vou usar um for parececido com o inicial, e dentro atribuir o valor de cada linha e preencher a tabela.
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numeroDados, (numeroDados * 6) + 1):
    TOTAL = i
    ROLLS = dicioSoma[i]
    PERCENTAGE = round(ROLLS / 10000, 1)
    
    print('  {} - {} rolls - {}%'.format(TOTAL, ROLLS, PERCENTAGE))