#Usando TUPLAS

'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.'''

times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG',
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo',
         'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

print(f'Os times são: {times}')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time Mirasool está na {times.index("Mirassol") + 1}ª posição na tabela.')