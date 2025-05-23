#Faço um programa que leia o nome completo de uma pessoa, mostrando ems eguida o primeiro e o último nome separadamente.
#ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome_completo = str(input('Digite seu nome completo: ')).strip()
separar = nome_completo.split()

print('O nome digitado foi "{}". O primeiro nome é {} e o último nome é {}.'.format(nome_completo, separar[0], separar[-1]))
