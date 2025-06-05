#Usando o laço WHILE

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente"
até ter um valor correto.'''

sexo = str(input('Informe seu sexo: [M/F] '))
while sexo != 'M' and sexo != 'F':
    print('Digite uma opção válida.')
    sexo = str(input(('''Qual gênero você se identifica:
[ M ] para masculino
[ F ] para feminino
'''))).strip().upper()
if sexo == 'M':
    print('Você selecionou que se identifica com o sexo MASCULINO.')
elif sexo == 'F':
    print('Você selecionou que se identifica com o sexo FEMININO.')