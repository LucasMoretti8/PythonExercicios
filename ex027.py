#nomecompleto = input('Digite o seu nome completo: ')
#separa = nomecompleto.split()
#x = separa.__len__()
#ult = x-1
#print('Nome completo: {}\nPrimeiro nome: {}\nÚltimo nome: {}'.format(nomecompleto,separa[0],separa[ult]))

n = str (input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(nome[0],nome[len(nome)-1]))