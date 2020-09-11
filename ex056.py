idadetotal = 0
count = 0
velho = str('Ninguém')
idadehomem = int(0)
media = int(0)
for c in range(4):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa: ')

    idadetotal = idadetotal+idade
    media = idadetotal / 4
    if sexo == 'f' and idade < 20:
        count = count + 1

    if sexo == 'm' and idade > idadehomem:
        velho = nome

print('Média: {}'.format(media))
print('Homem mais velho: {}'.format(velho))
print('{} mulheres possuem menos de 20 anos'.format(count))


