import random
from time import sleep
list = [0,1,2,3,4,5,6,7,8,9,10]
num = random.choice(list)
#print(num)
user = int(input('Escolha um número de 0 a 10: '))
count = 1
while num != user:
    if user < num:
        print('Mais...')
    if user > num:
        print('Menos...')
    user = int(input('Tente outra vez: '))
    count = count +1
print('Parabéns, você adivinhou! E você levou apenas {} tentativas.'.format(count))