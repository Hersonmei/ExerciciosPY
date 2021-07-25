message = 'E|_| \/0|_| c0n$eg|_|1rr!!|i'

charMapChaves = []

def englishToLeetspeak(message):
    """Convert the English string in message and return leetspeak."""
    
    
    charMapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/'], '!': ['i', '|']}
    leetspeek = ''

    a = list(charMapping.keys()) # Lista com todas as chaves da charMapping. Posso usar índice para pegar a chave nessa lista.

    for char in message: # Check each character:
        # There is a 70% chance we change the character to leetspeak.
        for char2 in charMapping.items():
            if char.lower() in list(char2):
                letraCerta = char2[0]
                leetspeek = leetspeek + letraCerta



        #if char.lower() in charMapping and random.random() <= 0.70:
            #possibleLeetReplacements = charMapping[char.lower()]
            #leetReplacemente = random.choice(possibleLeetReplacements)
            #leetspeek == leetspeek + leetReplacemente
            else:
                # Don't translate this character:
                leetspeek = leetspeek + char
                break
    return leetspeek