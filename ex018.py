from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo que você deseja: '))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))
coss = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,coss))
tang = tan(radians(ang))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ang,tang))
