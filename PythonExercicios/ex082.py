# Usando LISTAS

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número (-1 para parar): '))
    if num == -1:
        break
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Números: {numeros}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')