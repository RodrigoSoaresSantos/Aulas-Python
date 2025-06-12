#Utilizando a estrutura de repetição WHILE e o BREAK.

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''
  
pessoas = 0
mais_de_18 = 0
homens = 0
mulheres_menor = 0


while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    
    if idade > 18:
        mais_de_18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menor += 1

    pessoas += 1
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    
    if continuar not in 'S':
        break

print(f'''{pessoas} foram cadastradas. Dessas {pessoas}, {mais_de_18} tem mais de 18 anos. {homens} são homens e 
{mulheres_menor} são mulheres menor de idade. Obrigado por participar!''')

