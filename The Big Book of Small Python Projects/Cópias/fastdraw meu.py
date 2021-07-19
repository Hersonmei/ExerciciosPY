import random, time, sys

print('Fast Draw, by Al Sweigart al@inventwithpython.com')
print()
print('Time to test your reflexes and see if you are the fastest')
print('dram in the west!')
print('Whe you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')

while True:
    print()
    print('Vai aparecer...')
    #Primeiro um time.sleep com um random.randit de tempos, para ficar aleatório e escolha do tempo..
    time.sleep(random.randint(20, 50) / 10.0)
    #Apos isso, colocar o print do DRAW!
    print('DRAW!')
    #Tbm chamar, time.time(), não sei se antes ou depois, para pegar o tempo da impressão do DRAW.
    tempoDraw = time.time()
    #Depois disso vem o INPUT().
    input()
    # Depois vem uma variável que já pega o time.time() atual e subtrai do anterior que deve ser atribuído a uma variável.
    tempoTotal = time.time() - tempoDraw

    # Depois disso fazer os ifs, com <0.1, >0.3 e else.
    if tempoTotal < 0.1:
        print('Você perdeu pois apertou antes do Draw aparecer na tela!')
    elif tempoTotal > 0.3:
        print('Você está muito lento, pois apertou com {} segundos'.format(tempoTotal))
    else:
        print('Parabéns, você o gatilho mais rápido do sertão! Conseguiu em {} segundos'.format(tempoTotal))

    resposta = input('Presseione Enter para continuar ou Sair caso não deseje continuar.\n')

    if resposta.upper() == 'SAIR':
        sys.exit()

    # Por último perguntar se quer continuar.
