#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano para validarmos se é um ano bissexto: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano é bissexto')
        else:
            print('O ano não é bissexto')
    else:
        print('O ano é Bissexto')
else:
    print('O ano não é bissexto')        