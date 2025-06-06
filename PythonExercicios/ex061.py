#Utilizando o laço WHILE.

'''refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Vamos verificar qual é a PA (Progressão Aritimética) de um número.')
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contador = 0

while contador < 10:
    termo = num + (contador * razao)
    contador += 1
    print(termo)