#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 

nome_completo = str(input('Digite seu nome completo: '))
existe = nome_completo.upper().find('SILVA')

if existe<0:
    print('O nome digitado não tem "Silva".')
else:
    print('O nome digitado tem "Silva".')    



#MÉTODO DA CORREÇÃO

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.lower()))