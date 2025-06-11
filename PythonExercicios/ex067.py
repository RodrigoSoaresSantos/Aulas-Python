#Intorrompendo o laço WHILE com break.

'''Faça um progrma que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo'''

contador = num = mult = 0
num = int(input('Digite um número: '))

while True:
    contador += 1
    mult = num * contador
    print(f'{num} X {contador} = {mult}')
    if contador == 10:
        num = int(input('Digite outro número: '))
        contador = 0
    if num < 0:
        break
print('Tabuada encerrada. Obrigado por participar!')