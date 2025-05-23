#Faça um programa que leia o comprimeito do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Qual é o comprimento do cateto oposto do triangulo? '))
cateto_adjacente = float(input('Qual é o comprimento do cateto adjacente do triangulo? '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('Se o cateto oposto do triângulo retângulo é de {:.0f} e o adjacente é de {:.0f}, sua hipotenusa é igual a {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))