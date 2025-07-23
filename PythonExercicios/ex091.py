#Usando Dicionários

'''Crie um programa onde 4 jogadores joguem um dado e o tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

import random
from time import sleep
from operator import itemgetter

jogadores = {}
for i in range(1, 5):
    jogadores[f'Jogador {i}'] = random.randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.5)

print('=== Ranking ===')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, (jogador, valor) in enumerate(ranking):
    print(f'{i + 1}° lugar: {jogador} com {valor}')
    sleep(0.5)