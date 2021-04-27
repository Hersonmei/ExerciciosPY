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
