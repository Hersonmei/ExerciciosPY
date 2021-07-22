def main():
    for x in range(10):
        parteCima()
        parteBaixo()


def parteCima():
    for i in range(12):
        print(' ' * (1 - i), end='')
        print('/', end='')
        print(' ' * (3), end='')
        print('\\', end='')
        print(' ' * (5), end='')   
    print()
    for i in range(12):
        #print('#' * (1 - i), end='')
        print('/', end='')
        print(' ' * (5), end='')
        print('\\', end='')
        print('_' * (3), end='')
    print()

def parteBaixo():
    for i in range(12):
        print('\\', end='')
        print(' ' * (5), end='')
        print('/', end='')
        print(' ' * (3), end='')   
    print()
    for i in range(12):
        print(' ' * (1 - i), end='')
        print('\\', end='')
        print('_' * (3), end='')
        print('/', end='')
        print(' ' * (5), end='')
    print()


if __name__ == '__main__':
    main()
        
        



# /   \     /   \     /   \     /   \     /   \     /   \     /   \
#/     \___/     \___/     \___/     \___/     \___/     \___/     \
#\     /   \     /   \     /   \     /   \     /   \     /   \     /
# \___/     \___/     \___/     \___/     \___/     \___/     \___/
# /   \     /   \     /   \     /   \     /   \     /   \     /   \
#/     \___/     \___/     \___/     \___/     \___/     \___/     \