sal = float(input('Digite o salário do funcionário: R$'))
if (sal <= 1250):
    sal = sal + ((sal * 15) / 100)
    print('O novo salário deverá ser de R${}'.format(sal))
else:
    sal = sal + ((sal * 10) / 100)
    print('O novo salário deverá ser de R${}'.format(sal))