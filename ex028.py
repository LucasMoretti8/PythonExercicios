import random
from time import sleep
list = [0,1,2,3,4,5]
num = random.choice(list)
user = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if user == num:
    print('PARABÉNS!! VOCÊ ACERTOU!! O NÚMERO ERA {}'.format(num))
else:
    print("ERROU!!! O NÚMERO ERA {}".format(num))