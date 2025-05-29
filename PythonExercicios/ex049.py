'''Refaça o DESAFIO 009, motrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

print('Vamos ver a tabuada de um número que você vai escolher.')

num = int(input('Digite um número de 1 a 10: '))
print(f'A tabuada do número {num} é:')

for cont in range(1, 11):
    mult = num * cont
    print(f'{num} x {cont} = {mult}')