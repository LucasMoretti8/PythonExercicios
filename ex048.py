soma = 0
count = 0
for c in range (1, 500+1, 2):
    if c % 3 == 0:
        count = count +1
        soma = soma + c
print('Total:' , soma)
print('Foram somados {} números'.format(count))
