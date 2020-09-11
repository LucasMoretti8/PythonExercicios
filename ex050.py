t = 0
count = 0
for c in range (0,6):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        count = count +1
        t = t + n
print('Você informou {} números pares\nO total da soma dos números pares é:{}'.format(count,t))
