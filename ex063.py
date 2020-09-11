t2 = 1
t3 = 1
t1 = 0
n = 2
v = int(input('Quantos termos da Seqüência de Fibonacci você quer ver: '))
if v >= 1:
    print('O 1º termo da seqüência de Fibonacci é: 0')
if v >= 2:
    print('O 2º termo da seqüência de Fibonacci é: 1')

while v >= 3:
    t3 = t2 + t1
    n = n + 1
    print('O {}º termo da seqüência de Fibonacci é: {}'.format(n, t3))
    t1 = t2
    t2 = t3
    v = v -1


print('Fim!')