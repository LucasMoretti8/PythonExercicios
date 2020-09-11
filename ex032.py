ano = int(input('Digite o ano desejado: '))
if (ano % 400) == 0 or (ano % 4) == 0:
    print('O ano de {} é um ano Bissexto'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto'.format(ano))