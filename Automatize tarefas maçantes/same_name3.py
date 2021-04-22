def spam():
    global eggs
    eggs = 'spam' # essa é a variável global

def bacon():
    eggs = 'bacon' #essa é a variável local

def ham():
    print(eggs) #essa é a variável local

eggs = 42 #essa é a variável global

spam()
print(eggs)
