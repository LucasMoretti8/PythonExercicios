dist = float(input('Informe a distância em KMs da viagem: '))
if dist <= 200:
    valor = float(dist * 0.50)
    print('O Valor da viagem é de R${:.2f}'.format(valor))
else:
    valor = float(dist * 0.45)
    print('O valor da viagem é de R${:.2f}'.format(valor))