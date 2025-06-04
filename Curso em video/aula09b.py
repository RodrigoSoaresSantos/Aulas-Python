frase = 'Curso em Vídeo Python'

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::-1])

print(frase.count('O')) #Vai retornar 0 pois não tem nesse exemplo a letra 'O' Maiuscula
print(frase.upper().count('O')) #Vai retornar 3 pois ele transformou todas as letras em maiusculas e depois pediu para contar quantas vezes aparece 'O' maiusculo

print(len(frase))
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #Nesse comando ele vai mostrar a terceira palavra/frase da lista (0,1,2) e após o quarto caracter dessa palavra/frase (0,1,2,3).


print('''Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!''') #3 aspas (''') faz com que a função print funcione em linhas quebradas.
