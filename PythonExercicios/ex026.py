#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase qualquer: ').lower()).strip()

print('A frase que você digitou tem {} letras "A". A primeira vez que essa letra aparece na frase é na posição {} ' \
'e a última posição que a letra aparece na frase é na posição {}.'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))