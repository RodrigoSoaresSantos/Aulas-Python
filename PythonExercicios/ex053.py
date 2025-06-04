'''Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços.'''

frase1 = str(input('Digite uma frase: '))

formatada = frase1.replace(" ", "").lower()

if formatada == formatada[::-1]:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')



#MÉTODO GUANABARA

frase2 = str(input('Digite uma frase: ')).strip().upper()
palavras = frase2.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')