num = input('Digite um número de 0000 a 9999: ')
jn = ' '.join(num)
sp = jn.split()
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(sp[3],sp[2],sp[1],sp[0]))