#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

C = int(input('Quantos graus ºC está fazendo onde você mora? '))
F = (C * 9/5) + 32

print('Se onde você mora está {:.0f}ºC, essa mesma temperatura em Fahrenheit é de {:.0f}ºF'.format(C, F))