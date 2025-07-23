#Usando Listas

'''Crie um programa que leia Nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o
usuário possa mostrar as notas de cada aluno individualmente.'''

boletim = []
while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    
    continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break
print('=' * 30)
print("Boletim")
print('=' * 30)
for aluno in boletim:
    print(f"Nome: {aluno[0]}, Média: {aluno[2]}")

while True:
    consulta = input("\nDeseja consultar as notas de algum aluno? (s/n): ").strip().lower()
    if consulta != 's':
        break
    nome_consulta = input("Digite o nome do aluno: ")
    for aluno in boletim:
        if aluno[0] == nome_consulta:
            print(f"Notas de {nome_consulta}: {aluno[1]}")
            break
    else:
        print(f"Aluno {nome_consulta} não encontrado.")
