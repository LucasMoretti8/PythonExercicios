nome = str
valor = int
a = 0
b = 0
c = 0
cont = 0
while True:
    cont += 1
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: R$'))
    a += valor
    if valor > 1000:
        b += 1
    if cont == 1:
        c = valor
    else:
        if valor < c:
            c = valor
    continua = str(input('Deseja cadastrar outro produto [S / N ]?: ')).upper()
    if continua == 'N':
        break
print('Resumo da compra:\nTotal gasto: R${}\n{} produtos custaram mais do que R$1000\nE o produto mais barato da compra foi R${}'.format(a,b,c))