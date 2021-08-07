"""Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, beginner, scrolling"""


import sys, random, time, shutil

# Definir viriáveis constantes, o tamanho máxima da linha, o tamanho mínimo da linha, o tempo de cada linha impressa, a densidade e o WIDTH de impressão e os intes impressos.
LINHA_MINIMA = 6
LINHA_MAXIMA = 14
DENSIDADE = 0.03
IMPRESSAO = ['0', '1', '5']

TEMPO_LINHA = 0.1

WIDTH = shutil.get_terminal_size()[0]
# pegar o width de impressão do terminal, depois a baixo pegar esse WIDTH e subtrair 1.

WIDTH -= 1

print('Jogo do Al S.')
print('Pressione Ctrl-C para sair!')
time.sleep(2)

try:
    colunas = [0] * WIDTH
    while True:
        # Colunas vai ser uma lista de zeros [0] * o width.
        
        #fazer um for em WIDTH e interar com o i.
        for i in range(WIDTH):
            if colunas[i] == 0:
                if random.random() < DENSIDADE:
                    colunas[i] = random.randint(LINHA_MINIMA, LINHA_MAXIMA)
                
            #If o coluna[i] > 0: vou imprimir um caractere deles e depois subtrair 1, para poder fazer o efeito de terminar aquela linha.
            if colunas[i] > 0:
                print(random.choice(IMPRESSAO), end='')
                colunas[i] -= 1
            else:
                print(' ', end='')
                
            #print(end='') #  Tenha que fazer um print vazio.
        print()
        time.sleep(TEMPO_LINHA)
        sys.stdout.flush()
        
        
except KeyboardInterrupt:
    sys.exit()
