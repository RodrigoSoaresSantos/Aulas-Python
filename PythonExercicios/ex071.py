#Utilizando a estrutura de repetição WHILE e break.

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão fornecidas. As cédulas disponíveis são de R$50, R$20, R$10 e R$1. O programa deve informar quantas cédulas de cada valor serão fornecidas.'''

from time import sleep

print('-*-'*14)
print('BEM VINDO(a) AO PROGRAMINHA DE SACAR DINHEIRO')
print('-*-'*14)
valor = int(input("Digite o valor a ser sacado: R$ "))
notas_50 = notas_20 = notas_10 = notas_1 = 0
print('REALIZANDO DISTRIBUIÇÃO DE NOTAS...')
sleep(2)

while True:
    if valor >= 50:
        notas_50 = valor // 50
        valor = valor % 50
    elif valor >= 20:
        notas_20 = valor // 20
        valor = valor % 20
    elif valor >= 10:
        notas_10 = valor // 10
        valor = valor % 10
    elif valor >= 1:
        notas_1 = valor // 1
        valor = valor % 1
    else:
        break

print('Serão fornecidas:')
print(f'{notas_50} notas de R$50')
print(f'{notas_20} notas de R$20')
print(f'{notas_10} notas de R$10')
print(f'{notas_1} notas de R$1')
