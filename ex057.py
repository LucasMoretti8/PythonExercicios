s = str(input('Digite o sexo: ')).upper()
while s not in 'MmFf':
    s = str(input('DADOS INVÁLIDOS! Digite o sexo: ')).upper()
print('O Sexo informado é {}'.format(s))
