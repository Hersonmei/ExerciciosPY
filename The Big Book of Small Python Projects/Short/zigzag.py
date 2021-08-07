import sys
import time

print('Zigzagm By Herson.')
print('Ctrl-C to quit.')
time.sleep(3)

indent_size = 0 #How many spaces to indent.
ran = 1
try:
    while True: # The main program loop.
        #Zig to the right 20 times.
        for i in range(ran):
            indent_size = indent_size + 1
            
            print(' ' * indent_size + '*******')
            time.sleep(0.05) # Pause for 50 milliseconds.

         #Zag to the left 20 times:
        for i in range(ran):
            indent_size = indent_size - 1  #Esse indent_size vai começar do 10 e ir diminuindo, pq vai estar se referindo ao indent_size que foi definido antes do while, por isso vai estar no escopo global podendo ser usado.
            print(' ' * indent_size + '*******')
            time.sleep(0.05) #pause for 50 milliseconds
        ran = ran + 10
except KeyboardInterrupt:
    sys.exit() #When ctrl-C is pressed, end the program.
