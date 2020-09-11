num = int(1)
while True:
    num = int(input('Digite um número para ver a sua tabuada:'))
    if num < 0:
        break

    for c in range (1,11):
        print('{} x {:2} = {}'.format(num, c, num*c))

print('Fim do programa')