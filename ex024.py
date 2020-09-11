nome = input('Digite o nome da cidade: ')
primeiro = nome.split()
nome = primeiro[0].capitalize()
if nome.__contains__('Santo'):
    print("O nome da cidade começa com Santo")
else: print("O nome da cidade não começa com Santo")