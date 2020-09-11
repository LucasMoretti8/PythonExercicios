n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2
if m < 5.0:
    print('MÉDIA: {}\nALUNO REPROVADO'.format(m))
elif 5.0 <= m < 6.9:
    print('MÉDIA: {}\nALUNO EM RECUPERAÇÃO'.format(m))
elif m >= 7.0:
    print('MÉDIA: {}\nALUNO APROVADO'.format(m))