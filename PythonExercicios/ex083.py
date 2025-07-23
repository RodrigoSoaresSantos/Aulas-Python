#Usando LISTAS 

'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os 
parênteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite uma expressão: '))
parenteses = []

for character in expressao:
    if character == '(':
        parenteses.append(character)
    elif character == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(character)
            break
        
if len(parenteses) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
