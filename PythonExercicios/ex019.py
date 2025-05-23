#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno_1 = 'Aline'
aluno_2 = 'Bianca'
aluno_3 = 'Caio'
aluno_4 = 'Eduardo'
aluno_5 = 'Felicia'

sorteio = choice([aluno_1, aluno_2, aluno_3, aluno_4, aluno_5])

print('Entre os alunos: {}, {}, {}, {} e {}, o escolhido para apagar o quadro foi o(a) {}.'.format(aluno_1, aluno_2, aluno_3, aluno_4, aluno_5, sorteio))