#! python3
#lucky.py - Abre bários resultados de pesquisa no Google.

import requests, sys, webbrowser, bs4

print('Googling...') # exibe um texto enquanto faz download da página do Google
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Obtém os links dos principais resultados da pesquisa.

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# TODO: Abre uma aba do navegador para cada resultado

linkElems = soup.select('.LC20lb DKV0Md')
numOpem = min(5, len(linkElems))
for i in range(numOpem):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))