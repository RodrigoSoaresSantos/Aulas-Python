#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

num = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(2)
if num % 2 == 0:
    print('O número digitado é par.')
else:
    print('O número digitado é ímpar.')
