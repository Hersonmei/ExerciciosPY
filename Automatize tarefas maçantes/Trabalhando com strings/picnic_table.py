def print_picnic(itemsDict, leftWidth, rigthWidth):
    print('PICNIC ITEMS'.center(leftWidth + rigthWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rigthWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnicItems, 12, 5)
print_picnic(picnicItems, 20, 6)