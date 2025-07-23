#Usando Dicionários

'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela'''

aluno = {}
aluno['nome'] = input('Nome do aluno: ')    
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('---' * 10)
for k, v in aluno.items():
    print(f'O campo {k} tem valor {v}')
print('---' * 10)
print(f'O aluno {aluno["nome"]} tem média {aluno["media"]} e está {aluno["situacao"]}.')
