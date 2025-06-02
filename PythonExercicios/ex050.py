'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor difitado for ímpar, desconsidere-o'''

soma = 0

for c in range(1, 7):
    entrada = int(input('Digite um número: ')) 
    if entrada % 2 == 0:
        soma += entrada

print(f'A soma dos seis números digitados que são pares é: {soma}')
