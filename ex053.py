frase = input('Digite a frase: ')
frase = frase.replace(" ", "")
inverte = frase[::-1]
print('O inverso de {} é {}.'.format(frase,inverte))
if frase == inverte:
    print('A frase informada é um palíndromo')
else:
    print('A frase informada não é um palíndromo')

'''
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''