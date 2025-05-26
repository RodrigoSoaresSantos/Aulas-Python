'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
escolha = str(input('Você quer que o número digitado seja convertido para binário, octal ou hexadecimal? '))

if 'binário' in escolha:
    print('O número digitado convetido em binário é: {}'.format(bin(num)[2:]))
elif 'octal' in escolha:
    print('O número digitado convertido em octal é: {}'.format(oct(num)[2:]))
elif 'hexadecimal' in escolha:
    print('O número digitado convertido em hexadecimal é: {}'.format(hex(num)[2:]))
else:
    print('Digite uma opção válida.')