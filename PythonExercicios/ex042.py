'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
- Equilátero: Todos os lados igual
- Isosceles: Dois lados iguais
- Escaleno: Todos os lados diferentes'''

print('Vamos validar se 3 retas podem formar um triângulo e se sim, qual será o tipo do triangulo formado.')
print('=*='*20)

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('=*='*20) 
    print('Essas 3 retas podem formar um triângulo.')
    if r1 == r2 and r2 == r3:
        tipo = 'EQUILÁTERO'
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        tipo = 'ISÓSCELES'
    elif r1 != r2 != r3 != r1:
        tipo = 'ESCALENO'
    print('O triângulo formado é um {}.'.format(tipo))
else:
    print('Essas 3 retas não podem formar um triângulo')