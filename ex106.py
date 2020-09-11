from time import sleep

c =('\033[m', #sem cores
    '\033[0;30;41m', #Vermelho
    '\033[0;30;42m', #Verde
    '\033[0;30;43m', #Amarelo
    '\033[0;30;44m', #Azul
    '\033[0;30;45m', #Roxo
    '\033[7;30m'     #Branco
    );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca .> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)