#faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

limpa = '\033[m'
cores = {'limpa' : '\033[m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m'}

produto = float(699.90)
desconto = (produto / 100) * 5

print('O produto que você escolheu está com o desconto de 5% hoje. De {}R${:.2f}{} ele está saindo por {}R${:.2f}{}'.format(cores['vermelho'], produto, limpa, cores['verde'], (produto - desconto), limpa))