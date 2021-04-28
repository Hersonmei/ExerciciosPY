#Calculadora para IMC
#Primeiro solicitando o input das informações pelo usuário
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: ' ).replace(",", "."))

#Função de cálculo do IMC
def imc(peso, altura):
    return peso / (altura * altura)

#Atribuição dos valores do IMC a variável b
result = imc(peso, altura)

b = result

#Classificação de acordo com o resultado do IMC e impressão.
if b < 18.5:
    print('Abaixo do peso')
elif 18.5 < b < 24.9:
    print('Peso normal')
elif 25 < b < 29.9:
    print('Sobrepeso')
elif 30 < b < 34.9:
    print('Obesidade I')
elif 35 < b < 39.9:
    print('Obesidade II')
elif b > 40:
    print('Obesidade III')


#Função que recebe dois números do usuário e retorna o maior número. Se for igual, retornar mensagem informando.

num1 = input('Escolha o primeiro número: ')
num2 = input('Escolha o segundo número: ')

def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
    if num1 == num2:
        print('Por favor, informar números diferentes.')

resultado = maior_numero(num1, num2)
print(resultado)

#Função que recebe dois números do usuário e retorna o menor número. Se for igual, retornar mensagem informando.

num1 = input('Escolha o primeiro número: ')
num2 = input('Escolha o segundo número: ')

def maior_numero(num1, num2):
    if num1 > num2:
        return num2
    if num2 > num1:
        return num1
    if num1 == num2:
        print('Por favor, informar números diferentes.')

resultado = maior_numero(num1, num2)
print(resultado)

# Esse código primeiro escolhe um número aleatório de 1 a 3, depois a outra função vai receber um número inserido pelo usuário e vai mostrar se o usuário advinhou ou não.
import random

def aleatorio():
    return random.randint(1,3)

number = aleatorio()


def palpite(palp):
    if number == palp:
        print('Parabéns! Você acertou o número.')
    elif number != palp:
        print('O número era ' + str(number) + ' você errou o palpite.')

number_palpite = int(input('Digite um número: '))
palp = number_palpite
palpite(palp)