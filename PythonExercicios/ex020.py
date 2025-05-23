#O mesmo professor do desafio anterior quer sortear a ordem de apresentalção de trabalhos dos alunos.
#Faça um progrma aque leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = ['Pedro', 'Paulo', 'Bianca', 'Larissa']
shuffle(alunos)

print('A ordem de apresentação dos trabalhos será: ')
print('Primeiro: {} \nSegundo: {} \nTerceiro: {} \nQuarto: {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))