import random
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = random.choice(list(the_board.keys()))   #Aqui era o input do usuário, ele colocaria a posicação que queria colocar a jogada (ex. mid-M), no entanto coloquei o random para poder obser como funciona todo o processo, já que não funcina com input.
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(the_board)



