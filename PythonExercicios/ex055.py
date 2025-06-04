#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = int(input(f'Qual o peso da {pessoas}ª pessoas?: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso entre os 5 é o {maior}Kg e o menor é o {menor}Kg')