'''A confederação Nascional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFASTIL
- Até 19 anos: JUNIOR
- Se for 20 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento. Ex: 1997. '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
elif idade > 20:
    categoria = 'MASTER'

print('Como você tem {} anos, você está na categoria {} da natação'.format(idade, categoria))    