'''Desenvolva um programa que leio o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.'''

num = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))

for c in range(10):
    termo = num + (c * razao) 
    print(termo)