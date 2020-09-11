def area(h, b):
    a = h * b
    print(f'A área do terreno com as seguintes medidas:\nLargura: {h}m\nComprimento: {b}m\nÉ de {a}m ')


h = float(input('Digite a largura do terreno: '))
b = float(input('Digite o comprimento do terreno:  '))
area(h, b)