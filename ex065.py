#n = int(input('Digite o primeiro número: '))
user = 'S'
c = 1
t = 0
n = int(input('Digite o primeiro número número: '))
maior = n
menor = n
while user in 'Ss':
    n1 = int(input('Digite outro número: '))
    t = t + n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    c = c + 1
    user = input('Deseja continuar [S/N]: ').upper()
t = t + n
m = t / c
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print("Media: {}".format(m))
