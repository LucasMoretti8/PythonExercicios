numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20: '))
while num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número de 0 a 20: '))
else:
    print(f'Você digitou o número {numeros[num]}')