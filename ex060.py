'''n = int(input('Digite um número: '))
f = n
ft = n
while n > 1:
    f = f * ( n-1)
    n = n - 1
print('{}! = {}'.format(ft, f))
'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))