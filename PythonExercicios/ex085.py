'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e impares. No final, 
mostre os valores pares e ímpares em ordem crescente.'''

valores = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print(f'Os valores digitados par foram: {valores[0]}')
print(f'Os valores digitados ímpares foram: {valores[1]}')
