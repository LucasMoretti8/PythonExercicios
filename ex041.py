import datetime
now = datetime.datetime.now()
ano = int(input('Informe o ano do atleta: '))
idade = now.year - ano
if idade < 9:
    print('Idade do atleta: {}\nCategoria Mirim'.format(idade))
elif idade <= 14:
    print('Idade do atleta: {}\nCategoria Infantil'.format(idade))
elif idade <= 19:
    print('Idade do atleta: {}\nCategoria Junior'.format(idade))
elif idade <= 20:
    print('Idade do atleta: {}\nCategoria Sênior'.format(idade))
else:
    print('Idade do atleta: {}\nCategoria Master'.format(idade))
