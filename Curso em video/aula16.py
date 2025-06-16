lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são IMUTÁVEIS
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))
print(sorted(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) # Quantas vezes aparece o 5
print(c.index(8)) # Em que posição está o 8

pessoa = ('Gustavo', 39, 'M', 99.88) # Nome, idade, sexo, peso
del(pessoa) # apagar a variável pessoa
print(pessoa)
