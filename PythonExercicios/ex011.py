#Faça um progrma que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta necessária para pinta-la.
#Sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Qual é a altura da parede que você quer pintar? '))
largura = float(input('Qual é a largura da parede que você quer pintar? '))
metros = altura * largura
tinta = metros / 2

print('A parede com altura de {} metros e largura de {} metros,'.format(altura, largura), end=' ')
print('ela possúi {}M² e será necessário {} litros de tinta para pinta-la'.format(metros, tinta))