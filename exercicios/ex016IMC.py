peso = float(input('Qual seu peso em Kg: '))
altura = float(input('Qual sua altura em metros: '))
imc = peso / altura ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc <= 10 or imc >= 150 or peso < 0 or peso > 400 or altura < 0 or altura > 2.8:
    print('Valores incorrestos ou incompatíveis com o cálculo')
elif imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 24.9:
    print('PARABÉNS, faixa de peso normal.')
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 34.9:
    print('Você está com obesidade de grau 1')
elif imc <= 39.9:
    print('Você está com obesidade de grau 2')
else:
    print('Você está com obesidade de grau 3')