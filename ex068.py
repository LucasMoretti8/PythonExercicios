from random import randint
c = int(0)
while True:
    num = randint(0, 10)
    jog = int(input('Escolha um número e 1 a 10: '))
    pi = str(input('Você quer ser par ou ímpar?: '))
    tot = num + jog
    res = str
    if tot % 2 == 0:
        res = 'par'
    else:
        res = 'impar'
    print(tot)
    if  pi == res:
        print('Parabéns!')
        c += 1
    else:
        print('Ganhei! Chupa humano!')
        print('Você ganhou {} vezes consecutivas'.format(c))
        break
