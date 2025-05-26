'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = casa / (anos * 12)

if prestacao > 0.3 * salario: 
    print('Empréstimo negado. Você não pode realizar a compra dessa casa pois a prestação de R${:.2f} excede 30% do seu salário'.format(prestacao))
else:
    print('Empréstimo aprovado. Você pode realizar a compra dessa casa pois a prestação de R${:.2f} não excede 30% do seu salário'.format(prestacao))