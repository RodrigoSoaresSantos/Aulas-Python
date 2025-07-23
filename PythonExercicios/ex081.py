#Usando LISTAS

'''Cri um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    if numero == -1:
        break
    valores.append(numero)
print(f'Você digitou {len(valores)} números.')
valores.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é: {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado e está na lista na posição {valores.index(5)}.')
else:
    print('O valor 5 não foi digitado e não está na lista.')