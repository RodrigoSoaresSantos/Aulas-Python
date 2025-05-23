#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos sigitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#milhar: 1

num1 = str(input('Digite um número de 0 a 9999: '))
num_separado = num1.replace('', ' ')
num_formatado = num_separado.strip()
lista = num_formatado.split()

print('O número digitado foi {}.\nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(num1, lista[3], lista[2], lista[1], lista[0]))


#MÉTODO DA CORREÇÃO

num = int(input('Informa um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando seu número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:{}'.format(m))