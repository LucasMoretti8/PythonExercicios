from time import sleep
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~'*tam)


def contador(i, f, p):
    escreva((f'Contagem de {i} até {f} de {p} em {p}'))

    if i < f:
        cont = i
        while cont <= f:
            sleep(1)
            print(f'{cont} ', end='')
            cont += p
        sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            sleep(1)
            print(f'{cont} ', end='')
            cont -= p
        sleep(0.5)
        print('FIM!')




#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
escreva('CRIE O SEU PRÓPRIO CONTADOR:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('De quanto em quanto: '))
contador(i, f, p)