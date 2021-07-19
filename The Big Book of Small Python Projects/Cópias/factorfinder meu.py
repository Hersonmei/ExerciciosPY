import math, sys

while True:
    resposta = input('Digite um número maior que 0 ou SAIR: \n')
    
    if resposta.upper() == 'SAIR' or resposta.upper().startswith('S'):
        sys.exit()

    if not resposta.isdecimal() and resposta > 0:
        continue

    numero = int(resposta)

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
        
