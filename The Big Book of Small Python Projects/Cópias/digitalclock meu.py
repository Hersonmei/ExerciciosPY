import sys, time
import sevseg

try:
    while True:

        print('\n' * 60)

        # Pegar o timelocal e atribuir a uma variável.
        tempoAtual = time.localtime()

        # Pegar a hora, minutos e segundos locais e atribuir a cada variável.
        hora = tempoAtual.tm_hour
        minuto = tempoAtual.tm_min
        segundo = tempoAtual.tm_sec

        # fazer aquela separção toda, chamando a função do sevseg, usar o splitline para atribuir a cada uma variável.
        hDigitos = sevseg.getSevSegStr(hora, 2)
        hTopLinha, hMediaLinha, hBaixoLinha = hDigitos.splitlines()

        mDigitos = sevseg.getSevSegStr(minuto, 2)
        mTopLinha, mMediaLinha, mBaixoLinha = mDigitos.splitlines()

        sDigitos = sevseg.getSevSegStr(segundo, 2)
        sTopLinha, sMediaLinha, sBaixoLinha = sDigitos.splitlines()

        #Imprimir essas variáveis em três linhas.
        print(hTopLinha   + '    ' + mTopLinha   + '    ' + sTopLinha)
        print(hMediaLinha + ' *  ' + mMediaLinha + '  * ' + sMediaLinha)
        print(hBaixoLinha + ' *  ' + mBaixoLinha + '  * ' + sBaixoLinha)
        print()
        print('Press Ctrl-C para sair.')
        
        while True:
            time.sleep(0.001)
            if tempoAtual.tm_sec == time.localtime().tm_sec:
                break




#Inserir um while dentro dessse while, para que ele faça a comparação dos segundos, e só vai quebrar esse while, quando o segundo for diferente daquele segundo medido inicialmente.

except KeyboardInterrupt:
    sys.exit()