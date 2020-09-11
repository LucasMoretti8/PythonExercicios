valor = int(input('Insira o valor a ser sacado: R$'))
a = 0
b = 0
c = 0
d = 0
while valor >= 50:
    valor -= 50
    a += 1
while valor >= 20:
    valor -= 20
    b += 1
while valor >= 10:
    valor -= 10
    c += 1
while valor > 0:
    valor -= 1
    d += 1
print('Notas de R$50: {}\nNotas de R$20: {}\nNotas de R$10: {}\nNotas de R$1: {}\n'.format(a,b,c,d))