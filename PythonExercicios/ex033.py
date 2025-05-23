#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print('O maior número é o {} e o menor número é o {}'.format(n1, n3))
    else:
        print('O maior número é o {} e o menor número é o {}'.format(n1, n2))
else:
    if n2 >= n3 and n2 >= n1:
        if n3 >= n1: 
            print('O maior número é o {} e o menor número é o {}'.format(n2, n1))
        else:
            print('O maior número é o {} e o menor número é o {}'.format(n2, n3))
    else:
        if n3 >= n2 and n3 >= n1:
            if n2 >= n1:
                print('O maior número é o {} e o menor número é o {}'.format(n3, n1))
            else:
                print('O maior número é o {} e o menor número é o {}'.format(n3, n2))