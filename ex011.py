a = float(input('Digite a altura em metros da parede: '))
l = float(input('Digite a largura em metros da parede: '))
ar = a*l
lt = ar/2
print('A altura da parede é de: {:.2f}m\na largura da parede é de: {:.2f}m\na área da parede é de: {:.2f}\ne você precisará de {} litros de tinta para pintá-la'.format(a,l,ar,lt))