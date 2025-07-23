'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

principal = []

for linha in range(3):
    nova_linha = []
    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        nova_linha.append(valor)
    principal.append(nova_linha)

print('-*-' * 7)
for linha in principal:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()
print('-*-' * 7)