#Interrompendo repetições WHILE.

'''Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = soma = contador = 0

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles foi {soma}')