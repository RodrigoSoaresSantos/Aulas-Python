'''Crie um programa que faça o computador jogar Jokenpô com você'''

from random import randint  
from time import sleep

num_compu = randint(1,3)

if num_compu == 1:
    movimento_compu = 'PEDRA'
elif num_compu == 2:
    movimento_compu = 'PAPEL'
else: 
    movimento_compu = 'TESOURA' 

print('Você acaba de desafiar o computador para um JOKENPÔ!!!')
print('PROCESSANDO...')
sleep(2)
num_usuario = int(input('''Digite o número que corresponde ao movimento que você quer jogar:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
:'''))
print('Então você escolheu jogar assim...')
sleep(2)
print('=o='*20)

if num_usuario == num_compu:
    print('Você e o computador fizeram o mesmo movimento. EMPATE!!!')
elif num_compu == 1 and num_usuario == 2:
    print('DROGA! você jogou PAPEL em cima da minha PEDRA. Parabêns por vencer!!!')
elif num_compu == 1 and num_usuario == 3:
    print('Hahaha. GANHEI!!!. Você jogou TESOURA em cima do meu PAPEL e perdeu.')
elif num_compu == 2 and num_usuario == 1:
    print('Hahaha. GANHEI!!!. Você jogou PEDRA em cima do meu PAPEL e perdeu.')
elif num_compu == 2 and num_usuario == 3:
    print('DROGA! Você jogou TESOURA em cima do meu PAPEL. Parabêns por vencer!!!')
elif num_compu == 3 and num_usuario == 1:
    print('DROGA! Você jogou PEDRA em cima da minha TESOURA. Parabêns por vencer!!!')
elif num_compu == 3 and num_usuario == 2:
    print('Hahaha. Você jogou PAPEL em cima da minha TESOURA e perdeu.')

print('Vamos jogar mais vezes quando quiser ^^')