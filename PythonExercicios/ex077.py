#Usando TUPLAS

'''Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.'''

palavras = ('aprender', 'programar', 'linguagem', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    vogais = ''
    for letra in i:
        if letra in 'aeiou':
            vogais += letra + ' '
    print(f'Na palavra {i.upper()} temos: {vogais.upper()}')
