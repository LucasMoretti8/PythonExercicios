'''
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print(t)
for c in range (9):
    t = t + r
    print(t)
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('Acabou')