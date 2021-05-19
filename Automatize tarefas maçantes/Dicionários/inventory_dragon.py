inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
x = dragonLoot.count("gold coin")
y = dragonLoot.count("dagger")
z = dragonLoot.count("ruby")


def addToInventory(soma):
    soma['gold coin'] += x
    soma['dagger'] = y
    soma['ruby'] = z
 
        
addToInventory(inv)

def displayInventory(produto):
    n_total = 0
    for k, v in produto.items():
        print(str(v) + ' ' + str(k))
        n_total = n_total + v
    return n_total

print('Inventory: ')
print('Número total de itens será: ' + str(displayInventory(inv)))

