day = 'first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth'.split()

number = '''Two turtle doves, Three French hens, Four calling birds, Five golden rings, Six geese a-laying, Seven swans a-swimming, Eight maids a-milking, Nine ladies dancing, Ten Eleven Twelve, Eleven pipers piping, Twelve drummers drumming'''.split(', ')


while True:
    frases = []
    for i in range(0, 12):
        print('On the {} day of Crhristmas,'.format(day[i]))
        print('my true love sent to me,')
        
        if i > 0:
            frases.insert(0, number[i - 1])
            print(', \n'.join(frases))
                
        print('And a partridge in a pear tree!')
        print()
    break




'''On the first day of Christmas,
my true love sent to me
A partridge in a pear tree.

On the second day of Christmas,
my true love sent to me
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas,
my true love sent to me
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the fourth day of Christmas,
my true love sent to me
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the fifth day of Christmas,
my true love sent to me
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the eleventh day of Christmas,
my true love sent to me
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

On the twelfth day of Christmas,
my true love sent to me
Twelve drummers drumming,
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five golden rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree!'''
