#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: '))
existe = cidade.upper().find('SANTO ')

if existe<0: 
    print('A cidade digitada não começa com a palavra Santo')
else:
    print('A cidade digitada começa com a palavra Santo')


#MÉTODO DA CORREÇÃO

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')