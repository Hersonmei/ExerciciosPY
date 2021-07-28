"""Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
A simulation of one million dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math, simulation"""

import random, time

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
Enter how many six-sided dice you want to roll:''')
numberOfCoin = 1

# Set up a dictionary to store the results of each dice roll:
results = {1: 0, 2:0}



# Simulate dice rolls:
print('Simulating 1,000,000 rolls of {} coin...'.format(numberOfCoin))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i /10000, 1)))
        lastPrintTime = time.time()

    
    if random.randint(1, 2) == 1:
        results[1] += 1
    else:
        results[2] += 1
    

# Display Results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfCoin, (numberOfCoin * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rolls - {}%'. format(i, roll, percentage))