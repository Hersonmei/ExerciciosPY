#! python3
# phoneAndEmail.py - Encontra números de telefone e endereços de email no clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #código da área
    (\s|-|\.)?          #separador
    (\d{3})             #primeiros 3 dígitos
    (\s|-|\.)           #separador
    (\d{4})             #últimos 4 dígitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #Extensão
    )''', re.VERBOSE)

#Cria a regex para email.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%=-]+      #Nome do usuárip
    @           #Símbolo @
    [a-zA-Z0-9.-]+      #Nome do domínio
    (\.[a-zA-Z]{2,4})   #Ponto seguido de outros caracteres
    )''', re.VERBOSE)

#Encontra correspondências no texto do clipboard.


#Copia os resultados para o clipboard.

