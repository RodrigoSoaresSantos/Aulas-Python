#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras Maiúsculas.
#O nome com todas as letras Minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome_completo = str(input("Qual é o seu nome completo?: "))

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo.replace(' ','')))

primeiro_nome = nome_completo.split()

print(len(primeiro_nome[0]))


#MÉTODO DA CORREÇÃO

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))