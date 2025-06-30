num = [2, 5, 9, 1]
num[2] = 3
num[4] = 7
num.append(7) 
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2) #Elimina o ultimo valor da lista ou a posição especificada. 
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5) #Adiciona algum valor no final da lista.
valores.append(9)
valores.append(4)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3 ,4, 7]
b = a[:] #Cria uma cópia da lista A e ao mudar a lista B não irá alternar a lista A.
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
