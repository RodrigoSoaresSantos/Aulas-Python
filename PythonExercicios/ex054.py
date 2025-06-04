'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

maiores = 0
menores = 0

for c in range(1, 8):
    idade = int(input('Digite as idades: '))
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Dessas 7 pessoas, {maiores} são maiores de idade e {menores} ainda são menores.')