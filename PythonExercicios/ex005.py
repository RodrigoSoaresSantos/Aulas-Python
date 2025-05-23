#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número '))
sucessor = numero + 1
antecessor = numero - 1

print('O número digitado foi {}. O sucessor desse número é {} e o antecessor desse número é {}'.format(numero, sucessor, antecessor))
