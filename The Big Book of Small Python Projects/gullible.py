"""Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

print('Gullible, by Al Sweigart al@inventwithpython.com')

while True: # Main loop program.
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ') # Get the user response.
    if response.lower() == 'no' or response.lower() == 'n':
        break # If "no", break out of this loop.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue # If "yes", continue to the start of this loop.
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you! Have a nice day!')
