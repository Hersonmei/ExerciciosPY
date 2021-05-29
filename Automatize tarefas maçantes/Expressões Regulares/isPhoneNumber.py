def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12] # Aqui vai ser de i até i+12, então na primeira iteração será [0,12], na segunda [1,13], terceira [2, 14]...
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')





#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))
#print('Moshi moshi is a phone number:')
#print(isPhoneNumber('323-112-aaaa'))