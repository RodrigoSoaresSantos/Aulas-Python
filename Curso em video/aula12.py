nome = str(input('Qual é seu nome? '))
if nome == 'Noah':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jessica Juliana': 
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
