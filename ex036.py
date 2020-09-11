valor = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o salário do comprador: R$'))
anos = int(input('Insira a quantidade de anos que ele irá pagar: '))

parcela = valor / (12 * anos)
numparcelas = int(valor / parcela)
print('\nO Valor da parcela será de R${:.2f}\nSerão cobradas {} parcelas'.format(parcela, numparcelas))
if parcela > (30 * salario) / 100:
    print('EMPRÉSTIMO RECUSADO!!')
else:
    print('EMPRÉSTIMO APROVADO!!')