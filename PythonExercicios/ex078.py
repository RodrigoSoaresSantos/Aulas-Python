#Usando LISTAS

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''

num = list()

for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores: {num}')
maior = max(num)
menor = min(num)

print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c+1}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c+1}... ', end='')