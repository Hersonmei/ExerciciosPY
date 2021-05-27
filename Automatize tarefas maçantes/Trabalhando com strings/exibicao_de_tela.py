tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]



for i in range(len(tableData[0][:])):
    for x in tableData:
        print(x[i].rjust(8), end = ' ')
    print()