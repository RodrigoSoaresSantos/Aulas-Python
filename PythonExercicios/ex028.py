"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre o 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

n_computador = randint(0, 5)
print('O computador escolheu um número de 0 a 5. Tente vencer o computador acertando o número escolhido por ele.')
n_usuario = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(3)
print('O número que o computador escolheu foi {} e o que você digitou foi {}.'.format(n_computador, n_usuario))
if n_computador == n_usuario:
    print('Parabéns! você venceu o computador acertando o número que ele escolheu.')
else:
    print('Você errou o número que o computador escolheu. Puts!')