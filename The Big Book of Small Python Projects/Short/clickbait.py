"""Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
 A clickbait headline generator for your soulless content farm website.
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: large, beginner, humor, word"""

import random

 # Set up the constants.

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS =  ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
BAIRRO = ['Marambaia', 'Roger', 'Cuiá', 'Planeta dos Macacos', 'Beco da poeira']

def main():
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate')
        response = '4'
        if not response.isdecimal():
            print('Please enter a number')
        else:
            numberOfHeadlines = int(response)
            break # Exit the loop once a valid number is entered.
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(8, 8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()
        elif clickbaitType == 9:
            headline = aquieminhavez()
        elif clickbaitType == 10:
            headline = perigoso()
        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!') 

# Each of these functions returns a different type of headline:
def perigoso():
    place = random.choice(STATES)
    bairro = random.choice(BAIRRO)
    noun = random.choice(NOUNS)
    return 'Se você conhece alguém que nasceu em {} ou {}, você deve pegar o seu {} e tomar muito cuidado!'.format(place, bairro, noun)


def aquieminhavez():
    objectp = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    place = random.choice(PLACES)
    time = random.choice(WHEN)
    return '{} live in {} won\'t go post anything because {} exploded {}'.format(objectp, state, place, time)

def generateAreMillennialsKillingHeadline():
    noum = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noum)

def generateWhatYouDontKnowHeadline():
    noum = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill you {}'.format(noum, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoum = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies HAte {}! See How this {} {} Invented a Cheaper{}'.format(pronoum, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choices(PLACES)
    return 'You Won\'t Believe what this {} {} Found in {} {}'.format(state, noun, pronoun, place)

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return "What {} Don't Want you to Know About {}".format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = POSSESSIVE_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think robots would take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Wal Wrong.'.format(state, noun, pronoun1, pronoun2)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()


