#frase = input('Digite uma frase: ')
#frase = frase.lower()
#c = frase.count('a')
#pos1 = frase.find('a')
#pos2 = frase.rfind('a')
#print('Na frase "{}" a letra "A" aparece {} vezes.\nEla aparece na primeira vez na posição {},\ne ela aparece na última vez na posição {}'.format(frase, c, pos1, pos2))

frase= str (input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes nesta frase.\nA primeira letra A apareceu na posição {}\nA última letra A apareceu na posição {}'.format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))