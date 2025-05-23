#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários a cima R$ 1.250,00, calcule um aumento de 10%.
#Para as inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu salário para que possamos calcular o aumento proporcional: '))
aumento15 = (salario * 0.15) + salario
aumento10 = (salario * 0.1) + salario 

if salario > 1250:
    print('Você teve 10% de aumento em cima do seu salário atual e agora recebe o total de R${:.2f}'.format(aumento10))
else:
    print('Você teve 15% de aumento em cima do seu salário atual e agora recebe o total de R${:.2f}'.format(aumento15))