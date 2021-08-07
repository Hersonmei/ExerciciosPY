import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   ********* *       ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Entre um nome a sua escolha:')
nome = 'herson'
if nome == '':
    #se colocar um texto vazio no input, ativar o sys.exit().
    sys.exit()

for linha in bitmap.splitlines():
    #fazer um for para percorrer cada linha da string. #usar aquela .splitlines() para separar em cada linha em uma string dentro de uma lista.
    for i, ponto in enumerate(linha):
        #vai ter um for dentro do for anterior, para ao entrar nessa linha, eu tenho que percorrer cada item dessa linha, usando aquele enumerate com duas variáveis.
        if ponto == ' ':
            # se o item dentro da linha for vazio, printar  (' ', end='')??
            print(' ', end='')
        else:
            #else: print(input[i % len(input)])
            print(nome[i % len(nome)], end='')
    print('XX')


