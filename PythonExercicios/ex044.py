'''Elabora um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
- À vista, dinheiro ou cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: Preço normal.
- 3x ou mais no cartão: 20% de juros.'''

produto = 359
print('O produto que você está adquirindo custa R${}.'.format(produto))
pagamento = int(input('''Digite o número que corresponde a forma de pagamento desejada. 
                        [ 1 ] Dinheiro ou cheque
                        [ 2 ] Cartão
                        :'''))

if pagamento == 2:
    cartão = int(input('''Digite o número que corresponde se o pagamento no cartão será à vista ou parcelado.
            [ 1 ] À vista
            [ 2 ] Parcelado
            :'''))
    if cartão == 1:
        print('''Para o pagamento à vista no cartão conseguimos o desconto de 5%.
            Sendo assim, o produto que custa R${} passa a ser R${}'''.format(produto, produto - ((produto / 100) * 5 )))
    elif cartão == 2:
        parcelas = int(input('''Digite a opção correspondente a quantidade de parcelas.
                                [ 1 ] 2 parcelas
                                [ 2 ] 3 parcelas ou mais
                                :'''))
        if parcelas == 1:
            print('''O pagamento no cartão em 2 parcelas tem o preço normal do produto.
                O valor final do produto é de R${}'''.format(produto))
        elif parcelas == 2:
            print('''O pagamento no cartão em 3 parcelas ou mais tem um acréscimo de 20% de juros.
                O valor final do produto é de R${}'''.format(produto + ((produto / 100) * 20)))
        else:
            print('O Número digitado é inválido. Recomece e selecione uma opção válida.')
    else:
        print('O Número digitado é inválido. Recomece e selecione uma opção válida')
elif pagamento == 1:
    print('''O pagamento em dinheiro ou cheque tem 10% de desconto.
        Sendo assim, o produto que custa R${} com desconto fica R${}'''.format(produto, produto - ((produto / 100) * 10)))
else:
    print('O número digitado é inválido. Recomece e selecione uma opção válida. ')