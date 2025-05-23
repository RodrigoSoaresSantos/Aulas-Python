#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

SAtual = float(input('Qual é o seu salário atual? '))
aumento = SAtual * 0.15

print('Seu salário atual está em R${:.2f} e a partir de agora terá um aumento de 15%. Seu novo salário é de R${:.2f}'.format(SAtual, SAtual + aumento))