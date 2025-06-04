'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos'''

idade_somada = 0
mais_velho = 0
nome_guardado = ''
mulheres_menores = 0

for dados in range(1, 5):
    nome = str(input(f'Qual é o nome da {dados}ª pessoa?: '))
    idade = int(input(f'Qual é a idade da {dados}ª pessoa?: '))
    sexo = int(input(f'Qual é o sexo da {dados}ª pessoa? Digite [ 1 ] para masculino e [ 2 ] para feminino: '))

    idade_somada += idade
    media = idade_somada / 4

    if sexo == 1 and idade > mais_velho:
        mais_velho = idade
        nome_guardado = nome
    if sexo == 2 and idade < 20:
        mulheres_menores += 1

print(f'''A média de idade do grupo é de {media} anos. O homem mais velho é o {nome_guardado}. {mulheres_menores} mulheres que tem menos de 20 anos.''')