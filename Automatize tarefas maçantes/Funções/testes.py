import random
words = {'Colors':'red orange yellow green blue indigo violet white blackbrown'.split(), 
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

wordKey = random.choice(list(words.keys()))

wordIndex = random.randint(0, len(words[wordKey]) - 1)  #Aui também será (-1), pq o len() vai mostrar 2, mas o random tem que ir só de zero a 1.


print([words[wordKey][wordIndex], wordKey])