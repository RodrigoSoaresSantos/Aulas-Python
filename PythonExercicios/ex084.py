#Usando LISTAS compostas.

'''Faço um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])

    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')

pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

print(f'Maior peso: {maior}kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'Menor peso: {menor}kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
print()