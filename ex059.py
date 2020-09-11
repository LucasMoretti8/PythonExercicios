n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = int(0)
while op != 5:
    op = int(input('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n\nDigite a operação desejada: '))
    if op == 1:
        total = n1 + n2
        print('Resultado da soma entre {} e {} é {}\n'.format(n1, n2, total))
    if op == 2:
        total = n1 * n2
        print('Resultado da multiplicação entre {} e {} é {}\n'.format(n1, n2, total))
    if op == 3:
        if n1 > n2:
            print('O valor de {} é maior que o valor de {}'.format(n1, n2))
        else:
            print('O valor de {} é maior que o valor de {}'.format(n2, n1))
    if op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('Adeus')