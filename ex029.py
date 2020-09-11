veloc = int(input('Entre com a velocidade do veículo: '))
if veloc > 80:
    multa = float(veloc - 80)*7.00
    print('DEVAGAR!! Você levou uma multa de R${:.2f}!!!'.format(multa))
else:
    print('Muito bem! Continue respeitando o limite de velocidade. Bom dia!')