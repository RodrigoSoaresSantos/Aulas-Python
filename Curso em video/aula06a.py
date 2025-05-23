num1 = int(input('Digite um valor '))
num2 = int(input('Digite outro valor '))
soma = num1 + num2

#Desafio: Usar a função print para escrever na tela "A soma entre num1 e num2 vale soma"
#O jeito que eu fiz foi assim: print('A soma entre', num1, 'e', num2, 'vale', soma)

print('A some entre {} e {} vale {}'.format(num1, num2, soma))
