'''
pesoinicial = float(input('Digite o peso da pessoa: KG '))
pesomaior = pesoinicial
pesomenor = pesoinicial
for c in range (1,5):
    peso = float(input('Digite o peso da pessoa: KG '))
    if peso > pesomaior:
        pesomaior = peso
    elif peso < pesomenor:
        pesomenor = peso
print('O maior peso digitado foi: {} KG\nO menor peso digitado foi: {} KG'.format(pesomaior,pesomenor))
'''

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg'.format(maior,menor))