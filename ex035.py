a = int(input('Inisira a medida da primeira reta: '))
b = int(input('Inisira a medida da segunda reta: '))
c = int(input('Inisira a medida da terceira reta: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Sucesso! As três retas informadas podem formar um triângulo!')
else:
    print('Lamento, as três retas informadas não podem formar um triângulo.')