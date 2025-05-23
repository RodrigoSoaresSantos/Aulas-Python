#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Vamos calcular se 3 retas aleatórias podem formar um triangulo.')
print('-='*20)
r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimeiro da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas 3 retas podem formar um triângulo. Pois, {} + {} é maior que {} e {} + {} é maior que {} e {} + {} é maior que {}'.format(r1, r2, r3, r1, r3, r2, r2, r3, r1 ))
else:
    print('Essas 3 retas não podem formar um triângulo.')