import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa de um triângulo retângulo com um cateto oposto de {} e um cateto adjascente de {} é {:.2f}'.format(co,ca,hi))