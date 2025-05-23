
#ANÁLISE

frase = 'Curso em Vídeo Python'

len(frase) #len é utilizado para verificar quantos caracteres tem.

frase.count('o') #A função count é para contar quantas vezes o caracter aparece.
frase.count('o', 0, 13) #Nesse caso vai contar quantas vezes aparece a letra 'o' do o caracter 0 até o 13 na frase.

frase.find('deo') #Essa função vai indicar em qual momento (em caracter) aparece 'deo'.
frase.find('Android') #Se procurar uma palavra/frase que não existe, ele vai retornar -1.

'Curso' in frase #in nesse caso é um operador. Ele vai verificar se existe a palavra 'Curso' na frase e se sim retornar verdadeiro(True).


#TRANSFORMAÇÃO

frase.replace('Python', 'Android') #replace vai procurar a palavra 'Python' e substituir por 'Android'.

frase.upper() #Transforma a palavra/frase em letras maiusculas.
frase.lower() #Transforma a palavra/frase em letras minusculas.
frase.capitalize() #Transforma a palavra/frase/str em letras minusculas e apenas a primeira letra fica em maiuscula.
frase.title() #Transforma apenas a primeira letra da palavra, após uma quebra/espaço, em letra maiuscula. 

frase.strip() #Remove os espaços inúteis no inicio e no final da str.
frase.rstrip() #Remove somente os ultimos espaços (r = direita) vazios dentro da str.
frase.lstrip() #Remove somente os primeiros espaços (l = esquerda) vazios dentro da str.


#DIVISÃO

frase.split() #split vai agir para separar onde tiver espaços(' '). Gera uma lista com todas as palavras dentro de uma cadeia de caracteres.


#JUNÇÃO 

'-'.join(frase) #join junta todas as str com algo préviamente definido. Nesse caso '-'.

