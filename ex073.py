times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio','Atlético Paranaense', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Lista de times do Brasileirão: {times}\n')
print(f'Os cinco primeiros colocados são: {times[:5]}\n')
print(f'Os quatro últimos colocados são: {times[16:]}\n')
ordem = tuple(sorted(times))
print(f'Times em ordem alfabética{ordem}\n')
times.index(('Chapecoense'))
print('A Chapecoense está na {}ª posição'.format(times.index(('Chapecoense'))))
