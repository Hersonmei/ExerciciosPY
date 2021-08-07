"""Leetspeak, by Al Sweigart al@inventwithpython.com
Translates English messages into l33t5p34]<.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip
except ImportError:
    pass

def main():
    print('''L3375P34]< (leetspeek)
    By Al Sweigart al@inventwithpython.com
    Enter your leet message:''')
    
    fraseNormal = input('> ')
    fraseAlterada = trocaLetras(fraseNormal)
    print(fraseAlterada)

    try:
        pyperclip.copy(fraseAlterada)
        print('Frase codificada foi copiada com sucesso!')
    except NameError:
        pass


def trocaLetras(frase):
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}

    fraseAlterada = ''
    for carac in frase:
        if carac.lower() in charMapping and random.random() < 0.70:
            listaCorrepondenteLetra = charMapping[carac.lower()]
            stringParaSubstituir = random.choice(listaCorrepondenteLetra)
            fraseAlterada = fraseAlterada + stringParaSubstituir
        else:
            fraseAlterada = fraseAlterada + carac

    return fraseAlterada
if __name__ == '__main__':
    main()