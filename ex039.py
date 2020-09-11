import datetime
now = datetime.datetime.now()
nasc = int(input('Insira o ano de nascimento do jovem: '))
dif = now.year - nasc
idade = now.year - nasc
if dif < 18:
    print('Você ainda deverá se alistar!\nO seu alistamento será em {}\nFaltam {} anos'.format(nasc+18,18-idade))
elif dif > 18:
    print('Já passou do tempo de você se alistar!\nJá passaram {} anos'.format(idade-18))
elif dif == 18:
    print('É hora de se alistar!')