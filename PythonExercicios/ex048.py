'''Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.'''

from time import sleep

print('Vamos ver qual é a soma dos números impares são multiplos de 3 em um intervalo de 1 a 500.')
print('PROCESSANDO...')
sleep(2)

soma = 0

for cont in range(0, 501):
    if cont % 2 != 0 and cont % 3 == 0:
        soma = soma + cont 

print('A soma de todos os números ímpares que são múltiplos de 3 é... {}'.format(soma))
