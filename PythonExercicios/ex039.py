'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import datetime

ano_nascimento = int(input('Informe seu ano de nascimento. Ex: 1997. '))
idade = datetime.now().year - ano_nascimento

if idade < 18:
    print('Você ainda não está na idade de se alistar. Faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Você está na idade de alistamento.')
else:
    print('Você já passou da idade de se alistar. Deveria ter feito o alistamento a {} anos'.format(idade - 18))
