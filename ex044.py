valor = float(input('Insira o valor do produto: R$'))
condicao = int(input('\nEscolha a forma de pagamento:\n1) À vista no cheque ou em dinheiro\n2) À vista no cartão\n3) 2x no cartão\n4) 3x ou mais no cartão\nForma de pagamento:'))
if condicao == 1:
    valor = valor - ((10 * valor) / 100)
    print('Valor a ser pago: R${}'.format(valor))
elif condicao == 2:
    valor = valor - ((5 * valor) / 100)
    print('Valor a ser pago: R${}'.format(valor))
elif condicao == 3:
    print('Valor a ser pago: R${}'.format(valor))
elif condicao == 4:
    valor = valor + ((20 * valor) / 100)
    print('Valor a ser pago: R${}'.format(valor))