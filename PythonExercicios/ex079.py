#Usando LISTAS

'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em uma ordem crescente.'''

valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado...')
    else:
        print('Esse número já foi adicionado! Informe outro ou encerre...')
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
