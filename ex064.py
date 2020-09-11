'''n = 0
t = 0
c = 0
while n != 999:
    n = int(input('Digite um valor: '))
    t = t + n
    c = c + 1
print('Total:',t-999)
print('Count',c-1)
'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))