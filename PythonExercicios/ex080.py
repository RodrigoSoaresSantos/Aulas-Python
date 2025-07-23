#Usando LISTAS

'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

valores = []

for i in range(0, 5):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if len(valores) == 0:
        valores.append(numero)
        print('O valor foi adicionado no final da lista.')

    elif numero >= valores[-1]:
        valores.append(numero)
        print('O valor foi adicionado no final da lista.')

    else:
        posicao = 0
        while posicao < len(valores):
            if numero < valores[posicao]:
                valores.insert(posicao, numero)
                print(f'O valor foi inserido na posição {posicao}')
                break
            posicao += 1
            
print("Os valores inseridos organizados do menor para o maior ficou assim: ", valores)
