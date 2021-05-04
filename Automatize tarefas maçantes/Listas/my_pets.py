my_pets = ['Herson', 'Renan', 'Ivson']

while True:
    name = input('Digite o nome do pet: ')
    if name not in my_pets:
        print(f'Eu não tenho um pet chamado {name}.')
    else:
        print(f'{name} é meu pet.')
        break
        