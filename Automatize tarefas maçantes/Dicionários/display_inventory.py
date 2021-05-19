coisas = {'corda': 3, 'coração': 5, 'armadura': 2, 'energia': 6, 'mamadeira': 14}


def displayInventory(produto):
    n_total = 0
    for k, v in produto.items():
        print(str(v) + ' ' + str(k))
        n_total = n_total + v
    return n_total

print('Inventory: ')
print('Número total de itens será: ' + str(displayInventory(coisas)))