def imc(peso, altura):
    return peso / (altura * altura)
        
    if a < 18.5:
        print('Abaixo do peso')
    if 18.5 < a < 24.9:
        print('Peso normal')
    if 25 < a < 29.9:
        print('Sobrepeso')
    if 30 < a < 34.9:
        print('Obesidade I')
    if 35 < a < 39.9:
        print('Obesidade II')
    if a > 40:
        print('Obesidade III')

a = imc(80, 1.80)
print(a)
