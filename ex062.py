t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print(t)
c = 10
while c > 1:
    t = t + r
    print(t)
    c = c -1
print('Pausa')
user = int(input('Quer mostrar mais quantos termos: '))
while user != 0:
    while user > 0:
        t = t + r
        print(t)
        user = user - 1
    user = int(input('Quer mostrar mais quantos termos: '))
print('Adeus!')