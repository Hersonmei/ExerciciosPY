import random, time
def introducao():
    print('''Bem vindo ao jogo dos dragões das carverna...
    Garanto que será um jogo assustador e que você deverá escolher umas das cavernas e 
    tocer para ter sorte e encontrar o tão procurado tesouro. Boa sorte!!''')
print()

def escolha_jogador():
    player_choose = []

    while player_choose != '1' and player_choose != '2':
        print('Qual caverna você escolhe? (1 ou 2)')
        player_choose = input()
        

def caverna():
    dragon_escolhido = random.randint(1,2)
    return dragon_escolhido

# Botar dentro de uma função, para poder colocar o time e o suspense...
def jogo():
        escolha = escolha_jogador()
        dragão = caverna()
        if escolha == dragão:
            print('Que alívio... Você entrou na caverna do Dragão Gentil e ele lhe entregou todo o tesouro! Parabéns!')
        else:
            print('Teeente correrrr!!! Você caiu na caverna do Dragão Faminto! Fuja!!')

continuar = []
while continuar != 's' and continuar != 'n':
    introducao()
    escolha_jogador()
    caverna()
    jogo()
    print('Você deseja continuar jogando? (s ou n)')
    continuar = input()
    if continuar == 's':
        print('Vamos novamente...')
        continue
    if continuar == 'n':
        break