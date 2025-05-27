'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- De 25 até 30: Sobrepeso.
- de 30 até 40: Obesidade.
- Acima de 40: Obesidade mórbida'''

print('Vamos calcular seu IMC (Indice de massa corporal).')
print('=o='*20)

peso = float(input('Qual é o seu peso atual? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura * altura)

if imc < 18.5:
    status = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    status = 'Peso ideal'
elif imc >= 25 and imc < 30:
    status = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    status = 'Obesidade' 
else:
    status = 'Obesidade mórbida'

print('=o='*20)
print('De acordo com o peso e altura informados, seu IMC é de {:.2f}. Considerado {}.'.format(imc, status))    