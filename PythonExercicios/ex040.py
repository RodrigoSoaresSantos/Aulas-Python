'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- MéDIA 7.0 ou superior: APROVADO'''

nota1 = float(input('Qual foi a primeira nota?: '))
nota2 = float(input('Qual foi a segunda nova?: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi de {:.1f}. REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi de {:.1f}. RECUPERAÇÂO!'.format(media))
else:
    print('Sua média foi de {:.1f}. APROVADO!'.format(media))