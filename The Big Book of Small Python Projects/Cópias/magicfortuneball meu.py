"""Magic Fortune Ball, by Al Sweigart al@inventwithpython.com
Ask a yes/no question about your future. Inspired by the Magic 8 Ball.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

import time, random

def spaceTimePrint(texto, interval= 0.1):
    for letra in texto:
        if letra == 'I':
            print('i', end='', flush=True)
        else:
            print(letra, end='', flush= True)
        time.sleep(interval)
    print() # Esses prints são aqueles ao final de cada for, para fazer com que passe para linha seguinte e o end='' não fique 
    #colocando tudo lado a lado, só oq estiver dentro do for, acabando o for passa para linha abaixo.
    print()
spaceTimePrint('MAGiCFORTUNEBALL , BY AL SWEiGART', 0.1)
print()
spaceTimePrint('ASK ME YOUR YES/NO QUESTiON.', 0.1)
print()
input('> ')

replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]

spaceTimePrint(random.choice(replies), 0.1)
time.sleep(1)

spaceTimePrint('.' * random.randint(4, 12), 0.5)


answer= [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]

spaceTimePrint(random.choice(answer), 0.1)