from itertools import combinations
omega = combinations(range(1,11), 6)

evento = ''
i = 0

for x in omega:
    i += 1
    evento.append(x)
    
print("{:,}".format(i), 'resultados possíveis.')



#for j in evento:
    #print(j)
    