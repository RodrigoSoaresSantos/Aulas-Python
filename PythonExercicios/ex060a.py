#Usando laço WHILE e FOR

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120'''

print('Vamos ver qual é o fatorial de um número.')
num = int(input('Digite um número: '))
fatorial = 1

for contador in range(num, 0, -1):
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
print(fatorial)