#Usando laço WHILE e FOR

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120'''

print('Vamos ver qual é o fatorial de um número.')
num = int(input('Digite um número: '))
fatorial = 1
contador = num

while contador > 1:
    fatorial = fatorial * contador
    contador = contador - 1
print(f'O fatorial do número {num} é {fatorial}')
print(contador, fatorial)

