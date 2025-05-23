#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Condere US$1,00 = R$3,27

reais = float(input('Quantos Reais em espécie você tem na carteira nesse momento? '))
dolares = reais / 3.27

print('Com R${:.2f} que você tem agora, você teria US${:.2f}'.format(reais, dolares))