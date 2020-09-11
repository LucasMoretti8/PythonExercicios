num = int(input('Insira um número: '))
op = int(input('Escolha a opção para a conversão: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nOpção: '))
if op == 1:
    b = bin(num)[2:]
    print('Convertido para binário: {}'.format(b))
elif op == 2:
    b = oct(num)[2:]
    print('Convertido para octal: {}'.format(b))
elif op == 3:
    b = hex(num)[2:]
    print('Convertido para hexadecimal: {}'.format(b))
else:
    print('Opção inválida. Tente novamente.')