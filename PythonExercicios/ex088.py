#Usando LISTAS COMPOSTAS

'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

jogos = []
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Gerando {quantidade} jogos. Um instante...')
sleep(2)

for c in range(quantidade):
    jogo = []
    for j in range(6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)
    jogos.append(jogo)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    sleep(1)
print('========= Boa sorte! =========')