
def collatz(number):
    if (number % 2 == 0):
        return number // 2

    elif (number % 2 == 1):
        return 3 * number + 1

print('What number would you like to use?')

try:
    i = int(input())
    while i > 1:
        i = collatz(i)
        print(i)
except ValueError:
    print('Erro: Número inteiro deve ser fornecido')
#a importância desse print estar dentro do while, pois se ele ficar recuado, o print vai mostrar só uma vez, que será o primeiro número do while, mesmo o while funcionando normalmente, só irá mostrar o primeiro valor.
#No entanto, se colocar o print(i) dentro do while, o certo, o print(i) irá aparecer todas as vezes que o resultado passsar pelo while, mostrando o resultado correto então. Logo, este print(i) deve estar identado.



