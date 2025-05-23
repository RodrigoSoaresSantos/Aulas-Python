"""
Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 para viagens mais longas. 
"""

distancia = int(input('Qual é a distancia em Km da viagem?: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem de {}Km ficou em R${:.2f}'.format(distancia, valor))
else:
    valor = distancia * 0.45
    print('O valor da sua viagem de {}Km ficou em R${:.2f}'.format(distancia, valor))
