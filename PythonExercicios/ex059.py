#Utilizando o laço WHILE

'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

operacao = 0
while operacao != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    operacao = int(input('''Selecione a opção da operação desejada:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Qual é o maior
[ 4 ] Novos números
[ 5 ] Sair do programa
'''))
    if operacao == 1:
        soma = num1 + num2
        print(f'Os números {num1} + {num2} é igual a {soma}')
    if operacao == 2:
        multiplicacao = num1 * num2
        print(f'Os números {num1} x {num2} é igual a {multiplicacao}')
    if operacao == 3:
        if num1 > num2:
            print(f'O primeiro número digitado, {num1}, é maior que o segundo número, {num2}.')
        elif num2 > num1:
            print(f'O segundo número digitado, {num2}, é maior que o primeiro número, {num1}.')
    else:
        print('digite uma opção valida.')
print('Obrigado pela participação. Volte sempre.')