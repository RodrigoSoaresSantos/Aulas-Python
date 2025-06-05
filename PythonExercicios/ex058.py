#Usando o laço WHILE

'''Melhore o jogo do desafio 028 onde 0 computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep

contador = 1
n_computador = randint(0, 10)
print('O computador escolheu um número de 0 a 10. Tente vencer o computador acertando o número escolhido por ele.')
n_usuario = int(input('Digite um número: '))
print('Processando...')
sleep(1)
while n_usuario != n_computador:
    contador += 1
    n_usuario = int(input(f'''O número que você digitou {n_usuario} é diferente do número que o computador escolheu.
Digite outro número: '''))
    print('Processando...')
    sleep(1)
print(f'O número que você digitou {n_usuario} é igual ao número que o computador escolheu. Foram necessárias {contador} tentativas.')