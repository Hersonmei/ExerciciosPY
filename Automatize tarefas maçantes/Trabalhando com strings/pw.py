#! python3
# pwpy - Um programa para repositório de senhas que não é seguro.

PASSOWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [acount] - copy account password')
    sys.exit

account = sys.argv[1]  # o primeiro argumento da linha de comando é o nome da conta, pq o [0] sempre é o nome do prog.

if account in PASSOWORDS:
    pyperclip.copy(PASSOWORDS[account])  # Isso aqui vai ser a chamada da chave no dicionário, que vai retornar o valor dessa chave chamada.
    print('Password for ' + account + ' copied to cipbord')
else:
    print('There is no account named ' + account)


