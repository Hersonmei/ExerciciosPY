listra = []
def mutate_string(string, position, character):
    
    listaFinal = []
    listra = list(string)
    listaFinal += character.listra[position]
    listaFinal = str(listaFinal)
    return 

if __name__ == '__main__':
    s = 'abracadabra'
    i, c = ('5', 'k')
    s_new = mutate_string(s, int(i), c)
    print(s_new)