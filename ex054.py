import datetime
now = datetime.datetime.now()
count = 0
for c in range (7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = now.year - ano
    if idade >= 21:
        count = count + 1
print('O número de pessoas maiores de idade é: {}\nO número de pessoas menores de idade é: {}'.format(count,(c+1)-count))