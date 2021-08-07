import sys
import time

print('Esse é um jogo do Herson')
print('Digite Crtl+c para sair do jogo')
time.sleep(3)
indent_size = 0
ran = 1

try:
    while True:
        for i in range(ran):
            indent_size = indent_size + 1
            print(' ' * indent_size + '*********')
            time.sleep(0.05)
        for i in range(ran):
            indent_size = indent_size - 1
            print(' ' * indent_size + '*********')
            time.sleep(0.05)
        ran = ran + 5        
except KeyboardInterrupt:
    sys.exit()