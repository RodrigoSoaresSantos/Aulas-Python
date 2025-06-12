#Utilizando o laço de repetição WHILE e o BREAk

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1.000,00
C) Qual é o nome do produto mais barato.'''

total_gasto = 0
produtos_mais_de_1000 = 0 
produto_mais_barato = ' '
preco_mais_barato = 0

print('*-*-'*10)
print('Bem-vindo aos DOCES DO ALEC!!!')
print('*-*-'*10)

while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: R$ '))

    if preco_mais_barato == 0 and produto_mais_barato == ' ':
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        produtos_mais_de_1000 += 1
    
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    
    if continuar not in 'S':
        break

print(f'O total gasto em doces foi R$ {total_gasto}. {produtos_mais_de_1000} custam mais de R$ 1.000,00 e o produto mais barato foi: {produto_mais_barato}.')
print('Volte sempre pra dar mais dinheiro pro meu marido.')