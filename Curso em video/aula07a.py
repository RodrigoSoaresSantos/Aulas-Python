
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#Esse contra barra N "\n" é para quebrar a linha dentro da função print sem precisar criar outro print.
#Esse end=' ' é para juntar na mesma linha dois ou mais prints
#Esse ":.3f", (o f é de Float) dentro das chaves {} é para formatar o numero resultado com 3 casas após a virgula/ponto. 
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potencia {}'.format(di, e))
