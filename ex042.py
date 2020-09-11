a = int(input('Inisira a medida da primeira reta: '))
b = int(input('Inisira a medida da segunda reta: '))
c = int(input('Inisira a medida da terceira reta: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    if a == b == c:
        print('Você pode formar um triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Você pode formar um triângulo Isósceles')
    elif a != b and a != c:
        print('Você pode formar um triângulo Escaleno')
else:
    print('Você não pode formar nenhum triângulo')

#if r1 == r2 == r3
#r1 != r2 != r3 != r1
#else