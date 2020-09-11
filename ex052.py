num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end ='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')

'''
n = int(input('Digite um número inteiro: '))
s = int(0)
for c in range(1,n+1):
#    print(c)
#    print(n % c)
    if c != 1 and c != n:
        p = n % c
        if p == 0:
            s = s+1
if s != 0:
    print('Não é primo')
else:
    print('É primo')
'''