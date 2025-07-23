#Usando LISTAS COMPOSTAS

'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

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

soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = max(principal[1])
for linha in principal:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor
    soma_terceira_coluna += linha[2]
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
