#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros.

metros = int(input('Qual é a distância em metros que você percorre até o trabalho? '))
centimetros = metros * 100
milimetros = metros * 1000

print('Se você percorre {} metros até o trabalho, são {} centímetros e {} milímetros'.format(metros, centimetros, milimetros))
