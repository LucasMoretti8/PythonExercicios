'''n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'a soma dos {c} números que digitou vale {s}')
'''
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar):'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valors foi {soma}')