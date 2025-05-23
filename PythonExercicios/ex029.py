"""
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A Multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade = int(input('Em quantos Km/h está a velocidade do seu carro?: '))

if velocidade <= 80:
    print('Você está dentro do limite de velocidade')    
else:
    multa = (velocidade - 80) * 7
    print('Você está acima do limite de velocidade. Precisará pagar uma multa de R${:.2f}'.format(multa))