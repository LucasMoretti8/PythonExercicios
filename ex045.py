import random
list = ['Pedra', 'Papel', 'Tesoura']
jogada = int(input('Escolha entre:\n1)Pedra\n2)Papel\n3)Tesoura\nEscolha: '))
if jogada == 1:
    jogada = 'Pedra'
elif jogada == 2:
    jogada = 'Papel'
elif jogada == 3:
    jogada = 'Tesoura'
chosen = random.choice(list)
print('Eu escolhi {}\nVocê escolheu {}'.format(chosen,jogada))
if chosen == 'Pedra':
    if jogada == 'Pedra':
        print('Empate!')
    elif jogada == 'Papel':
        print('Você ganhou!')
    elif jogada == 'Tesoura':
        print('Eu ganhei!')
elif chosen == 'Papel':
    if jogada == 'Pedra':
        print('Eu ganhei!')
    elif jogada == 'Papel':
        print('Empate!')
    elif jogada == 'Tesoura':
        print('Você ganhou!')
elif chosen == 'Tesoura':
    if jogada == 'Pedra':
        print('Você ganhou!')
    elif jogada == 'Papel':
        print('Eu ganhei!')
    elif jogada == 'Tesoura':
        print('Empate!')
