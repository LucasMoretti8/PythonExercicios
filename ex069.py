sexo = str
idade = int
a = 0
b = 0
c = 0
while True:
    sexo = input('\nDigite o SEXO da pessoa[ M / F ]:').upper()
    idade = int(input('Digite a IDADE da pessoa: '))
    if idade  > 18:
        a +=1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade < 20:
        c += 1
    continua = input('\nDeseja cadastrar outra pessoa? [ S / N ]: ').upper()
    if continua == 'N':
        break
print('Foram cadastradas:\n{} pessoas menores de 18 anos\n{} Homens\n{} Mulheres menores de 20 anos'.format(a,b,c))

