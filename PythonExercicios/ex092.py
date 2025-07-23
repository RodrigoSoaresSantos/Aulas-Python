# Usando Dicionários

'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionários se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
ctps = int(input('Carteira de Trabalho (0 não tem): '))

if ctps != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['idade'] + 35) - (datetime.now().year - dados['contratação'])

print('--- Dados Cadastrados ---')
print(f'Nome: {dados["nome"]}')
print(f'Idade: {dados["idade"]} anos')

if ctps != 0:
    print(f'CTPS: {ctps}')
    print(f'Ano de Contratação: {dados["contratação"]}')
    print(f'Salário: R${dados["salário"]:.2f}')
    print(f'Aposentadoria: {dados["aposentadoria"]} anos')
