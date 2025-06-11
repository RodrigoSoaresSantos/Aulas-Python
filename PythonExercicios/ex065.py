#Utilizando a estrutura de repetição WHILE.

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar se o usuário quer continuar ou não.'''

contador = 0
soma = 0
media = soma / contador
maior = 0
menor = 0

print('Vamos ver a média de alguns números')
print('-o-'*30)
num = int(input(('Digite um número: ')))
while contador < 5:
    media += num
    num = int(input('Digite outro número: '))
    contador += 1
    if contador == 1:
        maior = num
        menor = num
    elif contador > 1:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num   
print(media / contador, maior, menor)
print('-o-'*30)
continuar = int(input('''Deseja continuar digitando mais números?
[ 1 ] SIM
[ 2 ] NÂO
:'''))
if continuar == 1:
    contador = 4 
else:
    print('Obrigado por participar!.')
