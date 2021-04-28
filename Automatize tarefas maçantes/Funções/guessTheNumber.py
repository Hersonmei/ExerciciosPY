#Este é um jogo de adivinhar o número.
import random
secret_number = random.randint(1,20)
print('I am think of a number between 1 and 20.')

#Peça para o jogador advinhar 6 vezes.
for guesses_taken in range (1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break #Essa condição corresponde ao palpite correto.

if guess == secret_number:
    print('Good Job! You guesses my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number i was thinkinf of was ' + str(secret_number))

