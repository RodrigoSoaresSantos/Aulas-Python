#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Digite qual foi sua primeira nota '))
n2 = float(input('Digete qual foi sua segunda nota '))
m = (n1 + n2) / 2

print('Se sua primeira nota foi {} e sua segunda nota foi {}, sua média é {}.'.format(n1, n2, m))
