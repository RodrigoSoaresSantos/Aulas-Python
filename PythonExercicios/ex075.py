#Usando TUPLAS

'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado.')

pares = [num for num in numeros if num % 2 == 0]
if pares:
    print(f'Os números pares digitados foram: {", ".join(map(str, pares))}.')
else:
    print('Nenhum número par foi digitado.')    
