def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n


#ProgramaPrincipal
num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {num}')