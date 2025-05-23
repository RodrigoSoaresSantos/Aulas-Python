#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo_graus = float(input('Qual é o angulo em graus? '))

angulo_radians = radians(angulo_graus)

seno = sin(angulo_radians)
cosseno = cos(angulo_radians)
tangente = tan(angulo_radians)

print('O angulo de {:.0f}º tem o seno de {:.3f}, o cosseno de {:.3f} e a tangente de {:.3f}'.format(angulo_graus, seno, cosseno, tangente))