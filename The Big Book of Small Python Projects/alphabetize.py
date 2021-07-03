import random, time

# Set up the constants:
# (!) Try change these constants:

QUESTION_SIZE = 5 # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30 # The quis last 30 seconds.

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALFABET = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

def main():
    # Fancy animation for the title:
    slowPrint(ALPHABET, 0.02) # (!) Try changing 0.02 to 0.0 or 1.0.
    slowPrint('     Alphabetize Quiz', 0.02)
    slowPrint(REVERSE_ALFABET, 0.02)
    time.sleep(0.5)

    print('''By Al Sweigart al@inventwithpython.com

Enter the alphabetical order of the letters shown as fast
as possible. Try to alphabetize as many as possible in {} seconds!

Example:
    P M O T Q <-- The letters.
    > mopqt    <-- Enter the correct alphabetical order.
    '''.format(QUIZ_DURATION))
    #input('Press Enter to begin...')|

    startTime = time.time()  # Get the current time for the start time. (Vai pegar o tempo atual, mas em formatação de um float extenso. Os segundos serão os últimos números antes do ponto 2424343*23*.93863)
    numCorrect = 0 # Number of questions answered correctly.
    while True: # Main loop game.
        # Come up with letters for the question:
        queizLetters = random.sample(ALPHABET, QUESTION_SIZE) #Aqui vai pegar o número 5 que foi definifo previamente em Question_Size, e depois vai pegar 5 itens randomicos do primeiro argumento, nesse caso o ALPHABET.
        print(' '.join(queizLetters))
        response = input('> ').upper()
        response = response.replace(' ', '') # Remove spaces (Aqui vai remover os espaçoes da resposta do jogador!)

        if response not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or len(response) != QUESTION_SIZE:
            continue

        # Check if the quiz's time is up:
        if time.time() - 5 > startTime: #Lá no primeiro time.time() o tempo vai ficar gravado em startTme, ai cada volta no while, ele vai avaliar, quando o time.time() -30 passar a ser maior que startTIme, é sinal que se passaram 30 segundos.
            print("TIME'S UP!")
            break
        
        # Check if the response is correct:
        if list(response) == sorted(queizLetters): # É igual ao sort(), que vai ordenar os valores. O método list.sort() é aplicável apenas às listas. Em contrapartida, a função sorted() aceita qualquer iterável.
            print('     Correct!')
            numCorrect += 1 # Increase the score by 1.
        else:
            print('     Sorry, wrong. :(\n')

    # After the loop exits, the quiz is over. Show the final score:
    print(' In {} seconds you'.format(QUIZ_DURATION))
    print('got {} correct!'.format(numCorrect))
    print('Thanks for playing!')
    jogarnovo()

def slowPrint(text, pauseAmount=0.1):
    """Slowly print out the characters in text one at a time"""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='') # end='' means no newline. (Esse fush=True, vai fazer com que cada elemento seja impresso no tempo definido. Evitando o erro de ele contar todo o tempo de uma vez e imprimir todos os itens de uma vez, sem respeitar o intervalo de tempo definido.)
        time.sleep(pauseAmount) # Pause in between each character.
    print() # Print a newline.

def jogarnovo():
    jogarnova = input('Do you wanna play novamente? (y ou n)\n')
    if jogarnova.lower() == 'y':
        main()
    else:
        print('Obrigado por jogar conosco!')
# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
    
