"""
n = int(input('Digite o número: '))
t = 1
for c in range(1, n * 10 + 1, n*t):
    #print(c)
    print('{} X {} = {}'.format(n, t, n*t))
    t = t+1
"""

num = int(input('Digite um número para ver a sua tabuada:'))
for c in range (1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))