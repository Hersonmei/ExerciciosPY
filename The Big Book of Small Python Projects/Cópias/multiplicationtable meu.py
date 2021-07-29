"""Multiplication Table, by Al Sweigart al@inventwithpython.com
Print a multiplication table.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math"""

print('Multiplication Table, by Al Al Sweigart al@inventwithpython.com')

# Print the horizontal number labels:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')


for number1 in range(0, 13):
    print(str(number1).rjust(2), end='')

    print('|', end='')

    for number2 in range(0, 13):
        print(str(number1 * number2).rjust(3), end=' ')
    
    print()