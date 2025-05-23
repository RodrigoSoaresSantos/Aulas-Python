#Escreva um programa que pergunte a quantidade em Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado. 

km = float(input('Quantos KMs você rodou com o carro? '))
dias = float(input('Quantos dias você ficou com o carro? '))
valorKm = km * 0.15
valorDias = dias * 60

print('Utilizando o carro por {:.0f} dias e percorrido {:.0f} Km o valor do aluguel será de R${:.2f}'.format(dias, km, valorKm + valorDias))