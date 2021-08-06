import random
try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''sPoNgEcAsE, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm
eNtEr YoUr MeSsAgE:''')
    messageFinal = fazerMudanca(input('> '))
    print()
    print(messageFinal)

    try:
        pyperclip.copy(messageFinal)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass

def fazerMudanca(menssagem):
    messageFinal = ''
    isUpper = False
    
    for caracter in menssagem:
        if not caracter.isalpha():
            messageFinal += caracter
        
        if isUpper:
            messageFinal += caracter.upper()
        else:
            messageFinal += caracter.lower()

        if random.random() < 0.9:
            isUpper = not isUpper


    return messageFinal


if __name__ == '__main__':
    main()