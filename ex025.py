nome = input('Digite o nome da pessoa: ').strip()
nome = nome.lower()
if nome.__contains__('silva'):
    print("O nome da pessoa possui Silva")
else: print("O nome da pessoa não possui Silva")