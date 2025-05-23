#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print(type(algo))
print('É número?',algo.isalnum())
print('É alpha?',algo.isalpha())
print(algo.isascii())
print('É decimal?',algo.isdecimal())
print('É digitado?',algo.isdigit())
print(algo.isidentifier())
print('Está em letra minuscula?',algo.islower())
print('É "printável"?',algo.isprintable())
print('É número?',algo.isnumeric())
print('Tem espaço?',algo.isspace())
print('Está em letra maiuscula?',algo.isupper())