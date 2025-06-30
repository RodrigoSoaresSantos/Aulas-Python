#Usando TUPLAS  

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também, indique 
o menor e o maior valor que estão na tupla.'''

import random

numeros = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
           random.randint(1, 100), random.randint(1, 100))


print(f'Os números gerados foram: ', end='')

for n in numeros:
    print(f'{n},', end=' ')

print(f'\nO maior número é {max(numeros)} e o menor é {min(numeros)}.')