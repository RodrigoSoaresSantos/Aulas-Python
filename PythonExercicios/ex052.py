'''Faço um programa que leia um número inteiro e diga se ele é ou não número primo'''

num = int(input('Digite um número: '))

if num < 2:
    print('Não é um primo')
else:
    resultado = True
    for c in range(2, int(num ** 0.5) + 1):
        if num % c == 0:
            resultado = False
            break
    if resultado == True:
        print('É primo')
    else:
        print('Não é primo')