#Utilizando o laço WHILE.

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.'''

from random import randint

wins = 0

while True:
    usuario = int(input('Digite um número: '))
    pc = randint(0, 10)
    par_ou_impar = ' '
    soma = usuario + pc

    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    print(f'Você escolheu o número {usuario} e o PC {pc}. A soma deu {soma}.')

    if soma % 2 == 0:
        print('É PAR!')
        if par_ou_impar == 'P':
            print('Ponto pra você!')
            wins += 1
        else:
            print('PERDEU! Hahahaha')
            break
        
    elif soma % 2 != 0:
        print('É ÍMPAR!')
        if par_ou_impar == 'I':
            print('Ponto pra você!')
            wins += 1
        else:
            print('PERDEU! Hahahaha')
            break

print(f'Você ganhou {wins} vezes do PC. Muito bom!!!.')