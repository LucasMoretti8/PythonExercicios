from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos, o seu voto é NEGADO')
    if 16 <= idade < 18 or idade > 70:
        return print(f'Com {idade} anos o seu voto é OPCIONAL')
    else:
        return print(f'Com {idade} anos o seu voto é OBRIGATÓRIO')


#ProgramaPrincipal
voto(int(input('Digite o ano de nascimento: ')))
