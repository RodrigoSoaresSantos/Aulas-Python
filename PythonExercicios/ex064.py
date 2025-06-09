#Utilizando o laço WHILE.

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

print('Vamos somar vários números')
num = 0
contador = 0
soma = 0

while num != 999:
    num = int(input('Digite um número: '))
    soma = soma + num
    contador += 1
    if num == 999:
        soma = soma - 999
print(f'Você digitou {contador} números e a soma deles deu {soma}')
