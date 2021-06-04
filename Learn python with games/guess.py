import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I  am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Seu palpite é muito baixo')
    if guess > number:
        print('Seu palpite é muito alto')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! Você acertou meu número em ' + guessesTaken + ' palpites!')

if guess != number:
    number = str(number)
    print('Não. O número que eu estava pensando era ' + number + '.')