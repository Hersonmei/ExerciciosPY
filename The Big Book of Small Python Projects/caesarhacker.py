"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This program hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# Let the usser specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('>  ')

#Every possivle symbol that can be encrypted/decrypted:
#(this must match ths SUMBOLS used when encrypting the message.)
#abcdefghijklmnopqrstuvxz
#ABCDEFGHIJKLMNOPQRSTUWXYZ
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

for key in range(len(SYMBOLS)): #Loop trough every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol.
            num = num - key # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)
            
            #ADD decryoted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol
    
    # Dysplay the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))
    
