#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz2 = numero **(1/2)

print('O número digitado foi {}. O dobro desse número é {}, o triplo é {} e a raiz quadrada é {:.0f}.'.format(numero, dobro, triplo, raiz2))