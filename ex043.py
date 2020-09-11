peso = float(input('Informe o peso do paciente: '))
altura = float(input('Informe a altura do paciente: '))
imc = (peso/(altura ** 2))
if imc < 18.5:
    print('IMC: {:.2f}\nPaciente abaixo do peso'.format(imc))
elif 18.5 < imc < 25:
    print('IMC: {:.2f}\nPaciente no peso ideal'.format(imc))
elif 25 < imc < 30:
    print('IMC: {:.2f}\nPaciente com sobrepeso'.format(imc))
elif 30 < imc < 40:
    print('IMC: {:.2f}\nPaciente com obesidade'.format(imc))
elif imc > 40:
    print('IMC: {:.2f}\nPaciente com obesidade mórbida'.format(imc))