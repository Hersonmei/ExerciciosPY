r"""Diamonds, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
View this code at https://nostarch.com/big-book-small-python-projects
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
Tags: tiny, beginner, artistic"""
import sys

def main():
    sys.stdout = open("test.txt", "w")
    for tamDia in range(0, 6):
        diamanteOco(tamDia)
        print()
        diamanteCheio(tamDia)
        print()
        triangulo(tamDia)
        print()
    sys.stdout.close()

def diamanteOco(tamanho):
    # Fazer um for com 4 prints para parte de cima.
    for i in range(tamanho):
        print(' ' * (tamanho - i- 1), end='')   # Espaços parte de cima
        print('/', end='')   # Primeiro traço /
        print(' ' * (i * 2), end='')   # Espaço meio
        print('\\')   # Traço \
    # Fazer um for com 4 prints para parte de baixo.
    for i in range(tamanho):
        print(' ' * (i * 1), end='')  # Espaços parte de cima
        print('\\', end='')   # Primeiro traço \
        print(' ' * ((tamanho - i - 1) * 2), end='')   # Espaço meio
        print('/')   # Traço 
        

def diamanteCheio(tamanho):
    # Fazer um for com 3 prints para parte de cima.
    for i in range(tamanho):
        print(' ' * (tamanho - i- 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1) )

    # Fazer um for com 3 prints para parte de baixo.
    for i in range(tamanho):
        print(' ' * (i * 1), end='')
        print('\\' * (tamanho - i), end='')
        print('/' * (tamanho - i))

def triangulo(tamanho):
    # Parte de cima do triângulo:
    for i in range(tamanho):
        print(' ' * (tamanho - i- 1), end='')   # Espaços parte de cima
        print('/', end='')   # Primeiro traço /
        print(' ' * (i * 2), end='')   # Espaço meio
        print('\\')   # Traço \
    # Base do triângulo:
    for i in range(tamanho):
        print('-' * 2 , end='')

if __name__ == '__main__':
    main() 