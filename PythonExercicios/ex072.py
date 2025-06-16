# Usando TUPLAS

'''Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero até cinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

while True:
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {numeros[num]}.')
        break
    elif num < 0 or num > 20:
        num = int(input('Número inválido! Digite um número entre 0 e 20: '))