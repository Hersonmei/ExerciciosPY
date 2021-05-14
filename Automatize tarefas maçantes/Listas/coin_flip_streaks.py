import random
from itertools import groupby

numberOfStreaks = []    
for experimentNumber in range(10000):
    # Code that creats a list of 100 'heads' or 'tails' values
    randomize = random.randint(0,1)
    if randomize == 0:
        numberOfStreaks.append('head')
    if randomize == 1:
        numberOfStreaks.append('tail')


count_dups = [sum(1 for _ in group) for _, group in groupby(numberOfStreaks)]
print(count_dups)

    # Code that cheks is there is a streak of 6 heads or tails in a row.
#print('Chance of streak: %s%%' % (numberOfStreaks / 100))