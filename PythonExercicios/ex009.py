#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número: '))
um = str(num) + 'x1 = ' + str(num * 1)
dois = str(num) + 'x2 = ' + str(num * 2)
tres = str(num) + 'x3 = ' + str(num * 3)
quatro = str(num) + 'x4 = ' + str(num * 4)
cinco = str(num) + 'x5 = ' + str(num * 5)
seis = str(num) + 'x6 = ' + str(num * 6)
sete = str(num) + 'x7 = ' + str(num * 7)
oito = str(num) + 'x8 = ' + str(num * 8)
nove = str(num) + 'x9 = ' + str(num * 9)
dez = str(num) + 'x10 = ' + str(num * 10)

print('A tabuada referente ao número {0} é: \n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(num, um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez))