#Utilizando o laço WHILE

print('Vamos verificar qual é a PA (Progressão Aritimética) de um número.')
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

termos = 0
contador = 10

while contador != 0:
    pa = num + (termos * razao)
    print(pa, end=' → ')
    termos += 1
    contador -= 1
    if contador == 0:
        print('Agora...')
        novo_num = int(input('Você deseja saber mais termos dessa PA? Se sim, digite o número de vezes. Se não, digite 0: '))
        contador = novo_num

print('Obrigado por participar!')

    