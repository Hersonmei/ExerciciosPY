import sys, time
import sevseg

segundosContagem = 7200

try:
    while True:
        print('\n' * 60)

        
        # Pegar e montar os calculos do numero de horas, minutos e segundos do total de segundos colocados.
        horas = segundosContagem // 3600
        minutos = (segundosContagem % 3600) // 60
        segundos = (segundosContagem % 60)

        # Chamar a função do sevseg e colocar dois parametros, e atribuir esse resultado a uma variável.
        horDigitos = sevseg.getSevSegStr(horas, 2)
        minDigitos = sevseg.getSevSegStr(minutos , 2)
        segDigitos = sevseg.getSevSegStr(segundos , 2)

        # Essa variável vai retornar uma string com três tinhas, por isso vou pegar essa variável e utilizar splitlines(), e atribuir uma linha para cada nova variável.
        horTopLinha, horMeioLinha, horBaixoLinha = horDigitos.splitlines()
        minTopLinha, minMeioLinha, minBaixoLinha = minDigitos.splitlines()
        segToplinha, segMeioLinha, segBaixoLinha = segDigitos.splitlines()
        # Vou imprimir esses três variáveis deveridas das três variáveis divididas, cada uma em um print diferente(3 prints)
        print(horTopLinha   + '     ' + minTopLinha   + '     '  + segToplinha)
        print(horMeioLinha  + '  *  ' + minMeioLinha  + '  *  ' + segMeioLinha)
        print(horBaixoLinha + '  *  ' + minBaixoLinha + '  *  ' + segBaixoLinha)
        
        #Inserir uma condição IF, se xxx == 0, mostrar a mensagem e adicionar o BREAK para sair do while.
        if segundosContagem == 0:
            print()
            print(' **** BOOM ****')
            break
        #acrestar ainda mais: time.sleepe(1) e segundosContagem -= 1

        time.sleep(1)
        segundosContagem -= 1

except KeyboardInterrupt:
    sys.exit() #Sair quando apertar Crtl-C.