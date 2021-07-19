import math, sys

while True:
    numero = input('Digite um número maior que 0 ou SAIR: \n')
    
    if numero.upper() == 'SAIR' or numero.upper().startswith('S'):
        sys.exit()

    if not numero.isdecimal() and numero > 0:
        continue

    numero = int(numero)

    fatores = []

    for i in range(1, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            fatores.append(i)
            fatores.append(numero // i)
    
    fatores = list(set(fatores))
    fatores.sort()

    

    for i, fator in enumerate(fatores):
        fatores[i] = str(fator)
    print(', '.join(fatores))
        
