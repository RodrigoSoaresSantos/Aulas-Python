#Utilizando o laço WHILE.

'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.'''

print('Vamos ver uma sequencia de Fibonacci.')
termos = int(input('Digite quantos termos da sequência você deseja visualizar: '))
contador = 0
primeiro_termo = 0
segundo_termo = 1

while contador < termos:
    print(primeiro_termo, end=' → ')
    primeiro_termo, segundo_termo = segundo_termo, primeiro_termo + segundo_termo
    contador += 1
print('FIM!')